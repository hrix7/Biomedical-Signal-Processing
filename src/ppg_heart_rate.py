"""Estimate heart rate from a one-dimensional PPG signal."""
from __future__ import annotations
import argparse
import numpy as np
import pandas as pd
from scipy.signal import butter, sosfiltfilt, find_peaks

def estimate_bpm(ppg, sample_rate_hz: float, low_hz: float = 0.7, high_hz: float = 3.5):
    signal = np.asarray(ppg, dtype=float)
    if signal.ndim != 1 or signal.size < sample_rate_hz * 3:
        raise ValueError("Provide at least three seconds of one-dimensional PPG")
    sos = butter(3, [low_hz, high_hz], btype="bandpass", fs=sample_rate_hz, output="sos")
    filtered = sosfiltfilt(sos, signal)
    peaks, _ = find_peaks(filtered, distance=int(sample_rate_hz * 0.3), prominence=np.std(filtered) * 0.25)
    if len(peaks) < 2:
        raise ValueError("Not enough peaks for a heart-rate estimate")
    bpm = 60.0 * sample_rate_hz / np.median(np.diff(peaks))
    return float(bpm), peaks, filtered

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--sample-rate", type=float, required=True)
    args = parser.parse_args()
    frame = pd.read_csv(args.csv)
    bpm, peaks, _ = estimate_bpm(frame["ppg"], args.sample_rate)
    print(f"Estimated heart rate: {bpm:.1f} bpm from {len(peaks)} peaks")
