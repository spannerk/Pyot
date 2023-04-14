from pyot.core.queue import Queue
from pyot.models import tft


async def get_matches(summoner_name="spannertft"):
    summoner = await tft.Summoner(name=summoner_name).get()
    history = await summoner.match_history.get()
    return [m.id for m in history.matches]