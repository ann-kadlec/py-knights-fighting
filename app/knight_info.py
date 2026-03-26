class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        if armour is None:
            armour = []
        self.armour = armour
        self.potion = potion
        self.protection = 0
