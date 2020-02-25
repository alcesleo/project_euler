LIMIT = 100

numbers = set()

for a in range(2, LIMIT + 1):
    for b in range(2, LIMIT + 1):
        numbers.add(a ** b)

numbers = list(numbers)
numbers.sort()

print(len(numbers))
