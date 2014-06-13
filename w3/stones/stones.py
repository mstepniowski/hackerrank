# https://www.hackerrank.com/contests/w3/challenges/half

def dlog(n):
    result = 0
    while n > 1:
        n = n / 2
        result += 1
    return result


def solve(n):
    # If number of stacks is odd, xor is always 1.
    # Let's remove the single stone from first stack and call it done.
    if n & 1 == 1:
        return 1

    # Otherwise, there are two stacks that matter: with [1] and [power] moves.
    power = dlog(n) + 1
    lowest_stack_power = 2 ** dlog(power)

    if lowest_stack_power == power:
        moves_to_make = power - 1
        moves_left = 1
    else:
        moves_to_make = lowest_stack_power - (lowest_stack_power ^ power ^ 1)
        moves_left = lowest_stack_power - moves_to_make
    # print bin(power), bin(lowest_stack_power), bin(lowest_stack_power ^ power ^ 1), moves_to_make, moves_left
    lowest_stack_size = 2 ** (lowest_stack_power - 1)
    return lowest_stack_size - (2 ** moves_left - 1)


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        n = int(raw_input())
        print solve(n)
