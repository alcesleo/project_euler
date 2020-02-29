from collections import Counter


def combinations(coins, target):
    """Returns the combinations of coin counts that equal a target sum
    """
    if len(coins) == 0:
        return []

    coin, *rest = coins
    most = target // coin

    result = []

    for count in range(0, most + 1):
        total = coin * count
        remainder = target - total
        combination = Counter([coin] * count)

        if total == target:
            result.append(combination)

        for rest_combination in combinations(rest, remainder):
            rest_total = combination + rest_combination
            result.append(combination + rest_combination)

    return result


def deduplicate(c):
    """Deduplicates an unhashable collection
    """
    result = []

    for i in c:
        if i not in result:
            result.append(i)

    return result


TARGET = 200
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

result = deduplicate(combinations(COINS, TARGET))

print(len(result))
