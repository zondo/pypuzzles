"""
Usage: {prog} [options] STRING

Description:
    Solve the Number Plate puzzle.

    Given the 3 consecutive letters on a UK number plate (e.g, for KS17 HRP
    it would be HRP), what's the smallest word you can find containing those
    letters in the same order?  Any letters before, in between, or after
    are allowed.

Options:
    -m, --maxwords=NUM   Print this many matches [default: 10]
    -t, --trace          Print traceback on error
    -h, --help           This help message
"""

import re
from .words import get_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        maxwords = int(opts["--maxwords"])
        solve(string, maxwords=maxwords)

    cli.run("numberplate", func, __doc__)


def numberplate(letters, wild=".*", words=None):
    """Yield words fitting the number plate letters, sorted by length.
    """

    if not words:
        words = get_words()

    pattern = wild + wild.join(letters) + wild
    words = filter(lambda w: re.match(pattern, w), words)
    return sorted(words, key=lambda w: len(w))


def solve(letters, maxwords=10):
    for word in numberplate(letters.lower())[:maxwords]:
        print(word.upper())
