# UE Config Tool

A user-friendly Command-Line Interface (CLI) tool designed to help you **visualize** and **edit key-value pairs** in Unreal Engine configuration files. This tool makes it easy to navigate, modify, and manage complex configuration data without requiring manual file editing.

---

## Features
- **Visualize Configuration Data**: Displays config sections and their keys in a clean, organized format.
- **Edit Configurations**: Modify key-value pairs easily through intuitive prompts.
- **Key Mapping Insights**: Displays `ActionMappings` and `AxisMappings` in a structured manner, showing device types and key details.
- **Error Handling**: Provides clear messages for invalid inputs or incorrect data formats.
- **Interactive Menu**: Navigate through config sections seamlessly using numeric or text-based input.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ue-config-tool.git
   cd ue-config-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
Run the CLI tool:
```bash
python main.py
```

### Key Commands
- **View Config Sections**: Lists all available sections from the config file.
- **Open Section**: Enter the section name or index to view its keys and values.
- **Edit Key-Value Pairs**: Follow on-screen instructions to modify specific keys.

---

## Example Output
### Main Menu
```plaintext
[CONFIG] default - Type the section name to open it
==========================================
ID    Section Name                
------------------------------------------
[0]   ActionMappings             
[1]   AxisMappings               
==========================================
```

### Viewing a Section
```plaintext
Key                                     Value
-----------------------------------------------
ActionMappings                          10 entries
AxisMappings                            8 entries
```

### Detailed Key View
```plaintext
[Jump]
Key: SpaceBar
Shift: False
Ctrl: False
Alt: False
Cmd: False
```

---

## Supported "Complex" Config Keys
The tool supports two key types:
1. **ActionMappings**: Displays `ActionName`, `Key`, and optional modifier states like `Shift`, `Ctrl`, etc.
2. **AxisMappings**: Displays `AxisName`, `Key`, and `Scale` values.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Issues
If you encounter any bugs or have feature requests, please open an issue on the [GitHub Issues page](https://github.com/mersadze/ue-config-tool/issues).

---

### Contact
For questions or suggestions, reach out [GitHub](https://github.com/mersadze).
```