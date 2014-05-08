import sys

MOD = 10 ** 9 + 7

# def solve_eager(xs, ys):
#     xs.sort()
#     ys.sort()
#     xs_sum = sum(xs)
#     ys_sum = sum(ys)
#     xs_multiplier = 1
#     ys_multiplier = 1
#     result = 0
#     while len(xs) > 0 and len(ys) > 0:
#         # print xs_sum, ys_sum, xs, ys, result
#         if xs[-1] > ys[-1] or xs[-1] == ys[-1] and xs_sum >= ys_sum:
#             x = xs.pop()
#             xs_sum -= x
#             result += x * xs_multiplier % MOD
#             ys_multiplier += 1
#         else:
#             y = ys.pop()
#             ys_sum -= y
#             result += y * ys_multiplier % MOD
#             xs_multiplier += 1
#     result += (xs_sum * xs_multiplier + ys_sum * ys_multiplier) % MOD
#     return result

def solve(xs, ys):
    xs.sort()
    ys.sort()
    LX, LY = len(xs), len(ys)
    results = [0] * (LX + 1)
    for x in range(LX):
        results[x + 1] = results[x] + xs[x] * (LY + 1)
    for y in range(LY):
        new_results = [0] * (LX + 1)
        new_results[0] = results[0] + ys[y] * (LX + 1)
        for x in range(LX):
            new_results[x + 1] = min(new_results[x] + xs[x] * (LY - y),
                                     results[x + 1] + ys[y] * (LX - x))
        results = new_results

    return results[LX] % MOD

def read_numbers():
    return [int(x) for x in sys.stdin.readline().split()]

if __name__ == '__main__':
    T = input()
    for t in range(T):
        m, n = read_numbers()
        ys = read_numbers()
        xs = read_numbers()
        print solve(xs, ys)
