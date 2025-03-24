# ABF-DPP
## *ABF Data Processing and Plotting*

*Tools to analyze `abf` files and directories containing `abf` files.*  

## Install

If you want to use the script all around, you should do

```bash
source setup_env.sh
```

each time you start to work around `abf` data. The script will also check, using `check_dependencies.py` if you have all the python packages for running the abf-dpp scripts and propose to install the missing ones.


## Structure

```
LICENSE: licence file
menu.py: a python script for the user
setup_env.sh: the setup script (to run when starting a session)
check_dependencies.py: check if you have all the required python 
   packages (used by setup_env.sh).

abf-dpp$ tree -L 3 ../abf-dpp/
../abf-dpp/
├── LICENSE
├── README.md
├── abf_data/              # abf data (for tests)
├── check_dependencies.py 
├── docs/                  # jupyter book in progress
├── latex/                 # paper in progress 
├── menu.py
├── python
│   ├── LHB.ipynb
│   ├── LHB_fabien.ipynb
│   ├── abf_scan.ipynb
│   ├── abf_scan_Nov24.ipynb
│   ├── abf_scan_final_example.ipynb
│   ├── abf_scan_final_example_old.ipynb
│   └── scripts
│       ├── README.md
│       ├── __pycache__
│       ├── abf_scan
│       └── purpose.txt
├── python_sandbox         # sand box
└── setup_env.sh
```

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



<br>
<br>
---

Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)

Copyright (c) 2025 Fabien Campillo

You are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes, unless you get permission from the author.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

You can find the full text of the license at:
https://creativecommons.org/licenses/by-nc/4.0/
