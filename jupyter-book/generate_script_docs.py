import os
import ast

# Adjust paths to work within the docs directory
scripts_dir = '../scripts/'  # Going up one level to access the scripts directory
output_dir = './scripts/'    # Save markdown files in docs/scripts

# Create output_dir if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop over all Python files in the scripts directory
for filename in os.listdir(scripts_dir):
    if filename.endswith('.py'):
        with open(os.path.join(scripts_dir, filename), 'r') as file:
            content = file.read()
            # Parse the Python file to extract docstrings
            tree = ast.parse(content)
            docstrings = []

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    docstrings.append(f"### Function: {node.name}\n")
                    docstrings.append(f"```python\n{ast.get_source_segment(content, node)}\n```\n")
                    if ast.get_docstring(node):
                        docstrings.append(f"{ast.get_docstring(node)}\n")

            # Create markdown file for this script
            doc_filename = f"{filename.replace('.py', '.md')}"
            with open(os.path.join(output_dir, doc_filename), 'w') as md_file:
                md_file.write(f"# Documentation for {filename}\n\n")
                md_file.write("\n".join(docstrings))
