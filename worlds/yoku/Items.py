"""
Author: T Makuluni
Date: Mon, 27 jan
Description: Manage items in the Yoku's Island Express multiworld randomizer
"""

from typing import Optional,List,Self
from enum import Enum,StrEnum
from BaseClasses import Item, ItemClassification

class ItemType(Enum):
    """
    Used to indicate to the multi-world if an item is useful or not
    """
    NORMAL = 0
    PROGRESSION = 1
    JUNK = 2


class ItemGroup(Enum):
    """
    Used to group items
    """
    COLLECTIBLE = 0
    FRUIT = 1
    MOVEMENT = 2
    TRACKER = 3
    KEYS = 4
    QUEST = 5
    MISC = 6


class YokuItem(Item):
    """
    A single item in Yoku's Island Express.
    """
    game: str = "Yoku's Island Express"
    """The name of the game"""

    def __init__(self, name: str, classification: ItemClassification,
                 code: Optional[int], player: int):
        """
        Initialisation of the Item
        :param name: The name of the item
        :param classification: If the item is useful or not
        :param code: The ID of the item (if None, it is an event)
        :param player: The ID of the player in the multiworld
        """
        super().__init__(name, classification, code, player)


class ItemData:
    """
    Data of an item.
    """
    id: int
    count: int
    type: ItemType
    group: ItemGroup
    yoku_ids: List[str]

    def __init__(self, id: int, count: int, type: ItemType, group: ItemGroup, yoku_ids: List[str]):
        """
        Initialisation of the item data
        @param id: The item ID
        @param count: the number of items in the pool
        @param type: the importance type of the item
        @param group: the usage of the item in the game
        """
        self.id = id
        self.count = count
        self.type = type
        self.group = group
        self.yoku_ids = yoku_ids

class ItemName(StrEnum):
    """
    Information data for every (not event) item.
    """
    AbilitiesDive = "Progressive Dive Fish"
    AbilitiesDoubleFruit = "Boon of plenty!"
    AbilitiesKickback = "Kickback"
    AbilitiesMailbag = "Mail bag"
    AbilitiesPartyhorn = "Noisemaker"
    AbilitiesSlugVacuum = "Progressive Slug Vacuum"
    AbilitiesSlugUpgrade = "Progressive Slug Vacuum"
    AbilitiesSpeed = "Grand Postmaster Badge"
    Bluekey = "Blue Key"
    BucketEmpty = "Empty Bucket"
    DustbunnyDirty = "Sootling"
    Greenkey = "Green Key"
    Guano = "Guano"
    Idol1 = "Statue Chunk"
    Idol2 = "Statue Piece"
    Idol3 = "Statue Piece 2"
    Idol4 = "Statue Piece 3"
    Mushroom2 = "Juicy Cove Mushroom"
    Mushroom3 = "Poison Toadstool"
    NimKey = "Nim Key"
    Nugget = "Smashed Piece of Statue"
    PostalBadge = "Postal Badge"
    PowerupsSkvader1 = "Progressive Skvader"
    PowerupsSkvader2 = "Progressive Skvader"
    RewardFruitMedium = "5 Fruit"
    RewardFruitBig = "10 Fruit"
    SeedPod = "Seed Pod"
    SkinsSkin1 = "Bling Sprinkles"
    SkinsSkin2 = "Creepy Sprinkles"
    SkinsSkin3 = "Deadly Sprinkles"
    SkinsSkin4 = "Crimson Sprinkles"
    SkinsSkin5 = "Sweet Sprinkles"
    SootlingLeash = "Sootling Leash"
    Spores1 = "Light Spores"
    Spores2 = "Dry Spores"
    Spores3 = "Damp Spores"
    Spores4 = "Annoyed Spores"
    Spores5 = "Frosty Spores"
    SpringKey = "Key to the Underbelly"
    Tadpole = "Tadpole"
    Toolbox = "Toolbox"
    TrackerCaves = "Tracker: Crystal Deep"
    TrackerJungle = "Tracker: Gorilla Woods"
    TrackerPeak = "Tracker: Ivory Peak"
    TrackerScarabs = "Tracker: Scarabs"
    TrackerSprings = "Tracker: Marrow Hill"
    TraitorSpirit = "Traitor Spirit"
    TreasureMap = "Treasure Map"
    Wallet = "Progressive Wallet Upgrade"
    Collectible = "Wickerling"
    
    @classmethod
    def from_yoku_id(cls, s: str) -> Self | None:
        for k,v in item_table.items():
            if s in v.yoku_ids:
                return cls(k)

    def yoku_ids(self) -> List[str]:
        return item_table[self].yoku_ids
            

