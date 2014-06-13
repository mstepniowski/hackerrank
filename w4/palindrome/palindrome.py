# https://www.hackerrank.com/contests/w4/challenges/palindrome-index

def is_palindrome(word):
    return word == ''.join(reversed(word))


def solve(word):
    indices = range(len(word))
    for i, j in zip(indices, reversed(indices)):
        if word[i] != word[j]:
            if is_palindrome(word[i + 1:j + 1]):
                return i
            else:
                return j

    # If a word already is a palindrome, return its center
    return len(word) / 2


if __name__ == '__main__':
    import sys

    T = int(raw_input())
    for t in range(T):
        print solve(sys.stdin.readline().strip())
