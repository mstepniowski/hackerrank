# https://www.hackerrank.com/contests/w2/challenges/cut-the-tree
import sys
from collections import defaultdict


sys.setrecursionlimit(2 * 10 ** 5)


def solve(values, edges):
    """Recursive solution."""
    tree_sum = sum(values)
    min_tree_diff = tree_sum
    m = {}

    def subtree_sum(v, w):
        """Sum of numbers in subtree pointed by edge v->w (including w)"""
        if m.get((v, w)) is None:
            m[(v, w)] = values[w - 1] + sum(subtree_sum(w, u) for u in edges[w] if u != v)
        return m[(v, w)]

    for v, ws in edges.items():
        for w in ws:
            ss = subtree_sum(v, w)
            tree_diff = abs(ss - (tree_sum - ss))
            min_tree_diff = min(min_tree_diff, tree_diff)
    return min_tree_diff


def solve_with_trampoline(values, edges):
    """Non-recursive solution using ad-hock stack."""
    tree_sum = sum(values)
    min_tree_diff = tree_sum
    m = {}

    def subtree_sum(v, w):
        """Sum of numbers in subtree pointed by edge v->w (including w)"""
        stack = [('call', v, w)]
        while stack:
            action, v, w = stack.pop()
            if m.get((v, w)) is not None:
                continue
            if action == 'return':
                m[(v, w)] = values[w - 1] + sum(m[(w, u)] for u in edges[w] if u != v)
            else:
                stack.append(('return', v, w))
                stack.extend(('call', w, u) for u in edges[w] if u != v)
        return m[(v, w)]

    for v, ws in edges.items():
        for w in ws:
            ss = subtree_sum(v, w)
            tree_diff = abs(ss - (tree_sum - ss))
            min_tree_diff = min(min_tree_diff, tree_diff)
    return min_tree_diff


def read_numbers():
    return [int(x) for x in sys.stdin.readline().split()]


if __name__ == '__main__':
    N = int(raw_input())
    values = read_numbers()
    edges = defaultdict(list)
    for _ in range(N - 1):
        v, w = read_numbers()
        edges[v].append(w)
        edges[w].append(v)
    print solve_with_trampoline(values, edges)
