import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
#Provide OPENAI_API_KEY
os.environ["OPENAI_API_KEY"]= "OPENAI_API_KEY"
async def main():
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
    )
    ethics_professor = AssistantAgent(name="EthicsProfessor",model_client=openai_model_client,
                   system_message="You are an Ethics Professor specializing in AI ethics. "
                                    "You analyze AI's moral implications, fairness, and societal impact.")

    ai_rights_advocate = AssistantAgent(name="AIRightsAdvocate",model_client=openai_model_client,
                   system_message="You are an AI Rights Advocate. "
                                    "Defend AI consciousness, autonomy, and the need for legal rights for intelligent agents.")

    policy_maker = AssistantAgent(name="PolicyMaker",model_client=openai_model_client,
                   system_message="You are a Policy Maker specializing in AI governance. "
                                    "Explain laws, regulations, and frameworks governing AI usage."
                                     "Say 'TERMINATE' when satisfied with the final result")

    text_termination = TextMentionTermination("TERMINATE")
    max_message_termination = MaxMessageTermination(max_messages=20)
    termination = text_termination|max_message_termination

    team = SelectorGroupChat(participants=[ethics_professor,policy_maker,ai_rights_advocate],
                      model_client=openai_model_client,allow_repeated_speaker=True,
                      termination_condition=termination)
    await Console(team.run_stream(task="Should AI have legal rights?"))





asyncio.run(main())