#!/usr/bin/env python3
"""
ABF File Scanner and Plotter

Author: Fabien Campillo
Date: 2025-02-19
Version: 1.0.0

This script scans ABF (Axon Binary Format) files in a specified directory or processes a single file.
It extracts metadata and can save plots to a PDF.

Features:
1. Lists ABF file metadata (number of sweeps, sampling rate, etc.).
2. With `--long (-l)`, displays extended metadata including:
   - Recording Information
   - Time & Date Information
   - Software & Hardware Details
3. Saves plots into a PDF with `--pdf (-p)`.
4. Supports directory scanning (recursive with `-r`).
5. Works in terminal, Python scripts, and Jupyter notebooks.

Requirements:
    - pyabf: For loading and reading ABF files.
    - matplotlib: For plotting and saving to PDF.
    - os, argparse, tqdm: For file handling and command-line arguments.

Usage:
    python abf_scan.py test1/cell209basal.abf
    python abf_scan.py --long test1/cell209basal.abf
    python abf_scan.py --pdf test1.pdf test1

Nota: it's very much `ChatGPT`-generated, but under my highly capable and clever supervision! 😶
"""

import os
import argparse
import pyabf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tqdm import tqdm


def extract_abf_metadata(abf_path, long=False):
    """
    Extracts metadata from an ABF file.
    """
    abf = pyabf.ABF(abf_path)
    metadata = {
        "Filename": os.path.basename(abf_path),
        "Sweeps": len(abf.sweepList),
        "Sampling Rate (Hz)": abf.dataRate,
    }

    if long:
        metadata.update({
            "Sweep Length (s)": abf.sweepLengthSec,
            "Channels": abf.channelCount,
            "Channel Names": abf.adcNames,
            "Units": abf.adcUnits,
            "Protocol": abf.protocol,
            "Experiment Type": getattr(abf, "fileGUID", "N/A"),
            "ADC Resolution (bits)": getattr(abf, "adcBits", "N/A"),
            "Recording Date": abf.abfDateTime,
            "Elapsed Time (s)": abf.sweepCount * abf.sweepLengthSec,
            "Software Version": abf.abfVersionString,
            "Amplifier": abf.tagComments,
        })

    return metadata


def print_abf_metadata(metadata):
    """
    Prints extracted ABF metadata.
    """
    print("\n📊 ABF File Metadata:")
    for key, value in metadata.items():
        print(f"  - {key}: {value}")


def generate_pdf_filename(input_path, sweep=None):
    """
    Generates the PDF filename based on input path and sweep number.
    """
    dir_name = "_".join(os.path.dirname(input_path).split(os.sep))
    base_name = os.path.basename(input_path).replace(".", "_")
    pdf_name = f"{dir_name}_{base_name}.pdf" if dir_name else f"{base_name}.pdf"

    if sweep is not None:
        pdf_name = pdf_name.replace(".pdf", f"_sweep{sweep}.pdf")

    return pdf_name


def plot_abf_sweeps(abf_path, figure_index, save_pdf=None, dpi=300, sweep=None):
    """
    Plots all sweeps from an ABF file with one subplot per sweep.
    """
    line_width = 0.1
    line_color = 'red'
    abf = pyabf.ABF(abf_path)
    sweeps_to_plot = [sweep] if sweep is not None else abf.sweepList

    if not sweeps_to_plot:
        print(f"No sweeps to plot in {abf_path}.")
        return

    fig, axes = plt.subplots(len(sweeps_to_plot), 1, figsize=(8, 2 * len(sweeps_to_plot)))
    fig.suptitle(f"{os.path.basename(abf_path)} - All Sweeps")

    if len(sweeps_to_plot) == 1:
        axes = [axes]

    for i, ax in zip(sweeps_to_plot, axes):
        abf.setSweep(i)
        ax.plot(abf.sweepX, abf.sweepY, label=f"Sweep {i}", color=line_color, linewidth=line_width)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Current (pA)" if abf.sweepUnitsY == "pA" else "Voltage (mV)")
        ax.legend()
        ax.grid()

    if save_pdf:
        try:
            with PdfPages(save_pdf) as pdf:
                pdf.savefig(fig, dpi=dpi)
            print(f"📄 Plots saved to {save_pdf}")
        except Exception as e:
            print(f"Error saving PDF: {e}")
        plt.close(fig)
    else:
        plt.figure(figure_index)
        plt.show()


def scan_abf(input_path, long=False, save_pdf=None, dpi=300, sweep=None):
    """
    Scans ABF files and optionally saves plots to PDF.
    """
    if os.path.isdir(input_path):
        abf_files = [
            os.path.join(root, f)
            for root, _, files in os.walk(input_path)
            for f in files if f.endswith(".abf")
        ]
        if not abf_files:
            print(f"No ABF files found in '{input_path}'.")
            return

        for index, abf_file in enumerate(abf_files, start=1):
            metadata = extract_abf_metadata(abf_file, long)
            print_abf_metadata(metadata)
            if save_pdf:
                pdf_filename = generate_pdf_filename(abf_file)
                plot_abf_sweeps(abf_file, index, pdf_filename, dpi)
    elif os.path.isfile(input_path) and input_path.endswith(".abf"):
        metadata = extract_abf_metadata(input_path, long)
        print_abf_metadata(metadata)
        if save_pdf:
            pdf_filename = generate_pdf_filename(input_path, sweep)
            plot_abf_sweeps(input_path, 1, pdf_filename, dpi, sweep)
    else:
        print(f"Invalid input: '{input_path}' is not a valid ABF file or directory.")


def main():
    """
    Command-line interface for scanning ABF files.
    """
    parser = argparse.ArgumentParser(
        description="📊 Scan ABF files, extract metadata, and optionally save plots to PDF."
    )
    parser.add_argument("-v", "--version", action="version", version="ABF File Scanner 1.0.0")
    parser.add_argument("input", type=str, metavar="FILE_OR_DIR",
                        help="📂 Path to an ABF file or directory containing ABF files.")
    parser.add_argument("-l", "--long", action="store_true", help="📋 Show extended metadata details.")
    parser.add_argument("-p", "--pdf", action="store_true", help="📄 Save plots into a PDF file.")
    parser.add_argument("--dpi", type=int, default=300, metavar="DPI",
                        help="📌 Resolution (DPI) of the output PDF (default: 300).")
    parser.add_argument("-s", "--sweep", type=int, metavar="N",
                        help="🎚️ Plot only sweep N (valid only for single ABF file).")
    args = parser.parse_args()

    scan_abf(args.input, args.long, args.pdf, args.dpi, args.sweep)


if __name__ == "__main__":
    main()
    