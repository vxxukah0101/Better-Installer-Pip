import os
import re
import subprocess
import sys
import time
import argparse

def find_imports_in_file(file_path):
    """Find all imported modules in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        imports = re.findall(r'^\s*(?:import|from)\s+([\w\.]+)', content, re.MULTILINE)
        return imports
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def is_module_installed(module_name):
    """Check if a module is installed."""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def install_module(module_name):
    """Install a module using pip with a loading animation."""
    print(f"Installing module: {module_name}")
    animation = "|/-\\"
    idx = 0
    process = subprocess.Popen([sys.executable, "-m", "pip", "install", module_name],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while process.poll() is None:
        sys.stdout.write("\r" + animation[idx % len(animation)] + " Installing...")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\rDone!                \n")
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Failed to install {module_name}. Error: {stderr.decode().strip()}")
    else:
        print(f"Successfully installed {module_name}.")

def list_python_files(directory, exclude_file):
    """List all Python files in the directory, excluding a specific file."""
    return [f for f in os.listdir(directory) if f.endswith('.py') and f != exclude_file and os.path.isfile(os.path.join(directory, f))]

def process_file(file_path):
    """Process a single Python file to find and install missing modules."""
    print(f"Processing file: {file_path}")
    imports = find_imports_in_file(file_path)
    missing_modules = [module for module in imports if not is_module_installed(module)]

    if missing_modules:
        print("\nModules to be installed:")
        for idx, module in enumerate(missing_modules, start=1):
            print(f"{idx}. {module}")
        
        input("\nPress Enter to install all missing modules...")
        for module in missing_modules:
            install_module(module)
    else:
        print("\nAll required modules are already installed.")

def process_all_files(directory, exclude_file):
    """Process all Python files in the directory to find and install missing modules."""
    python_files = list_python_files(directory, exclude_file)

    print("Python files detected:")
    for file in python_files:
        print(f"- {file}")
    
    input("\nPress Enter to analyze and list missing modules...")

    all_imports = set()
    for file in python_files:
        file_path = os.path.join(directory, file)
        all_imports.update(find_imports_in_file(file_path))
    
    missing_modules = [module for module in all_imports if not is_module_installed(module)]

    if missing_modules:
        print("\nModules to be installed:")
        for idx, module in enumerate(missing_modules, start=1):
            print(f"{idx}. {module}")
        
        input("\nPress Enter to install all missing modules...")
        for module in missing_modules:
            install_module(module)
    else:
        print("\nAll required modules are already installed.")

def main():
    """Main function to process files in the directory or a specific file."""
    parser = argparse.ArgumentParser(
        description="A script to analyze Python files and install missing modules."
    )
    parser.add_argument(
        "-f", "--file", 
        help="Specify a single Python file to process. Example: python src.py -f main.py"
    )
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_file = os.path.basename(__file__)

    if args.file:
        # Process only the specified file
        file_path = os.path.join(current_dir, args.file)
        if not os.path.isfile(file_path) or not args.file.endswith('.py'):
            print(f"Error: {args.file} is not a valid Python file.")
            return
        process_file(file_path)
    else:
        # Process all Python files in the directory
        process_all_files(current_dir, current_file)

if __name__ == "__main__":
    main()
