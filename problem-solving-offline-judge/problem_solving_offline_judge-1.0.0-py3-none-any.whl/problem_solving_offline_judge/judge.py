import importlib
import sys
import os
import datetime
import re
from colorama import init, Fore, Style

init()


class Pseudo:
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
        solve(argv[1])


def get_problem_by_keyword(keyword):
    problems = []
    for directory_or_file in os.listdir():
        if os.path.isdir(directory_or_file):
            problems.append(directory_or_file)
    problems = list(filter(lambda x: keyword in x, problems))
    problems.sort(key=lambda x: len(x))
    if len(problems) > 0:
        return problems.pop(0)
    else:
        return None


def solve(problem_keyword):
    stdout_original = sys.stdout
    stdout_pseudo = Pseudo()

    if '/' in problem_keyword:
        print('"/" cannot be used in keywords.')
        return

    problem_directory_name = get_problem_by_keyword(problem_keyword)
    if problem_directory_name == None:
        print(f'No directory with "{problem_keyword}"')
        return
    if problem_directory_name[0] in list(map(str, range(10))):
        print('Problem directories must start with "A-Z", "a-z", or "_".')
        return

    module_name = ""
    p = re.compile("([A-Za-z_]+)\.py")
    for directory_or_file in os.listdir(problem_directory_name):
        m = p.match(directory_or_file)
        if m:
            module_name = m.group(1)
            break
    if module_name == "":
        print('Problem module not found (*.py)')
        return

    module = importlib.import_module(
        problem_directory_name + "." + module_name)
    function_name = ""
    for name in dir(module):
        if name in ["solve", "main", "solution"]:
            function_name = name
    if function_name == "":
        print('It must have a method ("solve" or "main")')
        return
    solve = getattr(module, function_name)

    input_files = []
    for directory_or_file in os.listdir(problem_directory_name):
        if "in" in directory_or_file and ".py" not in directory_or_file:
            input_files.append(directory_or_file)
    input_files.sort()
    if len(input_files) == 0:
        print('An input file is required. (convention: *in*)')
        return

    for input_file in input_files:
        output_file = input_file.replace("in", "out")
        sys.stdin = open(problem_directory_name + '/' + input_file, "r")
        sys.stdout = stdout_pseudo
        stdout_pseudo.flush()

        start_time = datetime.datetime.now()
        solve()
        end_time = datetime.datetime.now()
        delta = end_time - start_time
        ms = delta.microseconds // 1000

        sys.stdout = stdout_original
        title = input_file + f" ({ms} ms)"
        in_result = stdout_pseudo.value().strip()
        if os.path.isfile(problem_directory_name + '/' + output_file):
            out_result = read_file(
                problem_directory_name + '/' + output_file).strip()
            if in_result == out_result:
                print(Fore.GREEN + 'SUCCESS!' + Style.RESET_ALL + ' ' + title)
            else:
                print(Fore.RED + 'FAIL!' + Style.RESET_ALL + ' ' + title)
                print("Result:")
                print(Fore.RED + in_result + Style.RESET_ALL)
                print("Expected:")
                print(Fore.WHITE + out_result + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + 'DONE!' + Style.RESET_ALL + ' ' + title)
            print('An output file is required for verification. (' + output_file + ')')
            print('Result:')
            print(in_result)


if __name__ == "__main__":
    cli()
