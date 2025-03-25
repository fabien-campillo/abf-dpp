#!/usr/bin/env python3
import argparse
import matplotlib.pyplot as plt
import pyabf  # Ensure this package is installed
import sys


def plot_abf_sweeps(file_path, color='b', linewidth=0.1, offset_step=140, figsize=(8, 5)):
    """
    Plot all sweeps from an ABF file with a vertical offset.

    Parameters:
        file_path: str, path to the ABF file.
        color: str, color of the sweeps (default: 'b' for blue).
        linewidth: float, width of the lines (default: 0.1).
        offset_step: float, vertical offset between sweeps (default: 140).
        figsize: tuple, figure size (default: (8, 5)).
    """
    abf = pyabf.ABF(file_path)

    plt.figure(figsize=figsize)

    # Plot each sweep with an increasing vertical offset
    for sweepNumber in abf.sweepList:
        abf.setSweep(sweepNumber)
        offset = offset_step * sweepNumber
        plt.plot(abf.sweepX, abf.sweepY + offset, color=color, lw=linewidth)

    # Decorate the plot
    plt.gca().get_yaxis().set_visible(False)  # Hide Y axis
    plt.title(file_path)
    plt.xlabel(abf.sweepLabelX)
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Plot ABF sweeps with vertical offsets.",
        usage="abf_plot file_path [options]"
    )

    parser.add_argument("file_path", nargs="?", help="Path to the ABF file")  # Positional argument
    parser.add_argument("-c", "--color", default="b", help="Line color (default: blue)")
    parser.add_argument("-lw", "--linewidth", type=float, default=0.1, help="Line width (default: 0.1)")
    parser.add_argument("-o", "--offset", type=float, default=140, help="Vertical offset between sweeps (default: 140)")

    args = parser.parse_args()

    if not args.file_path:
        print("Error: file_path is required!\n")
        parser.print_help()
        sys.exit(1)

    plot_abf_sweeps(args.file_path, color=args.color, linewidth=args.linewidth, offset_step=args.offset)


if __name__ == "__main__":
    main()
