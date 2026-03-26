from app.knight_info import Weapon, Knight
from app.preparation import apply_armour, apply_weapon, apply_potion
from app.battle import fight


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_dict: dict) -> dict:
    list_of_knights = []
    for key, value in knights_dict.items():
        weapon_ = Weapon(value["weapon"]["name"], value["weapon"]["power"])
        knight = Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            weapon=weapon_,
            armour=value["armour"],
            potion=value["potion"]
        )
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
        list_of_knights.append(knight)

    lancelot = None
    arthur = None
    mordred = None
    red_knight = None
    for knight in list_of_knights:
        if knight.name == "Lancelot":
            lancelot = knight
        elif knight.name == "Arthur":
            arthur = knight
        elif knight.name == "Mordred":
            mordred = knight
        elif knight.name == "Red Knight":
            red_knight = knight

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    results = {}
    for knight in list_of_knights:
        results[knight.name] = knight.hp
    return results
