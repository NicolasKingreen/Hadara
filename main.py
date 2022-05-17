# system imports
import random

# constants
from epochs import *
from card_types import *
from player_icons import *
from colony_types import *
from enums import *
import structure_types

# utilities
from utility import *

# classes
from collection import Collection
from player import Player
from statue import Statue

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


def fight_colony(player):
    # utility tables
    cost = {
        3: {
            'join': 1,
            'rob': 3
        },
        9: {
            'join': 1,
            'rob': 4
        },
        15: {
            'join': 2,
            'rob': 5
        },
        21: {
            'join': 2,
            'rob': 7
        },
        30: {
            'join': 4,
            'rob': 12
        }
    }
    colony_type_to_strength = {
        VERY_EASY: 3,
        EASY: 9,
        MEDIUM: 15,
        HARD: 21,
        VERY_HARD: 30
    }

    # TODO: make player choose between available colonies types

    # initialize max strength of player colonies if they exist
    max_strength = max([colony.strength for colony in player.colonies]) if len(player.colonies) else -1

    # allows to chose colonies that doesn't exist in player stash
    accessible_strength = -1
    for strength in collection.colonies:
        if max_strength < colony_type_to_strength[strength] <= player.track_values[MILITARY]:
            accessible_strength = colony_type_to_strength[strength]
            break

    if accessible_strength != -1:
        colony_type = get_key_from_value(colony_type_to_strength, accessible_strength)
        if collection.colonies[colony_type]:
            print(player)
            print(f"You can take or rob a colony with strength {accessible_strength}. "
                  f"It will cost {cost[accessible_strength]['join']} coins "
                  f"while robbing will give you {cost[accessible_strength]['rob']}. "
                  f"Number of colonies: {len(collection.colonies[colony_type])}")
            action = input("Chose what you want to do? (join or rob): ").lower()

        # choose random colony
        random_colony = random.choice(collection.colonies[colony_type])
        if action == 'join':

            # check if enough coins
            if player.coins > cost[random_colony.strength][action]:
                player.coins -= cost[accessible_strength][action]
                player.add_colony(random_colony)
                collection.colonies[colony_type].remove(random_colony)
            else:
                print(f"[Main] Player has not enough money")
        elif action == 'rob':
            # TODO: fix bug when player robs colonies, he can rob them again
            collection.colonies[colony_type].remove(random_colony)
            player.coins += cost[accessible_strength][action]
    else:
        print(f"{player.icon}, sorry, you can't take or rob any colonies.")


def build_statue(player):

    # rec available statue to build
    available_statues = []
    for statue in collection.statues.values():
        if statue.culture <= player.track_values[CULTURE]\
                and statue.culture not in [st.culture for st in player.statues]:
            available_statues.append(statue)

    if available_statues:
        print(player)
        print(f"You can make {len(available_statues)} statues.")
        main_action = input("Do you want to make a statue? (Y/[n]) ").lower()
        if main_action == 'y':
            statue_choice = 0
            if len(available_statues) > 1:
                for i, statue in enumerate(available_statues):
                    print(f"{i+1}. {statue}")
                statue_choice = int(input(f"Chose one (1-{len(available_statues)}): ")) - 1
            selected_statue = available_statues[statue_choice]
            print(f"You are going to build a statue "
                  f"that gives {selected_statue.counter} "
                  f"to the specified bonus value.")
            print("1. Income")
            print("2. Military")
            print("3. Culture")
            print("4. Food")
            print("5. Victory points")
            bonus_choice = int(input(f"Select bonus type: ")) - 1
            selected_bonus = None
            if bonus_choice == 0:
                selected_bonus = INCOME
            elif bonus_choice == 1:
                selected_bonus = MILITARY
            elif bonus_choice == 2:
                selected_bonus = CULTURE
            elif bonus_choice == 3:
                selected_bonus = FOOD
            # TODO: fix this mess with 'copying' statue from collection
            new_statue = Statue(selected_statue.culture,
                                selected_statue.counter,
                                selected_statue.victory_points,
                                selected_bonus)
            player.add_statue(new_statue)
    else:
        print(f"{player.icon}, you can't build any statues yet.")


