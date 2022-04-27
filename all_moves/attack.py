# from game_state import GameState
from base_move import BaseMove
import constant
import random


class Attack(BaseMove):

    def __init__(self):
        super(Attack, self).__init__("Attack", constant.MoveType.DUEL_MOVE)

    def play_move(self, my_game_state: "GameState"):
        victim = self.parameters[0]
        print(f"{my_game_state.curr_player.name} attack {victim.name}")

        if victim.fighter.safe:
            print(f"Attack faild, {victim.name} is safe")
        else:
            cube = random.randint(1, 6)
            print(f"cube = {cube}")
            damage = (cube * my_game_state.curr_player.fighter.strength) - victim.fighter.stamina
            print(f"damage = {damage}")

            print("victim before attack:")
            print(victim)
            if damage > 0:
                victim.fighter.hp -= damage
                if victim.fighter.hp < 0:
                    victim.fighter.hp = 0

            print("victim after attack:")
            print(victim)
