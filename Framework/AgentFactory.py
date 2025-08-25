from autogen_agentchat.agents import AssistantAgent

from Framework.cmp_config import McpConfig


class AgentFactory:
    def __init__(self,openai_model_client):
        self.openai_model_client = openai_model_client
        self.McpConfig = McpConfig()


    def create_database_agent(self,system_message):
        database_analyst = AssistantAgent(name="DatabaseAgent",
                                          model_client=self.openai_model_client,
                                          workbench=self.McpConfig.get_mysql_workbench(),
                                          system_message=system_message)
        return database_analyst

    def create_api_agent(self,system_message):
        file_system_workbench = self.McpConfig.get_filesystem_workbench()
        rest_api_workbench = self.McpConfig.get_restapi_workbench()
        api_analyst = AssistantAgent(name="ApiAgent",
                       model_client=self.openai_model_client,
                       workbench=[file_system_workbench,rest_api_workbench],
                       system_message=system_message)
        return api_analyst

    def create_excel_agent(self,system_message):
        excel_agent = AssistantAgent(name="ExcelAgent",
                       model_client=self.openai_model_client,
                       workbench=self.McpConfig.get_excel_workbench(),
                       system_message=system_message)
        return excel_agent

