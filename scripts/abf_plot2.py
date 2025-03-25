#!/usr/bin/env python3
import matplotlib.pyplot as plt
from IPython.display import display

def plot_abf_sweeps(abf, file_path, offset=140, color='b', lw=0.1):
    """
    Plots all sweeps of an ABF file with vertical offsets.
    
    Parameters:
    - abf: The ABF object
    - file_path: Path to the ABF file (for the plot title)
    - offset: Vertical offset between sweeps
    - color: Line color for the plot
    - lw: Line width
    """
    # Create the figure
    plt.figure(figsize=(8, 5))

    # Plot every sweep (with vertical offset)
    for sweepNumber in abf.sweepList:
        abf.setSweep(sweepNumber)
        plt.plot(abf.sweepX, abf.sweepY + offset * sweepNumber, color=color, lw=lw)

    # Decorate the plot
    plt.gca().get_yaxis().set_visible(False)  # Hide Y axis
    plt.title(file_path)
    plt.xlabel(abf.sweepLabelX)

    # Show the plot in Jupyter Notebook (inline) or in the terminal
    if 'ipykernel' in sys.modules:  # Check if running in a Jupyter notebook
        plt.show()  # In Jupyter, show the plot inline
    else:
        # In terminal (Unix), save the plot as a PDF
        plt.savefig(file_path.replace('.abf', '_sweeps.pdf'))
        print(f"Plot saved as {file_path.replace('.abf', '_sweeps.pdf')}")

    # Close the plot to avoid memory issues
    plt.close()
