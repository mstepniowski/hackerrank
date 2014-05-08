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

def div(a, b):
    return (a % MOD) * inverse(b, MOD) % MOD

f = [1]
for n in range(1, 2 * 10 ** 6):
    f.append(f[-1] * n % MOD)

import sys
T = input()
for t in range(T):
    n, m = [int(x) for x in sys.stdin.readline().split()]
    print div(f[n + m - 2], f[n - 1] * f[m - 1] % MOD)
