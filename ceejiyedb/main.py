from storage import Storage
from parser import Parser
from commands import CommandHandler

# ANSI colors for terminal output
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    banner = f"""{BOLD}{BLUE}
╔══════════════════════════════╗
║     CeejiyeDB v1.2.0  🇸🇴   ║
║  Xogta Soomaalida, Xoogga   ║
╚══════════════════════════════╝{RESET}
"""
    print(banner)
    print("Ku soo dhawoow CeejiyeDB v1.2.0. Qor CAAWI si aad amarrada u aragto.")

def print_help():
    help_text = f"""
{BOLD}📖 Amarrada CeejiyeLang v1.2.0{RESET}
{YELLOW}Amar        Isticmaalka             Tusaale             Macnaha{RESET}
KAYDI       KAYDI <fur> <qii>       KAYDI magac Jules   Keydi qiime
SOOQAAD     SOOQAAD <fur>           SOOQAAD magac       Soo qaad qiime
TIR         TIR <fur>               TIR magac           Tir fur
MUDDAD      MUDDAD <fur> <ilb>      MUDDAD x 60         Set TTL
KOOB        KOOB <fur>              KOOB tiriye         Kordhi (Increment)
DHIMIS      DHIMIS <fur>            DHIMIS tiriye       Dhim (Decrement)
XAALAD      XAALAD                  XAALAD              Tus xaaladda DB
CAAWI       CAAWI                   CAAWI               Tus amarrada
DHAMAN      DHAMAN                  DHAMAN              Ka bax
"""
    print(help_text)

def main():
    storage = Storage()
    parser = Parser()
    handler = CommandHandler(storage)

    print_banner()

    while True:
        try:
            # Active expiration purge before each prompt
            storage.purge_expired()

            user_input = input(f"{BOLD}{YELLOW}CeejiyeDB > {RESET}")

            command, args = parser.parse(user_input)

            if command is None:
                continue

            response = handler.execute(command, args)

            if response == "DATABASE_EXIT":
                print(f"{GREEN}Nabad gelyo! 👋{RESET}")
                break

            if response == "HELP_COMMAND":
                print_help()
                continue

            if isinstance(response, str) and response.startswith("SUCCESS:"):
                print(f"{GREEN}{response.replace('SUCCESS:', '')}{RESET}")
            elif isinstance(response, str) and response.startswith("ERROR:"):
                print(f"{RED}{response.replace('ERROR:', '')}{RESET}")
            else:
                # Value return or Multi-line report
                print(f"{BOLD}{response}{RESET}")

        except KeyboardInterrupt:
            print(f"\n{GREEN}Nabad gelyo! 👋{RESET}")
            break
        except Exception as e:
            print(f"{RED}Khalad: {e}{RESET}")

if __name__ == "__main__":
    main()
