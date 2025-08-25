import os.path
class AgentsSystemMessage:

    async def load_system_message(file_name: str) -> str:
        """Reads the system message from the system_messages folder."""
        base_path = os.path.join(os.path.dirname(r"scenario1.py"),"system_messages")
        file_path = os.path.join(base_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"System message file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


