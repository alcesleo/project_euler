TARGET = 1000

for a in range(1, TARGET):
    for b in range(a + 1, TARGET):
        for c in range(b + 1, TARGET):
            if a + b + c == TARGET and a * a + b * b == c * c:
                print(a * b * c)
                break
