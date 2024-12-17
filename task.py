items = {
    'r': (3, 25),  # Винтовка
    'p': (2, 15),  # Пистолет
    'a': (2, 15),  # Боекомплект
    'm': (2, 20),  # Аптечка
    'i': (1, 5),   # Ингалятор
    'k': (1, 15),  # Нож
    'x': (3, 20),  # Топор
    't': (1, 25),  # Оберег
    'f': (1, 15),  # Фляжка
    'd': (1, 10),  # Антидот
    's': (2, 20),  # Еда
    'c': (2, 20)   # Арбалет
}


max_cells = 9 
required_items = ['i', 'd']
initial_survival_points = 15


def knapsack(items, max_cells, required_items, initial_survival_points):
    from itertools import combinations

    best_combination = []
    best_survival_points = -1


    for r in range(1, len(items) + 1):
        for combo in combinations(items.keys(), r):
            total_cells = sum(items[item][0] for item in combo)
            total_points = sum(items[item][1] for item in combo)


            if total_cells <= max_cells and all(item in combo for item in required_items):
                final_points = initial_survival_points + total_points
                if final_points > best_survival_points:
                    best_survival_points = final_points
                    best_combination = combo

    return best_combination, best_survival_points


best_combination, best_survival_points = knapsack(items, max_cells, required_items, initial_survival_points)


inventory = [['' for _ in range(3)] for _ in range(3)]
for i, item in enumerate(best_combination):
    inventory[i // 3][i % 3] = item


for row in inventory:
    print(row)
print(f"Итоговые очки выживания: {best_survival_points}")
    