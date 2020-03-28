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
from common.logging import logger

TARGET = 42


def solve(limit=8):
    logger.debug(limit, TARGET)


if __name__ == "__main__":
    result = solve(1_000_000)
    print(result)
```

Structuring each solution like this is slightly more cumbersome than simply printing the answer, but gives several benefits:

- Each file can still simply be run to output the result
- Enables tools like `pydoc` and `doctest` to run without triggering the often expensive `solve()`-function
- Lets you keep variables from the example to verify the solution as default arguments rather than ugly commented out variables
- Lets you keep useful debugging output that often explains the solution really well without having ugly commented out `print()`-statements

## Documentation

Links to relevant Python documentation

- [collections](https://docs.python.org/3.6/library/collections.html)
- [doctest](https://docs.python.org/3.6/library/doctest.html)
- [fractions](https://docs.python.org/3.6/library/fractions.html)
- [functools](https://docs.python.org/3.6/library/functools.html)
- [itertools](https://docs.python.org/3.6/library/itertools.html)
- [math](https://docs.python.org/3.6/library/math.html)
- [numpy](https://numpy.org/doc/1.18/)
- [set](https://docs.python.org/3.6/library/stdtypes.html#set)
- [PEP257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
