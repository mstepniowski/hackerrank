# https://www.hackerrank.com/contests/101may14/challenges/sherlock-and-minimax
def solve(B):
    partial_sum = [0, 0]
    last_b = B[0]

    for b in B[1:]:
        partial_sum_min = max(partial_sum[0], partial_sum[1] + last_b - 1)
        partial_sum_max = max(partial_sum[0] + b - 1, partial_sum[1] + abs(b - last_b))
        partial_sum = [partial_sum_min, partial_sum_max]
        last_b = b

    return max(partial_sum)


if __name__ == '__main__':
    import sys
    T = int(raw_input())
    for t in range(T):
        size = int(raw_input())
        b = [int(d) for d in sys.stdin.readline().split()]
        print solve(b)
