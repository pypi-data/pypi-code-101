import sys

from matomerumi_lib import parse_cmd, MMI

if __name__ == '__main__':
    argv = sys.argv[:]
    argc = len(argv)
    ifile, ofile, mmic = parse_cmd(argc, argv)
    runner = MMI(ifile, mmic, '__main__')
    with open(str(ofile), 'wb') as out:
        out.write(runner.run())
