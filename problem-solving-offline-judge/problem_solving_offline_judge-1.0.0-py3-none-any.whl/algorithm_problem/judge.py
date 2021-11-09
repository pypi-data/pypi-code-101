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


def cli(*, problem_package="problem_:id", problem_module_name="problem", input_file_name=":id.input.txt", output_file_name=":id.output.txt"):
    argv = sys.argv
    if len(argv) > 1:
        solve(argv[1], problem_package=problem_package, problem_module_name=problem_module_name,
              input_file_name=input_file_name, output_file_name=output_file_name)


def solve(problem_id, *, problem_package, problem_module_name, input_file_name, output_file_name):
    stdout = sys.stdout
    package_name = problem_package.replace(":id", problem_id)
    module = importlib.import_module(package_name + "." + problem_module_name)
    package_path = os.getcwd() + "/" + package_name
    inputs = glob.glob(package_path + "/" +
                       input_file_name.replace(":id", "*"))
    for input_file in inputs:
        splited = input_file_name.split(":id")
        case_id = input_file.replace(
            package_path + "/" + splited[0], "").replace(splited[1], "")
        output_file = package_path + "/" + \
            output_file_name.replace(":id", case_id)
        sys.stdin = open(input_file, "r")
        monitor = Monitor()
        sys.stdout = monitor
        module.solve()
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
