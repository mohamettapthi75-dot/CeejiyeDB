class Parser:
    """
    Parses CeejiyeLang syntax for CeejiyeDB.
    """
    def parse(self, command_string):
        """
        Tokenizes the input string and identifies the command and arguments.
        Example: "KAYDI magac Ceejiye" -> ("KAYDI", ["magac", "Ceejiye"])
        """
        if not command_string.strip():
            return None, []

        parts = command_string.split()
        command = parts[0].upper()
        args = parts[1:]

        return command, args
