#!/usr/bin/env python3

import pyabf
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Set the base directory to search for ABF files
base_directory = "abf_data/"

# Create a PDF file to save all figures
pdf_path = "abf_figures.pdf"
with PdfPages(pdf_path) as pdf:
    # Initialize a counter for the number of plots on the current page
    plot_counter = 0

    # Loop through all subdirectories and files in the base directory
    for dirpath, _, filenames in os.walk(base_directory):
        for filename in filenames:
            if filename.endswith('.abf'):  # Check if the file is an ABF file
                abf_path = os.path.join(dirpath, filename)  # Get the full path of the ABF file
                abf = pyabf.ABF(abf_path)  # Load the ABF file

                # Check if a new page is needed
                if plot_counter % 3 == 0:
                    plt.figure(figsize=(8.5, 11))  # Portrait format (8.5 x 11 inches)

                # Create a subplot for the current figure
                relative_path = os.path.relpath(abf_path, base_directory)  # Get the relative path
                plt.subplot(3, 1, plot_counter % 3 + 1)  # 3 rows, 1 column
                plt.title(f"Sweeps from {relative_path}", pad=20)  # Set the title to the relative path with padding
                plt.xlabel("Time (s)")
                plt.ylabel("ADC Data")

                # Plotting each sweep
                for sweepNumber in abf.sweepList:
                    abf.setSweep(sweepNumber)
                    offset = 140 * sweepNumber
                    plt.plot(abf.sweepX, abf.sweepY + offset, color='C0', lw=0.1)
                    plt.gca().get_yaxis().set_visible(False)  # hide Y axis

                plot_counter += 1  # Increment the plot counter

                # Adjust the layout to prevent overlap
                plt.tight_layout()

                # Save the current figure to the PDF if we've reached 3 plots
                if plot_counter % 3 == 0 or (dirpath == list(os.walk(base_directory))[0][0] and plot_counter == len(filenames)):
                    pdf.savefig()  # Save the current figure to the PDF
                    plt.close()    # Close the figure to save memory

    # Check if there are any remaining plots to save after the loop
    if plot_counter % 3 != 0:
        pdf.savefig()  # Save the remaining figure(s)
        plt.close()    # Close the figure to save memory

# Optionally inform the user that the PDF has been created
print(f"All figures saved to {pdf_path}.")
