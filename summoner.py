from typing import Dict


class Summoner(object):
    id = str
    accountId = str
    puuid = str
    name = str
    profileIconId = int
    summonerLevel = int
    def __init__(self, dict_data):
        self.id = dict_data.get("id")
        self.accountId = dict_data.get("accountId")
        self.puuid = dict_data.get("puuid")
        self.name = dict_data.get("name")
        self.profileIconId = dict_data.get("profileIconId")
        self.summonerLevel = dict_data.get("summonerLevel")


        