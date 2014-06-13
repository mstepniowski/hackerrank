# https://www.hackerrank.com/contests/w4/challenges/roy-and-alpha-beta-trees
import sys


MOD = 10 ** 9 + 9
MAX_N = 150

dp = [[None] * MAX_N for _ in range(MAX_N)]


def read_numbers():
    return [int(d) for d in sys.stdin.readline().split()]


def subtree(numbers, start, end):
    """Calculates result for all trees from start to end, inclusive."""
    if start == end:
        return 1, 0, 0
    if dp[start][end] is not None:
        return dp[start][end]

    tree_count = 0
    even_sum = 0
    odd_sum = 0

    for i in range(start, end):
        left_count, left_even_sum, left_odd_sum = subtree(numbers, start, i)
        right_count, right_even_sum, right_odd_sum = subtree(numbers, i + 1, end)
        tree_count = (tree_count + left_count * right_count) % MOD
        # print '> subtree(%r, %r, %r) > %d (%r, %r, %r), (%r, %r, %r)' % (numbers[start:end], start, end, i, left_count, left_even_sum, left_odd_sum, right_count, right_even_sum, right_odd_sum)
        even_sum = (even_sum + numbers[i] * left_count * right_count + left_odd_sum * right_count + right_odd_sum * left_count) % MOD
        odd_sum = (odd_sum + left_even_sum * right_count + right_even_sum * left_count) % MOD

    dp[start][end] = (tree_count, even_sum, odd_sum)
    # print 'subtree(%r, %r, %r) = (%r, %r, %r)' % (numbers[start:end], start, end, tree_count, even_sum, odd_sum)
    return tree_count, even_sum, odd_sum


def solve(numbers, alpha, beta):
    global dp
    dp = [[None] * MAX_N for _ in range(MAX_N)]

    numbers.sort()
    tree_count, even_sum, odd_sum = subtree(numbers, 0, len(numbers))
    return (alpha * even_sum - beta * odd_sum) % MOD


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        n = int(raw_input())
        alpha, beta = read_numbers()
        numbers = read_numbers()
        print solve(numbers, alpha, beta)
