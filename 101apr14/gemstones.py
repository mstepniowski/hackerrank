import sys
import string


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


if __name__ == '__main__':
    n = read_numbers()[0]
    gem_elements = set(string.ascii_lowercase)
    for i in range(n):
        stone = sys.stdin.readline().strip()
        gem_elements = gem_elements & set(stone)
    print(len(gem_elements))
