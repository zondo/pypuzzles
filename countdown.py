"""Solve Countdown puzzles.
"""

from __future__ import division

import itertools as it
from operator import add, mul, sub
from operator import truediv as div

OPERATORS = {
    add: "+",
    sub: "-",
    mul: "*",
    div: "/",
}

OPLIST = list(OPERATORS.keys())


def solve(total, *numbers):
    for sol in countdown(total, *numbers):
        print(sol)


def countdown(total, *numbers):
    for used in range(len(numbers), 1, -1):
        for perm in it.permutations(numbers, used):
            for oplist in it.product(OPLIST, repeat=used - 1):
                if total == evalulate(perm, oplist):
                    yield formatted(perm, oplist)


def evalulate(numbers, oplist):
    total, numbers = numbers[0], numbers[1:]

    for func, num in zip(oplist, numbers):
        total = func(total, num)

    return total


def formatted(numbers, oplist):
    start, numbers = numbers[0], numbers[1:]
    fmt = str(start)

    for func, num in zip(oplist, numbers):
        fmt += " " + OPERATORS[func]
        fmt += " " + str(num)

    return fmt


if __name__ == '__main__':
    #solve(787, 50, 5, 10, 4, 5, 3)
    solve(204, 100, 25, 1, 9, 9, 1)
