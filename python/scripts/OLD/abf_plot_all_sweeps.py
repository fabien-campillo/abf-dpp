#!/usr/bin/env python3
"""
ABF Data Visualization: Plot all sweeps with a vertical offset.

Author: Fabien Campillo
Date: 2025-02-19
License: CC BY-NC
Version: 1.0.0

Description:
    This script plots all sweeps from an ABF (Axon Binary File) with an increasing vertical offset.

Requirements:
    - matplotlib
    - pyabf

Usage (Command Line):
    python abf_plot_all_sweeps.py path/to/file.abf

Usage (Python Import):
    import pyabf
    from abf_plot_all_sweeps import abf_plot_all_sweeps

    abf = pyabf.ABF("path/to/file.abf")
    abf_plot_all_sweeps(abf)
"""

import sys
import matplotlib.pyplot as plt
import pyabf

__author__ = "Fabien Campillo"
__date__ = "2025-02-19"
__version__ = "1.0.0"
__license__ = "CC BY-NC"
__description__ = "Utility for visualizing electrophysiology sweeps from ABF files."

# USER FUNCTION
def abf_plot_all_sweeps(abf, offset_step=100):
    """
    Plot all sweeps from an ABF (Axon Binary File) with a vertical offset.

    Parameters:
        abf (pyabf.ABF): An instance of the pyABF class representing the ABF file.
                         The file should be properly loaded before calling this function.
        offset_step (int, optional): Step size for vertical offset between sweeps. Default is 100.

    Raises:
        ValueError: If the `abf` parameter is not a valid `pyabf.ABF` instance.

    Notes:
        - Each sweep is offset vertically by `offset_step` units per sweep index to prevent overlap.
        - The Y-axis is hidden for clarity.
        - The file path is displayed as the plot title.
        - The function does not return any values but directly displays the plot.
    """
    if not isinstance(abf, pyabf.ABF):
        raise ValueError("Invalid input: 'abf' must be an instance of pyabf.ABF.")

    plt.figure(figsize=(12, 8))

    # Plot each sweep with a vertical offset
    for sweepNumber in abf.sweepList:
        abf.setSweep(sweepNumber)
        offset = 100 * sweepNumber
        plt.plot(abf.sweepX, abf.sweepY + offset, color='b', lw=0.1)

    # Customize plot appearance
    plt.gca().get_yaxis().set_visible(False)  # Hide Y-axis
    plt.title(abf.abfFilePath)  # Use the file path as the title
    plt.xlabel(abf.sweepLabelX, color='w')  # Use the X-axis label from the ABF file
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python abf_plot_all_sweeps.py path/to/file.abf")
        sys.exit(1)

    abf_path = sys.argv[1]

    try:
        abf = pyabf.ABF(abf_path)
        abf_plot_all_sweeps(abf)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)