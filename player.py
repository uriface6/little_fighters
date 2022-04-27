from base_fighter import BaseFighter


class Player:
    def __init__(self, name: str, fighter: BaseFighter):
        self.name = name
        self.fighter = fighter

    def __str__(self):
        str_to_print = f"Name: {self.name} ,"
        str_to_print += self.fighter.__str__()
        return str_to_print
