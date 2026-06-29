# Surface Chemistry Tools

This repository is a collection of Python tools and scripts designed to streamline data processing and analysis for surface chemistry, spectroscopy, and chemical engineering research. 

More tools (e.g., for XPS or other surface analyses) will be added to this repository in the future.

## Directory Structure

```text
surface-chemistry-tools/
├── FTIR-ATR/
│   └── ATR_corr.py      # Penetration depth correction for ATR-IR spectra
└── (Future tools will be added here in separate folders)

## Available Tools

### 1. ATR-IR Penetration Depth Corrector (`process.py`)
This script corrects the absorbance of Attenuated Total Reflection Infrared (ATR-IR) spectra by accounting for the wavelength-dependent penetration depth of the evanescent wave.

**Features:**
- **GUI File Selection:** Easily select multiple `.txt` (space-separated) or `.csv` files via a pop-up dialog.
- **Bulk Processing:** Automatically calculates the corrected absorbance and saves all processed files as `.csv` with a `corrected_` prefix in the original directory.
- **Customizable Parameters:** Adjust the refractive index of the crystal ($n_1$), the sample ($n_2$), and the angle of incidence within the script.

**Usage:**
1. Open the script and modify the measurement parameters at the bottom of the file:
   ```python
   # Example: Diamond crystal (n_1=2.39), Sample (n_2=1.50), Angle=45 degrees
   process(n_1=2.39, n_2=1.50, angle=45)
