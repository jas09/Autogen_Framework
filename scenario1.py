import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from dotenv import load_dotenv
from Utils.Agents_SystemMessage import AgentsSystemMessage
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
os.environ["JIRA_URL"]="https://ajjujas.atlassian.net/"
os.environ["JIRA_USERNAME"]="ajju.jas@gmail.com"
#Provide JIRA_API_TOKEN
os.environ["JIRA_API_TOKEN"] ="JIRA_API_TOKEN"
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







