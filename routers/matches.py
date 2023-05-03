from fastapi import APIRouter, Depends
import requests
from typing import Any

from dependencies import set_api_key
from models import RegionalRoutingValues


router = APIRouter(
    prefix="/matches",
    # dependencies=Depends[set_api_key()]
)

"""
Get a list of match ids by puuid
"""
@router.get("/puuid/{puuid}")
async def get_summoner_matches_list_by_puuid(server: RegionalRoutingValues, puuid: str, api_key=set_api_key()) -> Any:
    url = f"https://{server}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api_key}"
    resp = requests.get(url)
    matches = resp.json()
    return matches


@router.get("/matchId/{matchId}")
async def get_match_data_by_match_id(server: RegionalRoutingValues, match_id: str, puuid = None, api_key=set_api_key()) -> Any:
    url = f"https://{server}/lol/match/v5/matches/{match_id}?api_key={api_key}"
    resp = requests.get(url)
    match_data = resp.json()
    
    match_info = match_data['info'] # Every match-relevant info is stored in this key, such as:
    game_mode = match_info['gameMode']
    game_duration = match_info['gameDuration'] # And so on ...
    players_data = match_info['participants'] # A list of dicts, each dict contains data about a player
    
    summoners_puuids_list = match_data["metadata"]["participants"] # Same order as players_data
    if puuid:
        p_index = summoners_puuids_list.index(puuid) # Get the index of the puuid from summoners list
        player_data = players_data[p_index] # Get the player data by index (same order as summoners list)
    return match_data

