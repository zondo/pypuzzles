"""
Find the longest path in a DAG formed by splitting words into two halves.
"""

import networkx as nx
from puzzle.words import get_words

WORDLEN = 7
MINLEN  = 20

# Ignored words.
IGNORE = """
bandpass
bookwork
casework
ironlady
landside
reallife
sideband
timebase
workfare
"""


def main():
    wordset = get_words()
    ignored = set(IGNORE.lower().strip().split())
    wordset -= ignored

    graph = make_wordlinks(wordset, WORDLEN)
    nx.write_adjlist(graph, "wordlink.txt")
    for first, second in find_cycles(graph, MINLEN):
        print(first, second)


def make_wordlinks(wordset, wordlen):
    "Make a DAG from a word set."

    g = nx.DiGraph()
    words = [w.upper() for w in wordset if len(w) == wordlen]
    idx1 = wordlen // 2
    idx2 = wordlen - idx1

    for word in words:
        first, second = word[:idx1], word[idx1:]
        g.add_edge(first, second)
        first, second = word[:idx2], word[idx2:]
        g.add_edge(first, second)

    return g


def find_cycles(graph, minlen):
    longest = []
    for elt in nx.simple_cycles(graph):
        if len(elt) > len(longest):
            longest = elt
            longlen = len(longest)
            if longlen >= minlen:
                break

    if longest:
        first = longest[0]
        for second in longest[1:]:
            yield first, second
            first = second

        yield second, longest[0]


if __name__ == '__main__':
    main()
