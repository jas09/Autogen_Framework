import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ["OPENAI_API_KEY"]= "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"
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