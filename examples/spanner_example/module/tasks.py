from pyot.core.queue import Queue
from pyot.models import tft
from datetime import datetime


async def get_matches(summoner_name="spannertft"):
    start_date = datetime(2023, 4, 17, 0, 0, 0)
    end_date = datetime(2023, 4, 22, 0, 0, 0)
    summoner = await tft.Summoner(name=summoner_name).get()
    print(summoner.puuid)
    history = summoner.match_history
    history.query(count=100, start_time=start_date, end_time=end_date)
    await history.get()
    return [m.id for m in history.matches]