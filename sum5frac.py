"""
For ints a, b, c, d, e.
Find unequal fractions 1/a, 1/b, 1/c, 1/d, 1/e such that their sum is exactly 1.
Requires user input of the maximum denominator for all fractions.
Prints only unique solutions, For a solution, the fractions are summed in descending order.
"""

num_solutions = 0
max_denominator = int(input("Maximum denominator: ")) + 1
tolerance = .0000001
solutions = set()
iterations = 0

# Check if all fractions are different
def all_different(*args):
    return len(args) == len(frozenset(args))

# Check if solution is unique
def not_seen_before(*args):
    return frozenset(args) not in solutions

for a in range(2, max_denominator):
    # Significant optimization.
    # Once a (the largest fraction in the 5 sum) becomes this large, there cannot be any more solutions
    # For example, when a >= 4, there will be no further solutions because 1/4 + 1/5 + 1/6 + 1/7 + 1/8 < 1
    if (1/a + 1/(a+1) + 1/(a+2) + 1/(a+3) + 1/(a+4)) < 1:
        break;

    for b in range(2, max_denominator):
        for c in range(2, max_denominator):
            for d in range(2, max_denominator):
                for e in range(2, max_denominator):
                    iterations += 1
                    if iterations % 100000000 == 0:
                        print(f"{iterations:,} iterations done.", flush=True)

                    if abs(1/a + 1/b + 1/c + 1/d + 1/e - 1) < tolerance and all_different(a, b, c, d, e) and not_seen_before(a, b, c, d, e):
                        print(f"1/{a} + 1/{b} + 1/{c} + 1/{d} + 1/{e}", flush=True)
                        num_solutions += 1
                        solutions.add(frozenset({a, b, c, d, e}))

print("Number of solutions:", num_solutions)
