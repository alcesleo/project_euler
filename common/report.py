import pkgutil
from subprocess import run, PIPE
from timeit import default_timer as timer


SOLUTION_PKG = "solutions"


def print_solution(module_name):
    solution_module = f"{SOLUTION_PKG}.{module_name}"

    start = timer()
    result = run(["python", "-m", solution_module], stdout=PIPE)
    end = timer()

    seconds = end - start
    answer = result.stdout.decode().strip()

    print(f"{module_name:14} | {seconds:10.6f}s | {answer}")


def print_headers():
    print(f"Problem        | Time        | Answer")
    print(f"---------------|-------------|--------------------")


def print_solutions():
    for solution in pkgutil.iter_modules([SOLUTION_PKG]):
        print_solution(solution.name)


def print_report():
    print()
    print_headers()
    print_solutions()
    print()


if __name__ == "__main__":
    print_report()