"""Information data for every (not event) item."""
item_table = {
    #       name:           ID,    Nb,   Item Type,        Item Group
    ItemName.AbilitiesDive: ItemData(9658001, 2, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["abilities/dive", "abilities/dive_speed"]),
    ItemName.AbilitiesDoubleFruit: ItemData(9658003, 1, ItemType.NORMAL, ItemGroup.MISC, ["abilities/double_fruit"]),
    ItemName.AbilitiesKickback: ItemData(9658004, 1, ItemType.NORMAL, ItemGroup.MISC, ["abilities/kickback"]),
    ItemName.AbilitiesMailbag: ItemData(9658005, 1, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["abilities/mailbag"]),
    ItemName.AbilitiesPartyhorn: ItemData(9658006, 1, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["abilities/partyhorn"]),
    ItemName.AbilitiesSlugVacuum: ItemData(9658008, 2, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["abilities/slug_vaccum", "abilities/slug_upgrade"]),
    ItemName.AbilitiesSpeed: ItemData(9658009, 1, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["abilities/speed"]),
    ItemName.Bluekey: ItemData(9658010, 1, ItemType.PROGRESSION, ItemGroup.KEYS, ["bluekey"]),
    ItemName.BucketEmpty: ItemData(9658011, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["bucket_empty"]),
    ItemName.DustbunnyDirty: ItemData(9658012, 6, ItemType.PROGRESSION, ItemGroup.QUEST, ["dustbunny_dirty"]),
    ItemName.Greenkey: ItemData(9658013, 1, ItemType.PROGRESSION, ItemGroup.KEYS, ["greenkey"]),
    ItemName.Guano: ItemData(9658014, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["guano"]),
    ItemName.Idol1: ItemData(9658015, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["idol1"]),
    ItemName.Idol2: ItemData(9658016, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["idol2"]),
    ItemName.Idol3: ItemData(9658017, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["idol3"]),
    ItemName.Idol4: ItemData(9658018, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["idol4"]),
    ItemName.Mushroom2: ItemData(9658019, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["mushroom_2"]),
    ItemName.Mushroom3: ItemData(9658020, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["mushroom_3"]),
    ItemName.NimKey: ItemData(9658021, 1, ItemType.PROGRESSION, ItemGroup.KEYS, ["nim_key"]),
    ItemName.Nugget: ItemData(9658022, 4, ItemType.PROGRESSION, ItemGroup.QUEST, ["nugget"]),
    ItemName.PostalBadge: ItemData(9658023, 1, ItemType.PROGRESSION, ItemGroup.KEYS, ["postal_badge"]),
    ItemName.PowerupsSkvader1: ItemData(9658024, 2, ItemType.PROGRESSION, ItemGroup.MISC, ["powerups/skvader_1", "powerups/skvader_2"]),
    ItemName.RewardFruitMedium: ItemData(9658026, 39, ItemType.JUNK, ItemGroup.FRUIT, ["reward_fruit_medium"]),
    ItemName.RewardFruitBig: ItemData(9658027, 54, ItemType.JUNK, ItemGroup.FRUIT, ["reward_fruit_big"]),
    ItemName.SeedPod: ItemData(9658028, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["seed_pod"]),
    ItemName.SkinsSkin1: ItemData(9658029, 1, ItemType.PROGRESSION, ItemGroup.COLLECTIBLE, ["skins/skin_1"]),
    ItemName.SkinsSkin2: ItemData(9658030, 1, ItemType.PROGRESSION, ItemGroup.COLLECTIBLE, ["skins/skin_2"]),
    ItemName.SkinsSkin3: ItemData(9658031, 1, ItemType.PROGRESSION, ItemGroup.COLLECTIBLE, ["skins/skin_3"]),
    ItemName.SkinsSkin4: ItemData(9658032, 1, ItemType.PROGRESSION, ItemGroup.COLLECTIBLE, ["skins/skin_4"]),
    ItemName.SkinsSkin5: ItemData(9658033, 1, ItemType.PROGRESSION, ItemGroup.COLLECTIBLE, ["skins/skin_5"]),
    ItemName.SootlingLeash: ItemData(9658034, 1, ItemType.PROGRESSION, ItemGroup.MOVEMENT, ["sootling_leash"]),
    ItemName.Spores1: ItemData(9658035, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spores_1"]),
    ItemName.Spores2: ItemData(9658036, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spores_2"]),
    ItemName.Spores3: ItemData(9658037, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spores_3"]),
    ItemName.Spores4: ItemData(9658038, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spores_4"]),
    ItemName.Spores5: ItemData(9658039, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spores_5"]),
    ItemName.SpringKey: ItemData(9658040, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["spring_key"]),
    ItemName.Tadpole: ItemData(9658041, 8, ItemType.PROGRESSION, ItemGroup.MISC, ["tadpole"]),
    ItemName.Toolbox: ItemData(9658042, 1, ItemType.PROGRESSION, ItemGroup.QUEST, ["toolbox"]),
    ItemName.TrackerCaves: ItemData(9658043, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["tracker_caves"]),
    ItemName.TrackerJungle: ItemData(9658044, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["tracker_jungle"]),
    ItemName.TrackerPeak: ItemData(9658045, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["tracker_peak"]),
    ItemName.TrackerScarabs: ItemData(9658046, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["tracker_scarabs"]),
    ItemName.TrackerSprings: ItemData(9658047, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["tracker_springs"]),
    ItemName.TraitorSpirit: ItemData(9658048, 4, ItemType.PROGRESSION, ItemGroup.TRACKER, ["traitor_spirit"]),
    ItemName.TreasureMap: ItemData(9658049, 1, ItemType.PROGRESSION, ItemGroup.TRACKER, ["treasure_map"]),
    ItemName.Wallet: ItemData(9658050, 10, ItemType.PROGRESSION, ItemGroup.MISC, ["wallet"]),
    ItemName.Collectible: ItemData(9658051, 80, ItemType.JUNK, ItemGroup.COLLECTIBLE, ["wickerling"]),
}
