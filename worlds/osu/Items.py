from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification

import json

def load_text_file(name: str) -> str:
    import pkgutil
    return pkgutil.get_data(__name__, name).decode()

class OsuItem(Item):
    game = "osu!"


class OsuItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler


def get_song_data() -> list[dict]:
    OsuSongData = load_text_file("OsuSongData.json")
    packs = json.loads(OsuSongData)
    beatmapsets = []
    for pack in packs:
        for beatmapset in pack["beatmapsets"]:
            if beatmapset not in beatmapsets:
                beatmapsets.append(beatmapset)
    return beatmapsets


osu_song_data = get_song_data()
osu_song_max = len(osu_song_data)
osu_song_pool = []

item_data_table: Dict[str, OsuItemData] = {
    "Preformance Points": OsuItemData(
        code=726999999,
        type=ItemClassification.progression,
    ),
    "Circle": OsuItemData(
        code=726999998,
    ),
}

for i in range(osu_song_max):
    item_data_table[f"Song {i+1}"] = OsuItemData(
        code=727000000+i,
        type=ItemClassification.progression,
    )
    osu_song_pool.append(f"Song {i+1}")

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
