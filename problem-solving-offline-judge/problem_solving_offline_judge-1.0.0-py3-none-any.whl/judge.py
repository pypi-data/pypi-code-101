import importlib
import sys
import os
import glob
from colorama import init, Fore, Style

init()


class Monitor:
    def __init__(self):
        self.screen = ""

    def write(self, text):
        self.screen += text
        return

    def flush(self):
        self.screen = ""
        return

    def value(self):
        return self.screen


def read_file(filename):
    with open(filename) as f:
        return f.read()


def cli():
    argv = sys.argv
    if len(argv) > 1:
        solve()


def solve(problem_id):
    stdout = sys.stdout
    PACKAGE_AFFIX = "problem_"
    package_name = PACKAGE_AFFIX + problem_id
    problem = importlib.import_module(package_name + ".problem")
    inputs = glob.glob(os.getcwd() + "/" + package_name + "/*.input.txt")
    for input_file in inputs:
        case_id = input_file.replace(os.getcwd() + "/" + package_name + "/",
                                     "").replace(".input.txt", "")
        output_file = os.getcwd() + "/" + package_name + "/" + case_id + ".output.txt"
        sys.stdin = open(input_file, "r")
        monitor = Monitor()
        sys.stdout = monitor
        problem.solve()
        sys.stdout = stdout
        title = 'case #' + case_id
        input_result = monitor.value().strip()
        if os.path.isfile(output_file):
            correct_result = read_file(output_file).strip()
            if input_result == correct_result:
                print(title + ': ' + Fore.GREEN +
                      'SUCCESS!' + Style.RESET_ALL)
            else:
                print(title + ': ' + Fore.RED +
                      'FAIL!\n' + Style.RESET_ALL)

                print(Fore.RED + input_result)
                print(Fore.WHITE + correct_result)
                print(Style.RESET_ALL)
        else:
            print(title + ': ' + Fore.YELLOW + 'DONE!' + Style.RESET_ALL)
            print(input_result)


if __name__ == "__main__":
    cli()
