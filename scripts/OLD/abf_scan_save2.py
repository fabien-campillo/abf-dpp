#!/usr/bin/env python3

import os
import argparse
import pyabf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tqdm import tqdm


def get_abf_info(abf_path):
    """Extracts key metadata from an ABF file."""
    try:
        abf = pyabf.ABF(abf_path)
        return {
            "Filename": os.path.basename(abf_path),
            "Sweeps": len(abf.sweepList),
            "Channels": abf.channelCount,
            "Sampling Rate (Hz)": abf.dataRate,
            "Duration (s)": abf.dataLengthSec,
            "AD Units": abf.adcUnits,
            "ADC Names": abf.adcNames,
        }
    except Exception as e:
        return {"Filename": os.path.basename(abf_path), "Error": str(e)}


def scan_abf_files(input_path):
    """Scans a directory or file for ABF metadata."""
    abf_files = []

    if os.path.isdir(input_path):
        # Scan all ABF files in the directory (recursive)
        abf_files = [
            os.path.join(dirpath, filename)
            for dirpath, _, filenames in os.walk(input_path)
            for filename in filenames if filename.endswith('.abf')
        ]
    elif os.path.isfile(input_path) and input_path.endswith('.abf'):
        abf_files = [input_path]
    elif '*' in input_path:
        # Handle wildcard inputs like '*.abf'
        abf_files = [f for f in sorted(glob.glob(input_path)) if f.endswith('.abf')]

    if not abf_files:
        print(f"❌ No ABF files found in '{input_path}'.")
        return []

    # Extract metadata for each ABF file
    metadata = [get_abf_info(f) for f in tqdm(abf_files, desc="Scanning ABF files", unit="file")]

    # Print summary
    print("\n📜 ABF File Summary:")
    for entry in metadata:
        print(entry)

    return abf_files, metadata


def plot_abf_sweeps(abf, title, dpi):
    """Plots all sweeps from an ABF file with vertical offsets."""
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=dpi)
    ax.set_title(f"Sweeps from {title}", pad=20)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("ADC Data")

    for sweepNumber in abf.sweepList:
        abf.setSweep(sweepNumber)
        offset = 140 * sweepNumber
        ax.plot(abf.sweepX, abf.sweepY + offset, color='C0', lw=0.1)
        ax.text(abf.sweepX[-1], abf.sweepY[-1] + offset, f"Sweep {sweepNumber}",
                color='red', fontsize=8, va='center', ha='left')

    ax.get_yaxis().set_visible(False)
    plt.tight_layout()
    return fig


def generate_pdf(abf_files, output_pdf, dpi):
    """Generates a PDF with plots from ABF files."""
    with PdfPages(output_pdf) as pdf:
        for abf_path in tqdm(abf_files, desc="Generating PDF", unit="file"):
            try:
                abf = pyabf.ABF(abf_path)
                fig = plot_abf_sweeps(abf, os.path.basename(abf_path), dpi)
                pdf.savefig(fig, dpi=dpi)
                plt.close(fig)
            except Exception as e:
                print(f"⚠️ Error processing '{abf_path}': {e}")

    print(f"\n✅ PDF saved to {output_pdf} with {dpi} dpi.")


def main():
    """Command-line interface for the ABF scan script."""
    parser = argparse.ArgumentParser(description="📊 Scan and optionally plot ABF files.")
    parser.add_argument("-i", "--input", type=str, required=True, metavar="FILE/DIR",
                        help="📂 Path to an ABF file, directory, or a wildcard pattern.")
    parser.add_argument("-p", "--pdf", nargs="?", const=True, metavar="OUTPUT_PDF",
                        help="📌 Generate a PDF of sweeps. Optional custom filename.")
    parser.add_argument("--dpi", type=int, default=300, metavar="DPI",
                        help="📌 Resolution (DPI) of the output PDF (default: 300).")

    args = parser.parse_args()

    # Scan for ABF files
    abf_files, metadata = scan_abf_files(args.input)
    if not abf_files:
        return

    # Handle PDF output
    if args.pdf:
        if isinstance(args.pdf, str):
            output_pdf = args.pdf
        else:
            base_name = os.path.basename(os.path.normpath(args.input))
            output_pdf = f"{base_name}_scan.pdf" if os.path.isdir(args.input) else f"{base_name}.pdf"

        generate_pdf(abf_files, output_pdf, args.dpi)


if __name__ == "__main__":
    main()
