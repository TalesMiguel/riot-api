from fastapi import FastAPI
import requests
from typing import Any
from models import SummonerInfo, PlatformRoutingValues, RegionalRoutingValues

app = FastAPI()


api_key = "RGAPI-a19df1f2-7b5a-4bc1-a922-c932e9a98c7a" # Taken from https://developer.riotgames.com/
auth = f"api_key={api_key}" # API key param to be used in every request


# Summoner

"""
Get summoner info by summoner_name
"""
@app.get("/summoner/{summonerName}")
async def get_summoner_info_by_summoner_name(server: PlatformRoutingValues, summoner_name: str) -> SummonerInfo:
    url = f"https://{server}/lol/summoner/v4/summoners/by-name/{summoner_name}?{auth}"
    resp = requests.get(url)
    summoner_info = resp.json()
    return summoner_info


# Matches

"""
Get a list of match ids by puuid
"""
@app.get("/matches/{puuid}")
async def get_summoner_matches_list_by_puuid(server: RegionalRoutingValues, puuid: str) -> Any:
    url = f"https://{server}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&{auth}"
    resp = requests.get(url)
    matches = resp.json()
    return matches
