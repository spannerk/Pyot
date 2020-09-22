from .__core__ import PyotCore
from pyot.utils.cdragon import cdragon_url
from pyot.core.exceptions import NotFound
from typing import List, Iterator


# PYOT CORE OBJECTS

class Spell(PyotCore):
    id: int
    name: str
    description: str
    summoner_level: int
    cooldown: int
    modes: List[str]
    icon_path: str

    class Meta(PyotCore.Meta):
        raws = ["modes"]
        renamed = {"game_modes": "modes"}
        rules = {"cdragon_spells_full": ["id"]}

    def __init__(self, id: int = None, locale: str = None):
        self._lazy_set(locals())

    def filter(self, data):
        for item in data:
            if item["id"] == self.id:
                return item
        raise NotFound

    def _refactor(self):
        if self.locale.lower() == "en_us":
            self.meta.server = "default"
        load = getattr(self.meta, "load")
        load.pop("id")

    def _transform(self, data):
        data["iconPath"] = cdragon_url(data["iconPath"])
        return data


class Spells(PyotCore):
    spells: List[Spell]

    class Meta(PyotCore.Meta):
        rules = {"cdragon_spells_full": []}

    def __init__(self, locale: str = None):
        self._lazy_set(locals())

    def __getitem__(self, item):
        return self.spells[item]

    def __iter__(self) -> Iterator[Spell]:
        return iter(self.spells)

    def _refactor(self):
        if self.locale.lower() == "en_us":
            self.meta.server = "default"

    def _transform(self, data_):
        spells = []
        for data in data_:
            data["iconPath"] = cdragon_url(data["iconPath"])
            spells.append({"data": data})
        return {"spells": spells}