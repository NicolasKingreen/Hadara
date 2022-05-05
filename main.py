# system imports
import random

# constants
from epochs import *
from card_types import *
from player_icons import *

# classes
from collection import Collection
from player import Player

# initializing game
collection = Collection()
circle = [INCOME, MILITARY, CULTURE, FOOD]
epochs = [EPOCH1, EPOCH2, EPOCH3]
unused_icons = [SCARAB, MONKEY, PEGASUS, DRAGON, LION]

unused_setup_cards = []
for a, b in zip(collection.setup_cards["A"], collection.setup_cards["B"]):
    unused_setup_cards.append(a)  # only beginner setup cards !!!

print("Welcome to Hadara!")
players_count = int(input("Input the amount of players (2-5): "))

players = []
for _ in range(players_count):
    icon = random.choice(unused_icons)
    setup_card = random.choice(unused_setup_cards)
    new_player = Player(icon, setup_card)
    players.append(new_player)
    unused_icons.remove(icon)
    unused_setup_cards.remove(setup_card)

players.sort(key=lambda player: player.initiative_value)

current_epoch_n = 0
current_epoch = epochs[current_epoch_n]

game_finished = False
while not game_finished:
    print(current_epoch, "begins!")
    # ask starting player for wheel position
    start_pos = int(input(f"""
        {players[current_epoch_n].icon}, choose where to start:
        1. Income
        2. Military
        3. Culture
        4. Food
        5. Technical
        """)) - 1

    # phase A
    # while not at start
    #   ask every player for turn (takes 2 current type cards and decide to buy one on these or sell)
    for segment in range(len(circle)):
        for i, player in enumerate(players):
            print(player, "makes his move.")
            current_type_n = start_pos + i
            current_type = circle[current_type_n % len(circle)]
            choices = random.sample(collection.cards[current_epoch][current_type], 2)
            print(f"{player.icon} ({current_type}), choose (1 or 2):")
            print(choices)
            choice = int(input()) - 1
            chosen_card = choices[choice]
            choices.remove(chosen_card)
            remaining_card = choices[0]
            # collection.remove_card(remaining_card)  # implement card removal
            player.add_card(chosen_card)

    # pay coins
    # make sculptures
    # fight colonies
    print("Phase A ends. Players get  income. Time to fight a colony and make a sculpture.")

    # phase B
    # while cards on the table
    #   ask every player sorted by their initiative value to choose remaining card type and then ask for their decision

    # pay coins
    # make sculptures
    # fight colonies
    # if enough food

    # next epoch, starting player is the next by initiative value
    current_epoch_n += 1
    current_epoch = epochs[current_epoch_n]

