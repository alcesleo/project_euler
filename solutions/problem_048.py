
LIMIT = 1000
result = 0

for i in range(1, LIMIT + 1):
    result += i ** i

print(result % 10**10)
