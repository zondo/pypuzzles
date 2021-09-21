"""Common CLI tools.
"""

import sys
import docopt

from . import __version__


def run(progname, func, usage, args=sys.argv[1:]):
    version = f"{progname} {__version__}"
    usage = usage.format(prog=progname)
    opts = docopt.docopt(usage, argv=args, version=version)

    try:
        func(opts)
    except Exception as exc:
        trace = opts.get("--trace", False)
        if trace:
            raise
        else:
            sys.exit("%s: error: %s" % (progname, str(exc)))
