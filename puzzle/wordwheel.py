"""
Usage: {prog} [options] STRING

Description:
    Solve the Guardian word wheel puzzle.

    Find as many words as possible using letters in the wheel.  Each must
    use the central letter and at least two others.  Letters may be used
    only once.  You may not use plurals, foreign words or proper
    nouns.  There is at least one nine-letter word to be found.

Options:
    -m, --minlen=NUM   Set minimum word length [default: 3]
    -t, --trace        Print traceback on error
    -h, --help         This help message
"""

from collections import Counter
from string import ascii_lowercase as alphabet

from .words import get_words, print_words
from . import cli


def main():
    def func(opts):
        string = opts["STRING"]
        minlen = int(opts["--minlen"])
        solve(string, minlen)

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


def solve(letters, minlen):
    words = wordwheel(letters, minlen)
    print_words(letters, words)
