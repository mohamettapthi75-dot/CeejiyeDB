class CommandHandler:
    """
    Executes commands using the Rust core dispatcher.
    """
    def __init__(self, storage):
        self.storage = storage

    def execute(self, command, args):
        """
        Routes the command string directly to the Rust core dispatcher.
        """
        request = f"{command} {' '.join(args)}".strip()
        response = self.storage.execute(request)

        # Translate internal Rust success/error markers to CLI format
        if response.startswith("SUCCESS:"):
            return response.replace("SUCCESS:", "SUCCESS:Guul:").strip()
        elif response.startswith("ERROR:"):
            # If it's already a Somali error from dispatch.rs, keep it, otherwise prefix
            if "Khalad" in response:
                 return response.strip()
            return response.replace("ERROR:", "ERROR:Khalad:").strip()
        elif response.startswith("DATABASE_EXIT"):
            return "DATABASE_EXIT"
        elif response.startswith("HELP_COMMAND"):
            return "HELP_COMMAND"

        return response.strip()