print_centered("Welcome to Hadara!")
print_centered("Input the amount of players (2-5).")
players_count = int(input("[GameManager] > "))

players = []
for i in range(players_count):
    print_centered("Available icons: ")
    print_choices(unused_icons)
    icon = unused_icons[int(input(f"Player {i + 1} > ")) - 1]
    setup_card = random.choice(unused_setup_cards)

    # let players choose which side of setup cards to pick
    # setup_card_i = random.randint(0, len(unused_setup_cards) // 2 - 1) * 2
    # print(setup_card_i)
    # print(f"{icon}, choose your setup card (1 or 2):")
    # print(unused_setup_cards[setup_card_i], unused_setup_cards[setup_card_i+1])
    # setup_card = unused_setup_cards[setup_card_i + int(input()) - 1]

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
    print()
    print_centered(f' {current_epoch}, begins! ', filler='*')
    print()

    # ask starting player for wheel position
    print_centered(f"{players[0].icon} has the lowest initiative value.")
    print_centered("He chooses where to start.")
    print_choices(circle)
    start_pos = int(input(f'{players[0].icon} > ')) - 1

    # phase A
    # while not at start
    #   ask every player for turn (takes 2 current type cards and decide to buy one on these or sell)
    for _ in circle:
        for i, player in enumerate(players):
            print(player)
            current_type = circle[(start_pos + i) % len(circle)]
            choices = random.sample(collection.cards[current_epoch][current_type], 2)
            print_centered(f"You are on {current_type}.")
            print_centered("Now you have to choose between two cards of the current type.")
            print_centered("One of them will be available for you to buy or sell.")
            print_centered("The other one will be discarded back to the game.")
            print_choices(choices)
            print_centered("Choose card to buy/sell (1 or 2).")
            choice = int(input(f'{player.icon} > ')) - 1
            chosen_card = choices[choice]

            print_centered("You have to decide to buy it or sell.")
            print_centered("* Cards that you sell are completely discarded from the game.")
            decision = input(f'{player.icon} > ').lower()
            if decision == "buy":
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
        fight_colony(player)
    # make sculptures
    for player in players:
        build_statue(player)

    # phase B
    # TODO: Fix phase B
    # while cards on the table
    #   ask every player sorted by their initiative value
    #   to choose remaining card type and then ask for their decision
    print("Phase B starts.")
    while any(value for value in dropped_cards.values()):
        for player in players:
            print(f"{player.icon}, you can pick a card. There are: ")
            for i, card_type in enumerate(dropped_cards):
                print(f"{i+1}. {len(dropped_cards[card_type])} {card_type} card(s).")
            choice = int(input()) - 1
            chosen_type = circle[choice]
            chosen_card = dropped_cards[chosen_type].pop()
            print(chosen_card)
            if input("Buy or sell? ") == "buy":
                player.add_card(chosen_card)
            else:
                player.coins += (current_epoch_n + 1)

    print("Phase B ends. Players get income. Time to fight a colony and make a sculpture.")
    # pay coins
    for player in players:
        player.get_income()

    # fight colonies
    for player in players:
        fight_colony(player)

    # make sculptures
    for player in players:
        build_statue(player)

    print("Checking if every player has sufficient food.")
    # if enough food
    for player in players:
        player.has_enough_food()

    # next epoch, starting player is the next by initiative value
    current_epoch_n += 1
    current_epoch = epochs[current_epoch_n]
    players = shift(players, 1)

print("Game is over. Thanks for playing!")
print("Results:")
players.sort(key=lambda player: player.get_score(), reverse=True)
for i, player in enumerate(players):
    print(f"{i + 1}. {player.icon} ({player.get_score()})")
