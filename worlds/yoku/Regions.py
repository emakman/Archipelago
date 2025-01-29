"""
Author: T Makuluni
Date: Fri, 26 Jan 2025
Description: Used to manage Regions in the Yoku's Island Express multiworld randomizer
"""

from typing import Dict, Optional
from BaseClasses import MultiWorld, Region, Entrance, ItemClassification, CollectionState
from .Items import YokuItem, ItemName
from .Locations import YokuLocations, YokuLocation
from .Options import YokuOptions
from worlds.generic.Rules import add_rule, set_rule
from collections.abc import Callable

# combinators for item lookups
def _has(item: ItemName, count: int = 1) -> Callable[[CollectionState, int], bool]:
    """`player` in `state` has the item `item`"""
    return lambda state, player: state.has(item.value, player, count)

def _and_inner(state: CollectionState, player: int, *args: Callable[[CollectionState, int], bool]) -> bool:
    for arg in args:
        if not arg(state, player):
            return False
    return True

def _and_(*args: Callable[[CollectionState, int], bool]) -> Callable[[CollectionState, int], bool]:
    return lambda state, player: _and_inner(state, player, *args)

def _or_inner(state: CollectionState, player: int, *args: Callable[[CollectionState, int], bool]) -> bool:
    for arg in args:
        if arg(state, player):
            return True 
    return False

def _or_(*args: Callable[[CollectionState, int], bool]) -> Callable[[CollectionState, int], bool]:
    return lambda state, player: _or_inner(state, player, *args)

