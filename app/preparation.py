from app.knight_info import Knight


def apply_armour(knight: Knight) -> Knight:
    if knight.armour:
        for obj in knight.armour:
            knight.protection += obj["protection"]
    return knight


def apply_weapon(knight: Knight) -> Knight:
    knight.power += knight.weapon.power
    return knight


def apply_potion(knight: Knight) -> Knight:
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]
        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]
        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]
    return knight
