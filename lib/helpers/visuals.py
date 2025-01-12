import json
from colorama import Fore, Style
from lib.helpers.helpers import *
from lib.modify import *
from lib.parser import *

init(autoreset=True)

def printHelp():
    print(Fore.CYAN + breakLineDouble + Style.RESET_ALL)
    print(Fore.YELLOW + "Available commands:" + Style.RESET_ALL)
    print(Fore.RED + "[SET]" + Style.RESET_ALL + " - Set key to a specific value (e.g. set Key W)")
    print(Fore.CYAN + "[DEFAULT]" + Style.RESET_ALL + " - Set key to default value (e.g. default Key)")
    print(Fore.RED + "(note: keys and values are case sensitive)" + Style.RESET_ALL)

def jsonFormat(json_data, indent=4):
    return json.dumps(json_data, indent=indent)

def transformValue(value):
    if str(value).lower() == "false":
        return Fore.RED + "False" + Style.RESET_ALL
    elif str(value).lower() == "true":
        return Fore.GREEN + "True" + Style.RESET_ALL
    else:
        return Fore.BLUE + str(value) + Style.RESET_ALL

def getDeviceType(key):
    if str(key).startswith("Gamepad_"):
        return "Gamepad"
    else:
        return "Keyboard & Mouse"

def mapModifier(key):
    if isinstance(key, list):
        if key and isinstance(key[0], dict) and "ActionName" in key[0]:
            return {
                "ActionName": next((entry.get("ActionName") for entry in key if "ActionName" in entry), None),
                "Key": next((entry.get("Key") for entry in key if "Key" in entry), None),
                "bShift": next((entry.get("bShift") for entry in key if "bShift" in entry), None),
                "bCtrl": next((entry.get("bCtrl") for entry in key if "bCtrl" in entry), None),
                "bAlt": next((entry.get("bAlt") for entry in key if "bAlt" in entry), None),
                "bCmd": next((entry.get("bCmd") for entry in key if "bCmd" in entry), None)
            }
        elif key and isinstance(key[0], dict) and "AxisName" in key[0]:
            return {
                "AxisName": next((entry.get("AxisName") for entry in key if "AxisName" in entry), None),
                "Key": next((entry.get("Key") for entry in key if "Key" in entry), None),
                "Scale": next((entry.get("Scale") for entry in key if "Scale" in entry), None)
            }
    else:
        error("Unknown key type")
    
    return key

def openKey(key):
    while True:
        print(Fore.CYAN + breakLineDouble + Style.RESET_ALL)
        print("[type 'help' to print available commands]")

        if isinstance(key, list) and key:
            modifiers = mapModifier(key)
            if "ActionName" in modifiers:
                actionName = modifiers.get("ActionName")
                actionKey = modifiers.get("Key")
                bShift = modifiers.get("bShift")
                bCtrl = modifiers.get("bCtrl")
                bAlt = modifiers.get("bAlt")
                bCmd = modifiers.get("bCmd")

                actionKey = transformValue(actionKey)
                bShift = transformValue(bShift)
                bCtrl = transformValue(bCtrl)
                bAlt = transformValue(bAlt)
                bCmd = transformValue(bCmd)

                print("[" + Fore.RED + f"ActionName: {actionName}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Key: {actionKey}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Shift: {bShift}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Ctrl: {bCtrl}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Alt: {bAlt}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Cmd: {bCmd}" + Style.RESET_ALL + "]")
            elif "AxisName" in modifiers:
                axisName = modifiers.get("AxisName")
                actionKey = modifiers.get("Key")
                scale = modifiers.get("Scale")
                
                actionKey = transformValue(actionKey)
                scale = transformValue(scale)

                print("[" + Fore.RED + f"AxisName: {axisName}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Key: {actionKey}" + Style.RESET_ALL + "]")
                print("[" + Fore.RED + f"Scale: {scale}" + Style.RESET_ALL + "]")
            else:
                error("No valid modifiers found in key")
        else:
            error("Invalid key structure")

        choice = inp()
        if choice == "help":
            printHelp()
        elif str(choice).startswith("set"):
            config = parserInit()
            _, key, value = choice.split(" ", 3)
            print("Modifying " + Fore.RED + f"'{key}'" + Style.RESET_ALL + " to " + Fore.RED + f"'{value}'" + Style.RESET_ALL)
            config = modifyConfig(config, key, value)

        elif choice == "exit":
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            break

        print(Fore.CYAN + breakLineDouble + Style.RESET_ALL)

