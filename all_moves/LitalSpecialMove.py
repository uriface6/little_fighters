# from game_state import GameState
from base_move import BaseMove
import constant


class LitalSpecialMove(BaseMove):

    def __init__(self):
        super(LitalSpecialMove, self).__init__("boost strength", constant.MoveType.SINGLE_MOVE)

    def play_move(self, my_game_state: "GameState"):
        print(f"{my_game_state.curr_player.name} boost his strength")

        print("before move:")
        print(my_game_state.curr_player)
        my_game_state.curr_player.fighter.strength += 1
        print("after move:")
        print(my_game_state.curr_player)
