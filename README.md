# Biomedical Signal Processing

I use this repository to organize the signal-processing methods behind my wearable and physiological-monitoring work. It includes practical code for PPG heart-rate estimation, step-related signals, and sleep/social-jet-lag calculations.

## Work represented here

- Filtered PPG signals and detected pulse peaks for heart-rate estimation.
- Processed acceleration signals for candidate step detection.
- Reviewed EEG and heart-rate-variability concepts through research-volunteer work.
- Analyzed sleep timing and the difference between workday and free-day sleep schedules.
- Structured reusable checks for sampling rate, signal duration, missing data, and physiological plausibility.

## Repository code

- `src/ppg_heart_rate.py` band-pass filters PPG, detects peaks, and estimates beats per minute.
- `src/social_jetlag.py` calculates midsleep on workdays/free days and their circular time difference.
- `docs/SIGNAL_CHECKLIST.md` records the signal-quality checks I use before interpreting outputs.
- `examples/README.md` explains the expected input formats.

## Run the tools

```bash
python -m pip install -r requirements.txt
python src/ppg_heart_rate.py ppg.csv --sample-rate 100
python src/social_jetlag.py sleep.csv
```

For the sleep tool, use columns `day_type`, `sleep_onset`, and `wake_time`, with time values in `HH:MM` format.

## Tools

Python, MATLAB, NumPy, pandas, SciPy, filtering, peak detection, PPG, EEG/HRV concepts, sleep and circadian analysis.

## Scope

The scripts are educational analysis tools. They do not provide medical diagnoses and should not be used for clinical decisions without appropriate validation.

## Author and Project Setting

**Hritika Adhikary**  
Graduate Biomedical Signal Processing and Wearables Work  
Arizona State University  
2025

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
