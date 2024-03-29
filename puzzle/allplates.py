"""
Find the minimal solutions for all possible number plates.
"""

import string
import itertools as it

from puzzle.numberplate import numberplate
from puzzle.words import get_words


if __name__ == "__main__":
    words = get_words()
    for combo in it.product(string.ascii_lowercase, repeat=3):
        letters = "".join(combo)
        wordlist = list(numberplate(letters, words=words))
        if wordlist and len(wordlist[0]) > 5:
            minlen = len(wordlist[0])
            wordlist = filter(lambda w: len(w) == minlen, wordlist)
            wordlist = " ".join(w.upper() for w in wordlist)
            print(f"{letters.upper()}: {wordlist}")
