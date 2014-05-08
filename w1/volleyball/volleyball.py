import math

MODULO = 10 ** 9 + 7


def pow_mod(a, b, c):
    if b <= 0:
        return 1
    if (b % 2) == 0:
        return pow_mod((a * a) % c, b / 2, c) % c
    else:
        return (a * pow_mod(a, b-1, c)) % c


def volleyball_combinations(a, b):
    a, b = max(a, b), min(a, b)
    return math.factorial(a + b - 1) // (math.factorial(b) * math.factorial(a - 1))


def volleyball(a, b):
    a, b = max(a, b), min(a, b)
    if ((a < 25 and b < 25) or abs(a - b) < 2
            or (min(a, b) >= 24 and abs(a - b) != 2)):
        # Game can't be finished at this point
        return 0

    result = volleyball_combinations(min(a, 25), min(b, 24))
    return (result % MODULO) * pow_mod(2, max(min(a - 24, b - 24), 0), MODULO) % MODULO


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(volleyball(a, b))
