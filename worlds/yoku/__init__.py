"""
Author: T Makuluni
Date: Fri, 24 Jan 2025
Description: Main module for Yoku's Island Adventure multiworld randomizer
"""

import os

from typing import List, Dict, ClassVar, Any
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial, MultiWorld, ItemClassification
from .Items import item_table, YokuItem, ItemType, ItemGroup, ItemName
from .Locations import location_table,YokuLocation
from .Options import YokuOptions
from .Regions import YokuRegions
from .SaveFile import SaveFiles, SaveItem

class YokusWeb(WebWorld):
    """
    Class used to generate the Yoku's Island Adventure Game Web pages (setup, tutorial, etc.)
    """
    theme = "jungle"

    bug_report_page = "https://git.makuluni.com/emakman/YokusIslandAdventure_randomizer/issues"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Yoku's Island Adventure for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["T Makuluni"]
    )

    tutorials = [setup]


class YokuWorld(World):
    """
    In Yoku's Island Express, players control Yoku, a dung beetle,
    who becomes a postmaster as he arrives at a fictional island of Mokumana.
    The player is tasked with saving the island from a looming calamity,
    as the island's deity figure is attacked.
    From: https://en.wikipedia.org/wiki/Yoku's_Island_Express
    """

    game: str = "Yoku's Island Express"
    "The name of the game"

    topology_present = False # disabled until I have useful regions
    "show path to required location checks in spoiler" 

    web: WebWorld = YokusWeb()
    "The web page generation informations"

    item_name_to_id: ClassVar[Dict[str, int]] =\
        {name.value: data.id for name, data in item_table.items()}
    "The name and associated ID of each item of the world"

    item_name_groups = {
        "Movement": {"Progressive Dive Fish", "Mail bag", "Noisemaker",
                     "Slug Vacuum", "Grand Postmaster Badge", "Sootling Leash"},
    }
    """Grouping item make it easier to find them"""

    location_name_to_id = {loc: data["id"] for loc, data in location_table.items()}
    "The name and associated ID of each location of the world"

    # Is this needed? I'm using location ids from the game, so I hope not.
    # base_id = 698000
    # "The starting ID of the items and locations of the world"

    options_dataclass = YokuOptions
    "Used to manage world options"

    options: YokuOptions
    "Every options of the world"

    regions: YokuRegions
    "Used to manage Regions"

    def __init__(self, multiworld: MultiWorld, player: int):
        """Initialisation of the Yoku's Island Express World"""
        super(YokuWorld, self).__init__(multiworld, player)
        self.regions = YokuRegions(multiworld, player)

    def create_regions(self) -> None:
        """
        Create every Region in `regions`
        """
        self.regions.add_regions_to_world()
        self.regions.connect_regions(self.options)
        self.regions.add_event_locations()

    def create_item(self, name: ItemName) -> YokuItem:
        """
        Create an YokuItem using 'name' as item name.
        """
        result: YokuItem
        try:
            data = item_table[name]
            classification: ItemClassification = ItemClassification.useful
            if data.type == ItemType.JUNK:
                classification = ItemClassification.filler
            elif data.type == ItemType.PROGRESSION:
                classification = ItemClassification.progression
            result = YokuItem(name.value, classification, data.id, self.player)
        except BaseException:
            raise Exception('The item ' + name.value + ' is not valid.')

        return result

    def create_items(self) -> None:
        """Create every item in the world"""
        for name, data in item_table.items():
            for _ in range(data.count):
                item = self.create_item(name)
                self.multiworld.itempool.append(item)

    def set_rules(self) -> None:
        """
        Launched when the Multiworld generator is ready to generate rules
        """

        self.multiworld.completion_condition[self.player] = lambda \
            state: state.has("Victory", self.player)

    def generate_basic(self) -> None:
        """
        Player-specific randomization that does not affect logic.
        Used to fill then `ingredients_substitution` list
        """

    def fill_slot_data(self) -> Dict[str, Any]:
        return {}

    def generate_output(self, output_directory: str):
        # copy items back to locations
        items: list[SaveItem] = []
        for r in self.multiworld.get_regions(self.player):
            for loc in r.locations:
                if isinstance(loc, YokuLocation) and loc.name in location_table:
                    assert(loc.item)
                    items+=[SaveItem(loc.name,loc.item, self.multiworld)]

        file_base = self.multiworld.get_out_file_name_base(self.player)
        files = SaveFiles(os.path.join(output_directory,file_base),items)
        files.save()
