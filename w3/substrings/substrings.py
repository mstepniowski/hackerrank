# https://www.hackerrank.com/contests/w3/challenges/sam-and-substrings

MOD = 10 ** 9 + 7


def inverse(a, n):
    t = 0
    newt = 1
    r = n
    newr = a
    while newr != 0:
        quotient = r / newr
        t, newt = (newt, t - quotient * newt)
        r, newr = (newr, r - quotient * newr)
    return t if t >= 0 else t + n

def div_mod(a, b):
    return (a % MOD) * inverse(b, MOD) % MOD


def solve_for(digits, i, j):
    if j - i == 1:
        return int(digits[i])
    return solve_for(i, j - 1) + solve_for(i + 1, j) + 2


def solve(digits):
    result = 0
    number = 0
    for i, digit in enumerate(int(d) for d in reversed(digits)):
        number_right = (10 ** i * digit + number) % MODULO
        number_left = result - (i * 3)
        result = (result + number) % MODULO


if __name__ == '__main__':
    print solve(raw_input())


# T(i, i) = digits
# T(i, j) = T(i + 1, j) + T(i, j - 1) + digits[j] * 10 ** j
# T(i + 1, j) = (T(i, j) - digits[i] * (j - i)) / 10
# ...
# T(i, j) = T(i, j) - 10 * digits[i] * (j - i) + 10 * T(i, j - 1) + digits[j] * 10 ** j
# T(i, j - 1) = digits[j] * 10 ** j - digits[i] * (j - i) / 10
# ...
# T(i, j) = digits[i] * (j - i + 1) - digits[j + 1] * 10 ** j
