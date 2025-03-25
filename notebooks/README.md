# PEPYNA


*Tools to analyze `abf` files and directories containing `abf` files.*  


The directory contains `python notebooks` and a directory of `python scripts`. Scripts are first studied/developed in notebooks, then, if useful, factorized as python functions in `scripts/`.

```
python
├── 1_lhb.ipynb
├── 1_lhb_correlated.ipynb
├── 2_abf_scan.ipynb
├── 2_abf_scan_2024_11_24.ipynb
├── 2_abf_scan_final_example.ipynb
├── 2_abf_scan_final_example_old.ipynb
├── README.md
├── bifurcation_diagram.dat           # bif. diag. with XPP 
└── scripts
```

## Notebooks

- **`1_lhb`**: ODE + SDE 
	- `1_lhb.ipynb` first version: 

		* Hindmarsh-Rose bursting model in a 4D ODE
		* trajectories and bifurcation diagrams
		* SDE model with diagonal diffusion matrix

	- `1_lhb_correlated.ipynb`

		* same than `1_lhb.ipynb` but with correlated noise
		* non diagonal diffusion matrix

- **`2_abf_scan`** scanning and plotting abf directories 
	- `2_abf_scan.ipynb`
	- `2_abf_scan_2024_11_24.ipynb` an improved version
	- `2_abf_scan_final_example.ipynb`
	- `2_abf_scan_final_example_old.ipynb`