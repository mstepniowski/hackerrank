# https://www.hackerrank.com/contests/101may14/challenges/sherlock-and-array

def solve(numbers):
    partial_right = [0]
    for n in reversed(numbers):
        partial_right.append(partial_right[-1] + n)
    partial_right.pop()
    partial_right.reverse()

    partial_left = 0
    for i, n in enumerate(numbers):
        if partial_left == partial_right[i]:
            return True
        partial_left += n

    return False


if __name__ == '__main__':
    import sys
    T = int(raw_input())
    for t in range(T):
        size = int(raw_input())
        numbers = [int(d) for d in sys.stdin.readline().split()]
        print {True: 'YES', False: 'NO'}[solve(numbers)]
