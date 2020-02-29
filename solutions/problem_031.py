def combinations(coins, target):
    """Returns the combinations of coin counts that equal a target sum
    """

    # Store the counts as a set(frozenset(tuple(coin, count)))
    #
    # The frozenset of tuples is hashable unlike the collections.Counter
    # class which would be a conceptually nicer data structure, but isn't hashable
    result = set()

    if len(coins) == 0:  # TODO: Move down
        return result

    coin, *rest = coins
    most = target // coin

    for count in range(0, most + 1):
        total = coin * count
        remainder = target - total
        combination = frozenset([(coin, count)])

        if total == target and count != 0:
            result.add(combination)

        for rest_combination in combinations(rest, remainder):
            result.add(combination | rest_combination)

    return result


TARGET = 200
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

result = combinations(COINS, TARGET)

print(len(result))
