class CommandHandler:
    """
    Executes commands on the storage based on CeejiyeLang syntax v1.2.0.
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
                return f"ERROR:Khalad: '{key}' lama helin ama waa uu dhacay."

        elif command == "TIR":
            if len(args) < 1:
                return "ERROR:Khalad: TIR waxay u baahan tahay fure. (Tusaale: TIR magac)"
            key = args[0]
            if self.storage.delete(key):
                return f"SUCCESS:Guul: '{key}' waa la tiray."
            else:
                return f"ERROR:Khalad: '{key}' lama helin markaa lama tiri karo."

        elif command == "MUDDAD":
            if len(args) < 2:
                return "ERROR:Khalad: MUDDAD waxay u baahan tahay fure iyo ilbiriqsiyo. (Tusaale: MUDDAD magac 60)"
            key = args[0]
            try:
                seconds = int(args[1])
                if self.storage.set_ttl(key, seconds):
                    return f"SUCCESS:Guul: '{key}' waxaa loo muddeeyay {seconds} ilbiriqsi."
                else:
                    return f"ERROR:Khalad: '{key}' lama helin."
            except ValueError:
                return "ERROR:Khalad: Ilbiriqsiyadu waa inay noqdaan tiro."

        elif command == "KOOB":
            if len(args) < 1:
                return "ERROR:Khalad: KOOB wuxuu u baahan yahay fure. (Tusaale: KOOB tiriye)"
            try:
                new_val = self.storage.increment(args[0])
                return f"SUCCESS:Guul: '{args[0]}' hadda waa {new_val}."
            except ValueError as e:
                return str(e)

        elif command == "DHIMIS":
            if len(args) < 1:
                return "ERROR:Khalad: DHIMIS wuxuu u baahan yahay fure. (Tusaale: DHIMIS tiriye)"
            try:
                new_val = self.storage.decrement(args[0])
                return f"SUCCESS:Guul: '{args[0]}' hadda waa {new_val}."
            except ValueError as e:
                return str(e)

        elif command == "XAALAD":
            stats = self.storage.get_stats()
            return (f"XAALADDA DATABASE-KA (v1.2.0):\n"
                    f" - Wadarta Furayaasha: {stats['keys']}\n"
                    f" - Xajmiga RAM-ka (est): {stats['memory']} bytes\n"
                    f" - Xajmiga Faylka: {stats['file_size']} bytes")

        elif command == "DHAMAN":
            return "DATABASE_EXIT"

        elif command == "CAAWI":
            return "HELP_COMMAND"

        else:
            return f"ERROR:Khalad: Amarkan '{command}' ma garanayo. Qor CAAWI si aad u aragto amarrada."
