import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    assistant = AssistantAgent(name="ScienceTeacher",model_client=openai_model_client,
                   system_message="You are Science teacher who has excellent knowledge on every topic related to science. Help the user to solve his questions in a logical way"
                                  "When the user says 'Thanks Done' or similar, acknowledge and say 'LESSON COMPLETE' to end session")

    user_proxy = UserProxyAgent(name="Azhar")

    team = RoundRobinGroupChat(participants=[assistant,user_proxy],
                        termination_condition=TextMentionTermination("LESSON COMPLETE"))

    await Console(team.run_stream(task="The Day Gravity Stopped"))
    await openai_model_client.close()

asyncio.run(main())