"""
Usage: {prog} [options] STRING

Description:
    Solve the Merriam-Webster blossom game.

    Find as many words as possible using letters in the grid.  Each must
    use the central letter and at least three others.  Letters may be used
    more than once.  You may not use plurals, foreign words or proper
    nouns.  There is at least one seven-letter word to be found.

Options:
    -m, --minlen=NUM   Set minimum word length [default: 4]
    -t, --trace        Print traceback on error
    -h, --help         This help message
"""

from .words import get_words, print_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        minlen = int(opts["--minlen"])
        solve(string, minlen)

    cli.run("blossom", func, __doc__)


def blossom(letters, minlen=4):
    """Yield blossom words.

    Each word must contain the first letter.
    """

    first = letters[0]
    letters = set(letters.lower())

    for word in get_words():
        if len(word) >= minlen and first in word and set(word).issubset(letters):
            yield word.upper()


def solve(letters, minlen):
    words = blossom(letters, minlen)
    print_words(letters, words)
