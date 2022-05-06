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

dropped_cards = {
    INCOME: [],
    MILITARY: [],
    CULTURE: [],
    FOOD: []
}

unused_icons = [SCARAB, MONKEY, PEGASUS, DRAGON, LION]
unused_setup_cards = []
for a, b in zip(collection.setup_cards["A"], collection.setup_cards["B"]):
    unused_setup_cards.append(a)
    unused_setup_cards.append(b)

print("Welcome to Hadara!")
players_count = int(input("Input the amount of players (2-5): "))

players = []
for _ in range(players_count):
    icon = random.choice(unused_icons)
    setup_card = random.choice(unused_setup_cards)

    # let players choose which side of setup cards to pick
    #setup_card_i = random.randint(0, len(unused_setup_cards) // 2 - 1) * 2
    #print(f"{icon}, choose your setup card (1 or 2):")
    #print(unused_setup_cards[setup_card_i], unused_setup_cards[setup_card_i+1])
    #setup_card = unused_setup_cards[setup_card_i + int(input()) - 1]

    new_player = Player(icon, setup_card)
    players.append(new_player)
    unused_icons.remove(icon)
    unused_setup_cards.remove(setup_card)
players.sort(key=lambda player: player.initiative_value)

collection.set_for_n_players(players_count)  # removes excessive cards

current_epoch_n = 0
current_epoch = epochs[current_epoch_n]

game_finished = False
while not game_finished:
    print(current_epoch, "begins!")
    # ask starting player for wheel position
    print(f"{players[current_epoch_n].icon}, choose where to start:\n"
          f"1.Income\n2. Military\n3. Culture\n4. Food\n5. Technical")
    start_pos = int(input()) - 1

    # phase A
    # while not at start
    #   ask every player for turn (takes 2 current type cards and decide to buy one on these or sell)
    for _ in range(len(circle)):
        for i, player in enumerate(players[current_epoch_n:]):  # potential bug
            print(player, "makes his move.")
            current_type_n = start_pos + i
            current_type = circle[current_type_n % len(circle)]
            choices = random.sample(collection.cards[current_epoch][current_type], 2)
            print(f"{player.icon} ({current_type}), choose (1 or 2):")
            print(choices)
            choice = int(input()) - 1
            chosen_card = choices[choice]
            print(f"{chosen_card}")
            if input("Buy or sell? ") == "buy":
                player.add_card(chosen_card)
            else:
                player.coins += (current_epoch_n + 1)
            choices.remove(chosen_card)
            remaining_card = choices[0]
            dropped_cards[current_type].append(remaining_card)

            collection.remove_card(remaining_card)
            collection.remove_card(chosen_card)
        start_pos += 1

    print("Phase A ends. Players get  income. Time to fight a colony and make a sculpture.")
    # pay coins
    for player in players:
        player.get_income()
    # fight colonies
    for player in players:
        pass  # check if can fight a colony
    # make sculptures
    for player in players:
        pass  # check if can make a sculpture

    # phase B
    # while cards on the table
    #   ask every player sorted by their initiative value to choose remaining card type and then ask for their decision
    while not any(value for value in dropped_cards.values()):
        for player in players:
            print(f"{player.icon}, you can pick a card. There are: ")
            for i, card_type in enumerate(dropped_cards):
                print(f"{i}. {len(dropped_cards[card_type])} {card_type} card(s).")
            choice = int(input()) - 1
            chosen_type = circle[choice]
            chosen_card = dropped_cards[chosen_type].pop()
            print(f"{chosen_card}")
            if input("Buy or sell? ") == "buy":
                player.add_card(chosen_card)
            else:
                player.coins += (current_epoch_n + 1)

            dropped_cards[chosen_type].remove(chosen_card)

    # pay coins
    for player in players:
        player.get_income()

    # fight colonies
    for player in players:
        pass
    # make sculptures
    for player in players:
        pass
    # if enough food
    for player in players:
        player.has_enough_food()

    # next epoch, starting player is the next by initiative value
    current_epoch_n += 1
    current_epoch = epochs[current_epoch_n]

