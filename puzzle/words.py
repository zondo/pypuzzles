"""Tools for word lists.

TODO: Allow other word lists
"""

import re
import requests_cache

URL = "http://www.mieliestronk.com/corncob_lowercase.txt"


def get_words(minlen=None, maxlen=None):
    session = requests_cache.CachedSession("words")
    r = session.get(URL)

    words = set(re.split(r'(\w+)', r.text))

    if minlen is not None:
        words = set(w for w in words if len(w) >= minlen)

    if maxlen is not None:
        words = set(w for w in words if len(w) <= maxlen)

    return words
