"""
Author: T Makuluni
Date: Fri, 26 Jan 2025
Description: Manage options in the Yoku's Island Express multiworld randomizer
"""

from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, StartInventoryPool


class Mode(Choice):
    """
    Select the randomizer mode.
    These are the same choices as in the original game.
    """
    display_name = "Mode"
    option_normal = 0
    option_hard = 1
    option_very_hard = 2
    default = 0

@dataclass
class YokuOptions(PerGameCommonOptions):
    """
    Every option in the Yoku's Island Express randomizer
    """
    start_inventory_from_pool: StartInventoryPool
    mode: Mode
