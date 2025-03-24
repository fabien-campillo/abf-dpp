# Documentation for abf_plot_all_sweeps.py

### Function: abf_plot_all_sweeps

```python
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
```

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
