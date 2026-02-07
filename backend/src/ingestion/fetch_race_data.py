import fastf1
import pandas as pd

# Enabling caching for faster subsequent loads (important for speed and API stability)
fastf1.Cache.enable_cache('data/fastf1_cache')

def load_race_data():
    """
    This is just a test load to make sure API calls are working.
    
    Load Bahrain 2023 race data and extract:
    - Lap times
    - Tire compounds
    - Pit stop laps
    """
    session = fastf1.get_session(2023, 'Bahrain', 'R')
    session.load()
    
    laps = session.laps
    
    laps_df = laps[[
        "Driver",
        "LapNumber",
        "LapTime",
        "Compound",
        "Stint",
        "PitOutTime",
        "PitInTime"
    ]].copy()

    laps_df["LapTimeSeconds"] = laps_df["LapTime"].dt.total_seconds()
    
    pit_laps = laps_df[
        laps_df["PitInTime"].notna() | laps_df["PitOutTime"].notna()
    ][["Driver", "LapNumber", "PitInTime", "PitOutTime"]]
    
    return laps_df, pit_laps

if __name__ == "__main__":
    laps_df, pit_laps = load_race_data()

    print("\n=== LAP DATA (HEAD) ===")
    print(laps_df.head())

    print("\n=== PIT LAPS (HEAD) ===")
    print(pit_laps.head())