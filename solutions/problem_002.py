LIMIT = 4_000_000
a = 0
b = 1
result = 0

while a < LIMIT:
    a, b = b, a + b
    if (a % 2 == 0):
        result += a

print(result)
