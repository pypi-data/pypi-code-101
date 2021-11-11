import sys
import getopt

from . import DiskHashTree


HELP = '''Python Disk Hash Tree

Command-line interface for creating and managing hash trees built using
files and directories on the filesystem.

OPTIONS:
    -h
        Help. Print this message and exit.

    -d DIR
        Directory. Select the root directory DIR for the hash tree. This must be
        an empty directory and by default it is the current directory.

    -p PREFIX_LEN
        Prefix length. PREFIX_LEN must be an integer and determines the length
        of the string from the start of the provided key which is used for
        comparisons and subdirectories. Usually the smaller the better.
        PREFIX_LEN must be a minimum of 1 and a maximum of the length of the
        key. By default, this is 2.

FUNCTIONS:
    -a KEY, --add=KEY
        Adds KEY to the hash tree. Returns 0 always.

    -r KEY, --remove=KEY
        Removes KEY from the hash tree. Returns 0 always.

    -c KEY, --contains=KEY
        Checks whether KEY is in the hash tree. Returns 0 if the element is in
        the tree, else returns 1. Will also print "YES" and "NO" to stdout
        respectively.

AUTHOR:
    Written by Marcus Belcastro

SEE ALSO:
    Source code: https://gitlab.com/delta1512/disk-hash-tree
'''

root_dir = './'
func = None
key = ''
prefix_len = 2


opts, args = getopt.getopt(sys.argv[1:], 'hd:a:r:c:p:', ['add=', 'remove=', 'contains='])

for opt, arg in opts:
    if opt == '-h':
        print(HELP)
        sys.exit(0)
    elif opt == '-d':
        root_dir = arg
    elif opt == '-p':
        prefix_len = int(arg)
    elif opt in ('-a', '--add'):
        func = 'add'
        key = arg
    elif opt in ('-r', '--remove'):
        func = 'remove'
        key = arg
    elif opt in ('-c', '--contains'):
        func = 'contains'
        key = arg


dht = DiskHashTree(root_dir, prefix_len)

if func is None:
    print(HELP)
    sys.exit(-1)
elif func == 'add':
    dht.add(key)
    sys.exit(0)
elif func == 'remove':
    dht.discard(key)
    sys.exit(0)
elif func == 'contains':
    if dht.contains(key):
        print('YES')
        sys.exit(0)
    else:
        print('NO')
        sys.exit(1)
