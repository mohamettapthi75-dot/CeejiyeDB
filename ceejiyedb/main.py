import sys
import os

# Ensure we can import ceejiye_core after build
sys.path.append(os.getcwd())

import ceejiye_core
from ceejiyedb.parser import Parser
from ceejiyedb.commands import CommandHandler

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
║     CeejiyeDB v2.0.0  🦀   ║
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
MUDDAD      MUDDAD <fur> <ilb>      MUDDAD magac 60     Set TTL
KOOB        KOOB <fur>              KOOB tiriye         Increment
NOOC        NOOC <fur>              NOOC magac          Show type
CAAWI       CAAWI                   CAAWI               Tus amarrada oo dhan
DHAMAN      DHAMAN                  DHAMAN              Ka bax
"""
    print(help_text)

def main():
    # Initialize Rust core storage
    storage = ceejiye_core.CeejiyeStore()

    # Start TCP server in background
    storage.start_server(7379)

    parser = Parser()
    handler = CommandHandler(storage)

    print_banner()

    while True:
        try:
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
                print(f"{BOLD}{response}{RESET}")

        except KeyboardInterrupt:
            print(f"\n{GREEN}Nabad gelyo! 👋{RESET}")
            break
        except Exception as e:
            print(f"{RED}Khalad: {e}{RESET}")

if __name__ == "__main__":
    main()
