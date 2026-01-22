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

