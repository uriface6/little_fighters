from all_moves.field_barvaz_special_move import FieldBarvazSpecialMove
from base_fighter import BaseFighter
import constant


class FieldBarvaz(BaseFighter):
    def __init__(self):
        super(FieldBarvaz, self).__init__(constant.FIELD_BARVAZ_HP, constant.FIELD_BARVAZ_STAMINA,
                                          constant.FIELD_BARVAZ_STRENGTH, "FieldBarvaz")

    def add_special_move(self):
        self.optional_moves.append(FieldBarvazSpecialMove())
