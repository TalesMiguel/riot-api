from fastapi import FastAPI
import requests
from typing import Any
from models import SummonerInfo, PlatformRoutingValues, RegionalRoutingValues

app = FastAPI()

# For development pourposes. Taken from https://developer.riotgames.com/
api_key = os.getenv("RIOT_API_KEY", None) # Expires every 24 hours
auth = f"api_key={api_key}" # API key param to be used in every request


# Summoner
@app.get("/summoner/{summonerName}")
async def get_summoner_info_by_summoner_name(server: PlatformRoutingValues, summoner_name: str) -> SummonerInfo:
    url = f"https://{server}/lol/summoner/v4/summoners/by-name/{summoner_name}?{auth}"
    resp = requests.get(url)
    summoner_info = resp.json()
    return summoner_info


# Matches
@app.get("/matches/{matchId}")
async def get_match_info_by_match_id(server: RegionalRoutingValues, match_id: str) -> Any:
    url = f"https://{server}/lol/match/v5/matches/{match_id}?{auth}"
    resp = requests.get(url)
    match_info = resp.json()
    return match_info



"""
Get a list of match ids by puuid
"""
@app.get("/matches/{puuid}")
async def get_summoner_matches_list_by_puuid(server: RegionalRoutingValues, puuid: str) -> Any:
    url = f"https://{server}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&{auth}"
    resp = requests.get(url)
    matches = resp.json()
    return matches
