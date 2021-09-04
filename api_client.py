import aiohttp
from config import config
from summoner import Summoner


class ApiClient(object):
    session = None
    X_Riot_Token = None

    def __init__(self, *args):
        self.X_Riot_Token = config.get("riotgames").get("X_Riot_Token")
        self.init_session()

    def init_session(self) -> None:
        """Crate a session for the progam"""
        try:
            self.session = aiohttp.ClientSession()
        except Exception as e:
            print(f"Error creating aiohttp session: {e}")

    async def get_summoner_by_name(self, summoner_name: str, region: str) -> "Summoner":
        """Gets a summoner by name"""
        base_url_summonerV5 = config.get("riotgames").get("base_url_summonerV5").format(region=region)
        url_ = (
            config.get("riotgames")
            .get("summonerv4")
            .get("summonerByName")
            .format(summoner_name=summoner_name)
        )
        url = base_url_summonerV5 + url_
        headers = {
            "X-Riot-Token": self.X_Riot_Token,
        }
        try:
            async with self.session.get(url, headers=headers) as respose:
                payload = await respose.json()
                return Summoner(dict_data=payload)
        except Exception as e:
            print(f"Error getting summoner: {e}")

    async def get_summoner_by_accountId(self, encryptedAccountId: str, region: str) -> "Summoner":
        """Gets a summoner by accountId"""
        base_url_summonerV5 = config.get("riotgames").get("base_url_summonerV5").format(region=region)
        url_ = (
            config.get("riotgames")
            .get("summonerv4")
            .get("summonerByAccountId")
            .format(encryptedAccountId=encryptedAccountId)
        )
        url = base_url_summonerV5 + url_
        headers = {
            "X-Riot-Token": self.X_Riot_Token,
        }
        try:
            async with self.session.get(url, headers=headers) as respose:
                payload = await respose.json()
                return Summoner(dict_data=payload)
        except Exception as e:
            print(f"Error getting summoner: {e}")

    async def get_summoner_by_puuid(self, encrypted_puuid: str, region: str) -> "Summoner":
        """Gets a summoner by puuid"""
        base_url_summonerV5 = config.get("riotgames").get("base_url_summonerV5").format(region=region)
        url_ = (
            config.get("riotgames")
            .get("summonerv4")
            .get("summonerBy_puuid")
            .format(encrypted_puuid=encrypted_puuid)
        )
        url = base_url_summonerV5 + url_
        headers = {
            "X-Riot-Token": self.X_Riot_Token,
        }
        try:
            async with self.session.get(url, headers=headers) as respose:
                payload = await respose.json()
                return Summoner(dict_data=payload)
        except Exception as e:
            print(f"Error getting summoner: {e}")

    async def get_matches_by_puuid(self, encrypted_puuid: str, region: str) -> "Summoner":
        """Gets a summoner by puuid"""
        base_url_summonerV5 = config.get("riotgames").get("base_url_summonerV5").format(region=region)
        url_ = (
            config.get("riotgames")
            .get("summonerv4")
            .get("summonerBy_puuid")
            .format(encrypted_puuid=encrypted_puuid)
        )
        url = base_url_summonerV5 + url_
        headers = {
            "X-Riot-Token": self.X_Riot_Token,
        }
        try:
            async with self.session.get(url, headers=headers) as respose:
                payload = await respose.json()
                return Summoner(dict_data=payload)
        except Exception as e:
            print(f"Error getting summoner: {e}")
