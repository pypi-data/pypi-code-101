import pexpect
import argparse
import sys

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', type=str, required=True)
    parser.add_argument('-p', '--password', type=str, required=True)
    parser.add_argument('-c', '--command', type=str, required=True)
    parser.add_argument('-e', '--expect', type=str, default='-*Best result.*')
    parser.add_argument('--debug', type=int, default=1)
    parser.add_argument('--timeout', type=int, default=-1)
    args = parser.parse_args()
    return args

def change_user(user, password, command, expect='-*Best result.*', debug=1, timeout=-1):
    print(expect)
    if timeout == -1:
        timeout = None
    command = command.replace(',', ' ')
    if debug:
        # 关闭输出到标准输出
        child = pexpect.spawn(f'su {user}', encoding='utf-8', logfile=sys.stdout)
    else:
        child = pexpect.spawn(f'su {user}', encoding='utf-8')
    index = child.expect('Password:')

    child.sendline(password)
    child.sendline(command)
    child.expect([expect, pexpect.TIMEOUT], timeout=timeout)
            
    

def main():
    args = parse()
    change_user(args.user, args.password, args.command, args.expect, args.debug, args.timeout)



if __name__ == "__main__":
    main()