import random

def random_complection_matrix(n, m, choise):
    matrix = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            item = random.choice(choise)
            matrix[i][j].append(item)

    matrix[0][0] = ["HERO", "start"]

    free_cells = [(x, y) for y in range(n) for x in range(m)
                  if not (x == 0 and y == 0)]

    key_x, key_y = random.choice(free_cells)
    free_cells.remove((key_x, key_y))
    matrix[key_y][key_x] = ["key"]

    portal_x, portal_y = random.choice(free_cells)
    matrix[portal_y][portal_x] = ["portal"]

    return matrix


def motion(ans, x, y):
    if ans == "вверх":
        y -= 1
    elif ans == "вниз":
        y += 1
    elif ans == "вправо":
        x += 1
    elif ans == "влево":
        x -= 1

    return x, y

def show_field(mat, visited, hero_x, hero_y):
    print("Текущее поле:")
    for y, row in enumerate(mat):
        line_parts = []
        for x, cell in enumerate(row):
            if not visited[y][x] and not (x == hero_x and y == hero_y):
                cell_str = "[???]"
            else:
                cell_str = "[" + ",".join(cell) + "]"
            line_parts.append(cell_str)
        print(" ".join(line_parts))
    print()

def inventory_menu(inventory, mat, x, y):
    """
    Меню работы с инвентарём
    """
    while True:
        print("\n--- ИНВЕНТАРЬ ---")
        print("Сейчас в инвентаре:", inventory)
        print("1 - выбросить предмет по индексу (pop)")
        print("2 - выбросить предмет по названию (remove)")
        print("3 - сортировать по алфавиту (sort)")
        print("4 - сортировать по длине слова (lambda + reverse)")
        print("5 - поиск предмета (in / not in / index)")
        print("6 - назад в игру")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            if not inventory:
                print("Инвентарь пуст.")
                continue
            try:
                print("Введите индекс предмета: ")
                idx = int(input())
                if 0 <= idx < len(inventory):
                    item = inventory.pop(idx)
                    print(f"Вы выбросили {item}")
                    mat[y][x].append(item)
                else:
                    print("Неверный индекс.")
            except ValueError:
                print("Нужно ввести число.")

        elif choice == "2":
            if not inventory:
                print("Инвентарь пуст.")
                continue
            print("Название предмета: ")
            name = input().strip()
            if name in inventory:
                inventory.remove(name)
                print(f"Вы выбросили {name}.")
                mat[y][x].append(name)
            else:
                print("Такого предмета нет в инвентаре.")

        elif choice == "3":
            before = inventory.copy()
            inventory.sort()
            print("Было :", before)
            print("Стало:", inventory)

        elif choice == "4":
            before = inventory.copy()
            # sort + key=lambda + reverse
            inventory.sort(key=lambda item: len(item), reverse=True)
            print("Было :", before)
            print("Стало:", inventory)

        elif choice == "5":
            print("Название для поиска: ")
            name = input().strip()
            if name in inventory:
                idx = inventory.index(name)
                print(f"Предмет {name} найден в позиции {idx}.")
            else:
                print("Такого предмета нет (not in).")

        elif choice == "6":
            break
        else:
            print("Команда не распознана.")


# ---------------- ОСНОВНАЯ ЧАСТЬ ----------------

choise = ["empty", "chest", "monster", "trap"]
n, m = 4, 4
mat = random_complection_matrix(n, m, choise)

hp = 100
inventory = []
x = y = 0
win = False

# Матрица посещённых клеток
visited = [[False for _ in range(m)] for _ in range(n)]
visited[y][x] = True

print("Добро пожаловать в лабиринт!")
print("Цель: найти портал и выйти, предварительно подобрав ключ.")
print("Команды: вверх / вниз / влево / вправо / инвентарь / выход\n")

while hp > 0 and not win:
    print(f"Ваши HP: {hp}")
    print("Инвентарь:", inventory)
    show_field(mat, visited, x, y)

    command = input("Ваш ход: ").strip().lower()

    if command == "выход":
        print("Вы покинули игру.")
        break

    if command == "инвентарь":
        inventory_menu(inventory, mat, x, y)
        continue

    if command not in ("вверх", "вниз", "влево", "вправо"):
        print("Неизвестная команда.")
        continue

    new_x, new_y = motion(command, x, y)

    if not (0 <= new_x < m and 0 <= new_y < n):
        print("Вы упёрлись в стену лабиринта.")
        continue

    mat[y][x].remove("HERO")

    x, y = new_x, new_y

    visited[y][x] = True

    if "HERO" not in mat[y][x]:
        mat[y][x].insert(0, "HERO")

    cell_items = [item for item in mat[y][x] if item != "HERO"]

    for item in cell_items:
        if item == "start":
            print("Вы вернулись на стартовую клетку.")
        elif item == "empty":
            print("Здесь пусто.")
        elif item == "chest":
            print("Вы нашли сундук!")
            loot_pool = ["золото", "зелье", "камень", "хлеб"]
            count = random.randint(1, 3)
            loot = [random.choice(loot_pool) for _ in range(count)]
            print("В сундуке были:", loot)
            inventory.extend(loot)
            mat[y][x] = ["HERO", "empty"]
        elif item == "monster":
            dmg = random.randint(10, 30)
            print(f"На вас напал монстр! Вы теряете {dmg} HP.")
            hp -= dmg
            if hp > 0:
                drop = random.choice(["зуб монстра", "шкура монстра"])
                print("С монстра выпало:", drop)
                inventory.append(drop)
            mat[y][x] = ["HERO", "empty"]
        elif item == "trap":
            dmg = random.randint(5, 20)
            print(f"Вы наступили на ловушку! -{dmg} HP.")
            hp -= dmg
            mat[y][x] = ["HERO", "empty"]
        elif item == "key":
            print("Вы нашли ключ и кладёте его в инвентарь.")
            inventory.append("ключ")
            mat[y][x] = ["HERO", "empty"]
        elif item == "portal":
            if "ключ" in inventory:
                print("У вас есть ключ и вы входите в портал. Победа!")
                win = True
            else:
                print("Вы нашли портал, но у вас нет ключа.")

if hp <= 0:
    print("Вы погибли в лабиринте...")
