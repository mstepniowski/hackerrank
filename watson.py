import sys

def read_numbers():
    return [int(x) for x in sys.stdin.readline().split()]

N, K, Q = read_numbers()
array = read_numbers()
for _ in range(Q):
    x = input()
    print array[x - K % N]
