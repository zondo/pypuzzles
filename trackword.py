"""
Solve the Radio Times trackword puzzle.
"""

import enchant
import networkx as nx


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


def solve(string, lang="en_GB"):
    """Print trackword solution.
    """

    if enchant.dict_exists(lang):
        d = enchant.Dict(lang)
    else:
        raise ValueError(f"lang must be one of {enchant.list_languages()}")

    def isword(w):
        return d.check(w)

    words = set(trackword(string, wordfunc=isword))
    print(len(words))

    for word in sorted(words, key=lambda w: (len(w), w)):
        print(word.upper())


def trackword(string, minlen=3, wordfunc=None):
    """Yield words in a trackword puzzle.
    """

    # Create trackword graph.
    g = nx.Graph(GRAPH)

    # Create letter mapping.
    string = string.lower()
    lmap = {i: string[i] for i in range(len(string))}

    # Traverse all paths and check for words.
    for path in all_paths(g, minlen):
        word = "".join(lmap[n] for n in path)
        if not wordfunc or wordfunc(word):
            yield word


def all_paths(graph, minlen=0):
    """Yield all paths of a minimum length twixt any two nodes in a graph.
    """

    for source in graph:
        for target in graph:
            paths = nx.all_simple_paths(graph, source, target)
            yield from filter(lambda p: len(p) >= minlen, paths)


if __name__ == "__main__":
    solve("ATENHCIMA")
