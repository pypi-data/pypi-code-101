#!/usr/bin/env python3
import argparse
import os
import sys
import yaml

from seckerwiki.commands.lecture import lecture
from seckerwiki.commands.git import commit, log, sync, status
from seckerwiki.commands.receipt import receipt
from seckerwiki.commands.journal import journal
from seckerwiki.commands.setup import setup
from seckerwiki.commands.toc import toc
from seckerwiki.commands.stats import stats

def main():

  parser = argparse.ArgumentParser()

  # Global arguments
  # parser.add_argument("-c", "--config", help="custom path to wiki config file", default=None)

  # Add all the subparsers 
  subparsers = parser.add_subparsers()

  # Disabled because I don't need lecture functionality anymore
  # lecture_parser = subparsers.add_parser('lecture', help='create new lecture slides')
  # lecture_parser.add_argument('-b', '--blank', action='store_true', help='Create blank lecture slides.')
  # lecture_parser.set_defaults(func=lecture)

  setup_parser = subparsers.add_parser('setup', help='setup wiki CLI')
  setup_parser.set_defaults(func=setup)

  log_parser = subparsers.add_parser('log', help='show git log')
  log_parser.set_defaults(func=log)

  status_parser = subparsers.add_parser('status', help='show git status')
  status_parser.set_defaults(func=status)

  commit_parser = subparsers.add_parser('commit', help='commit wiki')
  commit_parser.add_argument('-y', action='store_true', help='Don\'t ask for confirmation before committing')
  commit_parser.add_argument('-a', '--add', action='store_true', help='Add all modified and unstaged files not gitignored')
  commit_parser.set_defaults(func=commit)

  sync_parser = subparsers.add_parser('sync', help='sync with remote repo')
  sync_parser.set_defaults(func=sync)

  journal_parser = subparsers.add_parser('journal', help='make journal entry')
  journal_parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt all unencrypted journal entries')
  journal_parser.add_argument('-d', '--decrypt', help='decrypt filename')
  journal_parser.set_defaults(func=journal)

  toc_parser = subparsers.add_parser('toc', help='generate table of contents in files')
  toc_parser.set_defaults(func=toc)

  stats_parser = subparsers.add_parser('stats', help="wiki stats")
  stats_parser.set_defaults(func=stats)

  args = parser.parse_args()

  # print help and exit if no arguments supplied
  if not hasattr(args, 'func'):
    parser.print_help()
    exit(0)

  # run setup script without config
  if args.func is setup:
    setup() 
    sys.exit()

  cfg = None
  try:
    cfg_file = os.path.expanduser("~/.config/seckerwiki/config.yml")
    with open(os.path.abspath(cfg_file), 'r') as f:
      cfg = yaml.safe_load(f)
  except FileNotFoundError:
    print(f"Config file not found at {cfg_file}. Have you ran `wiki setup`?")
    sys.exit(1)

  # Change directory
  os.chdir(os.path.expanduser(cfg['wiki-root']))

  # Run the subcommand
  args.func(cfg, args)


if __name__ == "__main__":
  main()