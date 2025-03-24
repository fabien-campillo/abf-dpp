#!/usr/bin/env python3
"""
ABF Data Plotting and PDF Generation

Author: Fabien Campillo
Date: 2025-02-19

This script scans a specified directory for ABF (Axon Binary Format) files, extracts and plots
the sweeps contained in each file, and saves the resulting figures into a single PDF document.

Features:
1. Recursively scans a base directory for ABF files.
2. Plots all sweeps in each file with a vertical offset.
3. Organizes the plots with up to 3 per page.
4. Generates a PDF containing all figures.
5. Allows the user to specify the resolution (`dpi`) of the output PDF.
6. Displays a progress bar using tqdm.

Requirements:
    - pyabf: For loading and reading ABF files.
    - matplotlib: For plotting and saving to PDF.
    - os, argparse, tqdm: For file handling and command-line arguments.

Usage:
    python abf_scan.py --input abf_data/ --dpi 300
"""

import os
import argparse
import pyabf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tqdm import tqdm  # Barre de progression


def plot_abf_sweeps(abf, relative_path, dpi):
    """
    Plots all sweeps from an ABF file with vertical offsets.

    Parameters:
        abf (pyabf.ABF): Loaded ABF file instance.
        relative_path (str): Path of the file relative to the base directory.
        dpi (int): Resolution of the output figure.

    Returns:
        matplotlib.figure.Figure: The created figure.
    """
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=dpi)  # Portrait format with custom DPI
    ax.set_title(f"Sweeps from {relative_path}", pad=20)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("ADC Data")

    for sweepNumber in abf.sweepList:
        abf.setSweep(sweepNumber)
        offset = 140 * sweepNumber  # Adjust offset to separate sweeps
        ax.plot(abf.sweepX, abf.sweepY + offset, color='C0', lw=0.1)

    ax.get_yaxis().set_visible(False)  # Hide Y-axis
    plt.tight_layout()
    return fig


def process_abf_directory(base_directory, output_pdf, dpi):
    """
    Scans a directory for ABF files, generates plots, and saves them into a PDF.

    Parameters:
        base_directory (str): Path to the directory containing ABF files.
        output_pdf (str): Path to the output PDF file.
        dpi (int): Resolution of the output figures.

    Returns:
        None
    """
    if not os.path.exists(base_directory):
        print(f"Error: Directory '{base_directory}' does not exist.")
        return

    abf_files = [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(base_directory)
        for filename in filenames if filename.endswith('.abf')
    ]

    if not abf_files:
        print(f"No ABF files found in '{base_directory}'.")
        return

    with PdfPages(output_pdf) as pdf:
        for abf_path in tqdm(abf_files, desc="Processing ABF files", unit="file"):
            try:
                abf = pyabf.ABF(abf_path)
                relative_path = os.path.relpath(abf_path, base_directory)
                fig = plot_abf_sweeps(abf, relative_path, dpi)
                pdf.savefig(fig, dpi=dpi)  # Save with custom DPI
                plt.close(fig)
            except Exception as e:
                print(f"\nError processing '{abf_path}': {e}")

    print(f"\nAll figures saved to {output_pdf} with {dpi} dpi.")


def main():
    """Command-line interface for the ABF data plotting script."""
    parser = argparse.ArgumentParser(description="Generate a PDF of sweeps from ABF files.")
    parser.add_argument("--input", type=str, required=True, help="Directory containing ABF files.")
    parser.add_argument("--dpi", type=int, default=300, help="Resolution (DPI) of the output PDF (default: 300).")

    args = parser.parse_args()

    if args.dpi <= 0:
        print("Error: DPI must be a positive integer.")
        return

    # Get the name of the input directory to use it as the output PDF filename
    input_dir_name = os.path.basename(os.path.normpath(args.input))
    output_pdf = f"{input_dir_name}_scan.pdf"  # Generate the output filename

    process_abf_directory(args.input, output_pdf, args.dpi)


if __name__ == "__main__":
    main()
