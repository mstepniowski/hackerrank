import sys
from collections import Counter

a = Counter(sys.stdin.readline().strip())
b = Counter(sys.stdin.readline().strip())
print sum((a - b).values()) + sum((b - a).values())
