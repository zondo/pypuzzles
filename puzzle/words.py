"""Tools for word lists.
"""

import re
import requests_cache

DEFAULT_URL = "http://www.mieliestronk.com/corncob_lowercase.txt"


def get_words(url=None, cachefile="~/.words.sqlite"):
    """Return a set of valid words.

    The URL should reference a text file containing a valid word list.
    """

    session = requests_cache.CachedSession(cachefile)
    r = session.get(url or DEFAULT_URL)
    words = set(re.split(r'(\w+)', r.text))

    return words
