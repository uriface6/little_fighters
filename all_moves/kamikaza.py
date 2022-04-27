# from game_state import GameState
from base_move import BaseMove
import constant
import random


class Kamikaza(BaseMove):

    def __init__(self):
        super(Kamikaza, self).__init__("Kamikaza", constant.MoveType.DUEL_MOVE)

    def play_move(self, my_game_state: "GameState"):
        victim = self.parameters[0]
        attacker = my_game_state.curr_player.fighter
        print(f"{my_game_state.curr_player.name} do kamikaza vs {victim.name}")

        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        print(f"cube1 = {cube1}, cube2 = {cube2}")
        match (cube1, cube2):
            case 2, 2:
                if victim.fighter.safe:
                    print(f"Kamikaza faild, {victim.name} is safe")
                    victim.fighter.safe = False
                    # !!!!!!!!!!!!!!!!!!
                    print("Check this!!!!!!!")
                    attacker.optional_moves[0].play_move(my_game_state)


                else:
                    print(f"{victim.name} is dad!")
                    victim.fighter.hp = 0

            case (1, _) | (_, 1):
                print(f"{my_game_state.curr_player.name} commit suicide!!!")
                attacker.hp = 0
                print(my_game_state.curr_player)
            case _:
                damage = ((cube1 + cube2) * 2 * attacker.strength) - victim.fighter.stamina
                print(f"damage = {damage}")

                print("victim before attack:")
                print(victim)
                if damage > 0:
                    victim.fighter.hp -= damage
                    if victim.fighter.hp < 0:
                        victim.fighter.hp = 0

                print("victim after attack:")
                print(victim)
