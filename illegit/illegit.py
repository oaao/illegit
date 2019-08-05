import collections
import configparser  # to read and write Git's .ini-like config file format
import hashlib       # to use SHA-1 hashing
import os
import re
import sys
import zlib          # used by Git for compression

from cli import parser


def test(args):
    print('hi')

def main(argv=sys.argv[1:]):

    args = parser.p.parse_args(argv)

    try:
        parser.COMMANDS[args.command](args)
    except KeyError:
        raise KeyError('Unknown command')
