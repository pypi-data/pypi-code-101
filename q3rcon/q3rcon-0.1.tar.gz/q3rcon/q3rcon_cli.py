#!/usr/bin/env python3

import argparse
import cmd
import getpass
import logging
import q3rcon


class RconShell(cmd.Cmd):

    def __init__(self, prompt, rconsole):
        super().__init__()
        self.intro = 'Welcome to %s. Type help or ? to list commands.\n' % prompt
        self.prompt = '(%s) ' % prompt
        self._rconsole = rconsole
        self._rconsole.connect()

    def do_status(self, arg):
        'Print game status'
        print(self._rconsole.run("status"))

    def do_map(self, arg):
        'Change map'
        print(self._rconsole.run("map %s" % arg))

    def do_quit(self, arg):
        'Quit shell'
        return True


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument(dest="host", nargs="?", type=str, default="localhost", help="Hostname or IP address and port")
    args = parser.parse_args()
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    rcon_args = {}
    
    if args.host:
        array = args.host.split(":")
        rcon_args['host'] = array.pop()
        if array:
            rcon_args['port'] = array.pop()

    rcon_args['password'] = getpass.getpass()

    rconsole = q3rcon.Rcon(**rcon_args)

    RconShell(rcon_args['host'], rconsole).cmdloop()


if __name__ == '__main__':
    main()
