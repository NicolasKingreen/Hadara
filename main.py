from epochs import *
from card_types import *

from player import Player


print("Welcome to Hadara!")
players_count = int(input("Input the amount of players (2-5): "))

players = []
for _ in range(players_count):
    new_player = Player("setup card :)")

starting_player = min(players, key=lambda player: player.setup_card.initiative_value)

current_epoch = EPOCH1

game_finished = False
while not game_finished:
    # ask starting player for wheel position
    start_pos = int(input(f"""
        {starting_player.fraction}, choose where to start:
        1. Income
        2. Military
        3. Culture
        4. Food
        5. Technical
        """)) - 1

    # phase A
    # while not at start
    #   ask every player for turn (takes 2 current type cards and decide to buy one on these or sell)

    # pay coins
    # make sculptures
    # fight colonies

    # phase B
    # while cards on the table
    #   ask every player sorted by their initiative value to choose remaining card type and then ask for their decision

    # pay coins
    # make sculptures
    # fight colonies
    # if enough food

    # next epoch, starting player is the next by initiative value

