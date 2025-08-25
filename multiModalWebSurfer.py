import asyncio
import os

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ["OPENAI_API_KEY"]= "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"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    web_surfer_agent = MultimodalWebSurfer(name="websurfer",
                        model_client=openai_model_client,
                        headless=False,
                        animate_actions=True)

    agent_team = RoundRobinGroupChat(participants=[web_surfer_agent],max_turns=3)

    await Console(agent_team.run_stream(task="Navigate to Google and search for 'What if AI became smarter than humanity overnight?'."
                               "Then Summarize what you have found"))

    await openai_model_client.close()
    await web_surfer_agent.close()




asyncio.run(main())