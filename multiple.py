def ninezero(n):
    return int(bin(n)[2:].replace('1', '9'))

numbers = [ninezero(n) for n in range(1, 10 ** 4 + 1)]
result = [None] * 501
for n in numbers:
    for d in range(1, 501):
        if n % d == 0 and (result[d] is None or result[d] > n):
            result[d] = n

T = input()
for t in range(T):
    N = input()
    print result[N]
