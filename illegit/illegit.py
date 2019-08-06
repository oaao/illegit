import collections
import hashlib       # to use SHA-1 hashing
import re
import sys
import zlib          # used by Git for compression

import repo
from cli import parser


def main(argv=sys.argv[1:]):

    args = parser.p.parse_args(argv)

    try:
        parser.COMMANDS[args.command](args)
    except KeyError:
        raise KeyError('Unknown command')
