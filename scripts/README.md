# python scripts for abf-dpp
 
This directory contains pythons functions.

The one that are dedicated to the users should be preceded by `# USER FUNCTION`, eg:

```
# USER FUNCTION
def abf_scan():
    """Command-line interface for the ABF data plotting script."""
    parser = argparse.ArgumentParser(description="Generate a PDF of sweeps from ABF files.")
```

> `abf_scan` is just a symbolic link to `abf_scan.py` (so we can just run  `abf_scan <name>`) 

They are other functions not directly used by the users. The one preceded by `# USER FUNCTION` will appear in the menu proposed by `menu.py`. [to be done]
