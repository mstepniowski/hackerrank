# https://www.hackerrank.com/contests/w2/challenges/huarongdao
import sys
from heapq import heappush, heappop


def read_numbers():
    return [int(x) for x in sys.stdin.readline().split()]


def h(ex, ey, sx, sy, tx, ty):
    return abs(ex - sx) + abs(ey - sy) + abs(tx - sx) + abs(ty - sy)


def moves(board, ex, ey, sx, sy, k):
    result = []

    # Cheating
    for x, y in [(sx - 1, sy), (sx, sy - 1),
                 (sx + 1, sy), (sx, sy + 1)]:
        if x < 1 or x > len(board):
            continue
        if y < 1 or y > len(board[0]):
            continue
        if board[x - 1][y - 1] == 0:
            continue
        if (x, y) == (ex, ey):
            continue
        result.append((x, y, sx, sy, k))

    # Optimization: If distance between empty space and Cao Cao block
    # is bigger than k, it's alway better to cheat.
    # This reduces solution space from M**2 * N**2 to M * N * K**2.
    if abs(ex - sx) + abs(ey - sy) > k:
        return result

    # Legal moves
    for x, y in [(ex - 1, ey), (ex, ey - 1),
                 (ex + 1, ey), (ex, ey + 1)]:
        if x < 1 or x > len(board):
            continue
        if y < 1 or y > len(board[0]):
            continue
        if board[x - 1][y - 1] == 0:
            continue
        if (x, y) == (sx, sy):
            result.append((x, y, ex, ey, 1))
        else:
            result.append((x, y, sx, sy, 1))

    return result


def astar(board, ex, ey, sx, sy, tx, ty, k):
    transitions = {}
    visited = set()
    queue = [(0, 0, ex, ey, sx, sy, None, None, None, None)]

    while queue:
        costh, distance, ex, ey, sx, sy, last_ex, last_ey, last_sx, last_sy = heappop(queue)
        # print costh, distance, '(', ex, ey, ') (', sx, sy, ')'
        if (ex, ey, sx, sy) in visited:
            continue
        visited.add((ex, ey, sx, sy))
        # transitions[(ex, ey, sx, sy)] = (last_ex, last_ey, last_sx, last_sy)

        if (sx, sy) == (tx, ty):
            return distance, transitions, (ex, ey, sx, sy)

        for ex_, ey_, sx_, sy_, cost in moves(board, ex, ey, sx, sy, k):
            heappush(queue, (h(ex_, ey_, sx_, sy_, tx, ty) + distance + cost, distance + cost,
                             ex_, ey_, sx_, sy_,
                             ex, ey, sx, sy))

    return -1, transitions, (None, None, None, None)


def walk_transitions(transitions, ex, ey, sx, sy):
    result = [(ex, ey, sx, sy)]
    while transitions.get((ex, ey, sx, sy)):
        ex, ey, sx, sy = transitions.get((ex, ey, sx, sy))
        result.append((ex, ey, sx, sy))
    result.reverse()
    return result


def solve(board, queries, k):
    for query in queries:
        ex, ey, sx, sy, tx, ty = query
        distance, transitions, (ex, ey, sx, sy) = astar(board, ex, ey, sx, sy, tx, ty, k)
        # print walk_transitions(transitions, ex, ey, sx, sy)
        print distance


if __name__ == '__main__':
    N, M, K, Q = read_numbers()
    board = []
    queries = []
    for _ in range(N):
        board.append(read_numbers())
    for _ in range(Q):
        queries.append(read_numbers())
    solve(board, queries, K)
