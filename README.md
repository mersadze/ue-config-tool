```markdown
# UE-Config-Tool

## Overview
**UE-Config-Tool** is a Python-based command-line utility designed to manage Unreal Engine configuration files. It provides an intuitive interface for viewing and modifying key bindings, including `ActionMappings` and `AxisMappings`.

## Features
- View all configuration sections in a table format.
- Edit `ActionMappings` and `AxisMappings` with ease.
- Detect and classify device types (Gamepad, Keyboard, Mouse).
- Format configurations into JSON for better readability.

## Requirements
- Python 3.8+
- Dependencies:
  - [colorama](https://pypi.org/project/colorama/)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/username/UE-Config-Tool.git
   cd UE-Config-Tool
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to interact with the tool.

## Example Output
```
[CONFIG] default - Type the section name to open it
----------------------------------------
ID   Section Name
[0]  InputSettings
[1]  RenderingSettings
----------------------------------------

> ActionMappings
----------------------------------------
ID         Key                 Device Type
[0]        Jump                Keyboard & Mouse
[1]        Fire                Gamepad
----------------------------------------
```

## Contributing
Contributions are welcome! Please create an issue or submit a pull request if you'd like to improve this tool.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
```