import asyncio
import os

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from Framework.AgentFactory import AgentFactory

os.environ["OPENAI_API_KEY"]= "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"
async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

    factory = AgentFactory(openai_model_client)
    database_agent = factory.create_database_agent(system_message=())
    api_agent = factory.create_api_agent(system_message=())
    excel_agent = factory.create_excel_agent(system_message=())
    team = RoundRobinGroupChat(participants=[database_agent,api_agent,excel_agent],
                        termination_condition=TextMentionTermination("REGISTRATION PROCESS COMPLETE"))
    await Console(team.run_stream(task=""))
    await openai_model_client.close()

asyncio.run(main())