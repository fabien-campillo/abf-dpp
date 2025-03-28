# PEPYNA

## *Python-based Electrophysiology Neuron Yield & Analysis*


This project focuses on analyzing **electrophysiology data**, initially starting with `ABF` files, and potentially expanding to other formats. It involves processing, plotting, and basics statistical analysis of **single-neuron data** using Python scripts and notebooks. Scripts are designed for `macOS`. The goal is to provide efficient tools for researchers in neurophysiology, facilitating data exploration and visualization.



**Purpose:** 
A set of Python tools (scripts and notebooks) for analyzing electrophysiology data.

## Structure

```
   abf-dpp_github/
   ├── LICENSE                # licence file
   ├── README.md              # this file
   ├── check_dependencies.py  # checks required dependencies for execution
*  ├── data/                  # data to analyze or already analyzed (*)
~  ├── docs_hub/              # jupyter book and latex 
*  ├── notebooks/             # notebooks (*)
~  ├── python_lib/            # Python library (core functionalities) (*)
   ├── sandbox/               # tests
*  ├── scripts/               # scripts for os-x shell (*)
   └── setup_env.sh           # script to set up environment

(*) these dirs already contain some tools 
(~) in contruction
    
Each subdirectory includes a README.md file.

```

