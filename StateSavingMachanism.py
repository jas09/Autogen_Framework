import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    agent1 = AssistantAgent(name="Helper",model_client=openai_model_client)
    agent2 = AssistantAgent(name="BackupHelper",model_client=openai_model_client)

    await Console(agent1.run_stream(task="In 2024 i was working for TechMahindra"))
    state = await agent1.save_state()
    with open("test.json","w") as f:
        json.dump(state,f,default=str)

    with open("test.json", "r") as t:
        saved_state = json.load(t)

    await agent2.load_state(saved_state)
    await Console(agent2.run_stream(task="where was i working in 2024?"))
    await openai_model_client.close()

asyncio.run(main())