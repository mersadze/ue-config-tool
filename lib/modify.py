import os
import json
from lib.helpers.helpers import *

def modifyConfig(config, key, value):
    print("Modifying config...")
    if key in config:
        print("Key found in config")
        try:
            config[key] = value
        except Exception as e:
            error(f"Error modifying config: {e}")
    else:
        print("Config: ", config)
        print("Key: ", key)
        print("Value: ", value)
        error("Key not found in config")

    return config