class YokuRegions:
    """
    Class used to create regions of the Yoku's Island Express game
    """
    cave_abyssal_access0: Region
    cave_abyssal_access1: Region
    cave_beach_bottom0: Region
    cave_beaver_blockade0: Region
    cave_beaver_blockade1: Region
    cave_beaver_blockade2: Region
    cave_clammy_cenote0: Region
    cave_clammy_cenote1: Region
    cave_clammy_cenote2: Region
    cave_east_bay_shore0: Region
    cave_east_bay_shore1: Region
    cave_east_bay_shore2: Region
    cave_east_bay_shore3: Region
    cave_temple_terror_lower0: Region
    cave_temple_terror_lower1: Region
    cave_temple_terror_lower2: Region
    cave_temple_terror_lower3: Region
    cave_temple_terror_lower4: Region
    cave_temple_terror_lower5: Region
    cave_temple_terror_lower6: Region
    cave_temple_terror_treasury0: Region
    cave_temple_terror_treasury1: Region
    cave_temple_terror_treasury2: Region
    cave_temple_terror_upper0: Region
    cave_winding_waterway0: Region
    hub_bowel_bumping_left0: Region
    hub_cliffside_creek0: Region
    hub_cliffside_creek1: Region
    hub_cliffside_creek2: Region
    hub_festival0: Region
    hub_festival_upper0: Region
    hub_festival_upper1: Region
    hub_festival_upper2: Region
    hub_hermits_home0: Region
    hub_island_express0: Region
    hub_island_express1: Region
    hub_island_express2: Region
    hub_island_express3: Region
    hub_left_lemur_lane0: Region
    hub_left_lofty_logo0: Region
    hub_left_lofty_logo1: Region
    hub_left_lofty_logo2: Region
    hub_obtainium_outland0: Region
    hub_obtainium_outland1: Region
    hub_soaring_stone0: Region
    hub_village0: Region
    hub_village1: Region
    hub_village2: Region
    hub_village3: Region
    hub_village4: Region
    hub_village5: Region
    hub_village6: Region
    hub_village7: Region
    hub_village8: Region
    hub_white_cliff0: Region
    hub_white_cliff1: Region
    hub_white_cliff2: Region
    menu: Region
    intro_landing1: Region
    intro_landing2: Region
    intro_landing3: Region
    intro_landing_creepy_cavern0: Region
    intro_landing_creepy_cavern1: Region
    intro_landing_left0: Region
    intro_landing_right0: Region
    intro_landing_right1: Region
    intro_landing_right2: Region
    intro_landing_right3: Region
    intro_landing_upper0: Region
    intro_landing_upper1: Region
    intro_landing_upper2: Region
    intro_landing_upper3: Region
    intro_landing_upper4: Region
    intro_landing_upper5: Region
    intro_muddled_morass0: Region
    intro_muddled_morass1: Region
    intro_secret0: Region
    jungle_canyon_caper0: Region
    jungle_canyon_caper1: Region
    jungle_crammed_canopy0: Region
    jungle_crammed_canopy1: Region
    jungle_misty_meadow0: Region
    jungle_misty_meadow1: Region
    jungle_misty_meadow2: Region
    jungle_mollusc_madness0: Region
    jungle_mollusc_madness1: Region
    jungle_mollusc_madness2: Region
    jungle_mollusc_madness3: Region
    jungle_roots0: Region
    jungle_roots1: Region
    jungle_slug_struggle0: Region
    jungle_slug_struggle1: Region
    jungle_slug_struggle2: Region
    jungle_slug_struggle3: Region
    jungle_slug_struggle4: Region
    jungle_spikey_stockade0: Region
    jungle_tall_tall_tower0: Region
    jungle_tall_tall_tower1: Region
    jungle_tall_tall_tower2: Region
    jungle_willy0: Region
    jungle_willy1: Region
    jungle_willy2: Region
    peak_aerial_ascent0: Region
    peak_aerial_ascent1: Region
    peak_aerial_ascent2: Region
    peak_aerial_ascent3: Region
    peak_aerial_ascent4: Region
    peak_aerial_ascent5: Region
    peak_aerial_ascent6: Region
    peak_aerial_ascent7: Region
    peak_beanstalk_base0: Region
    peak_beanstalk_base1: Region
    peak_beanstalk_base2: Region
    peak_beanstalk_base3: Region
    peak_beanstalk_base4: Region
    peak_beanstalk_base5: Region
    peak_crooked_cliff0: Region
    peak_crystal_crater0: Region
    peak_crystal_crater1: Region
    peak_crystal_crater2: Region
    peak_crystal_crater3: Region
    peak_filthy_flat0: Region
    peak_filthy_flat1: Region
    peak_filthy_flat2: Region
    peak_filthy_flat3: Region
    peak_filthy_flat4: Region
    peak_filthy_flat5: Region
    peak_frostpine_forest0: Region
    peak_frostpine_forest1: Region
    peak_frostpine_forest2: Region
    peak_guano_grief0: Region
    peak_guano_grief1: Region
    peak_guano_grief2: Region
    peak_guano_grief3: Region
    peak_guano_grief4: Region
    peak_guano_grief5: Region
    peak_guano_grief6: Region
    peak_ice_cold_idol0: Region
    peak_ice_cold_idol1: Region
    peak_obtainium_oracle0: Region
    peak_spider_fight0: Region
    peak_spider_fight1: Region
    spring_bubbly_basin0: Region
    spring_bubbly_basin1: Region
    spring_bubbly_basin2: Region
    spring_bubbly_basin3: Region
    spring_bubbly_basin4: Region
    spring_cloudburst_cliffs0: Region
    spring_cloudburst_cliffs1: Region
    spring_cloudburst_cliffs2: Region
    spring_cloudburst_cliffs3: Region
    spring_cloudburst_cliffs4: Region
    spring_cloudburst_cliffs5: Region
    spring_gangway_grotto0: Region
    spring_gangway_grotto1: Region
    spring_gangway_grotto2: Region
    spring_gangway_grotto3: Region
    spring_gangway_grotto4: Region
    spring_gangway_grotto5: Region
    spring_gangway_grotto6: Region
    spring_hidden_hotspring0: Region
    spring_hidden_hotspring1: Region
    spring_hidden_hotspring2: Region
    spring_hidden_hotspring3: Region
    spring_hidden_hotspring4: Region
    spring_jailhouse_japes0: Region
    spring_shoddy_shanty0: Region
    spring_shoddy_shanty1: Region
    spring_shoddy_shanty2: Region
    spring_shoddy_shanty3: Region
    spring_sleek_slabs0: Region
    spring_sleek_slabs1: Region
    spring_sleek_slabs2: Region
    spring_sleek_slabs3: Region
    spring_sleek_slabs4: Region
    spring_sleek_slabs5: Region
    spring_tiny_broad0: Region
    spring_tiny_broad1: Region
    spring_tiny_broad2: Region
    spring_tiny_broad3: Region
    spring_tiny_broad4: Region
    spring_tiny_broad5: Region
    spring_tiny_broad6: Region
    spring_tortoise_tunnel0: Region
    spring_yokos_yam0: Region
    spring_yokos_yam1: Region
    spring_yokos_yam2: Region
    win: Region
    """
    Every Region of the game
    """

    multiworld: MultiWorld
    """
    The Current Multiworld game.
    """

    player: int
    """
    The ID of the player
    """

    def __add_region(self, hint: str,
                     locations: Optional[Dict[str, int]]) -> Region:
        """
        Create a new Region, add it to the `world` regions and return it.
        Be aware that this function have a side effect on ``world`.`regions`
        """
        region: Region = Region(hint, self.player, self.multiworld, hint)
        if locations is not None:
            region.add_locations(locations, YokuLocation)
        return region

    def __create_regions_intro(self) -> None:
        """
        Create the intro regions.
        """
        self.menu = self.__add_region("Menu", YokuLocations.locations_menu)
        self.intro_landing1 = self.__add_region("intro_landing1", YokuLocations.locations_intro_landing1)
        self.intro_landing2 = self.__add_region("intro_landing2", YokuLocations.locations_intro_landing2)
        self.intro_landing3 = self.__add_region("intro_landing3", YokuLocations.locations_intro_landing3)
        self.intro_landing_creepy_cavern0 = self.__add_region("intro_landing_creepy_cavern0", YokuLocations.locations_intro_landing_creepy_cavern0)
        self.intro_landing_creepy_cavern1 = self.__add_region("intro_landing_creepy_cavern1", YokuLocations.locations_intro_landing_creepy_cavern1)
        self.intro_landing_left0 = self.__add_region("intro_landing_left0", YokuLocations.locations_intro_landing_left0)
        self.intro_landing_right0 = self.__add_region("intro_landing_right0", YokuLocations.locations_intro_landing_right0)
        self.intro_landing_right1 = self.__add_region("intro_landing_right1", YokuLocations.locations_intro_landing_right1)
        self.intro_landing_right2 = self.__add_region("intro_landing_right2", YokuLocations.locations_intro_landing_right2)
        self.intro_landing_right3 = self.__add_region("intro_landing_right3", YokuLocations.locations_intro_landing_right3)
        self.intro_landing_upper0 = self.__add_region("intro_landing_upper0", YokuLocations.locations_intro_landing_upper0)
        self.intro_landing_upper1 = self.__add_region("intro_landing_upper1", YokuLocations.locations_intro_landing_upper1)
        self.intro_landing_upper2 = self.__add_region("intro_landing_upper2", YokuLocations.locations_intro_landing_upper2)
        self.intro_landing_upper3 = self.__add_region("intro_landing_upper3", YokuLocations.locations_intro_landing_upper3)
        self.intro_landing_upper4 = self.__add_region("intro_landing_upper4", YokuLocations.locations_intro_landing_upper4)
        self.intro_landing_upper5 = self.__add_region("intro_landing_upper5", YokuLocations.locations_intro_landing_upper5)
        self.intro_muddled_morass0 = self.__add_region("intro_muddled_morass0", YokuLocations.locations_intro_muddled_morass0)
        self.intro_muddled_morass1 = self.__add_region("intro_muddled_morass1", YokuLocations.locations_intro_muddled_morass1)
        self.intro_secret0 = self.__add_region("intro_secret0", YokuLocations.locations_intro_secret0)

    def __create_regions_cave(self) -> None:
        """
        Create the underdark regions.
        """
        self.cave_abyssal_access0 = self.__add_region("cave_abyssal_access0", YokuLocations.locations_cave_abyssal_access0)
        self.cave_abyssal_access1 = self.__add_region("cave_abyssal_access1", YokuLocations.locations_cave_abyssal_access1)
        self.cave_beach_bottom0 = self.__add_region("cave_beach_bottom0", YokuLocations.locations_cave_beach_bottom0)
        self.cave_beaver_blockade0 = self.__add_region("cave_beaver_blockade0", YokuLocations.locations_cave_beaver_blockade0)
        self.cave_beaver_blockade1 = self.__add_region("cave_beaver_blockade1", YokuLocations.locations_cave_beaver_blockade1)
        self.cave_beaver_blockade2 = self.__add_region("cave_beaver_blockade2", YokuLocations.locations_cave_beaver_blockade2)
        self.cave_clammy_cenote0 = self.__add_region("cave_clammy_cenote0", YokuLocations.locations_cave_clammy_cenote0)
        self.cave_clammy_cenote1 = self.__add_region("cave_clammy_cenote1", YokuLocations.locations_cave_clammy_cenote1)
        self.cave_clammy_cenote2 = self.__add_region("cave_clammy_cenote2", YokuLocations.locations_cave_clammy_cenote2)
        self.cave_east_bay_shore0 = self.__add_region("cave_east_bay_shore0", YokuLocations.locations_cave_east_bay_shore0)
        self.cave_east_bay_shore1 = self.__add_region("cave_east_bay_shore1", YokuLocations.locations_cave_east_bay_shore1)
        self.cave_east_bay_shore2 = self.__add_region("cave_east_bay_shore2", YokuLocations.locations_cave_east_bay_shore2)
        self.cave_east_bay_shore3 = self.__add_region("cave_east_bay_shore3", YokuLocations.locations_cave_east_bay_shore3)
        self.cave_temple_terror_lower0 = self.__add_region("cave_temple_terror_lower0", YokuLocations.locations_cave_temple_terror_lower0)
        self.cave_temple_terror_lower1 = self.__add_region("cave_temple_terror_lower1", YokuLocations.locations_cave_temple_terror_lower1)
        self.cave_temple_terror_lower2 = self.__add_region("cave_temple_terror_lower2", YokuLocations.locations_cave_temple_terror_lower2)
        self.cave_temple_terror_lower3 = self.__add_region("cave_temple_terror_lower3", YokuLocations.locations_cave_temple_terror_lower3)
        self.cave_temple_terror_lower4 = self.__add_region("cave_temple_terror_lower4", YokuLocations.locations_cave_temple_terror_lower4)
        self.cave_temple_terror_lower5 = self.__add_region("cave_temple_terror_lower5", YokuLocations.locations_cave_temple_terror_lower5)
        self.cave_temple_terror_lower6 = self.__add_region("cave_temple_terror_lower6", YokuLocations.locations_cave_temple_terror_lower6)
        self.cave_temple_terror_treasury0 = self.__add_region("cave_temple_terror_treasury0", YokuLocations.locations_cave_temple_terror_treasury0)
        self.cave_temple_terror_treasury1 = self.__add_region("cave_temple_terror_treasury1", YokuLocations.locations_cave_temple_terror_treasury1)
        self.cave_temple_terror_treasury2 = self.__add_region("cave_temple_terror_treasury2", YokuLocations.locations_cave_temple_terror_treasury2)
        self.cave_temple_terror_upper0 = self.__add_region("cave_temple_terror_upper0", YokuLocations.locations_cave_temple_terror_upper0)
        self.cave_winding_waterway0 = self.__add_region("cave_winding_waterway0", YokuLocations.locations_cave_winding_waterway0)

    def __create_regions_hub(self) -> None:
        """
        Create the central regions.
        """
        self.hub_bowel_bumping_left0 = self.__add_region("hub_bowel_bumping_left0", YokuLocations.locations_hub_bowel_bumping_left0)
        self.hub_cliffside_creek0 = self.__add_region("hub_cliffside_creek0", YokuLocations.locations_hub_cliffside_creek0)
        self.hub_cliffside_creek1 = self.__add_region("hub_cliffside_creek1", YokuLocations.locations_hub_cliffside_creek1)
        self.hub_cliffside_creek2 = self.__add_region("hub_cliffside_creek2", YokuLocations.locations_hub_cliffside_creek2)
        self.hub_festival0 = self.__add_region("hub_festival0", YokuLocations.locations_hub_festival0)
        self.hub_festival_upper0 = self.__add_region("hub_festival_upper0", YokuLocations.locations_hub_festival_upper0)
        self.hub_festival_upper1 = self.__add_region("hub_festival_upper1", YokuLocations.locations_hub_festival_upper1)
        self.hub_festival_upper2 = self.__add_region("hub_festival_upper2", YokuLocations.locations_hub_festival_upper2)
        self.hub_hermits_home0 = self.__add_region("hub_hermits_home0", YokuLocations.locations_hub_hermits_home0)
        self.hub_island_express0 = self.__add_region("hub_island_express0", YokuLocations.locations_hub_island_express0)
        self.hub_island_express1 = self.__add_region("hub_island_express1", YokuLocations.locations_hub_island_express1)
        self.hub_island_express2 = self.__add_region("hub_island_express2", YokuLocations.locations_hub_island_express2)
        self.hub_island_express3 = self.__add_region("hub_island_express3", YokuLocations.locations_hub_island_express3)
        self.hub_left_lemur_lane0 = self.__add_region("hub_left_lemur_lane0", YokuLocations.locations_hub_left_lemur_lane0)
        self.hub_left_lofty_logo0 = self.__add_region("hub_left_lofty_logo0", YokuLocations.locations_hub_left_lofty_logo0)
        self.hub_left_lofty_logo1 = self.__add_region("hub_left_lofty_logo1", YokuLocations.locations_hub_left_lofty_logo1)
        self.hub_left_lofty_logo2 = self.__add_region("hub_left_lofty_logo2", YokuLocations.locations_hub_left_lofty_logo2)
        self.hub_obtainium_outland0 = self.__add_region("hub_obtainium_outland0", YokuLocations.locations_hub_obtainium_outland0)
        self.hub_obtainium_outland1 = self.__add_region("hub_obtainium_outland1", YokuLocations.locations_hub_obtainium_outland1)
        self.hub_soaring_stone0 = self.__add_region("hub_soaring_stone0", YokuLocations.locations_hub_soaring_stone0)
        self.hub_village0 = self.__add_region("hub_village0", YokuLocations.locations_hub_village0)
        self.hub_village1 = self.__add_region("hub_village1", YokuLocations.locations_hub_village1)
        self.hub_village2 = self.__add_region("hub_village2", YokuLocations.locations_hub_village2)
        self.hub_village3 = self.__add_region("hub_village3", YokuLocations.locations_hub_village3)
        self.hub_village4 = self.__add_region("hub_village4", YokuLocations.locations_hub_village4)
        self.hub_village5 = self.__add_region("hub_village5", YokuLocations.locations_hub_village5)
        self.hub_village6 = self.__add_region("hub_village6", YokuLocations.locations_hub_village6)
        self.hub_village7 = self.__add_region("hub_village7", YokuLocations.locations_hub_village7)
        self.hub_village8 = self.__add_region("hub_village8", YokuLocations.locations_hub_village8)
        self.hub_white_cliff0 = self.__add_region("hub_white_cliff0", YokuLocations.locations_hub_white_cliff0)
        self.hub_white_cliff1 = self.__add_region("hub_white_cliff1", YokuLocations.locations_hub_white_cliff1)
        self.hub_white_cliff2 = self.__add_region("hub_white_cliff2", YokuLocations.locations_hub_white_cliff2)
        self.win = self.__add_region("win", None)

    def __create_regions_jungle(self) -> None:
        """
        Create the Gorilla Woods regions.
        """
        self.jungle_canyon_caper0 = self.__add_region("jungle_canyon_caper0", YokuLocations.locations_jungle_canyon_caper0)
        self.jungle_canyon_caper1 = self.__add_region("jungle_canyon_caper1", YokuLocations.locations_jungle_canyon_caper1)
        self.jungle_crammed_canopy0 = self.__add_region("jungle_crammed_canopy0", YokuLocations.locations_jungle_crammed_canopy0)
        self.jungle_crammed_canopy1 = self.__add_region("jungle_crammed_canopy1", YokuLocations.locations_jungle_crammed_canopy1)
        self.jungle_misty_meadow0 = self.__add_region("jungle_misty_meadow0", YokuLocations.locations_jungle_misty_meadow0)
        self.jungle_misty_meadow1 = self.__add_region("jungle_misty_meadow1", YokuLocations.locations_jungle_misty_meadow1)
        self.jungle_misty_meadow2 = self.__add_region("jungle_misty_meadow2", YokuLocations.locations_jungle_misty_meadow2)
        self.jungle_mollusc_madness0 = self.__add_region("jungle_mollusc_madness0", YokuLocations.locations_jungle_mollusc_madness0)
        self.jungle_mollusc_madness1 = self.__add_region("jungle_mollusc_madness1", YokuLocations.locations_jungle_mollusc_madness1)
        self.jungle_mollusc_madness2 = self.__add_region("jungle_mollusc_madness2", YokuLocations.locations_jungle_mollusc_madness2)
        self.jungle_mollusc_madness3 = self.__add_region("jungle_mollusc_madness3", YokuLocations.locations_jungle_mollusc_madness3)
        self.jungle_roots0 = self.__add_region("jungle_roots0", YokuLocations.locations_jungle_roots0)
        self.jungle_roots1 = self.__add_region("jungle_roots1", YokuLocations.locations_jungle_roots1)
        self.jungle_slug_struggle0 = self.__add_region("jungle_slug_struggle0", YokuLocations.locations_jungle_slug_struggle0)
        self.jungle_slug_struggle1 = self.__add_region("jungle_slug_struggle1", YokuLocations.locations_jungle_slug_struggle1)
        self.jungle_slug_struggle2 = self.__add_region("jungle_slug_struggle2", YokuLocations.locations_jungle_slug_struggle2)
        self.jungle_slug_struggle3 = self.__add_region("jungle_slug_struggle3", YokuLocations.locations_jungle_slug_struggle3)
        self.jungle_slug_struggle4 = self.__add_region("jungle_slug_struggle4", YokuLocations.locations_jungle_slug_struggle4)
        self.jungle_spikey_stockade0 = self.__add_region("jungle_spikey_stockade0", YokuLocations.locations_jungle_spikey_stockade0)
        self.jungle_tall_tall_tower0 = self.__add_region("jungle_tall_tall_tower0", YokuLocations.locations_jungle_tall_tall_tower0)
        self.jungle_tall_tall_tower1 = self.__add_region("jungle_tall_tall_tower1", YokuLocations.locations_jungle_tall_tall_tower1)
        self.jungle_tall_tall_tower2 = self.__add_region("jungle_tall_tall_tower2", YokuLocations.locations_jungle_tall_tall_tower2)
        self.jungle_willy0 = self.__add_region("jungle_willy0", YokuLocations.locations_jungle_willy0)
        self.jungle_willy1 = self.__add_region("jungle_willy1", YokuLocations.locations_jungle_willy1)
        self.jungle_willy2 = self.__add_region("jungle_willy2", YokuLocations.locations_jungle_willy2)

    def __create_regions_peak(self) -> None:
        """
        Create the Ivory Peak regions.
        """
        self.peak_aerial_ascent0 = self.__add_region("peak_aerial_ascent0", YokuLocations.locations_peak_aerial_ascent0)
        self.peak_aerial_ascent1 = self.__add_region("peak_aerial_ascent1", YokuLocations.locations_peak_aerial_ascent1)
        self.peak_aerial_ascent2 = self.__add_region("peak_aerial_ascent2", YokuLocations.locations_peak_aerial_ascent2)
        self.peak_aerial_ascent3 = self.__add_region("peak_aerial_ascent3", YokuLocations.locations_peak_aerial_ascent3)
        self.peak_aerial_ascent4 = self.__add_region("peak_aerial_ascent4", YokuLocations.locations_peak_aerial_ascent4)
        self.peak_aerial_ascent5 = self.__add_region("peak_aerial_ascent5", YokuLocations.locations_peak_aerial_ascent5)
        self.peak_aerial_ascent6 = self.__add_region("peak_aerial_ascent6", YokuLocations.locations_peak_aerial_ascent6)
        self.peak_aerial_ascent7 = self.__add_region("peak_aerial_ascent7", YokuLocations.locations_peak_aerial_ascent7)
        self.peak_beanstalk_base0 = self.__add_region("peak_beanstalk_base0", YokuLocations.locations_peak_beanstalk_base0)
        self.peak_beanstalk_base1 = self.__add_region("peak_beanstalk_base1", YokuLocations.locations_peak_beanstalk_base1)
        self.peak_beanstalk_base2 = self.__add_region("peak_beanstalk_base2", YokuLocations.locations_peak_beanstalk_base2)
        self.peak_beanstalk_base3 = self.__add_region("peak_beanstalk_base3", YokuLocations.locations_peak_beanstalk_base3)
        self.peak_beanstalk_base4 = self.__add_region("peak_beanstalk_base4", YokuLocations.locations_peak_beanstalk_base4)
        self.peak_beanstalk_base5 = self.__add_region("peak_beanstalk_base5", YokuLocations.locations_peak_beanstalk_base5)
        self.peak_crooked_cliff0 = self.__add_region("peak_crooked_cliff0", YokuLocations.locations_peak_crooked_cliff0)
        self.peak_crystal_crater0 = self.__add_region("peak_crystal_crater0", YokuLocations.locations_peak_crystal_crater0)
        self.peak_crystal_crater1 = self.__add_region("peak_crystal_crater1", YokuLocations.locations_peak_crystal_crater1)
        self.peak_crystal_crater2 = self.__add_region("peak_crystal_crater2", YokuLocations.locations_peak_crystal_crater2)
        self.peak_crystal_crater3 = self.__add_region("peak_crystal_crater3", YokuLocations.locations_peak_crystal_crater3)
        self.peak_filthy_flat0 = self.__add_region("peak_filthy_flat0", YokuLocations.locations_peak_filthy_flat0)
        self.peak_filthy_flat1 = self.__add_region("peak_filthy_flat1", YokuLocations.locations_peak_filthy_flat1)
        self.peak_filthy_flat2 = self.__add_region("peak_filthy_flat2", YokuLocations.locations_peak_filthy_flat2)
        self.peak_filthy_flat3 = self.__add_region("peak_filthy_flat3", YokuLocations.locations_peak_filthy_flat3)
        self.peak_filthy_flat4 = self.__add_region("peak_filthy_flat4", YokuLocations.locations_peak_filthy_flat4)
        self.peak_filthy_flat5 = self.__add_region("peak_filthy_flat5", YokuLocations.locations_peak_filthy_flat5)
        self.peak_frostpine_forest0 = self.__add_region("peak_frostpine_forest0", YokuLocations.locations_peak_frostpine_forest0)
        self.peak_frostpine_forest1 = self.__add_region("peak_frostpine_forest1", YokuLocations.locations_peak_frostpine_forest1)
        self.peak_frostpine_forest2 = self.__add_region("peak_frostpine_forest2", YokuLocations.locations_peak_frostpine_forest2)
        self.peak_guano_grief0 = self.__add_region("peak_guano_grief0", YokuLocations.locations_peak_guano_grief0)
        self.peak_guano_grief1 = self.__add_region("peak_guano_grief1", YokuLocations.locations_peak_guano_grief1)
        self.peak_guano_grief2 = self.__add_region("peak_guano_grief2", YokuLocations.locations_peak_guano_grief2)
        self.peak_guano_grief3 = self.__add_region("peak_guano_grief3", YokuLocations.locations_peak_guano_grief3)
        self.peak_guano_grief4 = self.__add_region("peak_guano_grief4", YokuLocations.locations_peak_guano_grief4)
        self.peak_guano_grief5 = self.__add_region("peak_guano_grief5", YokuLocations.locations_peak_guano_grief5)
        self.peak_guano_grief6 = self.__add_region("peak_guano_grief6", YokuLocations.locations_peak_guano_grief6)
        self.peak_ice_cold_idol0 = self.__add_region("peak_ice_cold_idol0", YokuLocations.locations_peak_ice_cold_idol0)
        self.peak_ice_cold_idol1 = self.__add_region("peak_ice_cold_idol1", YokuLocations.locations_peak_ice_cold_idol1)
        self.peak_obtainium_oracle0 = self.__add_region("peak_obtainium_oracle0", YokuLocations.locations_peak_obtainium_oracle0)
        self.peak_spider_fight0 = self.__add_region("peak_spider_fight0", YokuLocations.locations_peak_spider_fight0)
        self.peak_spider_fight1 = self.__add_region("peak_spider_fight1", YokuLocations.locations_peak_spider_fight1)

    def __create_regions_spring(self) -> None:
        """
        Create the Marrow Hills regions.
        """
        self.spring_bubbly_basin0 = self.__add_region("spring_bubbly_basin0", YokuLocations.locations_spring_bubbly_basin0)
        self.spring_bubbly_basin1 = self.__add_region("spring_bubbly_basin1", YokuLocations.locations_spring_bubbly_basin1)
        self.spring_bubbly_basin2 = self.__add_region("spring_bubbly_basin2", YokuLocations.locations_spring_bubbly_basin2)
        self.spring_bubbly_basin3 = self.__add_region("spring_bubbly_basin3", YokuLocations.locations_spring_bubbly_basin3)
        self.spring_bubbly_basin4 = self.__add_region("spring_bubbly_basin4", YokuLocations.locations_spring_bubbly_basin4)
        self.spring_cloudburst_cliffs0 = self.__add_region("spring_cloudburst_cliffs0", YokuLocations.locations_spring_cloudburst_cliffs0)
        self.spring_cloudburst_cliffs1 = self.__add_region("spring_cloudburst_cliffs1", YokuLocations.locations_spring_cloudburst_cliffs1)
        self.spring_cloudburst_cliffs2 = self.__add_region("spring_cloudburst_cliffs2", YokuLocations.locations_spring_cloudburst_cliffs2)
        self.spring_cloudburst_cliffs3 = self.__add_region("spring_cloudburst_cliffs3", YokuLocations.locations_spring_cloudburst_cliffs3)
        self.spring_cloudburst_cliffs4 = self.__add_region("spring_cloudburst_cliffs4", YokuLocations.locations_spring_cloudburst_cliffs4)
        self.spring_cloudburst_cliffs5 = self.__add_region("spring_cloudburst_cliffs5", YokuLocations.locations_spring_cloudburst_cliffs5)
        self.spring_gangway_grotto0 = self.__add_region("spring_gangway_grotto0", YokuLocations.locations_spring_gangway_grotto0)
        self.spring_gangway_grotto1 = self.__add_region("spring_gangway_grotto1", YokuLocations.locations_spring_gangway_grotto1)
        self.spring_gangway_grotto2 = self.__add_region("spring_gangway_grotto2", YokuLocations.locations_spring_gangway_grotto2)
        self.spring_gangway_grotto3 = self.__add_region("spring_gangway_grotto3", YokuLocations.locations_spring_gangway_grotto3)
        self.spring_gangway_grotto4 = self.__add_region("spring_gangway_grotto4", YokuLocations.locations_spring_gangway_grotto4)
        self.spring_gangway_grotto5 = self.__add_region("spring_gangway_grotto5", YokuLocations.locations_spring_gangway_grotto5)
        self.spring_gangway_grotto6 = self.__add_region("spring_gangway_grotto6", YokuLocations.locations_spring_gangway_grotto6)
        self.spring_hidden_hotspring0 = self.__add_region("spring_hidden_hotspring0", YokuLocations.locations_spring_hidden_hotspring0)
        self.spring_hidden_hotspring1 = self.__add_region("spring_hidden_hotspring1", YokuLocations.locations_spring_hidden_hotspring1)
        self.spring_hidden_hotspring2 = self.__add_region("spring_hidden_hotspring2", YokuLocations.locations_spring_hidden_hotspring2)
        self.spring_hidden_hotspring3 = self.__add_region("spring_hidden_hotspring3", YokuLocations.locations_spring_hidden_hotspring3)
        self.spring_hidden_hotspring4 = self.__add_region("spring_hidden_hotspring4", YokuLocations.locations_spring_hidden_hotspring4)
        self.spring_jailhouse_japes0 = self.__add_region("spring_jailhouse_japes0", YokuLocations.locations_spring_jailhouse_japes0)
        self.spring_shoddy_shanty0 = self.__add_region("spring_shoddy_shanty0", YokuLocations.locations_spring_shoddy_shanty0)
        self.spring_shoddy_shanty1 = self.__add_region("spring_shoddy_shanty1", YokuLocations.locations_spring_shoddy_shanty1)
        self.spring_shoddy_shanty2 = self.__add_region("spring_shoddy_shanty2", YokuLocations.locations_spring_shoddy_shanty2)
        self.spring_shoddy_shanty3 = self.__add_region("spring_shoddy_shanty3", YokuLocations.locations_spring_shoddy_shanty3)
        self.spring_sleek_slabs0 = self.__add_region("spring_sleek_slabs0", YokuLocations.locations_spring_sleek_slabs0)
        self.spring_sleek_slabs1 = self.__add_region("spring_sleek_slabs1", YokuLocations.locations_spring_sleek_slabs1)
        self.spring_sleek_slabs2 = self.__add_region("spring_sleek_slabs2", YokuLocations.locations_spring_sleek_slabs2)
        self.spring_sleek_slabs3 = self.__add_region("spring_sleek_slabs3", YokuLocations.locations_spring_sleek_slabs3)
        self.spring_sleek_slabs4 = self.__add_region("spring_sleek_slabs4", YokuLocations.locations_spring_sleek_slabs4)
        self.spring_sleek_slabs5 = self.__add_region("spring_sleek_slabs5", YokuLocations.locations_spring_sleek_slabs5)
        self.spring_tiny_broad0 = self.__add_region("spring_tiny_broad0", YokuLocations.locations_spring_tiny_broad0)
        self.spring_tiny_broad1 = self.__add_region("spring_tiny_broad1", YokuLocations.locations_spring_tiny_broad1)
        self.spring_tiny_broad2 = self.__add_region("spring_tiny_broad2", YokuLocations.locations_spring_tiny_broad2)
        self.spring_tiny_broad3 = self.__add_region("spring_tiny_broad3", YokuLocations.locations_spring_tiny_broad3)
        self.spring_tiny_broad4 = self.__add_region("spring_tiny_broad4", YokuLocations.locations_spring_tiny_broad4)
        self.spring_tiny_broad5 = self.__add_region("spring_tiny_broad5", YokuLocations.locations_spring_tiny_broad5)
        self.spring_tiny_broad6 = self.__add_region("spring_tiny_broad6", YokuLocations.locations_spring_tiny_broad6)
        self.spring_tortoise_tunnel0 = self.__add_region("spring_tortoise_tunnel0", YokuLocations.locations_spring_tortoise_tunnel0)
        self.spring_yokos_yam0 = self.__add_region("spring_yokos_yam0", YokuLocations.locations_spring_yokos_yam0)
        self.spring_yokos_yam1 = self.__add_region("spring_yokos_yam1", YokuLocations.locations_spring_yokos_yam1)
        self.spring_yokos_yam2 = self.__add_region("spring_yokos_yam2", YokuLocations.locations_spring_yokos_yam2)

    def __connect_one_way_regions(self, source_name: str, destination_name: str,
                                  source_region: Region,
                                  destination_region: Region, rule=None) -> None:
        """
        Connect from the `source_region` to the `destination_region`
        """
        entrance = Entrance(source_region.player, source_name + " to " + destination_name, source_region)
        source_region.exits.append(entrance)
        entrance.connect(destination_region)
        if rule is not None:
            set_rule(entrance, rule)

    def __connect_regions(self, source_name: str, destination_name: str,
                          source_region: Region,
                          destination_region: Region, rule=None) -> None:
        """
        Connect the `source_region` and the `destination_region` (two-way)
        """
        self.__connect_one_way_regions(source_name, destination_name, source_region, destination_region, rule)
        self.__connect_one_way_regions(destination_name, source_name, destination_region, source_region, rule)

    def __connect_cave_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `cave` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "cave_abyssal_access0", self.menu, self.cave_abyssal_access0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_abyssal_access1", self.menu, self.cave_abyssal_access1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beach_bottom0", self.menu, self.cave_beach_bottom0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade0", self.menu, self.cave_beaver_blockade0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade1", self.menu, self.cave_beaver_blockade1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade2", self.menu, self.cave_beaver_blockade2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote0", self.menu, self.cave_clammy_cenote0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote1", self.menu, self.cave_clammy_cenote1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote2", self.menu, self.cave_clammy_cenote2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore0", self.menu, self.cave_east_bay_shore0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore1", self.menu, self.cave_east_bay_shore1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore2", self.menu, self.cave_east_bay_shore2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore3", self.menu, self.cave_east_bay_shore3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores3), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores3), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores3), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores3), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower0", self.menu, self.cave_temple_terror_lower0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower1", self.menu, self.cave_temple_terror_lower1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower2", self.menu, self.cave_temple_terror_lower2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower3", self.menu, self.cave_temple_terror_lower3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower4", self.menu, self.cave_temple_terror_lower4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves), _has(ItemName.Wallet,2)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves), _has(ItemName.Wallet,2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower5", self.menu, self.cave_temple_terror_lower5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower6", self.menu, self.cave_temple_terror_lower6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury0", self.menu, self.cave_temple_terror_treasury0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury1", self.menu, self.cave_temple_terror_treasury1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Greenkey), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Greenkey), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury2", self.menu, self.cave_temple_terror_treasury2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_upper0", self.menu, self.cave_temple_terror_upper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_winding_waterway0", self.menu, self.cave_winding_waterway0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

        elif options.mode == 1:
            self.__connect_regions("Menu", "cave_abyssal_access0", self.menu, self.cave_abyssal_access0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_abyssal_access1", self.menu, self.cave_abyssal_access1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beach_bottom0", self.menu, self.cave_beach_bottom0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade0", self.menu, self.cave_beaver_blockade0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade1", self.menu, self.cave_beaver_blockade1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade2", self.menu, self.cave_beaver_blockade2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote0", self.menu, self.cave_clammy_cenote0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote1", self.menu, self.cave_clammy_cenote1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote2", self.menu, self.cave_clammy_cenote2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore0", self.menu, self.cave_east_bay_shore0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore1", self.menu, self.cave_east_bay_shore1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore2", self.menu, self.cave_east_bay_shore2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore3", self.menu, self.cave_east_bay_shore3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores3)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores3))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower0", self.menu, self.cave_temple_terror_lower0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower1", self.menu, self.cave_temple_terror_lower1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower2", self.menu, self.cave_temple_terror_lower2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower3", self.menu, self.cave_temple_terror_lower3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower4", self.menu, self.cave_temple_terror_lower4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Wallet,2)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Wallet,2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower5", self.menu, self.cave_temple_terror_lower5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower6", self.menu, self.cave_temple_terror_lower6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury0", self.menu, self.cave_temple_terror_treasury0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury1", self.menu, self.cave_temple_terror_treasury1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Greenkey), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Greenkey), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury2", self.menu, self.cave_temple_terror_treasury2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_upper0", self.menu, self.cave_temple_terror_upper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_winding_waterway0", self.menu, self.cave_winding_waterway0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

        else:
            self.__connect_regions("Menu", "cave_abyssal_access0", self.menu, self.cave_abyssal_access0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_abyssal_access1", self.menu, self.cave_abyssal_access1,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beach_bottom0", self.menu, self.cave_beach_bottom0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade0", self.menu, self.cave_beaver_blockade0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade1", self.menu, self.cave_beaver_blockade1,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_beaver_blockade2", self.menu, self.cave_beaver_blockade2,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote0", self.menu, self.cave_clammy_cenote0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote1", self.menu, self.cave_clammy_cenote1,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "cave_clammy_cenote2", self.menu, self.cave_clammy_cenote2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore0", self.menu, self.cave_east_bay_shore0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore1", self.menu, self.cave_east_bay_shore1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore2", self.menu, self.cave_east_bay_shore2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_east_bay_shore3", self.menu, self.cave_east_bay_shore3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Spores3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.Spores3)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Spores3))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower0", self.menu, self.cave_temple_terror_lower0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower1", self.menu, self.cave_temple_terror_lower1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower2", self.menu, self.cave_temple_terror_lower2,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower3", self.menu, self.cave_temple_terror_lower3,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower4", self.menu, self.cave_temple_terror_lower4,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Wallet,2))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower5", self.menu, self.cave_temple_terror_lower5,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_lower6", self.menu, self.cave_temple_terror_lower6,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury0", self.menu, self.cave_temple_terror_treasury0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Bluekey))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury1", self.menu, self.cave_temple_terror_treasury1,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Greenkey))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_treasury2", self.menu, self.cave_temple_terror_treasury2,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_temple_terror_upper0", self.menu, self.cave_temple_terror_upper0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "cave_winding_waterway0", self.menu, self.cave_winding_waterway0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

    def __connect_hub_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `hub` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "hub_bowel_bumping_left0", self.menu, self.hub_bowel_bumping_left0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.NimKey), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.NimKey), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek0", self.menu, self.hub_cliffside_creek0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek1", self.menu, self.hub_cliffside_creek1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek2", self.menu, self.hub_cliffside_creek2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival0", self.menu, self.hub_festival0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper0", self.menu, self.hub_festival_upper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper1", self.menu, self.hub_festival_upper1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper2", self.menu, self.hub_festival_upper2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores1)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores1))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_hermits_home0", self.menu, self.hub_hermits_home0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express0", self.menu, self.hub_island_express0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSpeed), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSpeed), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express1", self.menu, self.hub_island_express1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express2", self.menu, self.hub_island_express2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express3", self.menu, self.hub_island_express3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lemur_lane0", self.menu, self.hub_left_lemur_lane0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo0", self.menu, self.hub_left_lofty_logo0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo1", self.menu, self.hub_left_lofty_logo1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo2", self.menu, self.hub_left_lofty_logo2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_obtainium_outland0", self.menu, self.hub_obtainium_outland0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_obtainium_outland1", self.menu, self.hub_obtainium_outland1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_soaring_stone0", self.menu, self.hub_soaring_stone0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village0", self.menu, self.hub_village0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves), _has(ItemName.TrackerPeak), _has(ItemName.TrackerScarabs), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village1", self.menu, self.hub_village1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village2", self.menu, self.hub_village2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village3", self.menu, self.hub_village3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village4", self.menu, self.hub_village4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village5", self.menu, self.hub_village5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village6", self.menu, self.hub_village6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores5), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores5), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village7", self.menu, self.hub_village7,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village8", self.menu, self.hub_village8,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff0", self.menu, self.hub_white_cliff0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff1", self.menu, self.hub_white_cliff1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff2", self.menu, self.hub_white_cliff2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_one_way_regions("hub_bowel_bumping_left0", "win", self.hub_bowel_bumping_left0, self.win, lambda state: _has(ItemName.AbilitiesPartyhorn)(state, self.player))


        elif options.mode == 1:
            self.__connect_regions("Menu", "hub_bowel_bumping_left0", self.menu, self.hub_bowel_bumping_left0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.NimKey), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.NimKey), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek0", self.menu, self.hub_cliffside_creek0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek1", self.menu, self.hub_cliffside_creek1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek2", self.menu, self.hub_cliffside_creek2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival0", self.menu, self.hub_festival0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper0", self.menu, self.hub_festival_upper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper1", self.menu, self.hub_festival_upper1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper2", self.menu, self.hub_festival_upper2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores1)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores1))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_hermits_home0", self.menu, self.hub_hermits_home0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express0", self.menu, self.hub_island_express0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSpeed), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSpeed), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express1", self.menu, self.hub_island_express1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express2", self.menu, self.hub_island_express2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express3", self.menu, self.hub_island_express3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lemur_lane0", self.menu, self.hub_left_lemur_lane0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo0", self.menu, self.hub_left_lofty_logo0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo1", self.menu, self.hub_left_lofty_logo1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo2", self.menu, self.hub_left_lofty_logo2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_obtainium_outland0", self.menu, self.hub_obtainium_outland0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_obtainium_outland1", self.menu, self.hub_obtainium_outland1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_soaring_stone0", self.menu, self.hub_soaring_stone0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village0", self.menu, self.hub_village0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village1", self.menu, self.hub_village1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village2", self.menu, self.hub_village2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village3", self.menu, self.hub_village3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village4", self.menu, self.hub_village4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village5", self.menu, self.hub_village5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village6", self.menu, self.hub_village6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores5), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores5), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village7", self.menu, self.hub_village7,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village8", self.menu, self.hub_village8,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff0", self.menu, self.hub_white_cliff0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff1", self.menu, self.hub_white_cliff1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff2", self.menu, self.hub_white_cliff2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_one_way_regions("hub_bowel_bumping_left0", "win", self.hub_bowel_bumping_left0, self.win, lambda state: _has(ItemName.AbilitiesPartyhorn)(state, self.player))

        else:
            self.__connect_regions("Menu", "hub_bowel_bumping_left0", self.menu, self.hub_bowel_bumping_left0,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.NimKey), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek0", self.menu, self.hub_cliffside_creek0,lambda state:
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek1", self.menu, self.hub_cliffside_creek1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin1), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin3), _has(ItemName.SkinsSkin4), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_cliffside_creek2", self.menu, self.hub_cliffside_creek2,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival0", self.menu, self.hub_festival0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.NimKey), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper0", self.menu, self.hub_festival_upper0,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_festival_upper1", self.menu, self.hub_festival_upper1)

            self.__connect_regions("Menu", "hub_festival_upper2", self.menu, self.hub_festival_upper2,lambda state:
                 _has(ItemName.Spores1)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_hermits_home0", self.menu, self.hub_hermits_home0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express0", self.menu, self.hub_island_express0)

            self.__connect_regions("Menu", "hub_island_express1", self.menu, self.hub_island_express1,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express2", self.menu, self.hub_island_express2,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_island_express3", self.menu, self.hub_island_express3)

            self.__connect_regions("Menu", "hub_left_lemur_lane0", self.menu, self.hub_left_lemur_lane0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo0", self.menu, self.hub_left_lofty_logo0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_left_lofty_logo1", self.menu, self.hub_left_lofty_logo1)

            self.__connect_regions("Menu", "hub_left_lofty_logo2", self.menu, self.hub_left_lofty_logo2)

            self.__connect_regions("Menu", "hub_obtainium_outland0", self.menu, self.hub_obtainium_outland0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Idol3), _has(ItemName.Idol4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_obtainium_outland1", self.menu, self.hub_obtainium_outland1,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_soaring_stone0", self.menu, self.hub_soaring_stone0)

            self.__connect_regions("Menu", "hub_village0", self.menu, self.hub_village0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village1", self.menu, self.hub_village1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin2), _has(ItemName.SkinsSkin5), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village2", self.menu, self.hub_village2,lambda state:
                    _and_(_has(ItemName.Idol1), _has(ItemName.Idol2), _has(ItemName.Idol3), _has(ItemName.Idol4))(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village3", self.menu, self.hub_village3,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village4", self.menu, self.hub_village4,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village5", self.menu, self.hub_village5,lambda state:
                _or_(
                 _has(ItemName.AbilitiesMailbag),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village6", self.menu, self.hub_village6,lambda state:
                    _and_(_has(ItemName.SootlingLeash), _has(ItemName.Spores5))(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village7", self.menu, self.hub_village7,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_village8", self.menu, self.hub_village8)

            self.__connect_regions("Menu", "hub_white_cliff0", self.menu, self.hub_white_cliff0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff1", self.menu, self.hub_white_cliff1,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "hub_white_cliff2", self.menu, self.hub_white_cliff2)
            
            self.__connect_one_way_regions("hub_bowel_bumping_left0", "win", self.hub_bowel_bumping_left0, self.win, lambda state: _has(ItemName.AbilitiesPartyhorn)(state, self.player))


    def __connect_intro_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `intro` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "intro_landing1", self.menu, self.intro_landing1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing2", self.menu, self.intro_landing2,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing3", self.menu, self.intro_landing3,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern0", self.menu, self.intro_landing_creepy_cavern0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern1", self.menu, self.intro_landing_creepy_cavern1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_left0", self.menu, self.intro_landing_left0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right0", self.menu, self.intro_landing_right0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right1", self.menu, self.intro_landing_right1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right2", self.menu, self.intro_landing_right2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right3", self.menu, self.intro_landing_right3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper0", self.menu, self.intro_landing_upper0)

            self.__connect_regions("Menu", "intro_landing_upper1", self.menu, self.intro_landing_upper1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper2", self.menu, self.intro_landing_upper2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                 _has(ItemName.AbilitiesPartyhorn)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper3", self.menu, self.intro_landing_upper3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper4", self.menu, self.intro_landing_upper4,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper5", self.menu, self.intro_landing_upper5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass0", self.menu, self.intro_muddled_morass0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass1", self.menu, self.intro_muddled_morass1,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_secret0", self.menu, self.intro_secret0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

        elif options.mode == 1:
            self.__connect_regions("Menu", "intro_landing1", self.menu, self.intro_landing1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                 _has(ItemName.AbilitiesPartyhorn)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing2", self.menu, self.intro_landing2,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing3", self.menu, self.intro_landing3,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern0", self.menu, self.intro_landing_creepy_cavern0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern1", self.menu, self.intro_landing_creepy_cavern1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_left0", self.menu, self.intro_landing_left0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right0", self.menu, self.intro_landing_right0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right1", self.menu, self.intro_landing_right1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right2", self.menu, self.intro_landing_right2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right3", self.menu, self.intro_landing_right3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper0", self.menu, self.intro_landing_upper0)

            self.__connect_regions("Menu", "intro_landing_upper1", self.menu, self.intro_landing_upper1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper2", self.menu, self.intro_landing_upper2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                 _has(ItemName.AbilitiesPartyhorn)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper3", self.menu, self.intro_landing_upper3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                 _has(ItemName.AbilitiesPartyhorn)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper4", self.menu, self.intro_landing_upper4,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper5", self.menu, self.intro_landing_upper5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass0", self.menu, self.intro_muddled_morass0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass1", self.menu, self.intro_muddled_morass1,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_secret0", self.menu, self.intro_secret0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

        else:
            self.__connect_regions("Menu", "intro_landing1", self.menu, self.intro_landing1)

            self.__connect_regions("Menu", "intro_landing2", self.menu, self.intro_landing2,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing3", self.menu, self.intro_landing3,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern0", self.menu, self.intro_landing_creepy_cavern0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_creepy_cavern1", self.menu, self.intro_landing_creepy_cavern1)

            self.__connect_regions("Menu", "intro_landing_left0", self.menu, self.intro_landing_left0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right0", self.menu, self.intro_landing_right0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right1", self.menu, self.intro_landing_right1,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_right2", self.menu, self.intro_landing_right2)

            self.__connect_regions("Menu", "intro_landing_right3", self.menu, self.intro_landing_right3)

            self.__connect_regions("Menu", "intro_landing_upper0", self.menu, self.intro_landing_upper0)

            self.__connect_regions("Menu", "intro_landing_upper1", self.menu, self.intro_landing_upper1)

            self.__connect_regions("Menu", "intro_landing_upper2", self.menu, self.intro_landing_upper2)

            self.__connect_regions("Menu", "intro_landing_upper3", self.menu, self.intro_landing_upper3)

            self.__connect_regions("Menu", "intro_landing_upper4", self.menu, self.intro_landing_upper4,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_landing_upper5", self.menu, self.intro_landing_upper5,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass0", self.menu, self.intro_muddled_morass0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_muddled_morass1", self.menu, self.intro_muddled_morass1,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "intro_secret0", self.menu, self.intro_secret0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

    def __connect_jungle_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `jungle` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "jungle_canyon_caper0", self.menu, self.jungle_canyon_caper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_canyon_caper1", self.menu, self.jungle_canyon_caper1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_crammed_canopy0", self.menu, self.jungle_crammed_canopy0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_crammed_canopy1", self.menu, self.jungle_crammed_canopy1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow0", self.menu, self.jungle_misty_meadow0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow1", self.menu, self.jungle_misty_meadow1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow2", self.menu, self.jungle_misty_meadow2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness0", self.menu, self.jungle_mollusc_madness0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness1", self.menu, self.jungle_mollusc_madness1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness2", self.menu, self.jungle_mollusc_madness2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness3", self.menu, self.jungle_mollusc_madness3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_roots0", self.menu, self.jungle_roots0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SkinsSkin3), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SkinsSkin3), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_roots1", self.menu, self.jungle_roots1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle0", self.menu, self.jungle_slug_struggle0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle1", self.menu, self.jungle_slug_struggle1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle2", self.menu, self.jungle_slug_struggle2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle3", self.menu, self.jungle_slug_struggle3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle4", self.menu, self.jungle_slug_struggle4,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores2)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_spikey_stockade0", self.menu, self.jungle_spikey_stockade0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4), _has(ItemName.TraitorSpirit,4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4), _has(ItemName.TraitorSpirit,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower0", self.menu, self.jungle_tall_tall_tower0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower1", self.menu, self.jungle_tall_tall_tower1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower2", self.menu, self.jungle_tall_tall_tower2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy0", self.menu, self.jungle_willy0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy1", self.menu, self.jungle_willy1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy2", self.menu, self.jungle_willy2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

        elif options.mode == 1:
            self.__connect_regions("Menu", "jungle_canyon_caper0", self.menu, self.jungle_canyon_caper0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_canyon_caper1", self.menu, self.jungle_canyon_caper1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_crammed_canopy0", self.menu, self.jungle_crammed_canopy0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_crammed_canopy1", self.menu, self.jungle_crammed_canopy1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow0", self.menu, self.jungle_misty_meadow0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow1", self.menu, self.jungle_misty_meadow1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow2", self.menu, self.jungle_misty_meadow2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness0", self.menu, self.jungle_mollusc_madness0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness1", self.menu, self.jungle_mollusc_madness1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness2", self.menu, self.jungle_mollusc_madness2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness3", self.menu, self.jungle_mollusc_madness3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_roots0", self.menu, self.jungle_roots0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SkinsSkin3), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SkinsSkin3), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_roots1", self.menu, self.jungle_roots1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin3))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle0", self.menu, self.jungle_slug_struggle0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle1", self.menu, self.jungle_slug_struggle1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle2", self.menu, self.jungle_slug_struggle2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle3", self.menu, self.jungle_slug_struggle3,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle4", self.menu, self.jungle_slug_struggle4,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Spores2)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Spores2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_spikey_stockade0", self.menu, self.jungle_spikey_stockade0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4), _has(ItemName.TraitorSpirit,4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SkinsSkin4), _has(ItemName.TraitorSpirit,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower0", self.menu, self.jungle_tall_tall_tower0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower1", self.menu, self.jungle_tall_tall_tower1,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower2", self.menu, self.jungle_tall_tall_tower2,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy0", self.menu, self.jungle_willy0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy1", self.menu, self.jungle_willy1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy2", self.menu, self.jungle_willy2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

        else:
            self.__connect_regions("Menu", "jungle_canyon_caper0", self.menu, self.jungle_canyon_caper0)

            self.__connect_regions("Menu", "jungle_canyon_caper1", self.menu, self.jungle_canyon_caper1)

            self.__connect_regions("Menu", "jungle_crammed_canopy0", self.menu, self.jungle_crammed_canopy0,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesPartyhorn)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_crammed_canopy1", self.menu, self.jungle_crammed_canopy1,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow0", self.menu, self.jungle_misty_meadow0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow1", self.menu, self.jungle_misty_meadow1,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_misty_meadow2", self.menu, self.jungle_misty_meadow2)

            self.__connect_regions("Menu", "jungle_mollusc_madness0", self.menu, self.jungle_mollusc_madness0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness1", self.menu, self.jungle_mollusc_madness1,lambda state:
                _or_(
                 _has(ItemName.AbilitiesPartyhorn),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness2", self.menu, self.jungle_mollusc_madness2,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_mollusc_madness3", self.menu, self.jungle_mollusc_madness3)

            self.__connect_regions("Menu", "jungle_roots0", self.menu, self.jungle_roots0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SkinsSkin3), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_roots1", self.menu, self.jungle_roots1,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin3))(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle0", self.menu, self.jungle_slug_struggle0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle1", self.menu, self.jungle_slug_struggle1,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle2", self.menu, self.jungle_slug_struggle2,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_slug_struggle3", self.menu, self.jungle_slug_struggle3)

            self.__connect_regions("Menu", "jungle_slug_struggle4", self.menu, self.jungle_slug_struggle4,lambda state:
                 _has(ItemName.Spores2)(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_spikey_stockade0", self.menu, self.jungle_spikey_stockade0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SkinsSkin4), _has(ItemName.TraitorSpirit,4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.TraitorSpirit,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower0", self.menu, self.jungle_tall_tall_tower0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_tall_tall_tower1", self.menu, self.jungle_tall_tall_tower1)

            self.__connect_regions("Menu", "jungle_tall_tall_tower2", self.menu, self.jungle_tall_tall_tower2)

            self.__connect_regions("Menu", "jungle_willy0", self.menu, self.jungle_willy0,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy1", self.menu, self.jungle_willy1,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "jungle_willy2", self.menu, self.jungle_willy2,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

    def __connect_peak_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `peak` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "peak_aerial_ascent0", self.menu, self.peak_aerial_ascent0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent1", self.menu, self.peak_aerial_ascent1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent2", self.menu, self.peak_aerial_ascent2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent3", self.menu, self.peak_aerial_ascent3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent4", self.menu, self.peak_aerial_ascent4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent5", self.menu, self.peak_aerial_ascent5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent6", self.menu, self.peak_aerial_ascent6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent7", self.menu, self.peak_aerial_ascent7,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base0", self.menu, self.peak_beanstalk_base0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base1", self.menu, self.peak_beanstalk_base1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base2", self.menu, self.peak_beanstalk_base2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base3", self.menu, self.peak_beanstalk_base3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base4", self.menu, self.peak_beanstalk_base4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base5", self.menu, self.peak_beanstalk_base5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crooked_cliff0", self.menu, self.peak_crooked_cliff0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater0", self.menu, self.peak_crystal_crater0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater1", self.menu, self.peak_crystal_crater1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater2", self.menu, self.peak_crystal_crater2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater3", self.menu, self.peak_crystal_crater3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak), _has(ItemName.Wallet,2)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak), _has(ItemName.Wallet,2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat0", self.menu, self.peak_filthy_flat0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat1", self.menu, self.peak_filthy_flat1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat2", self.menu, self.peak_filthy_flat2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat3", self.menu, self.peak_filthy_flat3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat4", self.menu, self.peak_filthy_flat4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat5", self.menu, self.peak_filthy_flat5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest0", self.menu, self.peak_frostpine_forest0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest1", self.menu, self.peak_frostpine_forest1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest2", self.menu, self.peak_frostpine_forest2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief0", self.menu, self.peak_guano_grief0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores4), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores4), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief1", self.menu, self.peak_guano_grief1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief2", self.menu, self.peak_guano_grief2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief3", self.menu, self.peak_guano_grief3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief4", self.menu, self.peak_guano_grief4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief5", self.menu, self.peak_guano_grief5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief6", self.menu, self.peak_guano_grief6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_ice_cold_idol0", self.menu, self.peak_ice_cold_idol0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_ice_cold_idol1", self.menu, self.peak_ice_cold_idol1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_obtainium_oracle0", self.menu, self.peak_obtainium_oracle0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight0", self.menu, self.peak_spider_fight0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerPeak))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight1", self.menu, self.peak_spider_fight1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

        elif options.mode == 1:
            self.__connect_regions("Menu", "peak_aerial_ascent0", self.menu, self.peak_aerial_ascent0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent1", self.menu, self.peak_aerial_ascent1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.Nugget,4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent2", self.menu, self.peak_aerial_ascent2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent3", self.menu, self.peak_aerial_ascent3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent4", self.menu, self.peak_aerial_ascent4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent5", self.menu, self.peak_aerial_ascent5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent6", self.menu, self.peak_aerial_ascent6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent7", self.menu, self.peak_aerial_ascent7,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base0", self.menu, self.peak_beanstalk_base0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base1", self.menu, self.peak_beanstalk_base1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base2", self.menu, self.peak_beanstalk_base2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base3", self.menu, self.peak_beanstalk_base3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base4", self.menu, self.peak_beanstalk_base4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base5", self.menu, self.peak_beanstalk_base5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crooked_cliff0", self.menu, self.peak_crooked_cliff0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater0", self.menu, self.peak_crystal_crater0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater1", self.menu, self.peak_crystal_crater1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol1), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Idol4), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater2", self.menu, self.peak_crystal_crater2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater3", self.menu, self.peak_crystal_crater3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.Wallet,2)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.Wallet,2))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat0", self.menu, self.peak_filthy_flat0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat1", self.menu, self.peak_filthy_flat1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat2", self.menu, self.peak_filthy_flat2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat3", self.menu, self.peak_filthy_flat3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat4", self.menu, self.peak_filthy_flat4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat5", self.menu, self.peak_filthy_flat5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest0", self.menu, self.peak_frostpine_forest0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest1", self.menu, self.peak_frostpine_forest1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest2", self.menu, self.peak_frostpine_forest2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief0", self.menu, self.peak_guano_grief0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores4), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Spores4), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief1", self.menu, self.peak_guano_grief1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief2", self.menu, self.peak_guano_grief2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief3", self.menu, self.peak_guano_grief3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief4", self.menu, self.peak_guano_grief4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief5", self.menu, self.peak_guano_grief5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief6", self.menu, self.peak_guano_grief6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_ice_cold_idol0", self.menu, self.peak_ice_cold_idol0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_ice_cold_idol1", self.menu, self.peak_ice_cold_idol1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_obtainium_oracle0", self.menu, self.peak_obtainium_oracle0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight0", self.menu, self.peak_spider_fight0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight1", self.menu, self.peak_spider_fight1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

        else:
            self.__connect_regions("Menu", "peak_aerial_ascent0", self.menu, self.peak_aerial_ascent0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent1", self.menu, self.peak_aerial_ascent1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1), _has(ItemName.Nugget,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2), _has(ItemName.Nugget,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3), _has(ItemName.Nugget,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4), _has(ItemName.Nugget,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent2", self.menu, self.peak_aerial_ascent2,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent3", self.menu, self.peak_aerial_ascent3,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent4", self.menu, self.peak_aerial_ascent4)

            self.__connect_regions("Menu", "peak_aerial_ascent5", self.menu, self.peak_aerial_ascent5,lambda state:
                _or_(
                 _has(ItemName.AbilitiesPartyhorn),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent6", self.menu, self.peak_aerial_ascent6,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_aerial_ascent7", self.menu, self.peak_aerial_ascent7,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base0", self.menu, self.peak_beanstalk_base0)

            self.__connect_regions("Menu", "peak_beanstalk_base1", self.menu, self.peak_beanstalk_base1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base2", self.menu, self.peak_beanstalk_base2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_beanstalk_base3", self.menu, self.peak_beanstalk_base3)

            self.__connect_regions("Menu", "peak_beanstalk_base4", self.menu, self.peak_beanstalk_base4)

            self.__connect_regions("Menu", "peak_beanstalk_base5", self.menu, self.peak_beanstalk_base5,lambda state:
                _or_(
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.AbilitiesSpeed)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crooked_cliff0", self.menu, self.peak_crooked_cliff0,lambda state:
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater0", self.menu, self.peak_crystal_crater0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater1", self.menu, self.peak_crystal_crater1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol1)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol2)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol3)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Idol4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_crystal_crater2", self.menu, self.peak_crystal_crater2)

            self.__connect_regions("Menu", "peak_crystal_crater3", self.menu, self.peak_crystal_crater3,lambda state:
                    _and_(_has(ItemName.SootlingLeash), _has(ItemName.Wallet,2))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat0", self.menu, self.peak_filthy_flat0,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat1", self.menu, self.peak_filthy_flat1,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat2", self.menu, self.peak_filthy_flat2,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat3", self.menu, self.peak_filthy_flat3,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat4", self.menu, self.peak_filthy_flat4,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_filthy_flat5", self.menu, self.peak_filthy_flat5,lambda state:
                 _has(ItemName.AbilitiesPartyhorn)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest0", self.menu, self.peak_frostpine_forest0,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest1", self.menu, self.peak_frostpine_forest1,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_frostpine_forest2", self.menu, self.peak_frostpine_forest2,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief0", self.menu, self.peak_guano_grief0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Spores4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.Spores4)),
                    _and_(_has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash), _has(ItemName.Spores4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief1", self.menu, self.peak_guano_grief1,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief2", self.menu, self.peak_guano_grief2,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief3", self.menu, self.peak_guano_grief3,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief4", self.menu, self.peak_guano_grief4)

            self.__connect_regions("Menu", "peak_guano_grief5", self.menu, self.peak_guano_grief5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "peak_guano_grief6", self.menu, self.peak_guano_grief6)

            self.__connect_regions("Menu", "peak_ice_cold_idol0", self.menu, self.peak_ice_cold_idol0,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_ice_cold_idol1", self.menu, self.peak_ice_cold_idol1,lambda state:
                    _and_(_has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_obtainium_oracle0", self.menu, self.peak_obtainium_oracle0,lambda state:
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight0", self.menu, self.peak_spider_fight0,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "peak_spider_fight1", self.menu, self.peak_spider_fight1,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.BucketEmpty), _has(ItemName.Guano), _has(ItemName.SeedPod), _has(ItemName.SootlingLeash))(state, self.player)
            )

    def __connect_spring_regions(self, options: YokuOptions) -> None:
        """
        Connect entrances of the different `spring` regions (we cheat and just connect everything to "Menu")
        """
        if options.mode == 0:
            self.__connect_regions("Menu", "spring_bubbly_basin0", self.menu, self.spring_bubbly_basin0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin1", self.menu, self.spring_bubbly_basin1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin2", self.menu, self.spring_bubbly_basin2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin3", self.menu, self.spring_bubbly_basin3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin4", self.menu, self.spring_bubbly_basin4,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Tadpole,8), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Tadpole,8), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs0", self.menu, self.spring_cloudburst_cliffs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs1", self.menu, self.spring_cloudburst_cliffs1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs2", self.menu, self.spring_cloudburst_cliffs2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs3", self.menu, self.spring_cloudburst_cliffs3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs4", self.menu, self.spring_cloudburst_cliffs4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs5", self.menu, self.spring_cloudburst_cliffs5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto0", self.menu, self.spring_gangway_grotto0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto1", self.menu, self.spring_gangway_grotto1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto2", self.menu, self.spring_gangway_grotto2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto3", self.menu, self.spring_gangway_grotto3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto4", self.menu, self.spring_gangway_grotto4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto5", self.menu, self.spring_gangway_grotto5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings), _has(ItemName.Wallet,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto6", self.menu, self.spring_gangway_grotto6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring0", self.menu, self.spring_hidden_hotspring0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring1", self.menu, self.spring_hidden_hotspring1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring2", self.menu, self.spring_hidden_hotspring2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring3", self.menu, self.spring_hidden_hotspring3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerCaves))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring4", self.menu, self.spring_hidden_hotspring4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_jailhouse_japes0", self.menu, self.spring_jailhouse_japes0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty0", self.menu, self.spring_shoddy_shanty0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty1", self.menu, self.spring_shoddy_shanty1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty2", self.menu, self.spring_shoddy_shanty2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty3", self.menu, self.spring_shoddy_shanty3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs0", self.menu, self.spring_sleek_slabs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs1", self.menu, self.spring_sleek_slabs1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs2", self.menu, self.spring_sleek_slabs2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs3", self.menu, self.spring_sleek_slabs3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs4", self.menu, self.spring_sleek_slabs4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs5", self.menu, self.spring_sleek_slabs5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.TreasureMap))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad0", self.menu, self.spring_tiny_broad0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad1", self.menu, self.spring_tiny_broad1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad2", self.menu, self.spring_tiny_broad2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad3", self.menu, self.spring_tiny_broad3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad4", self.menu, self.spring_tiny_broad4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad5", self.menu, self.spring_tiny_broad5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad6", self.menu, self.spring_tiny_broad6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tortoise_tunnel0", self.menu, self.spring_tortoise_tunnel0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam0", self.menu, self.spring_yokos_yam0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam1", self.menu, self.spring_yokos_yam1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox), _has(ItemName.TrackerSprings))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam2", self.menu, self.spring_yokos_yam2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey), _has(ItemName.TrackerScarabs))
                )(state, self.player)
            )

        elif options.mode == 1:
            self.__connect_regions("Menu", "spring_bubbly_basin0", self.menu, self.spring_bubbly_basin0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin1", self.menu, self.spring_bubbly_basin1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin2", self.menu, self.spring_bubbly_basin2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin3", self.menu, self.spring_bubbly_basin3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin4", self.menu, self.spring_bubbly_basin4,lambda state:
                _or_(
                    _and_(_has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Tadpole,8)),
                    _and_(_has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Tadpole,8))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs0", self.menu, self.spring_cloudburst_cliffs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs1", self.menu, self.spring_cloudburst_cliffs1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs2", self.menu, self.spring_cloudburst_cliffs2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs3", self.menu, self.spring_cloudburst_cliffs3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs4", self.menu, self.spring_cloudburst_cliffs4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs5", self.menu, self.spring_cloudburst_cliffs5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto0", self.menu, self.spring_gangway_grotto0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto1", self.menu, self.spring_gangway_grotto1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto2", self.menu, self.spring_gangway_grotto2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto3", self.menu, self.spring_gangway_grotto3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto4", self.menu, self.spring_gangway_grotto4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto5", self.menu, self.spring_gangway_grotto5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.Wallet,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto6", self.menu, self.spring_gangway_grotto6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring0", self.menu, self.spring_hidden_hotspring0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring1", self.menu, self.spring_hidden_hotspring1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring2", self.menu, self.spring_hidden_hotspring2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring3", self.menu, self.spring_hidden_hotspring3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring4", self.menu, self.spring_hidden_hotspring4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_jailhouse_japes0", self.menu, self.spring_jailhouse_japes0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty0", self.menu, self.spring_shoddy_shanty0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty1", self.menu, self.spring_shoddy_shanty1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty2", self.menu, self.spring_shoddy_shanty2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty3", self.menu, self.spring_shoddy_shanty3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs0", self.menu, self.spring_sleek_slabs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs1", self.menu, self.spring_sleek_slabs1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs2", self.menu, self.spring_sleek_slabs2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs3", self.menu, self.spring_sleek_slabs3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs4", self.menu, self.spring_sleek_slabs4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs5", self.menu, self.spring_sleek_slabs5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad0", self.menu, self.spring_tiny_broad0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad1", self.menu, self.spring_tiny_broad1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad2", self.menu, self.spring_tiny_broad2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad3", self.menu, self.spring_tiny_broad3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad4", self.menu, self.spring_tiny_broad4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad5", self.menu, self.spring_tiny_broad5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad6", self.menu, self.spring_tiny_broad6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tortoise_tunnel0", self.menu, self.spring_tortoise_tunnel0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam0", self.menu, self.spring_yokos_yam0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam1", self.menu, self.spring_yokos_yam1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey), _has(ItemName.Toolbox))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam2", self.menu, self.spring_yokos_yam2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom2), _has(ItemName.PostalBadge), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Mushroom3), _has(ItemName.PostalBadge), _has(ItemName.SpringKey))
                )(state, self.player)
            )

        else:
            self.__connect_regions("Menu", "spring_bubbly_basin0", self.menu, self.spring_bubbly_basin0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin1", self.menu, self.spring_bubbly_basin1,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin2", self.menu, self.spring_bubbly_basin2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin3", self.menu, self.spring_bubbly_basin3,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_bubbly_basin4", self.menu, self.spring_bubbly_basin4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Tadpole,8)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Tadpole,8)),
                    _and_(_has(ItemName.SootlingLeash), _has(ItemName.Tadpole,8))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs0", self.menu, self.spring_cloudburst_cliffs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs1", self.menu, self.spring_cloudburst_cliffs1)

            self.__connect_regions("Menu", "spring_cloudburst_cliffs2", self.menu, self.spring_cloudburst_cliffs2,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs3", self.menu, self.spring_cloudburst_cliffs3,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs4", self.menu, self.spring_cloudburst_cliffs4,lambda state:
                 _has(ItemName.AbilitiesMailbag)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_cloudburst_cliffs5", self.menu, self.spring_cloudburst_cliffs5,lambda state:
                _or_(
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto0", self.menu, self.spring_gangway_grotto0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto1", self.menu, self.spring_gangway_grotto1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto2", self.menu, self.spring_gangway_grotto2,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto3", self.menu, self.spring_gangway_grotto3,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto4", self.menu, self.spring_gangway_grotto4,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto5", self.menu, self.spring_gangway_grotto5,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.Wallet,4)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.Wallet,4))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_gangway_grotto6", self.menu, self.spring_gangway_grotto6,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring0", self.menu, self.spring_hidden_hotspring0,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring1", self.menu, self.spring_hidden_hotspring1,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring2", self.menu, self.spring_hidden_hotspring2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                 _has(ItemName.AbilitiesSlugVacuum)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring3", self.menu, self.spring_hidden_hotspring3,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SootlingLeash))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_hidden_hotspring4", self.menu, self.spring_hidden_hotspring4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_jailhouse_japes0", self.menu, self.spring_jailhouse_japes0,lambda state:
                 _has(ItemName.AbilitiesDive)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty0", self.menu, self.spring_shoddy_shanty0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty1", self.menu, self.spring_shoddy_shanty1,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty2", self.menu, self.spring_shoddy_shanty2,lambda state:
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_shoddy_shanty3", self.menu, self.spring_shoddy_shanty3,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs0", self.menu, self.spring_sleek_slabs0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs1", self.menu, self.spring_sleek_slabs1,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum)),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs2", self.menu, self.spring_sleek_slabs2,lambda state:
                _or_(
                 _has(ItemName.AbilitiesDive),
                 _has(ItemName.AbilitiesSlugVacuum),
                 _has(ItemName.SootlingLeash)
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs3", self.menu, self.spring_sleek_slabs3,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs4", self.menu, self.spring_sleek_slabs4,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_sleek_slabs5", self.menu, self.spring_sleek_slabs5,lambda state:
                 _has(ItemName.AbilitiesSlugVacuum)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad0", self.menu, self.spring_tiny_broad0,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesMailbag), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesMailbag), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad1", self.menu, self.spring_tiny_broad1,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad2", self.menu, self.spring_tiny_broad2,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.AbilitiesPartyhorn), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad3", self.menu, self.spring_tiny_broad3,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad4", self.menu, self.spring_tiny_broad4,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash), _has(ItemName.SpringKey)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad5", self.menu, self.spring_tiny_broad5,lambda state:
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tiny_broad6", self.menu, self.spring_tiny_broad6,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_tortoise_tunnel0", self.menu, self.spring_tortoise_tunnel0,lambda state:
                 _has(ItemName.SootlingLeash)(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam0", self.menu, self.spring_yokos_yam0,lambda state:
                    _and_(_has(ItemName.AbilitiesDive, 2), _has(ItemName.AbilitiesSlugVacuum,2), _has(ItemName.PowerupsSkvader1,2), _has(ItemName.SpringKey))(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam1", self.menu, self.spring_yokos_yam1,lambda state:
                _or_(
                    _and_(_has(ItemName.AbilitiesDive), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesPartyhorn), _has(ItemName.SootlingLeash)),
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SootlingLeash))
                )(state, self.player)
            )

            self.__connect_regions("Menu", "spring_yokos_yam2", self.menu, self.spring_yokos_yam2,lambda state:
                    _and_(_has(ItemName.AbilitiesSlugVacuum), _has(ItemName.SpringKey))(state, self.player)
            )

    def connect_regions(self, options: YokuOptions) -> None:
        """
        Connect every region (entrances and exits)
        """
        self.__connect_cave_regions(options)
        self.__connect_hub_regions(options)
        self.__connect_intro_regions(options)
        self.__connect_jungle_regions(options)
        self.__connect_peak_regions(options)
        self.__connect_spring_regions(options)

    def __add_event_location(self, region: Region, name: str, event_name: str) -> None:
        """
        Add an event to the `region` with the name `name` and the item
        `event_name`
        """
        location: YokuLocation = YokuLocation(
            self.player, name, None, region
        )
        region.locations.append(location)
        location.place_locked_item(YokuItem(event_name,
                                               ItemClassification.progression,
                                               None,
                                               self.player))

    def add_event_locations(self) -> None:
        """
        Add every event (locations and items) to the `world`
        """
        self.__add_event_location(self.win, "Objective complete",
                                  "Victory")

    def __add_cave_regions_to_world(self) -> None:
        """
        Add every `cave` region to the `world`
        """
        self.multiworld.regions.append(self.cave_abyssal_access0)
        self.multiworld.regions.append(self.cave_abyssal_access1)
        self.multiworld.regions.append(self.cave_beach_bottom0)
        self.multiworld.regions.append(self.cave_beaver_blockade0)
        self.multiworld.regions.append(self.cave_beaver_blockade1)
        self.multiworld.regions.append(self.cave_beaver_blockade2)
        self.multiworld.regions.append(self.cave_clammy_cenote0)
        self.multiworld.regions.append(self.cave_clammy_cenote1)
        self.multiworld.regions.append(self.cave_clammy_cenote2)
        self.multiworld.regions.append(self.cave_east_bay_shore0)
        self.multiworld.regions.append(self.cave_east_bay_shore1)
        self.multiworld.regions.append(self.cave_east_bay_shore2)
        self.multiworld.regions.append(self.cave_east_bay_shore3)
        self.multiworld.regions.append(self.cave_temple_terror_lower0)
        self.multiworld.regions.append(self.cave_temple_terror_lower1)
        self.multiworld.regions.append(self.cave_temple_terror_lower2)
        self.multiworld.regions.append(self.cave_temple_terror_lower3)
        self.multiworld.regions.append(self.cave_temple_terror_lower4)
        self.multiworld.regions.append(self.cave_temple_terror_lower5)
        self.multiworld.regions.append(self.cave_temple_terror_lower6)
        self.multiworld.regions.append(self.cave_temple_terror_treasury0)
        self.multiworld.regions.append(self.cave_temple_terror_treasury1)
        self.multiworld.regions.append(self.cave_temple_terror_treasury2)
        self.multiworld.regions.append(self.cave_temple_terror_upper0)
        self.multiworld.regions.append(self.cave_winding_waterway0)

    def __add_hub_regions_to_world(self) -> None:
        """
        Add every `hub` region around to the `world`
        """
        self.multiworld.regions.append(self.hub_bowel_bumping_left0)
        self.multiworld.regions.append(self.hub_cliffside_creek0)
        self.multiworld.regions.append(self.hub_cliffside_creek1)
        self.multiworld.regions.append(self.hub_cliffside_creek2)
        self.multiworld.regions.append(self.hub_festival0)
        self.multiworld.regions.append(self.hub_festival_upper0)
        self.multiworld.regions.append(self.hub_festival_upper1)
        self.multiworld.regions.append(self.hub_festival_upper2)
        self.multiworld.regions.append(self.hub_hermits_home0)
        self.multiworld.regions.append(self.hub_island_express0)
        self.multiworld.regions.append(self.hub_island_express1)
        self.multiworld.regions.append(self.hub_island_express2)
        self.multiworld.regions.append(self.hub_island_express3)
        self.multiworld.regions.append(self.hub_left_lemur_lane0)
        self.multiworld.regions.append(self.hub_left_lofty_logo0)
        self.multiworld.regions.append(self.hub_left_lofty_logo1)
        self.multiworld.regions.append(self.hub_left_lofty_logo2)
        self.multiworld.regions.append(self.hub_obtainium_outland0)
        self.multiworld.regions.append(self.hub_obtainium_outland1)
        self.multiworld.regions.append(self.hub_soaring_stone0)
        self.multiworld.regions.append(self.hub_village0)
        self.multiworld.regions.append(self.hub_village1)
        self.multiworld.regions.append(self.hub_village2)
        self.multiworld.regions.append(self.hub_village3)
        self.multiworld.regions.append(self.hub_village4)
        self.multiworld.regions.append(self.hub_village5)
        self.multiworld.regions.append(self.hub_village6)
        self.multiworld.regions.append(self.hub_village7)
        self.multiworld.regions.append(self.hub_village8)
        self.multiworld.regions.append(self.hub_white_cliff0)
        self.multiworld.regions.append(self.hub_white_cliff1)
        self.multiworld.regions.append(self.hub_white_cliff2)
        self.multiworld.regions.append(self.win)

    def __add_intro_regions_to_world(self) -> None:
        """
        Add every `intro` region to the `world`
        """
        self.multiworld.regions.append(self.menu)
        self.multiworld.regions.append(self.intro_landing1)
        self.multiworld.regions.append(self.intro_landing2)
        self.multiworld.regions.append(self.intro_landing3)
        self.multiworld.regions.append(self.intro_landing_creepy_cavern0)
        self.multiworld.regions.append(self.intro_landing_creepy_cavern1)
        self.multiworld.regions.append(self.intro_landing_left0)
        self.multiworld.regions.append(self.intro_landing_right0)
        self.multiworld.regions.append(self.intro_landing_right1)
        self.multiworld.regions.append(self.intro_landing_right2)
        self.multiworld.regions.append(self.intro_landing_right3)
        self.multiworld.regions.append(self.intro_landing_upper0)
        self.multiworld.regions.append(self.intro_landing_upper1)
        self.multiworld.regions.append(self.intro_landing_upper2)
        self.multiworld.regions.append(self.intro_landing_upper3)
        self.multiworld.regions.append(self.intro_landing_upper4)
        self.multiworld.regions.append(self.intro_landing_upper5)
        self.multiworld.regions.append(self.intro_muddled_morass0)
        self.multiworld.regions.append(self.intro_muddled_morass1)
        self.multiworld.regions.append(self.intro_secret0)

    def __add_jungle_regions_to_world(self) -> None:
        """
        Add every `jungle` region to the `world`
        """
        self.multiworld.regions.append(self.jungle_canyon_caper0)
        self.multiworld.regions.append(self.jungle_canyon_caper1)
        self.multiworld.regions.append(self.jungle_crammed_canopy0)
        self.multiworld.regions.append(self.jungle_crammed_canopy1)
        self.multiworld.regions.append(self.jungle_misty_meadow0)
        self.multiworld.regions.append(self.jungle_misty_meadow1)
        self.multiworld.regions.append(self.jungle_misty_meadow2)
        self.multiworld.regions.append(self.jungle_mollusc_madness0)
        self.multiworld.regions.append(self.jungle_mollusc_madness1)
        self.multiworld.regions.append(self.jungle_mollusc_madness2)
        self.multiworld.regions.append(self.jungle_mollusc_madness3)
        self.multiworld.regions.append(self.jungle_roots0)
        self.multiworld.regions.append(self.jungle_roots1)
        self.multiworld.regions.append(self.jungle_slug_struggle0)
        self.multiworld.regions.append(self.jungle_slug_struggle1)
        self.multiworld.regions.append(self.jungle_slug_struggle2)
        self.multiworld.regions.append(self.jungle_slug_struggle3)
        self.multiworld.regions.append(self.jungle_slug_struggle4)
        self.multiworld.regions.append(self.jungle_spikey_stockade0)
        self.multiworld.regions.append(self.jungle_tall_tall_tower0)
        self.multiworld.regions.append(self.jungle_tall_tall_tower1)
        self.multiworld.regions.append(self.jungle_tall_tall_tower2)
        self.multiworld.regions.append(self.jungle_willy0)
        self.multiworld.regions.append(self.jungle_willy1)
        self.multiworld.regions.append(self.jungle_willy2)

    def __add_peak_regions_to_world(self) -> None:
        """
        Add every `peak` region to the `world`
        """
        self.multiworld.regions.append(self.peak_aerial_ascent0)
        self.multiworld.regions.append(self.peak_aerial_ascent1)
        self.multiworld.regions.append(self.peak_aerial_ascent2)
        self.multiworld.regions.append(self.peak_aerial_ascent3)
        self.multiworld.regions.append(self.peak_aerial_ascent4)
        self.multiworld.regions.append(self.peak_aerial_ascent5)
        self.multiworld.regions.append(self.peak_aerial_ascent6)
        self.multiworld.regions.append(self.peak_aerial_ascent7)
        self.multiworld.regions.append(self.peak_beanstalk_base0)
        self.multiworld.regions.append(self.peak_beanstalk_base1)
        self.multiworld.regions.append(self.peak_beanstalk_base2)
        self.multiworld.regions.append(self.peak_beanstalk_base3)
        self.multiworld.regions.append(self.peak_beanstalk_base4)
        self.multiworld.regions.append(self.peak_beanstalk_base5)
        self.multiworld.regions.append(self.peak_crooked_cliff0)
        self.multiworld.regions.append(self.peak_crystal_crater0)
        self.multiworld.regions.append(self.peak_crystal_crater1)
        self.multiworld.regions.append(self.peak_crystal_crater2)
        self.multiworld.regions.append(self.peak_crystal_crater3)
        self.multiworld.regions.append(self.peak_filthy_flat0)
        self.multiworld.regions.append(self.peak_filthy_flat1)
        self.multiworld.regions.append(self.peak_filthy_flat2)
        self.multiworld.regions.append(self.peak_filthy_flat3)
        self.multiworld.regions.append(self.peak_filthy_flat4)
        self.multiworld.regions.append(self.peak_filthy_flat5)
        self.multiworld.regions.append(self.peak_frostpine_forest0)
        self.multiworld.regions.append(self.peak_frostpine_forest1)
        self.multiworld.regions.append(self.peak_frostpine_forest2)
        self.multiworld.regions.append(self.peak_guano_grief0)
        self.multiworld.regions.append(self.peak_guano_grief1)
        self.multiworld.regions.append(self.peak_guano_grief2)
        self.multiworld.regions.append(self.peak_guano_grief3)
        self.multiworld.regions.append(self.peak_guano_grief4)
        self.multiworld.regions.append(self.peak_guano_grief5)
        self.multiworld.regions.append(self.peak_guano_grief6)
        self.multiworld.regions.append(self.peak_ice_cold_idol0)
        self.multiworld.regions.append(self.peak_ice_cold_idol1)
        self.multiworld.regions.append(self.peak_obtainium_oracle0)
        self.multiworld.regions.append(self.peak_spider_fight0)
        self.multiworld.regions.append(self.peak_spider_fight1)

    def __add_spring_regions_to_world(self) -> None:
        """
        Add every `spring` region to the `world`
        """
        self.multiworld.regions.append(self.spring_bubbly_basin0)
        self.multiworld.regions.append(self.spring_bubbly_basin1)
        self.multiworld.regions.append(self.spring_bubbly_basin2)
        self.multiworld.regions.append(self.spring_bubbly_basin3)
        self.multiworld.regions.append(self.spring_bubbly_basin4)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs0)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs1)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs2)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs3)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs4)
        self.multiworld.regions.append(self.spring_cloudburst_cliffs5)
        self.multiworld.regions.append(self.spring_gangway_grotto0)
        self.multiworld.regions.append(self.spring_gangway_grotto1)
        self.multiworld.regions.append(self.spring_gangway_grotto2)
        self.multiworld.regions.append(self.spring_gangway_grotto3)
        self.multiworld.regions.append(self.spring_gangway_grotto4)
        self.multiworld.regions.append(self.spring_gangway_grotto5)
        self.multiworld.regions.append(self.spring_gangway_grotto6)
        self.multiworld.regions.append(self.spring_hidden_hotspring0)
        self.multiworld.regions.append(self.spring_hidden_hotspring1)
        self.multiworld.regions.append(self.spring_hidden_hotspring2)
        self.multiworld.regions.append(self.spring_hidden_hotspring3)
        self.multiworld.regions.append(self.spring_hidden_hotspring4)
        self.multiworld.regions.append(self.spring_jailhouse_japes0)
        self.multiworld.regions.append(self.spring_shoddy_shanty0)
        self.multiworld.regions.append(self.spring_shoddy_shanty1)
        self.multiworld.regions.append(self.spring_shoddy_shanty2)
        self.multiworld.regions.append(self.spring_shoddy_shanty3)
        self.multiworld.regions.append(self.spring_sleek_slabs0)
        self.multiworld.regions.append(self.spring_sleek_slabs1)
        self.multiworld.regions.append(self.spring_sleek_slabs2)
        self.multiworld.regions.append(self.spring_sleek_slabs3)
        self.multiworld.regions.append(self.spring_sleek_slabs4)
        self.multiworld.regions.append(self.spring_sleek_slabs5)
        self.multiworld.regions.append(self.spring_tiny_broad0)
        self.multiworld.regions.append(self.spring_tiny_broad1)
        self.multiworld.regions.append(self.spring_tiny_broad2)
        self.multiworld.regions.append(self.spring_tiny_broad3)
        self.multiworld.regions.append(self.spring_tiny_broad4)
        self.multiworld.regions.append(self.spring_tiny_broad5)
        self.multiworld.regions.append(self.spring_tiny_broad6)
        self.multiworld.regions.append(self.spring_tortoise_tunnel0)
        self.multiworld.regions.append(self.spring_yokos_yam0)
        self.multiworld.regions.append(self.spring_yokos_yam1)
        self.multiworld.regions.append(self.spring_yokos_yam2)

    def add_regions_to_world(self) -> None:
        """
        Add every region to the `world`
        """
        self.__add_cave_regions_to_world()
        self.__add_hub_regions_to_world()
        self.__add_intro_regions_to_world()
        self.__add_jungle_regions_to_world()
        self.__add_peak_regions_to_world()
        self.__add_spring_regions_to_world()

    def __init__(self, multiworld: MultiWorld, player: int):
        """
        Initialisation of the regions
        """
        self.multiworld = multiworld
        self.player = player
        self.__create_regions_cave()
        self.__create_regions_hub()
        self.__create_regions_intro()
        self.__create_regions_peak()
        self.__create_regions_jungle()
        self.__create_regions_spring()
