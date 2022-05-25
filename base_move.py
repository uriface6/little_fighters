from abc import ABC, abstractmethod

import auxiliary_functions
from typing import List

# from player import Player
# from game_state import GameState
from constant import MoveType


class BaseMove(ABC):
    def __init__(self, name: str, move_type: MoveType):
        self.name = name
        self.move_type = move_type
        self.parameters: List["Player"] = []

    def choose_move(self, my_game_state: "GameState"):
        # self.parameters.clear()
        match self.move_type:
            case MoveType.SINGLE_MOVE:
                pass

            case MoveType.DUEL_MOVE:
                self.get_victim_player(my_game_state)

            case MoveType.WITHOUT_ME_MOVE:
                self.parameters = []
                for curr_player in my_game_state.players:
                    if curr_player is not my_game_state.curr_player:
                        self.parameters.append(curr_player)

            case MoveType.GENERAL_MOVE:
                self.parameters = my_game_state.players


    @abstractmethod
    def play_move(self, my_game_state: "GameState"):
        pass

    def get_victim_player(self, my_game_state: "GameState"):
        user_choice = -1
        print("who do you want to attack?")
        index = 1
        attacker_index = 0
        for curr_player in my_game_state.players:
            if curr_player is not my_game_state.curr_player:
                print(f"{index}. {curr_player.name}")
                index += 1
            else:
                attacker_index = index

        user_choice = auxiliary_functions.get_user_int_choice(1, index - 1)
        if user_choice >= attacker_index:
            user_choice += 1

        self.parameters = [my_game_state.players[user_choice - 1]]
