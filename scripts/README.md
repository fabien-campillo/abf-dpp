# python scripts for PEPYNA
 
This directory contains pythons functions.

The one that are dedicated to the users should be preceded by `# USER FUNCTION`, eg:

```
# USER FUNCTION
def abf_scan():
    """Command-line interface for the ABF data plotting script."""
    parser = argparse.ArgumentParser(description="Generate a PDF of sweeps from ABF files.")
```

> `abf_scan` is just a symbolic link to `abf_scan.py` (so we can just run  `abf_scan <name>`) 

They are other functions not directly used by the users. The one preceded by `# USER FUNCTION` will appear in the menu proposed by `menu.py`. [to be done]



<br>
<br>
## `abf_scan.py`

> `abf_scan.py` is a python script. `abf_scan` is just a symbolic link to `abf_scan.py` (so we can just run  `abf_scan <name>`). Nota: it's very much `ChatGPT`-generated, but under my highly capable and clever supervision! 😶


```
usage: abf_scan [-h] [-v] [-l] [-p] [--dpi DPI] [-s N] FILE_OR_DIR

📊 Scan ABF files, extract metadata, and optionally save plots to PDF.

positional arguments:
  FILE_OR_DIR      📂 Path to an ABF file or directory containing ABF files.

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  -l, --long       📋 Show extended metadata details.
  -p, --pdf        📄 Save plots into a PDF file.
  --dpi DPI        📌 Resolution (DPI) of the output PDF (default: 300).
  -s N, --sweep N  🎚️ Plot only sweep N (valid only for single ABF file). 
```
