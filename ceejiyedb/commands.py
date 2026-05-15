class CommandHandler:
    """
    Executes commands on the storage based on CeejiyeLang syntax.
    """
    def __init__(self, storage):
        self.storage = storage

    def execute(self, command, args):
        """
        Routes the command to the appropriate storage method.
        Returns a prefixed string for the CLI to handle coloring.
        """
        if command == "KAYDI":
            if len(args) < 2:
                return "ERROR:Khalad: KAYDI waxay u baahan tahay fure iyo qiimo. (Tusaale: KAYDI magac Ceejiye)"
            key = args[0]
            value = " ".join(args[1:])
            self.storage.set(key, value)
            return f"SUCCESS:Guul: '{key}' waa la kaydiyay."

        elif command == "SOOQAAD":
            if len(args) < 1:
                return "ERROR:Khalad: SOOQAAD waxay u baahan tahay fure. (Tusaale: SOOQAAD magac)"
            key = args[0]
            value = self.storage.get(key)
            if value is not None:
                return value
            else:
                return f"ERROR:Khalad: '{key}' lama helin."

        elif command == "TIR":
            if len(args) < 1:
                return "ERROR:Khalad: TIR waxay u baahan tahay fure. (Tusaale: TIR magac)"
            key = args[0]
            if self.storage.delete(key):
                return f"SUCCESS:Guul: '{key}' waa la tiray."
            else:
                return f"ERROR:Khalad: '{key}' lama helin markaa lama tiri karo."

        elif command == "LIIS":
            keys = self.storage.get_all_keys()
            if not keys:
                return "Wax xog ah kuma jirto."
            return "\n".join(keys)

        elif command == "TIJAABO":
            if len(args) < 1:
                return "ERROR:Khalad: TIJAABO waxay u baahan tahay fure. (Tusaale: TIJAABO magac)"
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
                return "ERROR:Khalad: CUSB waxay u baahan tahay fure iyo qiimo. (Tusaale: CUSB magac Fadumo)"
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

        elif command == "CAAWI":
            return "HELP_COMMAND"

        elif command == "DHAMAN":
            return "DATABASE_EXIT"

        else:
            return f"ERROR:Khalad: Amarkan '{command}' ma garanayo. Fadlan isticmaal CAAWI si aad amarrada u aragto."
