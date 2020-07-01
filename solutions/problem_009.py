from common.logging import info

def solve(target):
    for a in range(1, target // 2):
        for b in range(a + 1, target // 2):
            for c in range(b + 1, target // 2):
                if a + b + c == target and a * a + b * b == c * c:
                    info(f"{a} + {b} + {c} = {target}")
                    return a * b * c

if __name__ == "__main__":
    print(solve(1000))
