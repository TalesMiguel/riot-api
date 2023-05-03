from fastapi import APIRouter, Depends, Header
import requests
from typing import Any

from dependencies import set_api_key
from models import PlatformRoutingValues, SummonerInfo

router = APIRouter(
    prefix="/summoner",
    # dependencies=Depends[set_api_key()]
)

@router.get("/{summonerName}")
async def get_summoner_info_by_summoner_name(server: PlatformRoutingValues, summoner_name: str, api_key=set_api_key()) -> Any:
    url = f"https://{server}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
    resp = requests.get(url)
    summoner_info = resp.json()
    return summoner_info
