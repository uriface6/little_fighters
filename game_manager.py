import constant

from end_game_exception import EndGameException
from game_state import GameState
from base_move import BaseMove
from player import Player

from fighters.field_barvaz import FieldBarvaz
from fighters.haim import Haim
from fighters.Lital import Lital
from fighters.rahamim import Rahamim

from typing import Dict, Union, Tuple, List


# am i brunch?
class GameManager:

    def __init__(self):
        # self.fighters_dict: Dict[str, BaseFighter] = {}
        # self.load_fighters()

        self.players_list: List[Player] = []

    def game_manager(self):
        # self.enter_menu()
        self.init_test_game()
        # self.rand_players()

        try:
            while len(self.players_list) > 1:
                self.round()
                self.end_round()
        except EndGameException:
            pass
        finally:
            match len(self.players_list):
                case 1:
                    print(f"{self.players_list[0].name} is the Winner!!!! heydad!!!")
                case 0:
                    print("Tye!!!!!!")
                case _:
                    print("End game error!!!!!!!")

#
#
    #
    # def load_fighters(self):
    #     fighters_dict_temp: Dict[str, BaseFighter] = {
    #         "Field Barvaz": FieldBarvaz(),
    #         "Haim": Haim(),
    #         "Lital": Lital(),
    #         "Rahamim": Rahamim()
    #     }
    #     self.fighters_dict = fighters_dict_temp
    #
    # def enter_menu(self):
    #     print("Welcome to Little Fighter!!")
    #     print("How much players do you play?")
    #     players_num = GameManager.get_user_int_choice(constant.MIN_PLAYERS, constant.MAX_PLAYERS)
    #     for i in range(players_num):
    #         print(f"\nwelcome player {i+1}")
    #         players_name = input("enter your name: ")
    #         self.players_list[players_name] = Player(players_name, self.create_player())  # append(self.create_player())
    #
    #     self.print_players()
    #
    # def create_player(self) -> BaseFighter:
    #     # players_name = input("enter your name: ")
    #     print("choose your fighter")
    #     for counter, fighter in enumerate(self.fighters_dict.keys()):
    #         hp, stamina, strength = self.fighters_dict[fighter]
    #         print(f"{counter + 1}. {fighter}: Hp - {hp}, Stamina - {stamina}, Strength - {strength}")
    #     fighter_choice = GameManager.get_user_int_choice(1, len(self.fighters_dict.keys()))
    #     fighter_choice_name = list(self.fighters_dict.keys())[fighter_choice - 1]
    #     # temp_fighter = BaseFighter(*self.fighters_dict[fighter_choice_name], fighter_name=fighter_choice_name)
    #     # return temp_fighter  # Player(players_name, temp_fighter)
    #     # return self.fighters_dict[fighter_choice_name]
    #     return copy.deepcopy(self.fighters_dict[fighter_choice_name])
    #
    # def rand_players(self):
    #     temp_list = list(self.players_list.items())
    #     random.shuffle(temp_list)
    #     self.players_list = {k: v for k, v in temp_list}
    #
    #     self.print_players()

    def round(self):
        round_moves: List[BaseMove] = []
        # !!!!!!!!!!!!!!! to-do
        round_players: List[Player] = []
        for curr_player in self.players_list:
            print(f"\nIt's {curr_player.name} turn:")
            my_game_state = GameState(self.players_list, curr_player)
            chosen_move = curr_player.choose_move(my_game_state)
            if chosen_move.move_type == constant.MoveType.SINGLE_MOVE:
                round_moves = [chosen_move] + round_moves
                round_players = [curr_player] + round_players
            else:
                round_moves.append(chosen_move)
                round_players.append(curr_player)

        for curr_move, curr_player1 in zip(round_moves, round_players):
            # !!!!!!!!!!!!! to-do
            my_game_state = GameState(self.players_list, curr_player1)
            curr_move.play_move(my_game_state)

    # def move_menu(self, curr_player: Player):
    #     print("choose your move:")
    #     index = 1
    #     method_list = []
    #     for name, method in inspect.getmembers(curr_player.fighter, predicate=inspect.ismethod):
    #         if name.startswith('_'):
    #             continue
    #         if name == "special_move":
    #             if inspect.getcomments(method) is not None:
    #                 print(f"{index}. {inspect.getcomments(method)[2:]}")
    #                 index += 1
    #         else:
    #             print(f"{index}. {name}")
    #             index += 1
    #
    #         method_list.append((method, len(inspect.getfullargspec(method)[-1])))
    #
    #     user_choice = self.get_user_int_choice(1, index - 1)
    #     chosen_method, parameters_num = method_list[user_choice - 1]
    #     if parameters_num == 1:
    #         victim_player = self.get_victim_player(curr_player)
    #         # self.moves_list.append((chosen_method, [curr_player, victim_player]))
    #         self.moves_list.append(Move1(chosen_method, [victim_player]))
    #     else:
    #         self.moves_list = [Move1(chosen_method, [])] + self.moves_list
    #     print()

    def end_round(self):
        print("\nbefore end : ")
        self.print_players()

        dead_list = []
        for curr_player in self.players_list:
            if curr_player.fighter.hp <= 0:
                dead_list.append(curr_player)
                print(f"{curr_player.name} is dad, Bye bye!!!")
            else:
                curr_player.fighter.safe = False
                curr_player.fighter.stamina += 1
                curr_player.fighter.strength += 1
                curr_player.fighter.hp += (curr_player.fighter.stamina * 0.75)
        first_player_name = self.players_list[0]
        temp_player = self.players_list.pop(0)
        self.players_list.append(temp_player)

        for curr_dead in dead_list:
            self.players_list.remove(curr_dead)

        print("after end: ")
        self.print_players()

    def print_players(self):
        for curr_player in self.players_list:
            print(curr_player)
        print()

    # def get_players_dict(self) -> Dict[str, Player]:
    #    return self.players_list

    # def get_victim_player(self, attecker_player: Player) -> Player:
    #     user_choice = -1
    #     print("\nwho do you want to attack?")
    #     index = 1
    #     attecker_index = 0
    #     for curr_player in self.players_list.values():
    #         if curr_player is not attecker_player:
    #             print(f"{index}. {curr_player.name}")
    #             index += 1
    #         else:
    #             attecker_index = index
    #
    #     user_choice = self.get_user_int_choice(1, index - 1)
    #     if user_choice >= attecker_index:
    #         user_choice += 1
    #     return list(self.players_list.values())[user_choice - 1]

    def init_test_game(self):
        self.players_list = [Player("Uri", Rahamim()), Player("Salay", Haim()),
                             Player("Tal", FieldBarvaz()), Player("Roee", Lital())]
        self.print_players()

