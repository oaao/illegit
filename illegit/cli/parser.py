import argparse

from .commands import Cmd

# to be called in illegit mainfile with COMMANDS[args.command](args)
COMMANDS = {
    'add':         Cmd.add,
    'cat-file':    Cmd.cat_file,
    'checkout':    Cmd.checkout,
    'commit':      Cmd.commit,
    'hash-object': Cmd.hash_object,
    'init':        Cmd.init,
    'log':         Cmd.log,
    'ls-tree':     Cmd.ls_tree,
    'merge':       Cmd.merge,
    'rebase':      Cmd.rebase,
    'rev-parse':   Cmd.rev_parse,
    'rm':          Cmd.rm,
    'show-ref':    Cmd.show_ref,
    'tag':         Cmd.tag
}

p     = argparse.ArgumentParser(description='illegit command processor')
p_sub = p.add_subparsers(title='Commands', dest='command')
