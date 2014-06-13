# https://www.hackerrank.com/contests/101may14/challenges/almost-sorted-interval
def solve(numbers):
    result = 0
    i = 0
    while i < len(numbers):
        size = 1
        while i < len(numbers) and numbers[i] >= numbers[i - 1]:
            size += 1
            i += 1
        result += size * (size + 1) / 2
        i += 1
    return result


if __name__ == '__main__':
    import sys
    size = int(raw_input())
    numbers = [int(d) for d in sys.stdin.readline().split()]
    print solve(numbers)
