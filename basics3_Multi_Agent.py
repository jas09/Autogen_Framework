import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    #creating first Assistant agent - Math Teacher
    Teacher = AssistantAgent(name="MathTeacher",model_client=openai_model_client,
                   system_message="you are a math teacher, Explain concepts clearly and ask follow up questions")

    Student = AssistantAgent(name="Student",model_client=openai_model_client,
                   system_message="you are curious student. Ask questions and show your thinking process")

    team = RoundRobinGroupChat(participants=[Teacher,Student],
                               termination_condition=MaxMessageTermination(max_messages=16))
    await Console(team.run_stream(task="Let's Discuss what is Pythagoras' Theorem"))
    await openai_model_client.close()

asyncio.run(main())