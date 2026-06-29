# Surface Chemistry Tools

This repository is a collection of Python tools and scripts designed to streamline data processing and analysis for surface chemistry, spectroscopy, and chemical engineering research. 

More tools (e.g., for XPS or other surface analyses) will be added to this repository in the future.

## Directory Structure

```text
surface-chemistry-tools/
├── FTIR-ATR/
│   └── ATR_corr.py      # Penetration depth correction for ATR-IR spectra
└── (Future tools will be added here in separate folders)
```

## Available Tools

### 1. `FTIR-ATR/ATR_corr.py` (ATR-IR Penetration Depth Corrector) (2026 Jun)
In Attenuated Total Reflection Infrared (ATR-IR) spectroscopy, the penetration depth of the evanescent wave is wavelength-dependent (penetrates deeper at lower wavenumbers). This script calculates the specific penetration depth for each wavenumber and corrects the absorbance, allowing for accurate quantitative analysis.

**Features:**
- **GUI File Selection:** Easily select multiple raw spectra files (`.txt` or `.csv`) using a pop-up dialog.
- **Batch Processing:** Processes multiple files at once and outputs them as standard `.csv` files with a `corrected_` prefix.
- **Customizable:** Refractive indices (crystal and sample) and the incident angle can be easily adjusted within the script.

**Usage:**
1. Navigate to the `FTIR-ATR` directory.
2. Open `ATR_corr.py` and adjust the experimental parameters at the bottom of the script if necessary:
   ```python
   # Example: Diamond crystal (n_1=2.39), Sample (n_2=1.50), Angle=45 degrees
   process(n_1=2.39, n_2=1.50, angle=45)
   ```
3. Run the script. A file dialog will appear to select your spectra files.

---

## Requirements
- Python 3.x
- `pandas`

## Installation
Clone this repository to your local machine:
```bash
git clone [https://github.com/kt31hub/surface-chemistry-tools.git](https://github.com/kt31hub/surface-chemistry-tools.git)
cd surface-chemistry-tools
pip install pandas
```
