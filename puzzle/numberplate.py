"""
Usage: {prog} [options] STRING

Description:
    Solve the Number Plate puzzle.

    Given the 3 consecutive letters on a UK number plate (e.g, for KS17 HRP
    it would be HRP), what's the smallest word you can find containing those
    letters in the same order?  Any letters before, in between, or after
    are allowed.

Options:
    -t, --trace      Print traceback on error
    -h, --help       This help message
"""

import re
from .words import get_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        solve(string)

    cli.run("numberplate", func, __doc__)


def numberplate(letters, wild=".*"):
    """Yield words fitting the number plate letters, sorted by length.
    """

    pattern = wild + wild.join(letters.lower()) + wild
    words = filter(lambda w: re.match(pattern, w), get_words())
    return sorted(words, key=lambda w: len(w))


def solve(letters, maxwords=10):
    for word in numberplate(letters)[:maxwords]:
        print(word.upper())
