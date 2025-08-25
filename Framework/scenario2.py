import asyncio
import os

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from Framework.AgentFactory import AgentFactory
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
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