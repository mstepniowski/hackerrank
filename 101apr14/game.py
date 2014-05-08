import sys


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    return [int(x) for x in line.split()]


def get(l, i, default=0):
    try:
        return l[i]
    except IndexError:
        return default


def calculate_best_result(stack, best_results, best_moves, i):
    took_one = get(stack, i) + max([0] + [get(best_results, i + 1 + move) for move in get(best_moves, i + 1, [])])
    took_two = get(stack, i) + get(stack, i + 1) + max([0] + [get(best_results, i + 2 + move) for move in get(best_moves, i + 2, [])])
    took_three = get(stack, i) + get(stack, i + 1) + get(stack, i + 2) + max([0] + [get(best_results, i + 3 + move) for move in get(best_moves, i + 3, [])])
    scores = sorted([(took_one, 1), (took_two, 2), (took_three, 3)], reverse=True)
    best_result, best_move = scores[0]
    best_moves = set([best_move])
    for score, move in scores[1:]:
        if score == best_results:
            best_moves.add(move)
    return best_result, best_moves


def game(stack):
    best_results = [0] * len(stack)
    best_moves = [set()] * len(stack)
    for i in range(len(stack) - 1, -1, -1):
        result, move = calculate_best_result(stack, best_results, best_moves, i)
        best_results[i] = result
        best_moves[i] = move
    return best_results[0]


if __name__ == '__main__':
    test_cases = read_numbers()[0]
    for t in range(test_cases):
        n = read_numbers()[0]
        stack = read_numbers()
        print(game(stack))