def openKeyList(key, value):
    print(Fore.CYAN + breakLine + Style.RESET_ALL)

    print(Fore.WHITE + "{:<10} {:<20} {:<10}".format("ID", "Key", "Device Type") + Style.RESET_ALL)
    print(Fore.CYAN + breakLine + Style.RESET_ALL)

    if key == "ActionMappings":
        for idx, item in enumerate(value):
            item_key = next((entry.get("Key") for entry in item if isinstance(entry, dict) and "Key" in entry), None)
            device_type = getDeviceType(item_key)
            actions_name = next((entry.get("ActionName") for entry in item if isinstance(entry, dict) and "ActionName" in entry), None)
            if actions_name:
                print(Fore.RED + "{:<10} {:<20} {:<10}".format(f"[{idx}]", actions_name, f"[{device_type}]") + Style.RESET_ALL)

    elif key == "AxisMappings":
        for idx, item in enumerate(value):
            item_key = next((entry.get("Key") for entry in item if isinstance(entry, dict) and "Key" in entry), None)
            device_type = getDeviceType(item_key)
            axis_name = next((entry.get("AxisName") for entry in item if isinstance(entry, dict) and "AxisName" in entry), None)
            if axis_name:
                print(Fore.RED + "{:<10} {:<20} {:<10}".format(f"[{idx}]", axis_name, f"[{device_type}]") + Style.RESET_ALL)
    else:
        for idx, item in enumerate(value):
            print(Fore.RED + "{:<10} {:<20}".format(f"[{idx}]", item) + Style.RESET_ALL)

    choice = inp()

    if choice.isdigit():
        idx = int(choice)
        if idx < len(value):
            selected_key = value[idx]
            openKey(selected_key)
        else:
            error("Invalid index")
    else:
        error("Invalid key")

def openSection(section):
    """Display all keys and values within a section in a table-like format."""
    print(Fore.CYAN + breakLine + Style.RESET_ALL)
    print(Fore.WHITE + "{:<40} {:<20}".format("Key", "Value") + Style.RESET_ALL)
    print(Fore.CYAN + breakLine + Style.RESET_ALL)

    for key, value in section.items():
        if "." in key:
            key = str(key).split(".", 1)[1]

        if isinstance(value, list):
            # Display the key and the number of entries inside
            print(Fore.WHITE + "{:<40} {:<20}".format(key, str(len(value)) + " entries") + Style.RESET_ALL)
        else:
            print(Fore.WHITE + "{:<20} {:<20}".format(key, value) + Style.RESET_ALL)

    choice = inp()
    
    if choice in section:
        openKeyList(choice, section[choice])
    print(Fore.CYAN + breakLine + Style.RESET_ALL)


def openConfig(config):
    """Display available sections in the config in a menu-like format."""
    while True:
        print(Fore.BLUE + "[CONFIG] default - Type the section name to open it" + Style.RESET_ALL)
        print(Fore.CYAN + breakLineDouble + Style.RESET_ALL)

        # Display sections in a table format
        sections = config.get("Sections", {})
        print(Fore.WHITE + "{:<5} {:<30}".format("ID", "Section Name") + Style.RESET_ALL)
        print(Fore.CYAN + breakLine + Style.RESET_ALL)

        for idx, section_name in enumerate(sections):
            print(Fore.RED + "{:<5} {:<30}".format(f"[{idx}]", section_name) + Style.RESET_ALL)

        print(Fore.CYAN + breakLineDouble + Style.RESET_ALL)
        choice = inp()

        if choice.lower() == "exit":
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            break

        elif choice.lower() == "back":
            print(Fore.GREEN + "Returning to main menu..." + Style.RESET_ALL)
            break

        if choice.isdigit():
            idx = int(choice)
            if idx < len(sections):
                section_name = list(sections.keys())[idx]
                openSection(sections[section_name])
            else:
                error("Invalid index")
        else:
            error(Fore.RED + "Section not found!" + Style.RESET_ALL)
