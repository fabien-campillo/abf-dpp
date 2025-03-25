import os
import inspect
import importlib.util

SCRIPTS_DIR = "python/scripts"
HELP_FILE = os.path.join(SCRIPTS_DIR, "purpose.txt")


def get_user_functions(module_path):
    """Extracts functions marked as user functions (with # USER FUNCTION)."""
    user_functions = []

    with open(module_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    marked_functions = set()
    for i, line in enumerate(lines):
        if "# USER FUNCTION" in line:
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if "def " in next_line:
                function_name = next_line.split("def ")[1].split("(")[0]
                marked_functions.add(function_name)

    if not marked_functions:
        print(f"⚠️ No user functions found in {module_path}. Check the `# USER FUNCTION` markers.")
        return []

    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name, func in inspect.getmembers(module, inspect.isfunction):
        if name in marked_functions:
            doc = inspect.getdoc(func)
            first_line = doc.split("\n")[0] if doc else "No description available."
            user_functions.append((name, first_line, module_path, func))

    return user_functions


def list_available_functions():
    """Lists all user-marked functions in `python/scripts/`, ignoring non-Python files."""
    available_functions = []

    for file in os.listdir(SCRIPTS_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            module_path = os.path.join(SCRIPTS_DIR, file)
            available_functions.extend(get_user_functions(module_path))

    return available_functions


def display_help():
    """Displays the help file if available."""
    if os.path.exists(HELP_FILE):
        with open(HELP_FILE, "r", encoding="utf-8") as f:
            print("\n📖 Help Information:\n")
            print(f.read())
    else:
        print("\n⚠️ No help file found.")


def execute_function(func):
    """Executes a function, handling arguments if required."""
    sig = inspect.signature(func)

    if len(sig.parameters) == 0:
        func()
    else:
        print(f"\n⚠️ Function `{func.__name__}` requires arguments: {sig}.")
        print("Modify the script to handle arguments if necessary.")


def menu():
    """Displays a menu of available user functions."""

    functions = list_available_functions()

    if not functions:
        print("❌ No user functions found in `python/scripts/`.")
        return

    while True:
        print("\n📜 Available Functions:\n")
        for i, (func_name, description, _, _) in enumerate(functions, 1):
            print(f"  {i}. {func_name} - {description}")

        print(f"  {len(functions) + 1}. Help - Display general information")
        print(f"  {len(functions) + 2}. Exit")

        choice = input("\n🔹 Select an option: ").strip()

        if not choice.isdigit():
            print("⚠️ Please enter a valid number.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(functions):
            func_name, _, module_path, func = functions[choice - 1]
            module_name = os.path.splitext(os.path.basename(module_path))[0]
            print(f"\n🚀 Running {func_name} from {module_name}...\n")
            execute_function(func)
        elif choice == len(functions) + 1:
            display_help()
        elif choice == len(functions) + 2:
            print("\n👋 Exiting menu.\n")
            break
        else:
            print("⚠️ Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    menu()
