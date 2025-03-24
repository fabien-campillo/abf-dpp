#!/bin/bash

# Ensure the script is sourced, not executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Please run with: source setup_env.sh"
    exit 1
fi

# Get the absolute path of the repository root
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set PATH and PYTHONPATH only if not already set
if [[ ":$PYTHONPATH:" != *":$REPO_ROOT/python/scripts:"* ]]; then
    export PYTHONPATH="$REPO_ROOT/python/scripts:$PYTHONPATH"
fi

if [[ ":$PATH:" != *":$REPO_ROOT/python/scripts:"* ]]; then
    export PATH="$REPO_ROOT/python/scripts:$PATH"
fi

# Print confirmation
echo "-----"
echo "Environment set up! You can now use the Python scripts from anywhere in the repository."
echo " "
echo "PATH set to: $PATH"
echo " "
echo "PYTHONPATH set to: $PYTHONPATH"
echo "-----"

# Check and install missing Python packages
python3 "$REPO_ROOT/check_dependencies.py"
