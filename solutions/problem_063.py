from common.logging import logger

limit = 100
count = 0

for b in range(1, limit):
    for e in range(1, limit):
        n = b ** e

        if len(str(n)) == e:
            count += 1
            logger.info(f"{count}: {b}^{e} = {n}")

print(count)
