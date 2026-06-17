import random

player = {
    "name": "Hero",
    "hp": 100,
    "money": 50,
    "inventory": []
}

def forest(player):
    event = random.choice(["monster", "treasure", "nothing"])

    if event == "monster":
        damage = random.randint(5, 30)
        player["hp"] -= damage
        print(f"Монстр! Ты потерял {damage} HP")

    elif event == "treasure":
        gold = random.randint(10, 50)
        player["money"] += gold
        print(f"Ты нашел {gold} монет!")

    else:
        print("Ничего не произошло")

def shop(player):
    print("1. Зелье (+20 HP) - 20 монет")

    try:
        choice = int(input("Выбор: "))

        if choice == 1:
            if player["money"] >= 20:
                player["money"] -= 20
                player["hp"] += 20
                player["inventory"].append("Potion")
            else:
                print("Не хватает денег")

    except:
        print("Ошибка ввода")

def status(player):
    print("Имя:", player["name"])
    print("HP:", player["hp"])
    print("Деньги:", player["money"])
    print("Инвентарь:", player["inventory"])

def rest(player):
    player["hp"] += 10
    print("Ты отдохнул +10 HP")


while True:
    print("""
1. Лес
2. Магазин
3. Статус
4. Отдых
5. Выход
""")

    choice = input("Выбор: ")

    if choice == "1":
        forest(player)
    elif choice == "2":
        shop(player)
    elif choice == "3":
        status(player)
    elif choice == "4":
        rest(player)
    elif choice == "5":
        break