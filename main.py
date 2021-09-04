from api_client import ApiClient
import asyncio

async def main():
    session = ApiClient()
    summoner = await session.get_summoner_by_name("HelStan", "la1")
    print(summoner.puuid)
    summoner = await session.get_summoner_by_puuid(summoner.puuid, "la1")
    print(summoner.name)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
