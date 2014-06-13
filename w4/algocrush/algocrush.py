# https://www.hackerrank.com/contests/w4/challenges/crush
import sys
from itertools import groupby


def read_numbers():
    return [int(d) for d in sys.stdin.readline().split()]


def solve(queries):
    events = []
    for a, b, k in queries:
        events.append((a, k))
        events.append((b + 1, -k))

    events.sort()
    max_value = 0
    current_value = 0

    for i, items in groupby(events, lambda v: v[0]):
        current_value += sum(k for (i, k) in items)
        max_value = max(current_value, max_value)

    return max_value


if __name__ == '__main__':
    n, m = read_numbers()
    queries = []
    for i in range(m):
        queries.append(read_numbers())
    print solve(queries)
