# Python Module Auto-Installer

This repository contains a Python script (`src.py`) designed to analyze Python files in the same directory, detect missing modules, and automatically install them using `pip`. It also includes a sample `main.py` file for testing purposes.

## Features

- Detects all Python files in the directory (excluding itself).
- Analyzes `import` statements to identify required modules.
- Checks if the modules are already installed.
- Automatically installs missing modules using `pip`.
- Supports processing a specific file or all files in the directory.
- Provides a user-friendly interface with clear prompts and progress animations.

## Files

- **`src.py`**: The main script that performs the module detection and installation.
- **`main.py`**: A sample Python file with various imports for testing purposes.

## Requirements

- Python 3.6 or higher
- `pip` (Python package manager)

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Run the Script

#### Process All Python Files in the Directory

To analyze all Python files in the directory and install missing modules:

```bash
python src.py
```

- The script will list all detected Python files.
- After pressing Enter, it will analyze the files and display a list of missing modules.
- Press Enter again to install the missing modules.

#### Process a Specific Python File

To analyze and install missing modules for a specific file:

```bash
python src.py -f main.py
```

- Replace `main.py` with the name of the file you want to process.
- The script will display the missing modules for the specified file and prompt you to install them.

### 3. Help Command

To view the available commands and usage instructions:

```bash
python src.py --help
```

### Example Output

#### Processing All Files

```plaintext
Python files detected:
- main.py

Press Enter to analyze and list missing modules...

Modules to be installed:
1. requests
2. discord-py

Press Enter to install all missing modules...
Installing module: requests
Done!
Installing module: discord-py
Done!
```

#### Processing a Specific File

```plaintext
Processing file: main.py

Modules to be installed:
1. requests
2. discord-py

Press Enter to install all missing modules...
Installing module: requests
Done!
Installing module: discord-py
Done!
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
