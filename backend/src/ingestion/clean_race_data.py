## Clean the race data
## Account for extra lap times due to pit stops, virtual SC and SC.
## If lap is x when car pits, it becomes x+1 when it comes out of the pit lane.

import fastf1
import pandas as pd

fastf1.Cache.enable_cache("data/fastf1_cache")

def load_sessions(year, gp_name, session_type):
    session = fastf1.get_session(year, gp_name, session_type)
    session.load()
    return session

def clean_race_data(session):
    laps = session.laps
    print("Number of lap columns:", len(laps.columns))
    print("Some lap columns:", list(laps.columns)[:30])
    for c in ["TrackStatus", "Weather", "IsAccurateLapTime", "IsAccurate"]:
        print(c, "->", c in laps.columns)

    columns = [
        "Driver",
        "LapNumber",
        "LapTime",
        "Compound",
        "Stint",
        "PitOutTime",
        "PitInTime",
        "TrackStatus",
        "IsAccurate", # quality filter for lap times (given by fastf1)
        "TyreLife",
        "Team" # normalise driver pace and used to compare drivers within the team
    ]
    