# Yoku's Island Adventure Randomizer Setup Guide

## Required Software

- Yoku's Island Adventure, from:
    - [GOG.com](https://www.gog.com/en/game/yokus_island_express), or
    - [Steam](https://store.steampowered.com/app/334940/Yokus_Island_Express/)
- The [Yoku's Island Express randomizer](https://git.makuluni.com/archipelago/YokusIslandAdventure_randomizer/)

## Optional Software
 
- For sending [commands](/tutorial/Archipelago/commands/en) like `!hint`: the TextClient from [the most recent Archipelago release](https://github.com/ArchipelagoMW/Archipelago/releases)

## Installation

You need to put `amwr_x102.sim` into the game "processed/items" subdirectory of the game folder.

Put `yam.exe` and `yamlib.dll` into the game folder (this is the easiest way to run, and the instructions assume that's what you did, but if you prefer not to you can install them anywhere you like. Run `yam.exe /Help` for more info)

If you are on linux and using steam, you should also put `yam-proton.sh` into the game folder.

## Launching
Launching the game depends on your platform and the version you are using:

### GOG
You can launch the game from the command line:
```bash
yam.exe /Gog Yoku.exe
```
Make sure you are in the game folder (or that you adjust the paths otherwise).

On linux, simply run it with wine:
```bash
wine yam.exe /Gog Yoku.exe
```
If you aren't running this from the game folder, make sure you use the windows path for `Yoku.exe`.

### Steam
Right click the game name in your library and select "Properties…"

Under "LAUNCH OPTIONS" enter:
```bash
yam.exe /Steam %command%
```
or, on linux:
```bash
yam-proton.sh %command%
```

## Opening a game and connecting to a server.
When you launch the mod, you will be asked if you want to load an `.apyoku` file. You should have gotten that from your host. Say `Yes`, direct the game to the `.apyoku` file, and don't forget to edit the server/password information in the file select dialog. You can also choose which save slot the game will use for your run.

Once you have loaded the file this way once, you should no longer need to worry about loading it again; the world will be in the same save slot you chose when you loaded it and it will remember the serve/password you selected.
