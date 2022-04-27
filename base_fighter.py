from abc import ABC, abstractmethod
from typing import List

from base_move import BaseMove
from all_moves.attack import Attack
from all_moves.defense import Defense
from all_moves.kamikaza import Kamikaza


class BaseFighter(ABC):

    def __init__(self, hp: int, stamina: int, strength: int, fighter_name: str):
        self.hp = hp
        self.stamina = stamina
        self.strength = strength
        self.fighter_name = fighter_name
        self.safe = False
        self.optional_moves: List[BaseMove] = [Attack(), Defense(), Kamikaza()]
        self.add_special_move()

    def __str__(self):
        str_to_print = f"Hp - {self.hp}, Stamina - {self.stamina}, Strength - {self.strength}," \
                       f"Safe - {self.safe}, Fighter name - {self.fighter_name}"
        return str_to_print

    @abstractmethod
    def add_special_move(self):
        pass

    # def kamikaza(self, victim: "Player"):
    #     print(f"Kamikaza against {victim.name}!!!!!")
    #     cube1 = random.randint(1, 6)
    #     cube2 = random.randint(1, 6)
    #     print(f"cube1 = {cube1}, cube2 = {cube2}")
    #     match (cube1, cube2):
    #         case 2, 2:
    #             if victim.fighter.safe:
    #                 print(f"Kamikaza faild, {victim.name} is safe")
    #                 victim.fighter.safe = False
    #                 self.attack(victim)
    #
    #             else:
    #                 print(f"{victim.name} is dad!")
    #                 victim.fighter.hp = 0
    #         case (1, _) | (_, 1):
    #             print("suicide!!!")
    #             self.hp = 0
    #             print(self)
    #         case _:
    #             damage = ((cube1 + cube2) * 2 * self.strength) - victim.fighter.stamina
    #             print(f"damage = {damage}")
    #
    #             print("victim before attack:")
    #             print(victim)
    #             if damage > 0:
    #                 victim.fighter.hp -= damage
    #
    #             print("victim before attack:")
    #             print(victim)
    #
    # def attack(self, victim: "Player"):
    #     print(f"attack against {victim.name}!!!!!")
    #     if victim.fighter.safe:
    #         print(f"Attack faild, {victim.name} is safe")
    #     else:
    #         cube = random.randint(1, 6)
    #         print(f"cube = {cube}")
    #         damage = (cube * self.strength) - victim.fighter.stamina
    #         print(f"damage = {damage}")
    #
    #         print("victim before attack:")
    #         print(victim)
    #         if damage > 0:
    #             victim. fighter.hp -= damage
    #
    #         print("victim before attack:")
    #         print(victim)
    #
    # def defense(self):
    #     self.safe = True
    #
    # @abstractmethod
    # def special_move(self):
    #     """i am base_fighter attack"""
    #     pass



