from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:

    @staticmethod
    def get_mysql_workbench():
        mysql_server_params = StdioServerParams(command="C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\uv.exe",
                                                args=["--directory",
                                                        "C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages",
                                                        "run",
                                                        "mysql_mcp_server"],
                                                env={"MYSQL_HOST": "localhost","MYSQL_PORT": "3306",
                                                        "MYSQL_USER": "root",
                                                        "MYSQL_PASSWORD": "Root_test@8609",
                                                        "MYSQL_DATABASE": "rahulshettyacademy"})
        return McpWorkbench(server_params=mysql_server_params)
    @staticmethod
    def get_restapi_workbench():
        restapi_server_params = StdioServerParams(command="node",
                                                  args=["C:\\Users\\HI\\AppData\\Roaming\\npm\\node_modules\\dkmaker-mcp-rest-api\\build/index.js"],
                                                  env={"REST_BASE_URL": "https://rahulshettyacademy.com","HEADER_Accept": "application/json"})
        return McpWorkbench(server_params=restapi_server_params)
    @staticmethod
    def get_filesystem_workbench():
        filesystem_server_params = StdioServerParams(command="C:\\PROGRA~1\\nodejs\\npx.cmd",
                          args=["-y","@modelcontextprotocol/server-filesystem","D:\\AI_Agent_Learning\\LLM-MCP(AI Agent)"])

        return McpWorkbench(server_params=filesystem_server_params)
    @staticmethod
    def get_excel_workbench():
        excel_server_params = StdioServerParams(command="cmd",
                          args=["/c", "npx", "--yes", "@negokaz/excel-mcp-server"],
                          env={"EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"})
        return McpWorkbench(server_params=excel_server_params)
