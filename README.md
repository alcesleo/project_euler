# [Project Euler](https://projecteuler.net/)

## Strategy

Readable and pragmatic over fast and short.

## Development

```bash
# Get a virtual environment with the correct python version and dependencies
pipenv shell

# Install dependencies
pipenv install

# Run a solution
python -m solutions.problem_xxx

# Benchmark a solution
time python -m solutions.problem_xxx

# Run doctests
python -m doctest -v solutions/problem_xxx.py

# Print more helpful information than the answer
LOG_LEVEL=info python -m solutions.problem_063

# View the documentation for a module
python -m pydoc solutions.problem_xxx
python -m pydoc common.tools

# Run and benchmark all solutions
python -m common.report
```

## Guidelines

```python
"""
Explain the solution in the module docstring
"""
from common.logging import info

def solve(limit):
    """Test the example given in the question in a doctest:

    >>> solve(8)
    42
    """
    info(f"Log other information using the logging functions.")
    return 42


if __name__ == "__main__":
    print(solve(1_000_000))
```

Structuring each solution like this is slightly more cumbersome than simply printing the answer, but gives several benefits:

- Each file can still simply be run to output the result
- Enables tools like `pydoc` and `doctest` to run without triggering the often expensive `solve()`-function
- Lets you import functions from other solutions
- Lets you keep variables from the examples around to verify the solution
- Lets you keep useful debugging output that often explains the solution really well without having ugly commented out `print()`-statements

## Documentation

Links to relevant Python documentation

- [collections](https://docs.python.org/3/library/collections.html)
- [decimal](https://docs.python.org/3/library/decimal.html)
- [doctest](https://docs.python.org/3/library/doctest.html)
- [fractions](https://docs.python.org/3/library/fractions.html)
- [functools](https://docs.python.org/3/library/functools.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [math](https://docs.python.org/3/library/math.html)
- [numpy](https://numpy.org/doc/1.18/)
- [set, frozenset](https://docs.python.org/3/library/stdtypes.html#set)
- [PEP257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
