from all_moves.pikatzu_special_move import PikatzuSpecialMove
from base_fighter import BaseFighter
import constant


class Pikatzu(BaseFighter):
    def __init__(self):
        super(Pikatzu, self).__init__(constant.PIKATZU_HP, constant.PIKATZU_STAMINA, constant.PIKATZU_STRENGTH, "Pikatzu")

    def add_special_move(self):
        self.optional_moves.append(PikatzuSpecialMove())
