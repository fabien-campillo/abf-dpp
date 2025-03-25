#!/usr/bin/env python3

"""
List ABF Files with Metadata

Author: Fabien Campillo
Date: 2025-03-03

This script scans a specified directory for ABF (Axon Binary Format) files
and displays metadata such as the number of sweeps, sampling rate, duration, 
number of channels, and other relevant information.

Usage:
    python list_abf_metadata.py --input abf_data/
"""

import os
import argparse
import pyabf

def get_abf_metadata(abf_path):
    """
    Extracts metadata from an ABF file.

    Parameters:
        abf_path (str): Path to the ABF file.

    Returns:
        dict: Metadata information.
    """
    abf = pyabf.ABF(abf_path)
    metadata = {
        "File": os.path.basename(abf_path),
        "Sweeps": len(abf.sweepList),
        "Sampling Rate (Hz)": abf.dataRate,
        "Sweep Duration (s)": abf.sweepLengthSec,
        "Total Channels": abf.channelCount,
        "Channels": ", ".join(abf.adcNames),
        "Units": ", ".join(abf.adcUnits),
        "Experiment Date": abf.abfDateTime.strftime("%Y-%m-%d %H:%M:%S"),
        "Protocol": abf.protocol if abf.protocol else "N/A"
    }
    return metadata

def list_abf_files(directory):
    """
    Lists ABF files in the directory and displays metadata.

    Parameters:
        directory (str): Path to the directory containing ABF files.

    Returns:
        None
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    abf_files = [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(directory)
        for filename in filenames if filename.endswith('.abf')
    ]

    if not abf_files:
        print(f"No ABF files found in '{directory}'.")
        return

    print(f"📂 Scanning directory: {directory}")
    print("=" * 80)

    for abf_path in abf_files:
        try:
            metadata = get_abf_metadata(abf_path)
            print(f"📄 {metadata['File']}")
            print(f"   ├─ Sweeps: {metadata['Sweeps']}")
            print(f"   ├─ Sampling Rate: {metadata['Sampling Rate (Hz)']} Hz")
            print(f"   ├─ Sweep Duration: {metadata['Sweep Duration (s)']} s")
            print(f"   ├─ Total Channels: {metadata['Total Channels']}")
            print(f"   ├─ Channels: {metadata['Channels']} ({metadata['Units']})")
            print(f"   ├─ Experiment Date: {metadata['Experiment Date']}")
            print(f"   └─ Protocol: {metadata['Protocol']}\n")
        except Exception as e:
            print(f"⚠️ Error reading '{abf_path}': {e}")

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(description="List ABF files with metadata.")
    parser.add_argument(
        "-i", "--input", type=str, required=True, metavar="DIR",
        help="📂 Path to the directory containing ABF files."
    )

    args = parser.parse_args()
    list_abf_files(args.input)

if __name__ == "__main__":
    main()
