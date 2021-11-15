import sys

def _print_commands():
    print("ltools {}".format('0.0.1'))
    print("\nUsage:")
    print("  ltools <command> [options] [args]\n")
    print("Available commands:")
    cmds = {"-h": "查看帮助"}
    for cmdname, cmdclass in sorted(cmds.items()):
        print("  %-13s %s" % (cmdname, cmdclass))



def main(args=None):
    """The main routine."""

    args = sys.argv
    if len(sys.argv) < 2:
        _print_commands()
        return
    command = args.pop(1)
    if command == '-h':
        print('啊哈哈哈哈哈！！！！')
    else:
        _print_commands()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    # print('__name__ == __main__')
    main()
