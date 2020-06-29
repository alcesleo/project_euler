import re
from common.data import read_data
from common.digits import split_digits, join_digits
from common.tools import slice_grid
from common.logging import info


SIZE = 9
NUMBERS = set(range(1, 10))
EMPTY = {0}


def parse_sudokus(data):
    """Returns a list of numpy 2d-arrays representing sudokus."""
    sudokus = []
    sudoku_data = filter(None, re.split(r"Grid \d\d\n", data))

    for sudoku in sudoku_data:
        parsed_sudoku = list(map(list, map(split_digits, sudoku.splitlines())))
        sudokus.append(parsed_sudoku)

    return sudokus


def region(sudoku, row, col):
    """Returns the numbers in a 3x3 region of a sudoku that row and col is in."""
    region_row = row // 3 * 3
    region_col = col // 3 * 3

    return sudoku[region_row][region_col:region_col + 3]\
            + sudoku[region_row + 1][region_col:region_col + 3]\
            + sudoku[region_row + 2][region_col:region_col + 3]


def options(sudoku, row, col):
    """Returns a set of numbers that are legal to put into a cell."""
    filled_row = set(sudoku[row]) - EMPTY
    filled_col = set(slice_grid(sudoku, col=col, vstep=1)) - EMPTY
    filled_reg = set(region(sudoku, row, col)) - EMPTY

    rule_out = filled_row | filled_col | filled_reg

    return NUMBERS - rule_out


def solve_sudoku(sudoku, cell=0):
    """Recursively solves a sudoku by trying all reasonable options depth first."""
    if cell == SIZE * SIZE:
        return True

    row = cell // SIZE
    col = cell % SIZE

    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, cell + 1)

    for candidate in options(sudoku, row, col):
        sudoku[row][col] = candidate
        if solve_sudoku(sudoku, cell + 1):
            return True

    sudoku[row][col] = 0
    return False


def solve():
    data = read_data("p096_sudoku.txt")
    sudokus = parse_sudokus(data)
    result = 0

    for i, sudoku in enumerate(sudokus, 1):
        solved = solve_sudoku(sudoku)
        top_left = join_digits(sudoku[0][0:3])
        result += top_left

        info(f"Sudoku {i} {'solved' if solved else 'FAILED'}: {top_left}")
        info(sudoku)
        info("")

    return result


if __name__ == "__main__":
    print(solve())
