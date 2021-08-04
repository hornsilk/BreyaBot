# BreyaBot, a basic battle bot for MTGA

![Breya](https://i.imgur.com/7ienKLP.png)

Directly inspired by Reddit user /u/lawrieee's [post](https://www.reddit.com/r/MagicArena/comments/otykvn/i_played_cards_left_to_right_for_652_games_in/) where they only played their leftmost card, making no decisions, and eventually hit mythic. This bot is a quick and incredibly messy implementation of just that strategy, playing their same deck left to right over and over.

![Gameplay Gif](./BreyaBot.gif)

## Our Progress to Mythic

Follow BreyaBot at our [untapped.gg page](https://mtga.untapped.gg/profile/7c67700d-e46a-46c0-b01a-16eae4d8ea55/ORTRAKF7FVBM7O3ASROZHCG2HQ/deck/51f5a152-6b40-47cd-85ff-f5fcdece5b4c?timeFrame=current_season&gameType=constructed&constructedType=ranked) or friend her at `BreyaBot#37727` on MTGA. We're not doing friend battles just yet.

## The Code

Is a Royal Mess which I wrote in a single day. Locations are based on hardcoded values from my 1920x1080 monitor, identifying and grabbing playable cards is a little buggy, and the game loop is a little slower than I'd want. Feel free to run the code but do so knowing you'll have to get your hands dirty. 

`output_fxns.py` is for getting info out of the MTGA game window

`input_fxns.py` is for inputting commands to MTGA

`click.ahk` gives us mouse support through [AutoHotkey](https://www.autohotkey.com/), getting past anti-hack code in MTGA, and must be running

`main.py` is the main game loop. Must be set up with the correct deck (`decklist.txt`) and play mode (Historic Ranked)

## Development

Immediate areas for improvement are using a better image recognition algorithm and add a text recognition module, as currently gamestate is found by pattern matching specific elements of the MTGA GUI.

Long-term areas for improvement are somehow running the screen captures through a MTG client like [CardBoard Live](https://cardboard.live/), letting BreyaBot recognize individual cards and opening the door for more advanced AI.
