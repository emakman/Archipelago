from .Locations import location_table
from .Items import YokuItem,ItemName,item_table
from BaseClasses import Item, MultiWorld
from copy import deepcopy
import json
import zipfile

class SaveItem:
    id: int
    item: str
    revealed: bool | None = None
    tracker: str | None = None
    def __init__(self, loc: str, item: Item, worlds: MultiWorld): 
        loc_data = location_table[loc]
        self.id = loc_data["save_id"]
        if isinstance(item, YokuItem):
            self.item = item_table[ItemName(item.name)].yoku_ids[0]
        else:
            self.item = f"amwr/{item.name}\u001e{worlds.player_name[item.player]}\u001e{worlds.worlds[item.player].game}"
        if "tracker_string" in loc_data:
            self.tracker = loc_data["tracker_string"]
        if "revealed" in loc_data:
            self.revealed = loc_data["revealed"]


class SaveFiles:
    base: str
    save_items: dict[int,SaveItem] = {}
    def __init__(self, base: str, save_items: list[SaveItem]) -> None:
        self.base = base
        self.save_items = {it.id:it for it in save_items}

    def save(self) -> None:
        with zipfile.ZipFile(f"{self.base}.zip", 'w') as zf:
            with zf.open("2.save", "w") as f:
                r = deepcopy(vh_save)
                for id in order:
                    r["_global"]["randomizer"] += [{k: v for k, v in vars(self.save_items[id]).items() if k[0] != "_"}]
                f.write(json.dumps(r).encode('utf-8'))
                f.close()
            with zf.open("2.trail", 'w') as f:
                f.write(vh_trail)
                f.close()
            with zf.open("2.map", 'w') as f:
                f.write(vh_map)
                f.close()

vh_save = {
        "_global": {
            "level": "intro_landing",
            "spawner": 1,
            "reset_count": 1,
            "distance_traveled": 18.106576919555665,
            "items": [
                {
                    "item": "abilities/map"
                }
            ],
            "gamemode": "randomizer",
            "randomizer_seed": 1634563954,
            "randomizer_difficulty": "veryhard",
            "randomizer": [],
            "duration": 91,
            "version": 2
        },
        "intro_landing": {},
        "intro_landing_upper": {},
        "intro_secret": {},
        "intro_landing_left": {},
        "hub_obtainium_outland": {},
        "intro_muddled_morass": {},
        "_main_map": {},
        "jens_soaring_heights": {}
    }

order = [
  21042450, 21042661, 55185998, 56689309, 57084164, 54007097, 54857324, 55185973, 30212240, 30217074, 38469887,
  38469941, 38470259, 38470383, 38470932, 38469896, 43910361, 43910358, 43910364, 43910355, 43910349, 43910346,
  43910161, 43910352, 45679083, 21761617, 53281572, 56691154, 48170179, 30216840, 25628609, 55771370, 48892285,
  48892094, 48892283, 48892281, 21042789, 21173193, 54857276, 21825866, 27592999, 53281548, 26481086, 38472445,
  28705266, 57085255, 57085246, 26284861, 56099584, 45351409, 25104987, 55185814, 21108767, 56098915, 21042729,
  21172921, 45351379, 21172926, 21761301, 21958374, 21825455, 46928212, 44042632, 53281476, 53281471, 30544446,
  31987048, 54007074, 26481036, 26284437, 55185744, 55185740, 38666800, 52103026, 25628632, 25628637, 38472470,
  52953351, 28445582, 56885316, 39454067, 54857259, 21108771, 47251676, 26481041, 30544450, 21042135, 21041407,
  21172735, 21173226, 23989298, 23988666, 23988671, 24840039, 24840041, 25628848, 25628865, 38472003, 38472598,
  38472624, 56690172, 56691137, 48433763, 48433802, 37424285, 37424029, 31983859, 31987188, 31987185, 48169307,
  48170870, 48170941, 27592975, 27592971, 27592983, 30216747, 30216750, 30216968, 30216951, 30216992, 30217006,
  25105120, 21958797, 21958795, 21958813, 21958834, 21958863, 21957122, 26284092, 31987079, 26284095, 23396960,
  26480910, 25105162, 28446220, 28445943, 28445932, 50727459, 48892757, 54528363, 47251961, 54329447, 55185471,
  55185986, 55185140, 55185856, 21172508, 21761516, 26284950, 43910274, 43910016, 28705196, 53281416, 48892764,
  30544501, 30217093, 21108214, 36899447, 24973035, 52103074, 57085027, 30544307, 45351467, 45220046, 44105819,
  22872105, 21108710, 21042679, 21040985, 21108621, 36766403, 36766387, 21042801, 21173121, 23987316, 36898607,
  21761097, 21758395, 21760842, 21957403, 21957816, 23397003, 23396866, 21825342, 26284713, 27657424, 23987363,
  54857284, 55185217, 55185735, 55185823, 45679114, 45679446, 28705041, 52103039, 24838662, 24839105, 21042438,
  50727469, 55771787, 52563019, 25627242, 25626797, 25628685, 25627136, 25628823, 38472500, 38471745, 38470609,
  28445810, 56689807, 56688830, 56691064, 57084663, 48891952, 57084973, 57085342, 54528431, 48431629, 48170957,
  26481085, 54006765, 54005874, 43910175, 26480930, 31983991, 31985568, 31982433, 31986809, 37424461, 30544191,
  30544153, 30544255, 30544389, 27790467, 27592682, 27592231, 44042001, 44040524, 44041093, 47251672, 25756550,
  41289047, 41288903, 21761425, 21761465, 21761423, 21761363 ]

vh_trail = bytearray([0x01, 0x00, 0x00, 0x00, 0x19, 0x00, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00,
                      0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00, 0xb0, 0xfe, 0xff, 0xff, 0x21, 0x01, 0x00, 0x00])

vh_map = bytearray([0x20, 0x57, 0x41, 0x52, 0xc0, 0x00, 0x00, 0x00, 0x66, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00]+[0xff]*19584)


