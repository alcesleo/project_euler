import os
import re
from timeit import default_timer as timer
from subprocess import run, PIPE

SCRIPT_PATH = os.path.dirname(__file__)
SOLUTIONS_PATH = os.path.join(SCRIPT_PATH, "solutions")


def print_solution(solution_file):
    start = timer()
    result = run(["python", os.path.join(
        SOLUTIONS_PATH, solution_file)], stdout=PIPE)
    end = timer()

    seconds = end - start
    answer = result.stdout.decode().strip()

    print(f"{solution_file:14} | {seconds:10.6f}s | {answer}")


def print_headers():
    print(f"Problem        | Time        | Answer")
    print(f"---------------|-------------|--------------------")


def get_solution_files():
    (_, _, filenames) = next(os.walk(SOLUTIONS_PATH))
    filenames.sort()
    return filenames


def print_solutions():
    for solution_file in get_solution_files():
        print_solution(solution_file)


def print_report():
    print()
    print_headers()
    print_solutions()
    print()


if __name__ == "__main__":
    print_report()
