import os
from lib.helpers.helpers import *
from lib.parser import *
from lib.helpers.visuals import *

def main():
    config = parserInit()

    print(Fore.BLUE + "[UE4] Config Parser" + Style.RESET_ALL)
    print("1. OPEN CONFIG (default)")
    choice = inp()

    if choice == "1":
        openConfig(config)
    else:
        error("Invalid choice")

main()