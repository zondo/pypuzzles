"""
Usage: {prog} [options] TOTAL NUM [NUM...]

Description:
    Solve the Radio Times countdown puzzle.

    Using addition, subtraction, multiplication and division, try to get as
    close to the target as possible.  You can use each of the six numbers
    only once, but you don't have to use them all.

Options:
    -t, --trace      Print traceback on error
    -h, --help       This help message

"""

from __future__ import division

import itertools as it
from operator import add, mul, sub
from operator import truediv as div

from . import cli

OPERATORS = {
    add: "+",
    sub: "-",
    mul: "*",
    div: "/",
}

OPLIST = list(OPERATORS.keys())


def main():
    def func(opts):
        total = int(opts["TOTAL"])
        numbers = map(int, opts["NUM"])
        solve(total, *numbers)

    cli.run("countdown", func, __doc__)


def solve(total, *numbers):
    seen = set()
    for sol in countdown(total, *numbers):
        if sol not in seen:
            seen.add(sol)
            print(sol)


def countdown(total, *numbers):
    for used in range(len(numbers), 1, -1):
        for perm in it.permutations(numbers, used):
            for oplist in it.product(OPLIST, repeat=used - 1):
                if total == evaluate(perm, oplist):
                    yield formatted(perm, oplist)


def evaluate(numbers, oplist):
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
