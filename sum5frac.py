"""
For ints a, b, c, d, e.
Find unequal fractions 1/a, 1/b, 1/c, 1/d, 1/e such that their sum is exactly 1.
Only searches for solutions with a denominator under a specified maximum value.
Prints only unique solutions. For each solution, the fractions are summed in descending order.
"""

import sys
import argparse
parser = argparse.ArgumentParser(description="Finds 5 unique fractions that add to 1.")
parser.add_argument("-m", "--max", type=int, default=100, help="Maximum denominator to be used in fractions (default: 100)")
parser.add_argument("-i", "--iterations", type=int, default=-1, help="Print message after every i iterations (default: print nothing)")
args = parser.parse_args()

num_solutions = 0
max_denominator = args.max + 1
tolerance = .000000001
i = 0

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

for a in range(2, max_denominator):
    # Significant optimization.
    # Once a (the largest fraction in the 5 sum) becomes this large, there cannot be any more solutions
    # For example, when a >= 4, there will be no further solutions because 1/4 + 1/5 + 1/6 + 1/7 + 1/8 < 1
    if (1/a + 1/(a+1) + 1/(a+2) + 1/(a+3) + 1/(a+4)) < 1:
        break

    for b in range(a + 1, max_denominator):
        # Similar optimization as above
        if (1/b + 1/(b+1) + 1/(b+2) + 1/(b+3)) < 1 - (1/a):
            break

        for c in range(b + 1, max_denominator):
            if (1/c + 1/(c+1) + 1/(c+2)) < 1 - (1/a) - (1/b):
                break

            for d in range(c + 1, max_denominator):
                if (1/d + 1/(d+1)) < 1 - (1/a) - (1/b) - (1/c):
                    break

                for e in range(d + 1, max_denominator):
                    i += 1
                    if args.iterations != -1 and i % args.iterations == 0:
                        eprint(f"{i:,} iterations done.", flush=True)

                    if abs(1/a + 1/b + 1/c + 1/d + 1/e - 1) < tolerance:
                        print(f"1/{a} + 1/{b} + 1/{c} + 1/{d} + 1/{e}", flush=True)
                        num_solutions += 1

eprint("Number of solutions:", num_solutions)
eprint("Number of iterations:", i)
