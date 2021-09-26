"""
Usage: {prog} [options] STRING

Description:
    Solve the Radio Times trackword puzzle.

    How many words of three letters or more can you find by tracking from
    one square to the next, going up, down, sideways or diagonally in
    order?  You may not use the same letter square twice in any word.
    Proper nouns or foreign words not allowed.  What is the nine-letter
    word?

Options:
    -t, --trace      Print traceback on error
    -h, --help       This help message

"""

import itertools as it
from collections import defaultdict

import networkx as nx

from .words import get_words
from . import cli

# Trackword adjacency graph.
#
#   012
#   345
#   678
GRAPH = {0: [1, 3, 4],
         1: [0, 2, 3, 4, 5],
         2: [1, 4, 5],
         3: [0, 1, 4, 6, 7],
         4: [0, 1, 2, 3, 5, 6, 7, 8],
         5: [1, 2, 4, 7, 8],
         6: [3, 4, 7],
         7: [3, 4, 5, 6, 8],
         8: [4, 5, 7]}


def main():
    def func(opts):
        string = opts["STRING"]
        solve(string)

    cli.run("trackword", func, __doc__)


def solve(string, lang="en_GB"):
    """Print trackword solution.
    """

    # Set up dictionary.
    d = get_words()

    def isword(w):
        return w in d

    # Get the words.
    words = set(trackword(string, wordfunc=isword))
    total = len(words)

    # Create list for each word length, and format to print them.
    lists = defaultdict(list)
    for word in sorted(words):
        lists[len(word)].append(word)

    lengths = list(range(3, 10))
    wordlists = [lists[wlen] for wlen in lengths]
    fmt = " ".join(f"%{wlen}s" for wlen in lengths)

    # Print the words.
    print(f"{total} words found")
    print()
    for words in it.zip_longest(*wordlists, fillvalue=""):
        print(fmt % words)


def trackword(string, minlen=3, wordfunc=None):
    """Yield words in a trackword puzzle.
    """

    # Create trackword graph.
    g = nx.Graph(GRAPH)

    # Create letter mapping.
    string = string.lower()
    lettermap = {i: string[i] for i in range(len(string))}

    # Traverse all paths and check for words.
    for path in all_paths(g, minlen):
        word = "".join(lettermap[n] for n in path)
        if not wordfunc or wordfunc(word):
            yield word.upper()


def all_paths(graph, minlen=0):
    """Yield all paths of a minimum length twixt any two nodes in a graph.
    """

    for source in graph:
        for target in graph:
            paths = nx.all_simple_paths(graph, source, target)
            yield from filter(lambda p: len(p) >= minlen, paths)
