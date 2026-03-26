from app.knight_info import Knight


def fight(knight_1: Knight, knight_2: Knight) -> str:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection
    if knight_1.hp <= 0:
        knight_1.hp = 0
        print(f"{knight_2.name} won the battle!")
    if knight_2.hp <= 0:
        knight_2.hp = 0
        print(f"{knight_1.name} won the battle!")
    return (
        f"{knight_1.name} : {knight_1.hp}"
        f"{knight_2.name} : {knight_2.hp}"
    )
