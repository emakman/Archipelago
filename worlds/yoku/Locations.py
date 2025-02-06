"""
Author: T Makuluni
Date: Fri, 25 Jan 2025
Description: Manage locations in the Yoku's Island Express randomizer
"""

from BaseClasses import Location, Region

class YokuLocation(Location):
    """
    A location in the game.
    """
    game: str = "Yoku's Island Express"
    """The name of the game"""

    def __init__(self, player: int, name: str="", code: int|None=None, parent: Region|None=None) -> None:
        """
        Initialisation of the object
        :param player: the ID of the player
        :param name: the name of the location
        :param code: the ID (or address) of the location (Event if None)
        :param parent: the Region that this location belongs to
        """
        super(YokuLocation, self).__init__(player, name, code, parent)
        self.event = code is None

location_table = {
            "Wl. 80: Behind Screech": { "id": 41288903, "tracker": 4277665904, "region": "cave_abyssal_access0", "tracker_string": "112,-264" },
            "Wl. 79: Screech Door Hook": { "id": 41289047, "tracker": 50334208, "region": "cave_abyssal_access1", "tracker_string": "2560,768" },
            "Fruit 90: Ocean Heart": { "id": 54329447, "tracker": 4178580032, "region": "cave_beach_bottom0", "tracker_string": "4672,-1776" },
            "Fruit 82: Screech Door Bones": { "id": 25105162, "tracker": 45614976, "region": "cave_beaver_blockade0", "tracker_string": "1920,696" },
            "Scarab 70: Door Friend I": { "id": 25105120, "tracker": 47190344, "region": "cave_beaver_blockade1" },
            "Chest: Screech": { "id": 25104987, "tracker": 92801584, "region": "cave_beaver_blockade2" },
            "Mailbox 11: Rolypoly": { "id": 44042632, "tracker": 4129817168, "region": "cave_clammy_cenote0" },
            "Wl. 76: Underdark Water Puzzle": { "id": 44041093, "tracker": 29885136, "region": "cave_clammy_cenote1", "tracker_string": "720,456", "revealed": True },
            "Wl. 74: Above Rolypoly": { "id": 44042001, "tracker": 4060610936, "region": "cave_clammy_cenote2", "tracker_string": "376,-3576" },
            "Wl. 75: Crystal Deep Beel. Ledge": { "id": 44040524, "tracker": 4108323872, "region": "cave_clammy_cenote2", "tracker_string": "3104,-2848" },
            "NPC: Quinbe": { "id": 53281416, "tracker": 3866626432, "region": "cave_east_bay_shore0" },
            "Mailbox 12: Beach": { "id": 53281476, "tracker": 4052225152, "region": "cave_east_bay_shore1" },
            "Mailbox 13: Quinbe": { "id": 53281471, "tracker": 3866628000, "region": "cave_east_bay_shore1" },
            "Chest: Beach": { "id": 53281548, "tracker": 3995075392, "region": "cave_east_bay_shore2" },
            "Mulch Pit: Beach": { "id": 53281572, "tracker": 3986163868, "region": "cave_east_bay_shore3", "tracker_string": "2204,-4712" },
            "Scarab 64: Trial I Right": { "id": 30216747, "tracker": 6028411, "region": "cave_temple_terror_lower0" },
            "Scarab 65: Trial I Left": { "id": 30216750, "tracker": 14285217, "region": "cave_temple_terror_lower0" },
            "Statue Piece: Underdark": { "id": 30216840, "tracker": 27851856, "region": "cave_temple_terror_lower1" },
            "Key: Green": { "id": 30217074, "tracker": 4256756216, "region": "cave_temple_terror_lower2", "tracker_string": "-3592,-584" },
            "Scarab 68: Trial III Right": { "id": 30216992, "tracker": 48295512, "region": "cave_temple_terror_lower3" },
            "Scarab 69: Trial III Left": { "id": 30217006, "tracker": 4269338416, "region": "cave_temple_terror_lower3" },
            "NPC: Liquorice": { "id": 30217093, "tracker": 4256757304, "region": "cave_temple_terror_lower4", "tracker_string": "-2504,-584" },
            "Key: Blue": { "id": 30212240, "tracker": 4276680744, "region": "cave_temple_terror_lower5", "tracker_string": "-2008,-280" },
            "Scarab 66: Trial II Right": { "id": 30216968, "tracker": 17888168, "region": "cave_temple_terror_lower6" },
            "Scarab 67: Trial II Left": { "id": 30216951, "tracker": 4279825456, "region": "cave_temple_terror_lower6" },
            "Wl. 77: Blue Chest": { "id": 47251672, "tracker": 15731168, "region": "cave_temple_terror_treasury0", "tracker_string": "2528,240" },
            "Fruit 32: Green Chest": { "id": 47251676, "tracker": 16779560, "region": "cave_temple_terror_treasury1" },
            "Fruit 89: Treasure Room": { "id": 47251961, "tracker": 26740240, "region": "cave_temple_terror_treasury2", "tracker_string": "1552,408" },
            "Mailbox 10: Sal": { "id": 46928212, "tracker": 68745024, "region": "cave_temple_terror_upper0" },
            "Wl. 78: Pitch": { "id": 25756550, "tracker": 4282389168, "region": "cave_winding_waterway0", "tracker_string": "4784,-192" },
            "Wl. 37: End Boss Fight": { "id": 52563019, "tracker": 4200596496, "region": "hub_bowel_bumping_left0", "tracker_string": "1040,-1440", "revealed": True },
            "Mailbox 05: Fleek": { "id": 45351379, "tracker": 4279764360, "region": "hub_cliffside_creek0" },
            "NPC: Fleek": { "id": 45351467, "tracker": 4241490784, "region": "hub_cliffside_creek1", "tracker_string": "864,-816" },
            "Chest: Fleek": { "id": 45351409, "tracker": 4203742464, "region": "hub_cliffside_creek2" },
            "NPC: Nim": { "id": 24973035, "tracker": 4294507088, "region": "hub_festival0", "tracker_string": "-1456,-8" },
            "Wl. 29: Instrument Cave": { "id": 45679446, "tracker": 4280352336, "region": "hub_festival_upper0", "tracker_string": "-432,-224" },
            "Wl. 28: Above Rinri": { "id": 45679114, "tracker": 4290251968, "region": "hub_festival_upper1", "tracker_string": "3264,-72" },
            "Mulch Pit: Village": { "id": 45679083, "tracker": 4235723044, "region": "hub_festival_upper2", "tracker_string": "292,-904" },
            "Mailbox 26: Sin": { "id": 52953351, "tracker": 4210035144, "region": "hub_hermits_home0" },
            "Wl. 24: Tower Top": { "id": 54857284, "tracker": 4289784184, "region": "hub_island_express0", "tracker_string": "-5768,-80" },
            "Mailbox 30: Tower": { "id": 54857259, "tracker": 2157592, "region": "hub_island_express1" },
            "Tower's Peak Crystal": { "id": 54857324, "tracker": 1109224, "region": "hub_island_express2", "tracker_string": "-4920,432" },
            "Chest: Tower": { "id": 54857276, "tracker": 4277726520, "region": "hub_island_express3" },
            "Mailbox 21: Sandro": { "id": 38666800, "tracker": 4251977216, "region": "hub_left_lemur_lane0" },
            "NPC: Treek": { "id": 28705196, "tracker": 1573800, "region": "hub_left_lofty_logo0" },
            "Wl. 30: Treek": { "id": 28705041, "tracker": 2097736, "region": "hub_left_lofty_logo1", "tracker_string": "584,32" },
            "Chest: Treek": { "id": 28705266, "tracker": 4247782280, "region": "hub_left_lofty_logo2" },
            "Statue Piece: Obt. Isles": { "id": 55771370, "tracker": 4111991128, "region": "hub_obtainium_outland0" },
            "Wl. 36: Obt. Puzzle": { "id": 55771787, "tracker": 4168679080, "region": "hub_obtainium_outland1", "tracker_string": "-344,-1928" },
            "Fruit 86: Sin": { "id": 50727459, "tracker": 4133488264, "region": "hub_soaring_stone0", "tracker_string": "1672,-2464", "revealed": True },
            "Wl. 35: Sin Totem": { "id": 50727469, "tracker": 4207936944, "region": "hub_soaring_stone0", "tracker_string": "1456,-1328" },
            "Wl. 27: All Mailboxes": { "id": 55185823, "tracker": 4247846584, "region": "hub_village0", "tracker_string": "-328,-720" },
            "NPC: Lemon, All Packages": { "id": 55185986, "tracker": 4268818048, "region": "hub_village1" },
            "Chest: Willo": { "id": 55185814, "tracker": 4224188720, "region": "hub_village2" },
            "Wl. 25: Lonka": { "id": 55185217, "tracker": 49348200, "region": "hub_village3", "tracker_string": "-408,752", "revealed": True },
            "Mailbox 19: Hub": { "id": 55185744, "tracker": 4291299880, "region": "hub_village4" },
            "Mailbox 20: Post Office": { "id": 55185740, "tracker": 4290773568, "region": "hub_village4" },
            "Post Office Attic": { "id": 55185973, "tracker": 4248370868, "region": "hub_village5", "tracker_string": "-334,-803", "revealed": True },
            "NPC: Rinri, Reward": { "id": 55185856, "tracker": 4212655816, "region": "hub_village6", "tracker_string": "3405,120" },
            "Wl. 26: Post Office Junk": { "id": 55185735, "tracker": 4267769816, "region": "hub_village7", "tracker_string": "-40,-416" },
            "Toolbox": { "id": 55185998, "tracker": 4212917772, "region": "hub_village8", "tracker_string": "1548,-1252", "revealed": True },
            "NPC: Lemon": { "id": 55185471, "tracker": 4269801480, "region": "hub_village8", "tracker_string": "8,-384" },
            "NPC: Rinri, Quest": { "id": 55185140, "tracker": 4213704344, "region": "hub_village8", "tracker_string": "1688,-1240" },
            "Mailbox 22: Dipperloaf": { "id": 52103026, "tracker": 4092071080, "region": "hub_white_cliff0" },
            "Wl. 31: Dipperloaf": { "id": 52103039, "tracker": 4032299056, "region": "hub_white_cliff1", "tracker_string": "48,-4008" },
            "NPC: Dipperloaf": { "id": 52103074, "tracker": 4093118592, "region": "hub_white_cliff2", "tracker_string": "2176,-3080" },
            "NPC: Posterodactyl": { "id": 21108214, "tracker": 84471568, "region": "menu", "tracker_string": "-4336,1288" },
            "Wl. 06: Fosfor Tunnel": { "id": 21108621, "tracker": 64488200, "region": "menu", "tracker_string": "776,984" },
            "Fruit 31: Banana Chest": { "id": 21108771, "tracker": 4286579384, "region": "intro_landing1" },
            "Mailbox 01: Hairy": { "id": 21108767, "tracker": 77657912, "region": "intro_landing2" },
            "Wl. 03: Hairy": { "id": 21108710, "tracker": 80278608, "region": "intro_landing3", "tracker_string": "-2992,1224" },
            "Wl. 07: Fosfor Cave": { "id": 36766403, "tracker": 76546608, "region": "intro_landing_creepy_cavern0", "tracker_string": "560,1168" },
            "Wl. 08: Fosfor Door": { "id": 36766387, "tracker": 3146336, "region": "intro_landing_creepy_cavern1", "tracker_string": "608,48" },
            "Wl. 01: Beach Dive 1": { "id": 44105819, "tracker": 15794168, "region": "intro_landing_left0", "tracker_string": "-8,240" },
            "Mailbox 06: Screech": { "id": 21172926, "tracker": 149429680, "region": "intro_landing_right0" },
            "Mailbox 04: Tweepers": { "id": 21172921, "tracker": 48239984, "region": "intro_landing_right1" },
            "Chest: Tweepers": { "id": 21173193, "tracker": 49288040, "region": "intro_landing_right2" },
            "NPC: Tweepers": { "id": 21172508, "tracker": 50861680, "region": "intro_landing_right2", "tracker_string": "5744,776" },
            "Wl. 10: Gorila Woods Beeline": { "id": 21173121, "tracker": 13635816, "region": "intro_landing_right2", "tracker_string": "4328,208" },
            "Scarab 37: Sootling House Upper": { "id": 21172735, "tracker": 108009552, "region": "intro_landing_right3" },
            "Scarab 38: Sootling House Lower": { "id": 21173226, "tracker": 116922472, "region": "intro_landing_right3" },
            "Chest: Noisemaker": { "id": 21042789, "tracker": 4145605912, "region": "intro_landing_upper0" },
            "Wl. 04: Intro 1": { "id": 21042679, "tracker": 4244172672, "region": "intro_landing_upper0", "tracker_string": "-4224,-776" },
            "Wl. 09: Above Fosfor": { "id": 21042801, "tracker": 4251976360, "region": "intro_landing_upper1", "tracker_string": "680,-656" },
            "Juicy Cove Mushroom": { "id": 21042450, "tracker": 4136111076, "region": "intro_landing_upper2", "tracker_string": "3044,-2424", "revealed": True },
            "Poison Toadstool": { "id": 21042661, "tracker": 4141878836, "region": "intro_landing_upper2", "tracker_string": "3648,-2356", "revealed": True },
            "Wl. 05: Intro 2": { "id": 21040985, "tracker": 4246796656, "region": "intro_landing_upper2", "tracker_string": "-1680,-736" },
            "Scarab 35: Mushrooms Left": { "id": 21042135, "tracker": 4181199648, "region": "intro_landing_upper3" },
            "Scarab 36: Mushrooms Right": { "id": 21041407, "tracker": 4113566464, "region": "intro_landing_upper3" },
            "Mailbox 03: Baldino": { "id": 21042729, "tracker": 4191743216, "region": "intro_landing_upper4" },
            "Wl. 34: Fleek": { "id": 21042438, "tracker": 4125625952, "region": "intro_landing_upper5", "tracker_string": "3680,-2584" },
            "Mailbox 02: Fosfor": { "id": 56098915, "tracker": 4260367648, "region": "intro_muddled_morass0" },
            "Chest: Fosfor Cave Left": { "id": 56099584, "tracker": 4240441800, "region": "intro_muddled_morass1" },
            "Wl. 02: Beach Dive 2": { "id": 22872105, "tracker": 6355600, "region": "intro_secret0", "tracker_string": "-1392,96" },
            "Wl. 12: Ape Chest": { "id": 36898607, "tracker": 70255784, "region": "jungle_canyon_caper0", "tracker_string": "1192,1072" },
            "NPC: Kickback": { "id": 36899447, "tracker": 4255645816, "region": "jungle_canyon_caper1", "tracker_string": "120,-600" },
            "Wl. 19: Waterfall Bottom": { "id": 23396866, "tracker": 4272951248, "region": "jungle_crammed_canopy0", "tracker_string": "4048,-336", "revealed": True },
            "Fruit 80: Meadows Slug Rock": { "id": 23396960, "tracker": 17828208, "region": "jungle_crammed_canopy1", "tracker_string": "2416,272" },
            "Wl. 18: Meadow Slug Jump": { "id": 23397003, "tracker": 4271901792, "region": "jungle_crammed_canopy1", "tracker_string": "3168,-352" },
            "Wl. 20: Shed": { "id": 21825342, "tracker": 4272949352, "region": "jungle_misty_meadow0", "tracker_string": "2152,-336" },
            "Mailbox 09: Shed": { "id": 21825455, "tracker": 4277667776, "region": "jungle_misty_meadow1" },
            "Chest: Shed": { "id": 21825866, "tracker": 4261416384, "region": "jungle_misty_meadow2" },
            "Mailbox 08: Slug Gardener": { "id": 21958374, "tracker": 4148691816, "region": "jungle_mollusc_madness0" },
            "Wl. 16: Slug Gardener Spot 2": { "id": 21957403, "tracker": 4167565528, "region": "jungle_mollusc_madness1", "tracker_string": "216,-1944", "revealed": True },
            "Wl. 17: Slug Gardener Spot 1": { "id": 21957816, "tracker": 4132503504, "region": "jungle_mollusc_madness1", "tracker_string": "-48,-2480", "revealed": True },
            "Scarab 75: Meadow IV": { "id": 21958863, "tracker": 50857256, "region": "jungle_mollusc_madness2" },
            "Scarab 76: Meadow V": { "id": 21957122, "tracker": 36700816, "region": "jungle_mollusc_madness2" },
            "Scarab 71: Meadow I Left": { "id": 21958797, "tracker": 4192731944, "region": "jungle_mollusc_madness3" },
            "Scarab 72: Meadow I Right": { "id": 21958795, "tracker": 4192470124, "region": "jungle_mollusc_madness3" },
            "Scarab 73: Meadow II Upper": { "id": 21958813, "tracker": 4216850488, "region": "jungle_mollusc_madness3" },
            "Scarab 74: Meadow II Lower": { "id": 21958834, "tracker": 4262987576, "region": "jungle_mollusc_madness3" },
            "Scarab 42: Juicery Lower": { "id": 24840039, "tracker": 63766623, "region": "jungle_roots0" },
            "Scarab 43: Juicery Upper": { "id": 24840041, "tracker": 58916968, "region": "jungle_roots0" },
            "Wl. 32: Juicery Upper": { "id": 24838662, "tracker": 37813824, "region": "jungle_roots1", "tracker_string": "-448,576" },
            "Wl. 33: Juicery Left": { "id": 24839105, "tracker": 78707832, "region": "jungle_roots1", "tracker_string": "-904,1200", "revealed": True },
            "Traitor Spirit 1": { "id": 21761425, "tracker": 4271376216, "region": "jungle_slug_struggle0", "tracker_string": "1880,-360", "revealed": True },
            "Traitor Spirit 2": { "id": 21761465, "tracker": 4287367148, "region": "jungle_slug_struggle0", "tracker_string": "2028,-116", "revealed": True },
            "Traitor Spirit 3": { "id": 21761423, "tracker": 4292610368, "region": "jungle_slug_struggle0", "tracker_string": "2368,-36", "revealed": True },
            "Traitor Spirit 4": { "id": 21761363, "tracker": 4269804191, "region": "jungle_slug_struggle0", "tracker_string": "2719,-384", "revealed": True },
            "Mailbox 07: Ape": { "id": 21761301, "tracker": 4219470584, "region": "jungle_slug_struggle1" },
            "Wl. 13: Ape Hook": { "id": 21761097, "tracker": 4261413072, "region": "jungle_slug_struggle2", "tracker_string": "208,-512" },
            "NPC: Skeeper": { "id": 21761516, "tracker": 4212131424, "region": "jungle_slug_struggle3", "tracker_string": "1632,-1264" },
            "Wl. 14: Ape Entry": { "id": 21758395, "tracker": 4238344672, "region": "jungle_slug_struggle3", "tracker_string": "480,-864" },
            "Wl. 15: Ape Right": { "id": 21760842, "tracker": 4721960, "region": "jungle_slug_struggle3", "tracker_string": "3368,72", "revealed": True },
            "Mulch Pit: Ape": { "id": 21761617, "tracker": 4293263672, "region": "jungle_slug_struggle4", "tracker_string": "144,-72" },
            "NPC: Dusk": { "id": 45220046, "tracker": 4214227832, "region": "jungle_spikey_stockade0", "tracker_string": "888,-1232" },
            "Scarab 40: Tower Left": { "id": 23988666, "tracker": 4266983160, "region": "jungle_tall_tall_tower0" },
            "Scarab 41: Tower Upper": { "id": 23988671, "tracker": 4237361040, "region": "jungle_tall_tall_tower0" },
            "Wl. 11: Tower Table": { "id": 23987316, "tracker": 4276158136, "region": "jungle_tall_tall_tower1", "tracker_string": "-328,-288" },
            "Wl. 23: Tower Mid": { "id": 23987363, "tracker": 4081058584, "region": "jungle_tall_tall_tower1", "tracker_string": "792,-3264" },
            "Scarab 39: Tower Right": { "id": 23989298, "tracker": 4281336640, "region": "jungle_tall_tall_tower2" },
            "Scarab 58: Willo Right": { "id": 48169307, "tracker": 4261938264, "region": "jungle_willy0" },
            "Scarab 59: Willo Mid": { "id": 48170870, "tracker": 4253549712, "region": "jungle_willy0" },
            "Scarab 60: Willo Left": { "id": 48170941, "tracker": 4266656820, "region": "jungle_willy0" },
            "Statue Piece: Waterfall": { "id": 48170179, "tracker": 4274061152, "region": "jungle_willy1", "tracker_string": "-160,-320" },
            "Wl. 56: Above Willo at Waterfall": { "id": 48170957, "tracker": 4210097784, "region": "jungle_willy2", "tracker_string": "-392,-1296" },
            "Mailbox 23: Treek": { "id": 25628632, "tracker": 4286584032, "region": "peak_aerial_ascent0" },
            "Mailbox 24: Orestation": { "id": 25628637, "tracker": 4195312, "region": "peak_aerial_ascent0" },
            "Statue Piece: Ivory": { "id": 25628609, "tracker": 4069001504, "region": "peak_aerial_ascent1" },
            "Wl. 42: Orestation Hook": { "id": 25628823, "tracker": 4141940344, "region": "peak_aerial_ascent2", "tracker_string": "-392,-2336", "revealed": True },
            "Wl. 40: Leap of Faith": { "id": 25628685, "tracker": 4154986888, "region": "peak_aerial_ascent3", "tracker_string": "4488,-2136" },
            "Wl. 38: Orestation Bottom": { "id": 25627242, "tracker": 29886208, "region": "peak_aerial_ascent4", "tracker_string": "1792,456" },
            "Wl. 39: God Misfire": { "id": 25626797, "tracker": 4215804432, "region": "peak_aerial_ascent5", "tracker_string": "4624,-1208", "revealed": True },
            "Wl. 41: Squirrowl": { "id": 25627136, "tracker": 4133489384, "region": "peak_aerial_ascent6", "tracker_string": "2792,-2464" },
            "Scarab 44: Orestation Right": { "id": 25628848, "tracker": 4191686032, "region": "peak_aerial_ascent7" },
            "Scarab 45: Orestation Left": { "id": 25628865, "tracker": 4196928536, "region": "peak_aerial_ascent7" },
            "Wl. 53: Jamja Ledge": { "id": 57085342, "tracker": 3984066824, "region": "peak_beanstalk_base0", "tracker_string": "2312,-4744" },
            "Seed Pod": { "id": 57084164, "tracker": 4057990928, "region": "peak_beanstalk_base1", "tracker_string": "1808,-3616" },
            "Wl. 50: Ivory Hook Lower": { "id": 57084663, "tracker": 4094230104, "region": "peak_beanstalk_base2", "tracker_string": "-424,-3064" },
            "Wl. 52: Ivory Hook Upper": { "id": 57084973, "tracker": 4000381992, "region": "peak_beanstalk_base2", "tracker_string": "-984,-4496", "revealed": True },
            "NPC: Jamja": { "id": 57085027, "tracker": 4016572576, "region": "peak_beanstalk_base3", "tracker_string": "2208,-4248" },
            "Chest: Town Skip": { "id": 57085255, "tracker": 4204265672, "region": "peak_beanstalk_base4" },
            "Chest: Lava": { "id": 57085246, "tracker": 4087351776, "region": "peak_beanstalk_base5" },
            "Mailbox 29: Space Monks": { "id": 39454067, "tracker": 4169666808, "region": "peak_crooked_cliff0" },
            "Nugget 1": { "id": 48892285, "tracker": 4199811636, "region": "peak_crystal_crater0", "tracker_string": "2612,-1452" },
            "Nugget 2": { "id": 48892094, "tracker": 4166519832, "region": "peak_crystal_crater0", "tracker_string": "3096,-1960" },
            "Nugget 3": { "id": 48892283, "tracker": 4168355476, "region": "peak_crystal_crater0", "tracker_string": "3732,-1932" },
            "Nugget 4": { "id": 48892281, "tracker": 4165734492, "region": "peak_crystal_crater0", "tracker_string": "4188,-1972" },
            "Fruit 87: Crystal Lake": { "id": 48892757, "tracker": 4134013448, "region": "peak_crystal_crater1", "tracker_string": "2568,-2456", "revealed": True },
            "Wl. 51: Sumoe": { "id": 48891952, "tracker": 4199548264, "region": "peak_crystal_crater2", "tracker_string": "1384,-1456" },
            "NPC: Sumoe": { "id": 48892764, "tracker": 4150264984, "region": "peak_crystal_crater3", "tracker_string": "1176,-2208" },
            "Mailbox 25: Lighthouse": { "id": 38472470, "tracker": 4272950488, "region": "peak_filthy_flat0" },
            "Sootling 6": { "id": 38469896, "tracker": 4028630608, "region": "peak_filthy_flat1", "tracker_string": "1616,-4064" },
            "Sootling 1": { "id": 38469887, "tracker": 4194305584, "region": "peak_filthy_flat2", "tracker_string": "1584,-1536" },
            "Sootling 2": { "id": 38469941, "tracker": 4140303400, "region": "peak_filthy_flat2", "tracker_string": "1064,-2360" },
            "Sootling 3": { "id": 38470259, "tracker": 4093117904, "region": "peak_filthy_flat2", "tracker_string": "1488,-3080" },
            "Sootling 4": { "id": 38470383, "tracker": 4092593784, "region": "peak_filthy_flat3", "tracker_string": "1656,-3088" },
            "Sootling 5": { "id": 38470932, "tracker": 4098360920, "region": "peak_filthy_flat3", "tracker_string": "1624,-3000" },
            "Wl. 43: Lighthouse Ledge": { "id": 38472500, "tracker": 4149215848, "region": "peak_filthy_flat3", "tracker_string": "616,-2224" },
            "Wl. 44: Lighthouse Slug Rock": { "id": 38471745, "tracker": 4131914688, "region": "peak_filthy_flat3", "tracker_string": "960,-2488" },
            "Wl. 45: Lighthouse Leap": { "id": 38470609, "tracker": 4057467200, "region": "peak_filthy_flat3", "tracker_string": "2368,-3624", "revealed": True },
            "Scarab 46: Lighthouse I Right": { "id": 38472003, "tracker": 4194829752, "region": "peak_filthy_flat4" },
            "Scarab 47: Lighthouse I Left": { "id": 38472598, "tracker": 4163896448, "region": "peak_filthy_flat4" },
            "Scarab 48: Lighthouse II": { "id": 38472624, "tracker": 4103079440, "region": "peak_filthy_flat4" },
            "Chest: Leash": { "id": 38472445, "tracker": 4270850376, "region": "peak_filthy_flat5" },
            "Fruit 83: Sootling Cave Water": { "id": 28446220, "tracker": 27791184, "region": "peak_frostpine_forest0", "tracker_string": "3920,424", "revealed": True },
            "Mailbox 27: Ithaqua": { "id": 28445582, "tracker": 4268229600, "region": "peak_frostpine_forest1" },
            "Fruit 84: Sootling Cave Right": { "id": 28445943, "tracker": 4232581944, "region": "peak_frostpine_forest2", "tracker_string": "4920,-952", "revealed": True },
            "Fruit 85: Sootling Cave Left": { "id": 28445932, "tracker": 4227337984, "region": "peak_frostpine_forest2", "tracker_string": "3840,-1032", "revealed": True },
            "Wl. 46: Sootling Cave": { "id": 28445810, "tracker": 4257224384, "region": "peak_frostpine_forest2", "tracker_string": "5824,-576" },
            "Mulch Pit: Ivory": { "id": 56691154, "tracker": 3955491464, "region": "peak_guano_grief0", "tracker_string": "648,-5180" },
            "Guano": { "id": 56689309, "tracker": 4037281604, "region": "peak_guano_grief1", "tracker_string": "1860,-3932" },
            "Wl. 49: Telescope Skip Upper": { "id": 56691064, "tracker": 4140826648, "region": "peak_guano_grief2", "tracker_string": "24,-2352" },
            "Wl. 48: Telescope Skip Lower": { "id": 56688830, "tracker": 4211081552, "region": "peak_guano_grief3", "tracker_string": "336,-1280" },
            "Scarab 49: Town Skip": { "id": 56690172, "tracker": 4261938544, "region": "peak_guano_grief4" },
            "Scarab 50: Bat": { "id": 56691137, "tracker": 4029153584, "region": "peak_guano_grief5" },
            "Wl. 47: Kickback Hiding Cave": { "id": 56689807, "tracker": 4292870664, "region": "peak_guano_grief6", "tracker_string": "520,-32" },
            "Wl. 54: Spider Cave Entry": { "id": 54528431, "tracker": 3783850472, "region": "peak_ice_cold_idol0", "tracker_string": "-1560,-7800", "revealed": True },
            "Fruit 88: Spider Cave": { "id": 54528363, "tracker": 3811113640, "region": "peak_ice_cold_idol1", "tracker_string": "-1368,-7384", "revealed": True },
            "Mailbox 28: Ojva": { "id": 56885316, "tracker": 4218423200, "region": "peak_obtainium_oracle0" },
            "Wl. 55: Spider Cave Slug Rock": { "id": 48431629, "tracker": 198245132, "region": "peak_spider_fight0", "tracker_string": "-1268,3024" },
            "Scarab 51: Spider Cave I": { "id": 48433763, "tracker": 203488136, "region": "peak_spider_fight1" },
            "Scarab 52: Spider Cave II": { "id": 48433802, "tracker": 128515136, "region": "peak_spider_fight1" },
            "Wl. 60: Dive Cave Chest": { "id": 43910175, "tracker": 4288675928, "region": "spring_bubbly_basin0", "tracker_string": "88,-96" },
            "Tadpole 1": { "id": 43910361, "tracker": 4291364328, "region": "spring_bubbly_basin1", "tracker_string": "1512,-55", "revealed": True },
            "Tadpole 3": { "id": 43910364, "tracker": 9505096, "region": "spring_bubbly_basin1", "tracker_string": "2376,145", "revealed": True },
            "Tadpole 4": { "id": 43910355, "tracker": 4268296856, "region": "spring_bubbly_basin1", "tracker_string": "2712,-407", "revealed": True },
            "Tadpole 5": { "id": 43910349, "tracker": 4260957888, "region": "spring_bubbly_basin1", "tracker_string": "3776,-519", "revealed": True },
            "Tadpole 6": { "id": 43910346, "tracker": 4276162816, "region": "spring_bubbly_basin1", "tracker_string": "4352,-287", "revealed": True },
            "Tadpole 7": { "id": 43910161, "tracker": 4251849008, "region": "spring_bubbly_basin1", "tracker_string": "4400,-658", "revealed": True },
            "Tadpole 8": { "id": 43910352, "tracker": 4282979928, "region": "spring_bubbly_basin1", "tracker_string": "5720,-183", "revealed": True },
            "Tadpole 2": { "id": 43910358, "tracker": 4244178552, "region": "spring_bubbly_basin2", "tracker_string": "1656,-775", "revealed": True },
            "NPC: Dive Fish": { "id": 43910274, "tracker": 4220521232, "region": "spring_bubbly_basin3", "tracker_string": "2832,-1136" },
            "NPC: Myrtle": { "id": 43910016, "tracker": 4226290800, "region": "spring_bubbly_basin4", "tracker_string": "5232,-1048" },
            "NPC: Cleepers": { "id": 26284950, "tracker": 3993503480, "region": "spring_cloudburst_cliffs0", "tracker_string": "1784,-4600" },
            "Fruit 77: Waterfall Left": { "id": 26284092, "tracker": 4223664200, "region": "spring_cloudburst_cliffs1", "tracker_string": "72,-1088", "revealed": True },
            "Fruit 79: Waterfall Right": { "id": 26284095, "tracker": 4232054056, "region": "spring_cloudburst_cliffs2", "tracker_string": "1320,-960", "revealed": True },
            "Wl. 21: Waterfall Ledge": { "id": 26284713, "tracker": 4188538192, "region": "spring_cloudburst_cliffs3", "tracker_string": "1360,-1624" },
            "Mailbox 18: Waterfall": { "id": 26284437, "tracker": 4204855176, "region": "spring_cloudburst_cliffs4" },
            "Chest: Waterfall": { "id": 26284861, "tracker": 4029742568, "region": "spring_cloudburst_cliffs5" },
            "Mailbox 14: Hideout": { "id": 30544446, "tracker": 4181196864, "region": "spring_gangway_grotto0" },
            "Wl. 67: Sush": { "id": 30544191, "tracker": 4271374928, "region": "spring_gangway_grotto1", "tracker_string": "592,-360" },
            "Wl. 69: Hideout Slug Rock": { "id": 30544255, "tracker": 4132965728, "region": "spring_gangway_grotto1", "tracker_string": "3424,-2472" },
            "Fruit 34: Underwater Chest": { "id": 30544450, "tracker": 4188538672, "region": "spring_gangway_grotto2" },
            "NPC: Jojo": { "id": 30544307, "tracker": 4115139088, "region": "spring_gangway_grotto3", "tracker_string": "2576,-2744" },
            "Wl. 68: Hideout Ledge": { "id": 30544153, "tracker": 4138731872, "region": "spring_gangway_grotto4", "tracker_string": "2400,-2384" },
            "NPC: Splank": { "id": 30544501, "tracker": 4115664624, "region": "spring_gangway_grotto5", "tracker_string": "3824,-2736" },
            "Wl. 70: Hideout Drop 1": { "id": 30544389, "tracker": 4226814048, "region": "spring_gangway_grotto6", "tracker_string": "4192,-1040", "revealed": True },
            "Wl. 73: Crystal Skull Chest": { "id": 27592231, "tracker": 33555616, "region": "spring_hidden_hotspring0", "tracker_string": "1184,512" },
            "Chest: Crystal Skull": { "id": 27592999, "tracker": 56100280, "region": "spring_hidden_hotspring1" },
            "Scarab 62: Crystal Skull Left": { "id": 27592971, "tracker": 4293984032, "region": "spring_hidden_hotspring2" },
            "Scarab 63: Crystal Skull Right": { "id": 27592983, "tracker": 31457744, "region": "spring_hidden_hotspring2" },
            "Wl. 72: Crystal Skull Slug Rock": { "id": 27592682, "tracker": 4258856512, "region": "spring_hidden_hotspring3", "tracker_string": "-448,-552" },
            "Scarab 61: Crystal Skull Upper": { "id": 27592975, "tracker": 4255645976, "region": "spring_hidden_hotspring4" },
            "Wl. 22: Waterfall Dive Through": { "id": 27657424, "tracker": 75497552, "region": "spring_jailhouse_japes0", "tracker_string": "80,1152", "revealed": True },
            "Mailbox 16: Church": { "id": 54007074, "tracker": 4213765056, "region": "spring_shoddy_shanty0" },
            "Wl. 59: Dive Cave Entry": { "id": 54005874, "tracker": 4261476320, "region": "spring_shoddy_shanty1", "tracker_string": "-2080,-512" },
            "Underwater Puzzle": { "id": 54007097, "tracker": 37813616, "region": "spring_shoddy_shanty2", "tracker_string": "-656,576" },
            "Wl. 58: Church Ceiling": { "id": 54006765, "tracker": 4194367360, "region": "spring_shoddy_shanty3", "tracker_string": "-2176,-1536" },
            "Mailbox 17: Kambi": { "id": 26481036, "tracker": 4279239408, "region": "spring_sleek_slabs0" },
            "Wl. 61: Underwater at Hook Chest": { "id": 26480930, "tracker": 31988528, "region": "spring_sleek_slabs1", "tracker_string": "6960,488", "revealed": True },
            "Fruit 81: Marrow Jump": { "id": 26480910, "tracker": 4281341648, "region": "spring_sleek_slabs2", "tracker_string": "5840,-208", "revealed": True },
            "Fruit 33: Hook Chest": { "id": 26481041, "tracker": 4282392888, "region": "spring_sleek_slabs3" },
            "Wl. 57: Church Chest": { "id": 26481085, "tracker": 23069552, "region": "spring_sleek_slabs4", "tracker_string": "880,352" },
            "Chest: Church": { "id": 26481086, "tracker": 11010136, "region": "spring_sleek_slabs5" },
            "Mailbox 15: Underbelly": { "id": 31987048, "tracker": 4239458120, "region": "spring_tiny_broad0" },
            "Scarab 55: Underbelly I Right": { "id": 31983859, "tracker": 4276094200, "region": "spring_tiny_broad1" },
            "Wl. 64: Underbelly I Right": { "id": 31982433, "tracker": 4281336280, "region": "spring_tiny_broad2", "tracker_string": "472,-208", "revealed": True },
            "Scarab 56: Underbelly I Left": { "id": 31987188, "tracker": 4294508008, "region": "spring_tiny_broad3" },
            "Scarab 57: Underbelly I Mid": { "id": 31987185, "tracker": 11534600, "region": "spring_tiny_broad3" },
            "Wl. 62: Underbelly I Left": { "id": 31983991, "tracker": 36765112, "region": "spring_tiny_broad4", "tracker_string": "-584,560", "revealed": True },
            "Wl. 63: Underbelly I Upper": { "id": 31985568, "tracker": 13631616, "region": "spring_tiny_broad4", "tracker_string": "128,208" },
            "Fruit 78: Underbelly": { "id": 31987079, "tracker": 4287106288, "region": "spring_tiny_broad5", "tracker_string": "3312,-120", "revealed": True },
            "Wl. 65: Underbelly II Hidden": { "id": 31986809, "tracker": 17828304, "region": "spring_tiny_broad6", "tracker_string": "2512,272" },
            "Wl. 71: Crystal Skull Upper": { "id": 27790467, "tracker": 106431648, "region": "spring_tortoise_tunnel0", "tracker_string": "1184,1624" },
            "Scarab 53: Underbelly II Right": { "id": 37424285, "tracker": 4175102945, "region": "spring_yokos_yam0" },
            "Wl. 66: Hideout Drop 2": { "id": 37424461, "tracker": 4292345912, "region": "spring_yokos_yam1", "tracker_string": "56,-40" },
            "Scarab 54: Underbelly II Left": { "id": 37424029, "tracker": 4208984856, "region": "spring_yokos_yam2" }
        }

