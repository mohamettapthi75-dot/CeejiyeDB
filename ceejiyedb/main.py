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
║     CeejiyeDB v1.1.0  🇸🇴   ║
║  Xogta Soomaalida, Xoogga   ║
╚══════════════════════════════╝{RESET}
"""
    print(banner)
    print("Ku soo dhawoow CeejiyeDB. Qor CAAWI si aad amarrada u aragto.")

def print_help():
    help_text = f"""
{BOLD}📖 Amarrada CeejiyeLang{RESET}
{YELLOW}Amar        Isticmaalka             Tusaale             Macnaha{RESET}
KAYDI       KAYDI <fur> <qii>       KAYDI magac Ceejiye Keydi qiime
SOOQAAD     SOOQAAD <fur>           SOOQAAD magac       Soo qaad qiime
TIR         TIR <fur>               TIR magac           Tir fur
CUSB        CUSB <fur> <qii>        CUSB magac Fadumo   Cusboonaysii qiime
TIJAABO     TIJAABO <fur>           TIJAABO magac       Hubi in fur jiro
LIIS        LIIS                    LIIS                Tus dhammaan furahaaga
TIRI        TIRI                    TIRI                Tiri furaha
NADIIFI     NADIIFI                 NADIIFI             Nadiifi xog oo dhan
CAAWI       CAAWI                   CAAWI               Tus amarrada oo dhan
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
            # Interactive terminal prompt
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

            # Internal markers from CommandHandler are now checked using explicit codes
            if isinstance(response, str) and response.startswith("SUCCESS:"):
                clean_msg = response.replace("SUCCESS:", "")
                print(f"{GREEN}{clean_msg}{RESET}")
            elif isinstance(response, str) and response.startswith("ERROR:"):
                clean_msg = response.replace("ERROR:", "")
                print(f"{RED}{clean_msg}{RESET}")
            else:
                # This is likely a value returned from SOOQAAD or LIIS/TIRI
                print(f"{BOLD}{response}{RESET}")

        except KeyboardInterrupt:
            print(f"\n{GREEN}Nabad gelyo! 👋{RESET}")
            break
        except Exception as e:
            print(f"{RED}Khalad aan la filayn: {e}{RESET}")

if __name__ == "__main__":
    main()
