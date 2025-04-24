# ingestion/extract_sleep_data.py

import os
import pandas as pd

INPUT_CSV = os.path.join(os.path.dirname(__file__), "samples", "example_raw_data.csv")
OUTPUT_CSV = os.path.join(os.path.dirname(__file__), "samples", "example_sleep_data_new.csv")

# Select only relevant sleep columns
SLEEP_COLUMNS = [
    "Date", "Time", "Heart Rate (bpm)", "Heart Rate Variability (ms)",
    "Respiratory Rate (breaths/min)", "Blood Oxygen (%)",
    "Sleep Duration (hours)", "Time Awake (minutes)",
    "REM Sleep (%)", "Core Sleep (%)", "Deep Sleep (%)"
]

def extract_sleep_data(input_csv, output_csv):
    print(f"[INFO] Reading raw data from: {input_csv}")
    df = pd.read_csv(input_csv)

    missing = [col for col in SLEEP_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    sleep_df = df[SLEEP_COLUMNS].copy()

    # Optional: Rename columns to snake_case
    sleep_df.columns = [c.strip().lower().replace(" ", "_").replace("(", "").replace(")", "") for c in sleep_df.columns]

    print(f"[INFO] Extracted {len(sleep_df)} sleep rows with columns: {sleep_df.columns.tolist()}")
    sleep_df.to_csv(output_csv, index=False)
    print(f"[SUCCESS] Saved cleaned sleep data to: {output_csv}")

if __name__ == "__main__":
    extract_sleep_data(INPUT_CSV, OUTPUT_CSV)