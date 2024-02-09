def greedy_algorithm(items, budget):
    items_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    items_list.sort(key=lambda x: x[2] / x[1], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, cost, calories in items_list:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i, (name, data) in enumerate(items.items(), start=1):
        cost = data["cost"]
        calories = data["calories"]

        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    total_calories = dp[len(items)][budget]

    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))
