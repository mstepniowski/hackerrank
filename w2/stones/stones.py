# https://www.hackerrank.com/contests/w2/challenges/manasa-and-stones

def stones(n, a, b):
    a, b = min(a, b), max(a, b)
    diff = b - a
    result = [a * (n - 1)]
    if diff == 0:
        return result
    for i in range(n - 1):
        result.append(result[-1] + diff)
    return result


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(raw_input())
        a = int(raw_input())
        b = int(raw_input())
        print ' '.join(str(s) for s in stones(n, a, b))
