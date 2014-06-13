# https://www.hackerrank.com/contests/w4/challenges/lucy-and-flowers

MOD = 10 ** 9 + 9
MAX_N = 5000

dp = [1] * (MAX_N + 1)
inv = [0] * (MAX_N + 1)
mem = [0] * (MAX_N + 1)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def precompute(n):
    for i in range(1, n + 1):
        r = 0
        for j in range(i):
            r += (dp[j] * dp[i - j - 1]) % MOD
        dp[i] = r % MOD

    for i in range(1, MAX_N + 1):
        inv[i] = modinv(i, MOD)


def solve(n):
    if mem[n] != 0:
        return mem[n]

    result = 0
    comb = 1
    for i in range(1, n + 1):
        comb = (comb * (n - i + 1) * inv[i]) % MOD
        result = (result + dp[i] * comb) % MOD

    mem[n] = result
    return result


if __name__ == '__main__':
    precompute(MAX_N)
    T = int(raw_input())
    for t in range(T):
        n = int(raw_input())
        print solve(n)
