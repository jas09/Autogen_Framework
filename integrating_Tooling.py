import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.base import TerminationCondition
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

os.environ["OPENAI_API_KEY"]= "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"
async def main():

    filesystem_server_params = StdioServerParams(command="npx",args=["-y",
            "@modelcontextprotocol/server-filesystem",
            "D:\AI_Gent_Project"],read_timeout_seconds=60)
    fs_workbench = McpWorkbench(filesystem_server_params)

    async with fs_workbench as fs_wb:

        openai_model_client = OpenAIChatCompletionClient(
            model="gpt-4o-mini",
             # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
        )
        assistant = AssistantAgent(name="MathTutor",model_client=openai_model_client,workbench=fs_wb,
                       system_message="You are helpful math tutor.Help the use solve math problem step by step."
                                      "You have access to file system"
                                      "when user says 'Thanks Done' or similar, acknowledge and say 'Lesson Complete' to end session")

        user_proxy = UserProxyAgent(name="Student")

        team = RoundRobinGroupChat(participants=[user_proxy,assistant],
                            termination_condition=TextMentionTermination("Lesson Complete"))

        await Console(team.run_stream(task="I need help with algebra problem. Tutor, feel free to create"
                             "files to help with student learning"))
    await openai_model_client.close()

asyncio.run(main())