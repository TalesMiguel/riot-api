from pydantic import BaseModel
from enum import Enum

"""
Platform IDs and regions as routing values, such as na1 and americas.
Routing values are determined by the topology of the underlying services.
Services are frequently clustered by platform resulting in platform IDs
being used as routing values. Services may also be clustered by region,
which is when regional routing values are used. The best way to tell if
an endpoint uses a platform or a region as a routing value is to execute
a sample request through the [Reference page](https://developer.riotgames.com/apis).
"""
class RegionalRoutingValues(str, Enum):
    AMERICAS = "americas.api.riotgames.com"
    ASIA = "asia.api.riotgames.com"
    EUROPE = "europe.api.riotgames.com"
    SEA = "sea.api.riotgames.com"


class PlatformRoutingValues(str, Enum):
    BR1 = "br1.api.riotgames.com"
    EUN1 = "eun1.api.riotgames.com"
    EUW1 = "euw1.api.riotgames.com"
    JP1 = "jp1.api.riotgames.com"
    KR = "kr.api.riotgames.com"
    LA1 = "la1.api.riotgames.com"
    LA2 = "la2.api.riotgames.com"
    NA1 = "na1.api.riotgames.com"
    OC1 = "oc1.api.riotgames.com"
    TR1 = "tr1.api.riotgames.com"
    RU = "ru.api.riotgames.com"
    PH2 = "ph2.api.riotgames.com"
    SG2 = "sg2.api.riotgames.com"
    TH2 = "th2.api.riotgames.com"
    TW2 = "tw2.api.riotgames.com"
    VN2 = "vn2.api.riotgames.com"


class SummonerInfo(BaseModel):
    id: str
    accountId: str
    puuid: str
    name: str
    profileIconId: int
    revisionDate: int
    summonerLevel: int
