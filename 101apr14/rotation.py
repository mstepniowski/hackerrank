import sys


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def rotation(blocks):
    total_sum = sum(blocks)
    pmean = sum((i + 1) * block for (i, block) in enumerate(blocks))
    max_pmean = pmean
    for block in blocks:
        pmean = pmean - total_sum + block * len(blocks)
        max_pmean = max(max_pmean, pmean)
    return max_pmean


if __name__ == '__main__':
    n = read_numbers()[0]
    blocks = read_numbers()
    print(rotation(blocks))
