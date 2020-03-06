limit = 100
count = 0
DEBUG = False

for b in range(1, limit):
    for e in range(1, limit):
        n = b ** e

        if len(str(n)) == e:
            count += 1
            if DEBUG:
                print(f"{count}: {b}^{e} = {n}")

print(count)
