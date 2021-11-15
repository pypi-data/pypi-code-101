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
    if timeout == -1:
        timeout = None
    stop_string = ["$STOP_FLAG", "ssdlh_lhbzj_ddxss"]
    command = command + '\n' + f'echo {stop_string[0]}'
    command = command.replace(',', ' ')
    if debug:
        # 关闭输出到标准输出
        child = pexpect.spawn(f'su {user}', encoding='utf-8', logfile=sys.stdout)
    else:
        child = pexpect.spawn(f'su {user}', encoding='utf-8')
    index = child.expect('Password:')

    child.sendline(password)
    child.sendline(command)
    # child.expect([stop_string, pexpect.TIMEOUT], timeout=timeout)
    child.expect([stop_string[1], pexpect.TIMEOUT], timeout=timeout)
            
    

def main():
    args = parse()
    change_user(args.user, args.password, args.command, args.expect, args.debug, args.timeout)



if __name__ == "__main__":
    main()