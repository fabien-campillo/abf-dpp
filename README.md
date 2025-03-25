# PEPYNA: 

### *Python-based Electrophysiology Neuron Yield & Analysis*


This project focuses on analyzing **electrophysiology data**, initially starting with `ABF` files, and potentially expanding to other formats. It involves processing, plotting, and basics statistical analysis of **single-neuron data** using Python scripts and notebooks. Scripts are designed for `macOS`. The goal is to provide efficient tools for researchers in neurophysiology, facilitating data exploration and visualization.



**Purpose:** 
A set of Python tools (scripts and notebooks) for analyzing electrophysiology data.

## Structure

```
abf-dpp_github/
├── LICENSE                # licence file
├── README.md              # this file
├── check_dependencies.py  # checks required dependencies for execution
├── data/                  # data to analyze or already analyzed (*)
├── docs_hub/              # jupyter book and latex 
├── notebooks/             # notebooks (*)
├── python-lib/            # Python library (core functionalities) (*)
├── sandbox/               # tests
├── scripts/               # scripts for os-x shell (*)
└── setup_env.sh           # script to set up environment

(*) The tools are in notebooks/ and scripts/, data/ contains also 
    notebooks to analyze the data. 
    
Each subdirectory includes a README.md file.

```


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
