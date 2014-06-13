# https://www.hackerrank.com/contests/w3/challenges/the-love-letter-mystery

def solve(s):
    result = 0
    for i in range(len(s) / 2):
        result += abs(ord(s[i]) - ord(s[-i - 1]))
    return result


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        print solve(raw_input())
