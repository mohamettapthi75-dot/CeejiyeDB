import ceejiye_core

class CommandHandler:
    """
    Executes commands using the Rust core via ceejiye_core.
    """
    def __init__(self, storage):
        self.storage = storage

    def execute(self, command, args):
        """
        Routes the command to the Rust storage methods.
        """
        if command == "KAYDI":
            if len(args) < 2:
                return "ERROR:Khalad: KAYDI <fur> <qii>"
            key = args[0]
            value = " ".join(args[1:])
            self.storage.set(key, value)
            return f"SUCCESS:Guul: '{key}' waa la kaydiyay."

        elif command == "SOOQAAD":
            if len(args) < 1:
                return "ERROR:Khalad: SOOQAAD <fur>"
            key = args[0]
            value = self.storage.get(key)
            if value is not None:
                return value
            else:
                return f"ERROR:Khalad: '{key}' lama helin."

        elif command == "TIR":
            if len(args) < 1:
                return "ERROR:Khalad: TIR <fur>"
            key = args[0]
            if self.storage.delete(key):
                return f"SUCCESS:Guul: '{key}' waa la tiray."
            else:
                return f"ERROR:Khalad: '{key}' lama helin."

        elif command == "LIIS":
            keys = self.storage.keys()
            if not keys:
                return "Wax xog ah kuma jirto."
            return "\n".join(keys)

        elif command == "TIJAABO":
            if len(args) < 1:
                return "ERROR:Khalad: TIJAABO <fur>"
            key = args[0]
            if self.storage.exists(key):
                return "Haa, waa jirtaa."
            else:
                return "Maya, kuma jirto."

        elif command == "TIRI":
            count = self.storage.count()
            return f"Wadarta furaha: {count}"

        elif command == "CUSB":
            if len(args) < 2:
                return "ERROR:Khalad: CUSB <fur> <qii>"
            key = args[0]
            value = " ".join(args[1:])
            if self.storage.exists(key):
                self.storage.set(key, value)
                return f"SUCCESS:Guul: '{key}' waa la cusboonaysiiyay."
            else:
                return "ERROR:Furaha kuma jiro xogta."

        elif command == "NADIIFI":
            self.storage.clear()
            return "SUCCESS:Dhammaan xogta waa la tirtiray."

        elif command == "MUDDAD":
            if len(args) < 2:
                return "ERROR:Khalad: MUDDAD <fur> <ilbiriqsi>"
            key = args[0]
            try:
                seconds = int(args[1])
                val = self.storage.get(key) or "TTL_VALUE"
                self.storage.set_with_ttl(key, val, seconds)
                return f"SUCCESS: '{key}' waxaa loo muddeeyay {seconds} ilbiriqsi."
            except ValueError:
                return "ERROR: Muddaddu waa inay noqotaa tiro."

        elif command == "KOOB":
            if len(args) < 1:
                return "ERROR:Khalad: KOOB <fur>"
            try:
                new_val = self.storage.increment(args[0])
                return f"SUCCESS: '{args[0]}' hadda waa {new_val}."
            except Exception as e:
                return f"ERROR: {str(e)}"

        elif command == "NOOC":
            if len(args) < 1:
                return "ERROR:Khalad: NOOC <fur>"
            t = self.storage.get_type(args[0])
            if t:
                return t
            else:
                return "ERROR: Furaha lama helin."

        elif command == "CAAWI":
            return "HELP_COMMAND"

        elif command == "DHAMAN":
            return "DATABASE_EXIT"

        else:
            return f"ERROR:Khalad: Amarkan '{command}' ma garanayo."
