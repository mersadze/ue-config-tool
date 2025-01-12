import os
import json
from lib.helpers.helpers import *

dir_name = os.path.dirname(__file__)
current_file = os.path.join(os.path.dirname(dir_name), 'data', 'configs', 'DefaultEditor.ini')

# Value Types
valueTypes = ["bool", "float", "int", "keybind", "string"]
configTypes = ["render", "input", "graphics", "audio"]

def getInputStruct(line, input_type):
    if input_type == "ActionMappings":
        input_data = line.split("=", 1)[1].strip()
        input_data = input_data.split("(", 1)[1].rstrip(")")
        input_parts = input_data.split(",", 5)
        input_struct = []

        for part in input_parts:
            key, value = map(str.strip, part.split("=", 1))
            input_struct.append({key: value.strip('"')})

        return input_struct

    elif input_type == "AxisMappings":
        input_data = line.split("=", 1)[1].strip()
        input_data = input_data.split("(", 1)[1].rstrip(")")
        input_parts = input_data.split(",", 2)
        input_struct = []

        for part in input_parts:
            key, value = map(str.strip, part.split("=", 1))
            input_struct.append({key: value.strip('"')})

        return input_struct

    else:
        raise ValueError("Unknown input type")

def getStructure(file_path):
    config = {"Sections": {}}
    current_section = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # Detect section headers
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1]
                if current_section not in config["Sections"]:
                    config["Sections"][current_section] = {}

            # Process render keys
            elif line.startswith("r."):
                if current_section:
                    key, value = map(str.strip, line[2:].split("=", 1))
                    config["Sections"][current_section][key] = value

            # Process input mappings
            elif line.startswith("+"):
                if current_section:
                    input_type = "ActionMappings" if "ActionMappings" in line else "AxisMappings"
                    input_struct = getInputStruct(line, input_type)
                    if input_type not in config["Sections"][current_section]:
                        config["Sections"][current_section][input_type] = []
                    config["Sections"][current_section][input_type].append(input_struct)

            # Ignore other lines (optional)
            elif line.startswith("-"):
                continue

            else:
                line = line.split("=", 1)
                if len(line) == 2:
                    key, value = map(str.strip, line)
                    config["Sections"][current_section][key] = value

    return config

def parserInit():
    global current_file
    if not os.path.exists(current_file):
        raise FileNotFoundError("Config file not found")

    return getStructure(current_file)

if __name__ == "__main__":
    result = parserInit()
    print(result)
