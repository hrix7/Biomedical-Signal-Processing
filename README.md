# Biomedical Signal Processing

A collection of clear, reusable signal-processing examples for physiological and wearable data.

## Planned modules

- PPG filtering and heart-rate estimation
- Step detection and activity features
- Sleep timing and social jet lag
- EEG/HRV feature exploration
- Filtering, quality checks, and visualization

## Included example

`src/ppg_heart_rate.py` applies a band-pass filter and detects candidate systolic peaks. Use synthetic or permission-cleared signals only.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/ppg_heart_rate.py examples/synthetic_ppg.csv --sample-rate 50
```

## Research boundary

Outputs are exploratory and are not validated clinical measurements.

## License

MIT.
