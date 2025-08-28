🤖 Autogen Agentic Framework
A modular, scalable automation system built with OpenAI-powered agents that interact via structured prompts. Designed for database analysis, REST API integration, Excel automation, and more — all orchestrated through a factory pattern and config-driven architecture.

📦 Project Structure
Autogen_Framework/
├── AGENTS/                      # Domain-specific agent logic
├── Framework/
│   ├── agents/                  # Core agent classes (e.g., AutogenAgent, AssistantAgent)
│   ├── config/                  # Model and execution config (MapConfig)
│   └── AgentFactory.py          # Factory class to instantiate agents
├── main.py                      # Entry point for agent orchestration
├── basic3_AdvancedMathAgent.py  # Sample agent for advanced math tasks

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/jas09/Autogen_Framework.git

3. Set Up Environment

4. Configure Your Models
Update  with:
• 	OpenAI API keys
• 	Model names
• 	Filesystem workbench paths (for agents with code execution)

🧠 Agent Factory Overview
The  class supports:
| Method                                      | Agent Type     | Features                                      |
|--------------------------------------------|----------------|-----------------------------------------------|
| create_database_agent()                    | Database Agent | Prompt-driven, model-only                     |
| create_database_agent_with_filesys()       | Database Agent | Includes code execution + workbench           |
| create_excel_agent()                       | Excel Agent    | Prompt-driven, model-only                     |
| create_excel_agent_with_filesystem()       | Excel Agent    | Includes code execution + workbench           |

Each agent is initialized with:
• 	A unique name
• 	A system prompt
• 	Config from  (LLM + execution)

🧩 Multi-Agent Interaction
Agents communicate via structured prompts and shared context. You can orchestrate workflows where:
• 	A database agent extracts insights
• 	An Excel agent formats and visualizes data
• 	A REST API agent fetches external resources
• 	Agents pass messages and outputs to each other
Example flow:


📊 Reporting & Demo Readiness
Integrate with:
• 	✅ Allure or HTML reporting
• 	✅ Assertion helpers
• 	✅ Modular gesture/action suites (for mobile automation)

🛠️ Troubleshooting Tips
• 	IDE auto-suggestions: Check Python path and module visibility
• 	Filesystem workbench errors: Validate config paths and permissions
• 	Docker persistence: Ensure volumes are mounted correctly
• 	Selector issues: Use dynamic parameterization for gestures

📈 Roadmap
• 	[x] Modular agent factory
• 	[x] Filesystem-enabled agents
• 	[ ] Lucidchart/Lucidspark integration for visual demos
• 	[ ] Azure-native CI/CD orchestration
• 	[ ] Multi-agent prompt chaining with memory

👨‍💻 Contributing
Pull requests welcome! For major changes, open an issue first to discuss.

📜 License
MIT License. See  file for details.
