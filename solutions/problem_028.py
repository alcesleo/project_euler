WIDTH = 1001
SIDES = 4

n = 1
step = 2
diagonals = [n]
while n < WIDTH * WIDTH:
    for i in range(SIDES):
        n += step
        diagonals.append(n)

    step += 2


print(sum(diagonals))
