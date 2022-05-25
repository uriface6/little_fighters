# from game_state import GameState
import random

from base_move import BaseMove
import constant


class FieldBarvazSpecialMove(BaseMove):

    def __init__(self):
        super(FieldBarvazSpecialMove, self).__init__("random dropping strength", constant.MoveType.GENERAL_MOVE)

    def play_move(self, my_game_state: "GameState"):
        print(f"{my_game_state.curr_player.name} random dropping strength")

        victim_index = random.randint(0, len(self.parameters) - 1)
        victim = self.parameters[victim_index]

        print("before move:")
        print(victim)
        victim.fighter.strength -= 1
        if victim.fighter.strength < 0:
            victim.fighter.strength = 0
        print("after move:")
        print(victim)
