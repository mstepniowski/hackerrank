# https://www.hackerrank.com/contests/101may14/challenges/sherlock-and-minimax
from itertools import tee, izip


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def solve(numbers, p, q):
    numbers.sort()
    max_diff = max(0, numbers[0] - p)
    result = p

    for a, b in pairwise(numbers):
        if p >= b or q <= a:
            continue

        diff = (b - a) / 2
        if p > a:
            diff = min(b - p, diff)
        if q < b:
            diff = min(q - a, diff)

        if diff > max_diff:
            max_diff = diff
            result = min(max(a + diff, p), q)

    diff = max(0, q - numbers[-1])
    if diff > max_diff:
        max_diff = diff
        result = q

    return result


if __name__ == '__main__':
    import sys
    size = int(raw_input())
    numbers = [int(d) for d in sys.stdin.readline().split()]
    p, q = [int(d) for d in sys.stdin.readline().split()]
    print solve(numbers, p, q)
