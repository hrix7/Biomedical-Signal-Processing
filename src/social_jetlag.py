"""Calculate social jet lag from my workday and free-day sleep records."""
from __future__ import annotations
import argparse
import json
import pandas as pd

def to_minutes(value: str) -> int:
    hours, minutes = map(int, value.split(":"))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError(f"Invalid time: {value}")
    return hours * 60 + minutes

def midsleep(onset: str, wake: str) -> float:
    start, end = to_minutes(onset), to_minutes(wake)
    duration = (end - start) % (24 * 60)
    return (start + duration / 2) % (24 * 60)

def circular_difference_hours(a: float, b: float) -> float:
    difference = abs(a - b) % (24 * 60)
    return min(difference, 24 * 60 - difference) / 60.0

def analyze(frame: pd.DataFrame) -> dict[str, float]:
    required = {"day_type", "sleep_onset", "wake_time"}
    if missing := required.difference(frame.columns):
        raise ValueError(f"Missing columns: {sorted(missing)}")
    data = frame.copy()
    data["midsleep_min"] = [midsleep(a, b) for a, b in zip(data.sleep_onset, data.wake_time)]
    means = data.groupby("day_type")["midsleep_min"].mean()
    if not {"workday", "free_day"}.issubset(means.index):
        raise ValueError("day_type must include workday and free_day")
    return {"workday_midsleep_hour": float(means["workday"] / 60),
            "free_day_midsleep_hour": float(means["free_day"] / 60),
            "social_jetlag_hours": circular_difference_hours(means["workday"], means["free_day"])}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    print(json.dumps(analyze(pd.read_csv(args.csv)), indent=2))
