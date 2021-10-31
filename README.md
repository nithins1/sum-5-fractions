# sum-5-fractions

Problem: Find values for the 5 integers `a, b, c, d, e` such that `1/a + 1/b + 1/c + 1/d + 1/e = 1`
Given a max denominator D, this program searches for all solutions where a, b, c, d, e ≤ D.

## How to run:
`python sum5frac.py [-h] [-m MAX] [-i ITERATIONS]`

Optional arguments:

`-h, --help` - print help message and exit

`-m MAX, --max MAX` - Specify maximum denominator (default: 100)

`-i ITERATIONS, --iterations ITERATIONS` - Log number of combinations attempted after every `ITERATIONS` trials

You can redirect the output to a file and the log messages will be sent to stderr, not the file.
