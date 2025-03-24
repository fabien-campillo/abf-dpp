import os
import re
import sys
import subprocess

SCRIPTS_DIR = "python/scripts"

def get_imported_packages():
    """Extracts all imported packages from Python scripts in SCRIPTS_DIR."""
    imported_packages = set()
    pattern = re.compile(r"^\s*(?:import|from)\s+([a-zA-Z0-9_]+)")

    for file in os.listdir(SCRIPTS_DIR):
        if file.endswith(".py"):
            with open(os.path.join(SCRIPTS_DIR, file), "r", encoding="utf-8") as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        imported_packages.add(match.group(1))

    return imported_packages

def check_missing_packages(packages):
    """Checks which packages are missing and prompts for installation."""
    missing = []
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)

    if not missing:
        print("✅ All required Python packages are installed.")
        return

    print("⚠️ Missing Python packages detected:")
    for pkg in missing:
        print(f"  - {pkg}")

    choice = input("\nDo you want to install them now? (y/n): ").strip().lower()
    if choice == "y":
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing, check=True)
        print("\n✅ All missing packages have been installed.")
    else:
        print("\n⚠️ Some scripts may not work correctly until you install the missing packages.")

if __name__ == "__main__":
    required_packages = get_imported_packages()
    check_missing_packages(required_packages)
