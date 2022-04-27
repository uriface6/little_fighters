import inspect
import constant
import random
import copy

from base_fighter import BaseFighter
from player import Player
from moves import Move

from fighters.field_barvaz import FieldBarvaz
from fighters.haim import Haim
from fighters.Lital import Lital
from fighters.rahamim import Rahamim

from typing import Dict, Union, Tuple, List


class GameManager:

    def __init__(self):
        # self.fighters_dict = constant.FIGHTERS_DICT
        self.fighters_dict: Dict[str, BaseFighter] = {}
        self.load_fighters()
        # self.moves_dict = constant.MOVES_DICT
        self.players_dict: Dict[str, Player] = {}
        # self.moves_list: List[Union[Tuple[any, Player], Tuple[any, Player, Player]]] = []
        self.moves_list: List[Move] = []

    def game_manager(self):
        # self.enter_menu()
        self.init_test_game()
        # self.rand_players()

        while len(self.players_dict) > 1:
            self.round()
            self.end_round()
        print(f"{list(self.players_dict.keys())[0]} is the Winner!!!!!!!! heydad!!!")

#
#

    def load_fighters(self):
        fighters_dict_temp: Dict[str, BaseFighter] = {
            "Field Barvaz": FieldBarvaz(),
            "Haim": Haim(),
            "Lital": Lital(),
            "Rahamim": Rahamim()
        }
        self.fighters_dict = fighters_dict_temp

    def enter_menu(self):
        print("Welcome to Little Fighter!!")
        print("How much players do you play?")
        players_num = GameManager.get_user_int_choice(constant.MIN_PLAYERS, constant.MAX_PLAYERS)
        for i in range(players_num):
            print(f"\nwelcome player {i+1}")
            players_name = input("enter your name: ")
            self.players_dict[players_name] = Player(players_name, self.create_player())  # append(self.create_player())

        self.print_players()

    def create_player(self) -> BaseFighter:
        # players_name = input("enter your name: ")
        print("choose your fighter")
        for counter, fighter in enumerate(self.fighters_dict.keys()):
            hp, stamina, strength = self.fighters_dict[fighter]
            print(f"{counter + 1}. {fighter}: Hp - {hp}, Stamina - {stamina}, Strength - {strength}")
        fighter_choice = GameManager.get_user_int_choice(1, len(self.fighters_dict.keys()))
        fighter_choice_name = list(self.fighters_dict.keys())[fighter_choice - 1]
        # temp_fighter = BaseFighter(*self.fighters_dict[fighter_choice_name], fighter_name=fighter_choice_name)
        # return temp_fighter  # Player(players_name, temp_fighter)
        # return self.fighters_dict[fighter_choice_name]
        return copy.deepcopy(self.fighters_dict[fighter_choice_name])

    def rand_players(self):
        temp_list = list(self.players_dict.items())
        random.shuffle(temp_list)
        self.players_dict = {k: v for k, v in temp_list}

        self.print_players()

    def round(self):
        for curr_player in self.players_dict.values():
            print(f"It's {curr_player.name} turn:")
            self.move_menu(curr_player)

        for curr_move in self.moves_list:
            curr_move.do_move()

    def move_menu(self, curr_player: Player):
        print("choose your move:")
        index = 1
        method_list = []
        for name, method in inspect.getmembers(curr_player.fighter, predicate=inspect.ismethod):
            if name.startswith('_'):
                continue
            if name == "special_move":
                if inspect.getcomments(method) is not None:
                    print(f"{index}. {inspect.getcomments(method)[2:]}")
                    index += 1
            else:
                print(f"{index}. {name}")
                index += 1

            method_list.append((method, len(inspect.getfullargspec(method)[-1])))

        user_choice = self.get_user_int_choice(1, index - 1)
        chosen_method, parameters_num = method_list[user_choice - 1]
        if parameters_num == 1:
            victim_player = self.get_victim_player(curr_player)
            # self.moves_list.append((chosen_method, [curr_player, victim_player]))
            self.moves_list.append(Move(chosen_method, [victim_player]))
        else:
            self.moves_list = [Move(chosen_method, [])] + self.moves_list
        print()

    def end_round(self):
        print("\nbefore end : ")
        self.print_players()

        dead_list = []
        for player_name, curr_player in self.players_dict.items():
            if curr_player.fighter.hp <= 0:
                dead_list.append(player_name)
                print(f"{player_name} is dad, Bye bye!!!")
            else:
                curr_player.fighter.safe = False
                curr_player.fighter.stamina += 1
                curr_player.fighter.strength += 1
                curr_player.fighter.hp += (curr_player.fighter.stamina * 0.75)
        first_player_name = list(self.players_dict.keys())[0]
        temp_player = self.players_dict.pop(first_player_name)
        self.players_dict[first_player_name] = temp_player

        for curr_dead in dead_list:
            self.players_dict.pop(curr_dead)

        print("after end: ")
        self.print_players()
        self.moves_list.clear()

    def print_players(self):
        for curr_player in self.players_dict.values():
            print(curr_player)
        print()

    def get_players_dict(self) -> Dict[str, Player]:
        return self.players_dict

    def get_victim_player(self, attecker_player: Player) -> Player:
        user_choice = -1
        print("\nwho do you want to attack?")
        index = 1
        attecker_index = 0
        for curr_player in self.players_dict.values():
            if curr_player is not attecker_player:
                print(f"{index}. {curr_player.name}")
                index += 1
            else:
                attecker_index = index

        user_choice = self.get_user_int_choice(1, index - 1)
        if user_choice >= attecker_index:
            user_choice += 1
        return list(self.players_dict.values())[user_choice - 1]

    def init_test_game(self):
        self.players_dict = {
            "Uri": Player("Uri", Rahamim()),
            "Salay": Player("Salay", Haim()),
            "Tal": Player("Tal", FieldBarvaz()),
            "Roee": Player("Roee", Lital()),
        }

        self.print_players()

    @staticmethod
    def get_user_int_choice(min: int, max: int) -> int:
        # user_choice_str = ""
        user_choice_int = min - 1
        while min > user_choice_int or max < user_choice_int:
            user_choice_str = input(f"enter number between {min} to {max}: ")
            try:
                user_choice_int = int(user_choice_str)
            except ValueError:
                print("Enter valid number!")
        return user_choice_int
