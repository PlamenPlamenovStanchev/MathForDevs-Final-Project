# Calculus in Medical Data: ECG Analysis

## Overview

This project explores how concepts from calculus and mathematical modeling can be applied to electrocardiogram (ECG) data. By treating the ECG signal as a continuous time-dependent function, we apply advanced mathematical tools—such as first and second derivatives, local extrema detection, and smoothing algorithms—to extract vital medical information from raw, noisy physiological data.

## Features

- **ECG Signal Visualization**: Accurate representation of P, QRS, and T complexes.
- **Calculus-based Analysis**: Utilizing first ($V'(t)$) and second derivatives ($V''(t)$) to interpret signal slopes and curvature.
- **R-Peak Detection**: Identifying local maxima to isolate individual heartbeats.
- **RR Interval & Heart Rate Variability (HRV)**: Detailed statistical and visual analysis of the variations between heartbeats.
- **Heart Rate Estimation (BPM)**: Deriving beats-per-minute from the processed signal intervals.
- **Signal Processing**: Applying moving average filters to mitigate high-frequency artifacts and baseline wander.

## Project Structure

- `src/` – Core Python algorithms for signal processing and data loading (`ecg_analysis.py`, `load_ecg_data.py`).
- `data/` – Raw physiological datasets (EDF format) and annotations.
- `images/` – Explanatory diagrams and figures.
- `ecg_analysis.ipynb` – Main Jupyter Notebook containing the full academic analysis, mathematical proofs, code, and visualizations.

## How to Run

1. Clone the repository and navigate to the project root.
2. Ensure you have Python installed and create a virtual environment (`.venv`).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

5. Open `ecg_analysis.ipynb` and run the cells.

## Author

Plamen Stanchev