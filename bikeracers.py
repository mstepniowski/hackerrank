import sys


def dist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def solve(bikers, bikes, K):
    distances = []
    for biker in bikers:
        for bike in bikes:
            distances.append((dist(biker[1], bike[1]), biker[0], bike[0]))
    distances.sort()


def read_numbers():
    return [int(x) for x in sys.stdin.readline().split()]

if __name__ == '__main__':
    N, M, K = read_numbers()
    bikers = [(n, read_numbers()) for n in range(N)]
    bikes = [(m, read_numbers()) for m in range(M)]
    print solve(bikers, bikes, K)
