# import game_manager
# import random
# from game_manager import GameManager
#
#
# # def attack(player_name: str, my_game_manager: GameManager):
# #     print("Choose who you want to attack:")
# #     player_dict = my_game_manager.get_players_dict()
# #     counter = 1
# #     for curr_player in my_game_manager.get_players_dict():
# #         if curr_player.name != player_name:
# #             print(f"{counter}. curr_player.name")
# #             counter += 1
# #     user_choice = game_manager.GameManager.get_user_int_choice(1, len(player_dict) + 1)
# #
# #     cube = random.randint(1, 6)
# #     print(f"cube = {cube}")
# #     damage = (cube * player_dict[player_name].fighter.strength) - player_dict[player_name].fighter.stamina
# #     print(f"damage = {damage}")
# #
#
# def base_attack(player_name: str, my_game_manager: GameManager) -> str:
#     print("Who you want to attack:")
#     player_dict = my_game_manager.get_players_dict()
#     counter = 1
#     temp = 1
#     for curr_player in my_game_manager.get_players_dict():
#         if curr_player.name != player_name:
#             print(f"{counter}. curr_player.name")
#             counter += 1
#         else:
#             temp = 0
#     user_choice = game_manager.GameManager.get_user_int_choice(1, len(player_dict) + 1)
#     return player_dict[player_dict.keys()[user_choice - temp]]
#
from typing import List


class Move:
    def __init__(self, my_move: any, parameters: List[any]):
        self.my_move = my_move
        self.parameters = parameters

    def do_move(self):
        self.my_move(*self.parameters)
