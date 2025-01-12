from colorama import *

init(autoreset=True)

breakLine = "-" * 60
breakLineDouble = "=" * 60
def inp() : return input(Fore.BLUE + "$: " + Style.RESET_ALL)

def error(message):
    message = str(message)
    message = message.upper()
    print(Fore.RED + "[ERROR] " + message + Style.RESET_ALL)

def warning(message):
    message = str(message)
    message = message.upper()
    print(Fore.YELLOW + "[WARNING] " + message + Style.RESET_ALL)

def debug(key, value):
    print(Fore.LIGHTMAGENTA_EX + f"[DEBUGGING] ('{key}': '{value}')" + Style.RESET_ALL)