def region_locations(region: str) -> dict[str,int]:
    return { loc: data["id"] for loc,data in location_table.items() if data["region"]==region }

class YokuLocations:
    locations_cave_abyssal_access0 = region_locations("cave_abyssal_access0")
    locations_cave_abyssal_access1 = region_locations("cave_abyssal_access1")
    locations_cave_beach_bottom0 = region_locations("cave_beach_bottom0")
    locations_cave_beaver_blockade0 = region_locations("cave_beaver_blockade0")
    locations_cave_beaver_blockade1 = region_locations("cave_beaver_blockade1")
    locations_cave_beaver_blockade2 = region_locations("cave_beaver_blockade2")
    locations_cave_clammy_cenote0 = region_locations("cave_clammy_cenote0")
    locations_cave_clammy_cenote1 = region_locations("cave_clammy_cenote1")
    locations_cave_clammy_cenote2 = region_locations("cave_clammy_cenote2")
    locations_cave_east_bay_shore0 = region_locations("cave_east_bay_shore0")
    locations_cave_east_bay_shore1 = region_locations("cave_east_bay_shore1")
    locations_cave_east_bay_shore2 = region_locations("cave_east_bay_shore2")
    locations_cave_east_bay_shore3 = region_locations("cave_east_bay_shore3")
    locations_cave_temple_terror_lower0 = region_locations("cave_temple_terror_lower0")
    locations_cave_temple_terror_lower1 = region_locations("cave_temple_terror_lower1")
    locations_cave_temple_terror_lower2 = region_locations("cave_temple_terror_lower2")
    locations_cave_temple_terror_lower3 = region_locations("cave_temple_terror_lower3")
    locations_cave_temple_terror_lower4 = region_locations("cave_temple_terror_lower4")
    locations_cave_temple_terror_lower5 = region_locations("cave_temple_terror_lower5")
    locations_cave_temple_terror_lower6 = region_locations("cave_temple_terror_lower6")
    locations_cave_temple_terror_treasury0 = region_locations("cave_temple_terror_treasury0")
    locations_cave_temple_terror_treasury1 = region_locations("cave_temple_terror_treasury1")
    locations_cave_temple_terror_treasury2 = region_locations("cave_temple_terror_treasury2")
    locations_cave_temple_terror_upper0 = region_locations("cave_temple_terror_upper0")
    locations_cave_winding_waterway0 = region_locations("cave_winding_waterway0")
    locations_hub_bowel_bumping_left0 = region_locations("hub_bowel_bumping_left0")
    locations_hub_cliffside_creek0 = region_locations("hub_cliffside_creek0")
    locations_hub_cliffside_creek1 = region_locations("hub_cliffside_creek1")
    locations_hub_cliffside_creek2 = region_locations("hub_cliffside_creek2")
    locations_hub_festival0 = region_locations("hub_festival0")
    locations_hub_festival_upper0 = region_locations("hub_festival_upper0")
    locations_hub_festival_upper1 = region_locations("hub_festival_upper1")
    locations_hub_festival_upper2 = region_locations("hub_festival_upper2")
    locations_hub_hermits_home0 = region_locations("hub_hermits_home0")
    locations_hub_island_express0 = region_locations("hub_island_express0")
    locations_hub_island_express1 = region_locations("hub_island_express1")
    locations_hub_island_express2 = region_locations("hub_island_express2")
    locations_hub_island_express3 = region_locations("hub_island_express3")
    locations_hub_left_lemur_lane0 = region_locations("hub_left_lemur_lane0")
    locations_hub_left_lofty_logo0 = region_locations("hub_left_lofty_logo0")
    locations_hub_left_lofty_logo1 = region_locations("hub_left_lofty_logo1")
    locations_hub_left_lofty_logo2 = region_locations("hub_left_lofty_logo2")
    locations_hub_obtainium_outland0 = region_locations("hub_obtainium_outland0")
    locations_hub_obtainium_outland1 = region_locations("hub_obtainium_outland1")
    locations_hub_soaring_stone0 = region_locations("hub_soaring_stone0")
    locations_hub_village0 = region_locations("hub_village0")
    locations_hub_village1 = region_locations("hub_village1")
    locations_hub_village2 = region_locations("hub_village2")
    locations_hub_village3 = region_locations("hub_village3")
    locations_hub_village4 = region_locations("hub_village4")
    locations_hub_village5 = region_locations("hub_village5")
    locations_hub_village6 = region_locations("hub_village6")
    locations_hub_village7 = region_locations("hub_village7")
    locations_hub_village8 = region_locations("hub_village8")
    locations_hub_white_cliff0 = region_locations("hub_white_cliff0")
    locations_hub_white_cliff1 = region_locations("hub_white_cliff1")
    locations_hub_white_cliff2 = region_locations("hub_white_cliff2")
    locations_menu = region_locations("menu")
    locations_intro_landing1 = region_locations("intro_landing1")
    locations_intro_landing2 = region_locations("intro_landing2")
    locations_intro_landing3 = region_locations("intro_landing3")
    locations_intro_landing_creepy_cavern0 = region_locations("intro_landing_creepy_cavern0")
    locations_intro_landing_creepy_cavern1 = region_locations("intro_landing_creepy_cavern1")
    locations_intro_landing_left0 = region_locations("intro_landing_left0")
    locations_intro_landing_right0 = region_locations("intro_landing_right0")
    locations_intro_landing_right1 = region_locations("intro_landing_right1")
    locations_intro_landing_right2 = region_locations("intro_landing_right2")
    locations_intro_landing_right3 = region_locations("intro_landing_right3")
    locations_intro_landing_upper0 = region_locations("intro_landing_upper0")
    locations_intro_landing_upper1 = region_locations("intro_landing_upper1")
    locations_intro_landing_upper2 = region_locations("intro_landing_upper2")
    locations_intro_landing_upper3 = region_locations("intro_landing_upper3")
    locations_intro_landing_upper4 = region_locations("intro_landing_upper4")
    locations_intro_landing_upper5 = region_locations("intro_landing_upper5")
    locations_intro_muddled_morass0 = region_locations("intro_muddled_morass0")
    locations_intro_muddled_morass1 = region_locations("intro_muddled_morass1")
    locations_intro_secret0 = region_locations("intro_secret0")
    locations_jungle_canyon_caper0 = region_locations("jungle_canyon_caper0")
    locations_jungle_canyon_caper1 = region_locations("jungle_canyon_caper1")
    locations_jungle_crammed_canopy0 = region_locations("jungle_crammed_canopy0")
    locations_jungle_crammed_canopy1 = region_locations("jungle_crammed_canopy1")
    locations_jungle_misty_meadow0 = region_locations("jungle_misty_meadow0")
    locations_jungle_misty_meadow1 = region_locations("jungle_misty_meadow1")
    locations_jungle_misty_meadow2 = region_locations("jungle_misty_meadow2")
    locations_jungle_mollusc_madness0 = region_locations("jungle_mollusc_madness0")
    locations_jungle_mollusc_madness1 = region_locations("jungle_mollusc_madness1")
    locations_jungle_mollusc_madness2 = region_locations("jungle_mollusc_madness2")
    locations_jungle_mollusc_madness3 = region_locations("jungle_mollusc_madness3")
    locations_jungle_roots0 = region_locations("jungle_roots0")
    locations_jungle_roots1 = region_locations("jungle_roots1")
    locations_jungle_slug_struggle0 = region_locations("jungle_slug_struggle0")
    locations_jungle_slug_struggle1 = region_locations("jungle_slug_struggle1")
    locations_jungle_slug_struggle2 = region_locations("jungle_slug_struggle2")
    locations_jungle_slug_struggle3 = region_locations("jungle_slug_struggle3")
    locations_jungle_slug_struggle4 = region_locations("jungle_slug_struggle4")
    locations_jungle_spikey_stockade0 = region_locations("jungle_spikey_stockade0")
    locations_jungle_tall_tall_tower0 = region_locations("jungle_tall_tall_tower0")
    locations_jungle_tall_tall_tower1 = region_locations("jungle_tall_tall_tower1")
    locations_jungle_tall_tall_tower2 = region_locations("jungle_tall_tall_tower2")
    locations_jungle_willy0 = region_locations("jungle_willy0")
    locations_jungle_willy1 = region_locations("jungle_willy1")
    locations_jungle_willy2 = region_locations("jungle_willy2")
    locations_peak_aerial_ascent0 = region_locations("peak_aerial_ascent0")
    locations_peak_aerial_ascent1 = region_locations("peak_aerial_ascent1")
    locations_peak_aerial_ascent2 = region_locations("peak_aerial_ascent2")
    locations_peak_aerial_ascent3 = region_locations("peak_aerial_ascent3")
    locations_peak_aerial_ascent4 = region_locations("peak_aerial_ascent4")
    locations_peak_aerial_ascent5 = region_locations("peak_aerial_ascent5")
    locations_peak_aerial_ascent6 = region_locations("peak_aerial_ascent6")
    locations_peak_aerial_ascent7 = region_locations("peak_aerial_ascent7")
    locations_peak_beanstalk_base0 = region_locations("peak_beanstalk_base0")
    locations_peak_beanstalk_base1 = region_locations("peak_beanstalk_base1")
    locations_peak_beanstalk_base2 = region_locations("peak_beanstalk_base2")
    locations_peak_beanstalk_base3 = region_locations("peak_beanstalk_base3")
    locations_peak_beanstalk_base4 = region_locations("peak_beanstalk_base4")
    locations_peak_beanstalk_base5 = region_locations("peak_beanstalk_base5")
    locations_peak_crooked_cliff0 = region_locations("peak_crooked_cliff0")
    locations_peak_crystal_crater0 = region_locations("peak_crystal_crater0")
    locations_peak_crystal_crater1 = region_locations("peak_crystal_crater1")
    locations_peak_crystal_crater2 = region_locations("peak_crystal_crater2")
    locations_peak_crystal_crater3 = region_locations("peak_crystal_crater3")
    locations_peak_filthy_flat0 = region_locations("peak_filthy_flat0")
    locations_peak_filthy_flat1 = region_locations("peak_filthy_flat1")
    locations_peak_filthy_flat2 = region_locations("peak_filthy_flat2")
    locations_peak_filthy_flat3 = region_locations("peak_filthy_flat3")
    locations_peak_filthy_flat4 = region_locations("peak_filthy_flat4")
    locations_peak_filthy_flat5 = region_locations("peak_filthy_flat5")
    locations_peak_frostpine_forest0 = region_locations("peak_frostpine_forest0")
    locations_peak_frostpine_forest1 = region_locations("peak_frostpine_forest1")
    locations_peak_frostpine_forest2 = region_locations("peak_frostpine_forest2")
    locations_peak_guano_grief0 = region_locations("peak_guano_grief0")
    locations_peak_guano_grief1 = region_locations("peak_guano_grief1")
    locations_peak_guano_grief2 = region_locations("peak_guano_grief2")
    locations_peak_guano_grief3 = region_locations("peak_guano_grief3")
    locations_peak_guano_grief4 = region_locations("peak_guano_grief4")
    locations_peak_guano_grief5 = region_locations("peak_guano_grief5")
    locations_peak_guano_grief6 = region_locations("peak_guano_grief6")
    locations_peak_ice_cold_idol0 = region_locations("peak_ice_cold_idol0")
    locations_peak_ice_cold_idol1 = region_locations("peak_ice_cold_idol1")
    locations_peak_obtainium_oracle0 = region_locations("peak_obtainium_oracle0")
    locations_peak_spider_fight0 = region_locations("peak_spider_fight0")
    locations_peak_spider_fight1 = region_locations("peak_spider_fight1")
    locations_spring_bubbly_basin0 = region_locations("spring_bubbly_basin0")
    locations_spring_bubbly_basin1 = region_locations("spring_bubbly_basin1")
    locations_spring_bubbly_basin2 = region_locations("spring_bubbly_basin2")
    locations_spring_bubbly_basin3 = region_locations("spring_bubbly_basin3")
    locations_spring_bubbly_basin4 = region_locations("spring_bubbly_basin4")
    locations_spring_cloudburst_cliffs0 = region_locations("spring_cloudburst_cliffs0")
    locations_spring_cloudburst_cliffs1 = region_locations("spring_cloudburst_cliffs1")
    locations_spring_cloudburst_cliffs2 = region_locations("spring_cloudburst_cliffs2")
    locations_spring_cloudburst_cliffs3 = region_locations("spring_cloudburst_cliffs3")
    locations_spring_cloudburst_cliffs4 = region_locations("spring_cloudburst_cliffs4")
    locations_spring_cloudburst_cliffs5 = region_locations("spring_cloudburst_cliffs5")
    locations_spring_gangway_grotto0 = region_locations("spring_gangway_grotto0")
    locations_spring_gangway_grotto1 = region_locations("spring_gangway_grotto1")
    locations_spring_gangway_grotto2 = region_locations("spring_gangway_grotto2")
    locations_spring_gangway_grotto3 = region_locations("spring_gangway_grotto3")
    locations_spring_gangway_grotto4 = region_locations("spring_gangway_grotto4")
    locations_spring_gangway_grotto5 = region_locations("spring_gangway_grotto5")
    locations_spring_gangway_grotto6 = region_locations("spring_gangway_grotto6")
    locations_spring_hidden_hotspring0 = region_locations("spring_hidden_hotspring0")
    locations_spring_hidden_hotspring1 = region_locations("spring_hidden_hotspring1")
    locations_spring_hidden_hotspring2 = region_locations("spring_hidden_hotspring2")
    locations_spring_hidden_hotspring3 = region_locations("spring_hidden_hotspring3")
    locations_spring_hidden_hotspring4 = region_locations("spring_hidden_hotspring4")
    locations_spring_jailhouse_japes0 = region_locations("spring_jailhouse_japes0")
    locations_spring_shoddy_shanty0 = region_locations("spring_shoddy_shanty0")
    locations_spring_shoddy_shanty1 = region_locations("spring_shoddy_shanty1")
    locations_spring_shoddy_shanty2 = region_locations("spring_shoddy_shanty2")
    locations_spring_shoddy_shanty3 = region_locations("spring_shoddy_shanty3")
    locations_spring_sleek_slabs0 = region_locations("spring_sleek_slabs0")
    locations_spring_sleek_slabs1 = region_locations("spring_sleek_slabs1")
    locations_spring_sleek_slabs2 = region_locations("spring_sleek_slabs2")
    locations_spring_sleek_slabs3 = region_locations("spring_sleek_slabs3")
    locations_spring_sleek_slabs4 = region_locations("spring_sleek_slabs4")
    locations_spring_sleek_slabs5 = region_locations("spring_sleek_slabs5")
    locations_spring_tiny_broad0 = region_locations("spring_tiny_broad0")
    locations_spring_tiny_broad1 = region_locations("spring_tiny_broad1")
    locations_spring_tiny_broad2 = region_locations("spring_tiny_broad2")
    locations_spring_tiny_broad3 = region_locations("spring_tiny_broad3")
    locations_spring_tiny_broad4 = region_locations("spring_tiny_broad4")
    locations_spring_tiny_broad5 = region_locations("spring_tiny_broad5")
    locations_spring_tiny_broad6 = region_locations("spring_tiny_broad6")
    locations_spring_tortoise_tunnel0 = region_locations("spring_tortoise_tunnel0")
    locations_spring_yokos_yam0 = region_locations("spring_yokos_yam0")
    locations_spring_yokos_yam1 = region_locations("spring_yokos_yam1")
    locations_spring_yokos_yam2 = region_locations("spring_yokos_yam2")
