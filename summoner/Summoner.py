from typing import Dict, Optional, List, Union, Any
from riotwatcher import LolWatcher

from config import config

class Summoner(object):
    """ Invocador de League of Legends """
    summonerId = str
    puuid = str
    summonerName = str
    leagueId = str
    region = str
    tier = str
    rank = str
    leaguePoints = str
    wins = int
    losses = int
    inactive = bool
    summonerLevel = int
    accountId = str
    def __init__(
        self,
        summonerName: str,
        region: str
    ) -> None:
        self.summonerName = summonerName
        self.region = region
        self.make_summoner()

    def __str__(self) -> str:
        return f"Summoner {self.summonerName} with summonerId: {self.summonerId} and puuid: {self.puuid}"

    def parse_summoner(self, summoner: str) -> None:
        """ Parsea los datos que se envian en summoner """
        self.summonerId = summoner.get("id")
        self.puuid = summoner.get("puuid")
        self.summonerLevel = summoner.get("summonerLevel")

    def make_summoner(self) -> None:
        """ Termina de crear al invocador """
        lol_watcher= LolWatcher(config.get("riotgames").get("api_key"))
        summoner = lol_watcher.summoner.by_name(self.region, self.summonerName)
        self.parse_summoner(summoner)

    def  get_matchs(self) -> List:
        if self.region == "la1" or self.region == "la2":
            lol_watcher = LolWatcher(config.get("riotgames").get("api_key"))
            matchlist = lol_watcher.match_v5.matchlist_by_puuid('AMERICAS', self.puuid)
        return matchlist     
