#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <unistd.h>
#include <math.h>

#define OPTIONS "hm:i:"
#define TOLERANCE .0000001

int main(int argc, char **argv)
{
    int opt = 0;
    char *ptr;
    int max_denom = 100;
    int iterations = -1;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'm':
            max_denom = strtoul(optarg, &ptr, 10);
            if (*ptr != '\0') {
                printf("Invalid max denominator\n");
                return 1;
            }
            break;
        case 'i':
            iterations = strtoul(optarg, &ptr, 10);
            if (*ptr != '\0') {
                printf("Invalid number of iterations\n");
                return 1;
            }
            break;
        case 'h':
	default:
            fprintf(stderr, "usage: ./sum5frac [-h] [-m MAX] [-i ITERATIONS]\n\n");
            fprintf(stderr, "Finds 5 unique fractions that add to 1.\n\n");
            fprintf(stderr, "optional arguments:\n");
            fprintf(stderr, "-h: show this help message and exit\n");
            fprintf(stderr, "-m MAX: Maximum denominator to be used in fractions (default: 100)\n");
            fprintf(stderr, "-i ITERATIONS: Print message after every i iterations (default: print nothing)\n");
            return 0;
        }
    }

    uint64_t i = 0;
    uint64_t num_solutions = 0;
    for (double a = 2; a <= max_denom; a++) {
        if (1.0/a + 1.0/(a+1) + 1.0/(a+2) + 1.0/(a+3) + 1.0/(a+4) < 1.0) {
            break;
        }
        for (double b = a + 1; b <= max_denom; b++) {
            if (1.0/b + 1.0/(b+1) + 1.0/(b+2) + 1.0/(b+3) < 1.0 - (1.0/a)) {
                break;
            }
            for (double c = b + 1; c <= max_denom; c++) {
                if (1.0/c + 1.0/(c+1) + 1.0/(c+2) < 1.0 - (1.0/a) - (1.0/b)) {
                    break;
                }
                for (double d = c + 1; d <= max_denom; d++) {
                    if (1.0/d + 1.0/(d+1) < 1.0 - (1.0/a) - (1.0/b) - (1.0/c)) {
                        break;
                    }
                    for (double e = d + 1; e <= max_denom; e++) {
                        i++;
                        if (iterations != -1 && i % iterations == 0) {
                            fprintf(stderr, "%" PRIu64 " iterations done.\n", i);
                        }

                        if (fabs(1.0/a + 1.0/b + 1.0/c + 1.0/d + 1.0/e - 1) < TOLERANCE) {
                            printf("1/%.0f + 1/%.0f + 1/%.0f + 1/%.0f + 1/%.0f\n", a, b, c, d, e);
                            num_solutions++;
                        }
                    }
                }
            }
        }
    }

    printf("Number of solutions: %" PRIu64 "\n", num_solutions);
    printf("Number of iterations: %" PRIu64 "\n", i);
    return 0;
}
