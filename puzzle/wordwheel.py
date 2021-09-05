"""Word wheel.
"""

from collections import Counter
from itertools import groupby
from string import ascii_lowercase as alphabet
from textwrap import fill

from words import get_words


def wordwheel(letters):
    """Yield word wheel words.

    Each word must contain the first letter.
    """

    letters = letters.lower()
    count = Counter(letters)
    for word in get_words(3, 9):
        wcount = Counter(word)
        for letter in alphabet:
            if count[letter] < wcount[letter]:
                break
        else:
            if letters[0] in word:
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


if __name__ == "__main__":
    solve('LRUNDGNTI')
