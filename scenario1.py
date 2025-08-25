import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

from Utils.Agents_SystemMessage import AgentsSystemMessage

os.environ["OPENAI_API_KEY"]= "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"
os.environ["JIRA_URL"]="https://ajjujas.atlassian.net/"
os.environ["JIRA_USERNAME"]="ajju.jas@gmail.com"
os.environ["JIRA_API_TOKEN"] ="ATCTT3xFfGN0Bx7pESpkgPW_PpJ3ATUprD3qBNe-cgAhbGr8U0WMfhMHQAuVwQsO-nBMzP-b2hhOVbJMHyuqPwQAw6rZQBz2SCrE76bFPjyTiAolQ4nqqS12bem2GqwHgWHJxyGCkOi7pz-MPR5_BZc29FvI9swSyrPvQur_UIF49aJCY2xLWGM=BA655C7F"
os.environ["JIRA_PROJECTS_FILTER"] = "AL"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    jira_server_params = StdioServerParams(command="docker",args=["run","-i","--rm",
                                                "--dns", "8.8.8.8", "--dns", "1.1.1.1",
                                                "-e", f"JIRA_URL={os.environ['JIRA_URL']}",
                                                "-e", f"JIRA_USERNAME={os.environ['JIRA_USERNAME']}",
                                                "-e", f"JIRA_API_TOKEN={os.environ['JIRA_API_TOKEN']}",
                                                "-e", f"JIRA_PROJECTS_FILTER={os.environ['JIRA_PROJECTS_FILTER']}",
                                                "ghcr.io/sooperset/mcp-atlassian:latest"])
    playwright_server_params = StdioServerParams(command="npx",args=["@playwright/mcp@latest"])
    jira_workbench = McpWorkbench(jira_server_params)
    playwright_workbench = McpWorkbench(playwright_server_params)

    async with jira_workbench as jira_wb,playwright_workbench as playwright_wb:
        bug_analyst_msg = await AgentsSystemMessage.load_system_message("bug_analyst1.txt")
        automation_analyst_msg = await AgentsSystemMessage.load_system_message("automation_analyst1.txt")
        Jira_Playwright_Goal_msg = await AgentsSystemMessage.load_system_message("Jira_Playwright_Goal.txt")
        bug_analyst = AssistantAgent(name="BugAnalyst",model_client=openai_model_client,workbench=jira_wb,
                       system_message=bug_analyst_msg)
        automation_analyst = AssistantAgent(name="AutomationAgent",model_client=openai_model_client,workbench=playwright_wb,
                       system_message=automation_analyst_msg)
        team = RoundRobinGroupChat(participants=[bug_analyst,automation_analyst],
                            termination_condition=TextMentionTermination("TESTNG COMPLETE"))
        await Console(team.run_stream(task=Jira_Playwright_Goal_msg))
        await OpenAIChatCompletionClient.close()

asyncio.run(main())







