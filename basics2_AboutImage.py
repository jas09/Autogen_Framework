import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    assistant = AssistantAgent(name="MultiModelAssistant",model_client=openai_model_client)
    image = Image.from_file("D:\\AI_Agent_Learning\\321231.JPG")
    multimodal_message = MultiModalMessage(content=["what do you see in this image", image],source="user")
    await Console(assistant.run_stream(task=multimodal_message))

asyncio.run(main())