# https://www.hackerrank.com/contests/101apr14/challenges/morgan-and-a-string
import sys


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def hash_add(h, c, base, mod):
    return h * base + c % mod


BASE = [1]
for i in range(10 ** 5):
    BASE.append((BASE[-1] * 101) % (10 ** 9 + 7))


class QuickSearch:
    def __init__(self, s, base=101, mod=10 ** 9 + 7):
        self.s = s
        self.base = base
        self.mod = mod
        self.hashes = self.calculate_hashes(s)

    def calculate_hashes(self, s):
        # print('start', len(s))
        hashes = [0] * (len(s) + 1)
        # print('end')
        for i, c in enumerate(s):
            o = ord(c) - ord('A') + 1
            hashes[i + 1] = (hashes[i] * self.base + o) % self.mod
        return hashes

    def get_hash(self, i, j):
        # print((self.hashes[j + 1] - self.hashes[i] * BASE[j - i + 1] % self.mod) % self.mod)
        return (self.hashes[j + 1] - self.hashes[i] * BASE[j - i + 1]) % self.mod


def maximum_common_prefix(qa, qb, ia, ib):
    start = 0
    end = min(len(qa.s) - ia, len(qb.s) - ib)
    last_good = 0

    while start < end:
        middle = (start + end) // 2
        # print(start + ia, middle + ia,
        #       start + ib, middle + ib,
        #       qa.s[start + ia: middle + ia + 1], qb.s[start + ib: middle + ib + 1],
        #       qa.get_hash(start + ia, middle + ia), qb.get_hash(start + ib, middle + ib))

        if qa.get_hash(start + ia, middle + ia) == qb.get_hash(start + ib, middle + ib):
            # print('good')
            last_good = max(last_good, middle)
            start = middle + 1
        else:
            # print('bad')
            end = middle
    return last_good


def morgan(a, b):
    qa = QuickSearch(a)
    qb = QuickSearch(b)
    ia = 0
    ib = 0

    result = []

    while ia < len(a) and ib < len(b):
        # print(ia, ib)
        # sys.stderr.write('%d %s, %d %s -> %s\n' % (ia, a[ia], ib, b[ib], result))
        if a[ia] > b[ib]:
            result.append(b[ib])
            ib += 1
        elif a[ia] < b[ib]:
            result.append(a[ia])
            ia += 1
        else:
            peek = maximum_common_prefix(qa, qb, ia, ib) + 1
            if ia + peek >= len(a) or ib + peek >= len(b):
                result.append(a[ia])
                ia += 1
            elif a[ia + peek] > b[ib + peek]:
                result.append(b[ib])
                ib += 1
            elif a[ia + peek] < b[ib + peek]:
                result.append(a[ia])
                ia += 1
            else:
                print("Shouldn't happen!")
                # print(a[ia:])
                # print()
                # print(b[ib:])
                print()
                print(peek, a[ia + peek], b[ib + peek])
                sys.exit(1)

    result.append(a[ia:])
    result.append(b[ib:])

    return ''.join(result)


if __name__ == '__main__':
    test_cases = read_numbers()[0]
    for t in range(test_cases):
        a = sys.stdin.readline().strip()
        b = sys.stdin.readline().strip()
        print(morgan(a, b))
