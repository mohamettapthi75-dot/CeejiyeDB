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

def print_welcome():
    print(f"{BOLD}{BLUE}====================================={RESET}")
    print(f"{BOLD}{GREEN}      CeejiyeDB (Somali Syntax)      {RESET}")
    print(f"{BOLD}{BLUE}====================================={RESET}")
    print("Ku soo dhawaada CeejiyeDB!")
    print("Amarrada: KAYDI, SOOQAAD, TIR, DHAMAN")
    print("-------------------------------------")

def main():
    storage = Storage()
    parser = Parser()
    handler = CommandHandler(storage)

    print_welcome()

    while True:
        try:
            # Interactive terminal prompt
            user_input = input(f"{BOLD}{YELLOW}CeejiyeDB > {RESET}")

            command, args = parser.parse(user_input)

            if command is None:
                continue

            response = handler.execute(command, args)

            if response == "DATABASE_EXIT":
                print(f"{GREEN}Nabad gelyo! Database-ka waa la xirayaa...{RESET}")
                break

            # Internal markers from CommandHandler are now checked using explicit codes
            if isinstance(response, str) and response.startswith("SUCCESS:"):
                clean_msg = response.replace("SUCCESS:", "")
                print(f"{GREEN}{clean_msg}{RESET}")
            elif isinstance(response, str) and response.startswith("ERROR:"):
                clean_msg = response.replace("ERROR:", "")
                print(f"{RED}{clean_msg}{RESET}")
            else:
                # This is likely a value returned from SOOQAAD
                print(f"{BOLD}{response}{RESET}")

        except KeyboardInterrupt:
            print(f"\n{GREEN}Nabad gelyo!{RESET}")
            break
        except Exception as e:
            print(f"{RED}Khalad aan la filayn: {e}{RESET}")

if __name__ == "__main__":
    main()
