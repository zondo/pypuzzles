"""Tools for word lists.
"""

import re
import requests_cache

import itertools as it
from collections import defaultdict

DEFAULT_URL = "https://raw.githubusercontent.com/N1xis10t/Corncob/main/corncob_lowercase.txt"


def get_words(url=None, cachefile="~/.words.sqlite"):
    """Return a set of valid words.

    The URL should reference a text file containing a valid word list.
    """

    session = requests_cache.CachedSession(cachefile)
    r = session.get(url or DEFAULT_URL)
    words = set(re.split(r'(\w+)', r.text))

    return words


def print_words(string, words, separator="  "):
    words = list(words)
    total = len(words)
    minlen = min(len(word) for word in words)

    # Create list for each word length, and format to print them.
    lists = defaultdict(list)
    for word in sorted(words):
        lists[len(word)].append(word)

    lengths = list(range(minlen, 10))
    wordlists = [lists[wlen] for wlen in lengths]
    fmt = separator.join(f"%{wlen}s" for wlen in lengths)

    # Print the words.
    print(f"{string.upper()}: {total}")
    print()
    for words in it.zip_longest(*wordlists, fillvalue=""):
        print((fmt % words).rstrip())
