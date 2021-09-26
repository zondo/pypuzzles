"""
Usage: {prog} [options] STRING

Description:
    Solve the Guardian word wheel puzzle.

Options:
    -t, --trace      Print traceback on error
    -h, --help       This help message
"""

from collections import Counter
from itertools import groupby
from string import ascii_lowercase as alphabet
from textwrap import fill

from .words import get_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        solve(string)

    cli.run("wordwheel", func, __doc__)


def wordwheel(letters, minlen=3):
    """Yield word wheel words.

    Each word must contain the first letter.
    """

    letters = letters.lower()
    count = Counter(letters)
    for word in get_words():
        wcount = Counter(word)
        for letter in alphabet:
            if count[letter] < wcount[letter]:
                break
        else:
            if letters[0] in word and len(word) >= minlen:
                yield word.upper()


def printwords(letters, words, indent=4, width=60):
    words = list(sorted(words, key=len))

    print(letters.upper() + ":", len(words))
    print()

    for length, wlist in groupby(words, key=len):
        text = " ".join(sorted(wlist))
        tag = "%-*d" % (indent, length)
        print(fill(text, width=width,
                   initial_indent=tag,
                   subsequent_indent=" " * indent))

    print()


def solve(letters):
    words = wordwheel(letters)
    printwords(letters, words)
