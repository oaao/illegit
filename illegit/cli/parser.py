import argparse

from .commands import *

# to be called in illegit mainfile with COMMANDS[args.command](args)
COMMANDS = {
    'add':         add,
    'cat-file':    cat_file,
    'checkout':    checkout,
    'commit':      commit,
    'hash-object': hash_object,
    'init':        init,
    'log':         log,
    'ls-tree':     ls_tree,
    'merge':       merge,
    'rebase':      rebase,
    'rev-parse':   rev_parse,
    'rm':          rm,
    'show-ref':    show_ref,
    'tag':         tag
}

p     = argparse.ArgumentParser(description='illegit command processor')
p_sub = p.add_subparsers(title='Commands', dest='command')
