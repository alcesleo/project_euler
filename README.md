# [Project Euler](https://projecteuler.net/)

## Strategy

Readable and pragmatic over fast and short.

## Development

```bash
# Get a virtual environment with the correct python version and dependencies
pipenv shell

# Install dependencies
pipenv install

# Run a solution file
python solutions/problem_xxx.py

# Benchmark a solution
time python solutions/problem_xxx.py

# Run doctests
python -m doctest -v solutions/problem_xxx.py

# Print more helpful information than the answer
DEBUG=True python solutions/problem_063.py

# View the documentation for a module
cd solutions/
python -m pydoc problem_xxx
python -m pydoc common.tools

# Run and benchmark all solutions
python solutions/common/report.py
```

## Documentation

- [collections](https://docs.python.org/3.6/library/collections.html)
- [doctest](https://docs.python.org/3.6/library/doctest.html)
- [fractions](https://docs.python.org/3.6/library/fractions.html)
- [functools](https://docs.python.org/3.6/library/functools.html)
- [itertools](https://docs.python.org/3.6/library/itertools.html)
- [math](https://docs.python.org/3.6/library/math.html)
- [numpy](https://numpy.org/doc/1.18/)
- [set](https://docs.python.org/3.6/library/stdtypes.html#set)
