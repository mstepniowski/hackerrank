import math


def divisors(n):
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            yield d


def pairs(p):
    result = 0
    for x in range(1, p + 1):
        result += p // x
    return result


def pairs2(p):
    d = [0] + list(divisors(p))
    result = 0
    for i in range(len(d) - 1):
        result += p // d[i + 1] * (d[i + 1] - d[i])
    return result


def psequences(n, p):




if __name__ == '__main__':
    n = int(input())
    p = int(input())
    print psequences(n, p)
