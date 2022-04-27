import auxiliary_functions
from base_fighter import BaseFighter
# from game_state import GameState
from base_move import BaseMove


class Player:
    def __init__(self, name: str, fighter: BaseFighter):
        self.name = name
        self.fighter = fighter

    def __str__(self):
        str_to_print = f"Name: {self.name} ,"
        str_to_print += self.fighter.__str__()
        return str_to_print

    def choose_move(self, my_game_state: "GameState") -> BaseMove:
        print("choose your move:")
        end_index = 0
        for index, curr_optional_move in enumerate(self.fighter.optional_moves, 1):
            print(f"{index}. {curr_optional_move.name}")
            end_index = index
        print()

        user_choice = auxiliary_functions.get_user_int_choice(1, end_index)
        chosen_move = self.fighter.optional_moves[user_choice - 1]
        chosen_move.choose_move(my_game_state)
        return chosen_move

