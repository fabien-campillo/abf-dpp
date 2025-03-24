# Documentation for abf_plot_single_sweep.py

### Function: abf_plot_single_sweep

```python
def abf_plot_single_sweep(abf, num_of_sweep=0, xlim_min=None, xlim_max=None):
    """
    Plot a specific sweep from an ABF (Axon Binary File) with customizable X-axis limits.

    Parameters:
        abf (pyabf.ABF): A loaded ABF file instance.
        num_of_sweep (int): The sweep number to plot (default is 0).
        xlim_min (float, optional): The minimum value for the X-axis.
        xlim_max (float, optional): The maximum value for the X-axis.

    Raises:
        ValueError: If `num_of_sweep` is out of range or X-axis limits are incorrect.
        TypeError: If `abf` is not an instance of `pyabf.ABF`.
    """
    if not isinstance(abf, pyabf.ABF):
        raise TypeError("Expected a pyabf.ABF instance.")

    if num_of_sweep not in abf.sweepList:
        raise ValueError(f"Sweep number {num_of_sweep} is out of range (0-{len(abf.sweepList)-1}).")

    if xlim_min is not None and xlim_max is not None and xlim_min >= xlim_max:
        raise ValueError("xlim_min must be smaller than xlim_max.")

    plt.figure(figsize=(8, 5))
    plt.ylabel(abf.sweepLabelY)
    plt.xlabel(abf.sweepLabelX)

    abf.setSweep(num_of_sweep)
    plt.plot(abf.sweepX, abf.sweepY, alpha=1, lw=0.1)

    if xlim_min is not None and xlim_max is not None:
        plt.xlim((xlim_min, xlim_max))

    plt.show()
```

Plot a specific sweep from an ABF (Axon Binary File) with customizable X-axis limits.

Parameters:
    abf (pyabf.ABF): A loaded ABF file instance.
    num_of_sweep (int): The sweep number to plot (default is 0).
    xlim_min (float, optional): The minimum value for the X-axis.
    xlim_max (float, optional): The maximum value for the X-axis.

Raises:
    ValueError: If `num_of_sweep` is out of range or X-axis limits are incorrect.
    TypeError: If `abf` is not an instance of `pyabf.ABF`.

### Function: main

```python
def main():
    """Command-line interface for plotting a single sweep from an ABF file."""
    parser = argparse.ArgumentParser(description="Plot a single sweep from an ABF file.")
    parser.add_argument("abf_file", type=str, help="Path to the ABF file.")
    parser.add_argument("--sweep", type=int, default=0, help="Sweep number to plot (default: 0).")
    parser.add_argument("--xmin", type=float, default=None, help="Minimum X-axis limit.")
    parser.add_argument("--xmax", type=float, default=None, help="Maximum X-axis limit.")

    args = parser.parse_args()

    # Vérifier si le fichier existe
    if not os.path.exists(args.abf_file):
        print(f"Error: File '{args.abf_file}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        abf = pyabf.ABF(args.abf_file)
        abf_plot_single_sweep(abf, args.sweep, args.xmin, args.xmax)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```

Command-line interface for plotting a single sweep from an ABF file.
