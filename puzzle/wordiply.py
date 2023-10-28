"""
Usage: {prog} [options] STRING

Description:
    Solve the Guardian wordiply puzzle.

    Find the longest word possible which contains the given letters.

Options:
    -m, --maxwords=NUM   Print this many words [default: 5]
    -t, --trace          Print traceback on error
    -h, --help           This help message
"""

from .words import get_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        maxwords = int(opts["--maxwords"])
        solve(string, maxwords)

    cli.run("wordiply", func, __doc__)


def solve(letters, maxwords):
    words = wordiply(letters)
    words = list(sorted(words, key=lambda w: -len(w)))

    for word in words[:maxwords]:
        print(f"{len(word):2} {word.upper()}")


def wordiply(letters):
    """Yield wordiply words.

    Each word must contain the given letters.
    """

    for word in get_words():
        if letters in word:
            yield word
