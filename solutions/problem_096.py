from common.data import read_data
from common.tools import split_digits, join_digits
import numpy as np

SIZE = 9
NUMBERS = set(range(1, 10))
EMPTY = {0}


def parse_sudokus(data):
    """Returns a list of numpy 2d-arrays representing sudokus
    """
    sudokus = []
    current = []

    for row in data.splitlines():
        if "Grid" in row:
            continue

        current.append(split_digits(row))

        if len(current) == SIZE:
            sudokus.append(np.array(current))
            current = []

    return sudokus


def region(sudoku, row, col):
    """Returns the numbers in a 3x3 region of a sudoku that row and col is in
    """
    row_start = row // 3 * 3
    row_end = row_start + 3
    col_start = col // 3 * 3
    col_end = col_start + 3

    return sudoku[row_start:row_end, col_start:col_end].flatten()


def options(sudoku, row, col):
    """Returns a set of numbers that are legal to put into a cell
    """
    filled_row = set(sudoku[row]) - EMPTY
    filled_col = set(sudoku[:, col]) - EMPTY
    filled_reg = set(region(sudoku, row, col)) - EMPTY

    rule_out = filled_row | filled_col | filled_reg

    return NUMBERS - rule_out


def solve_sudoku(sudoku, cell=0):
    """Recursively solves a sudoku by trying all reasonable options depth first
    """
    if cell == SIZE * SIZE:
        return True

    row = cell // SIZE
    col = cell % SIZE

    if sudoku[row, col] != 0:
        return solve_sudoku(sudoku, cell + 1)

    for candidate in options(sudoku, row, col):
        sudoku[row, col] = candidate
        if solve_sudoku(sudoku, cell + 1):
            return True

    sudoku[row, col] = 0
    return False


def solve(debug=False):
    data = read_data("p096_sudoku.txt")
    sudokus = parse_sudokus(data)
    result = 0

    for i, sudoku in enumerate(sudokus, 1):
        solved = solve_sudoku(sudoku)
        top_left = join_digits(sudoku[0, 0:3])
        result += top_left

        if debug:
            print(f"Sudoku {i} {'solved' if solved else 'FAILED'}: {top_left}")
            print(sudoku)
            print()

    return result


print(solve())
