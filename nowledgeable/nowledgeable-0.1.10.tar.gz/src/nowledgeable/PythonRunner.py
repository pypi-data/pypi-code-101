# -*- coding:utf-8 -*-

from io import StringIO
import sys
import functools
import os
import re
import time

from lib.executeCode import *
from lib.OneFileCodeRunner import OneFileCodeRunner, read_file_content

__open = open
__print = print
__sum = sum
__sorted = sorted
__max = max
__min = min
__abs = abs
__type = type


class PythonRunner():

    def get_datasets(self):

        return [
            {
                'filename': 'CT_scan.dcm',
                'path': 'data'
            },
            {
                'filename': 'movie-lens-small',
                'path': 'data'
            },
            {
                'filename': 'ct_scan',
                'path': 'data'
            },
            {
                'filename': 'utils.py',
                'path': 'python_utils'
            },
            {
                'filename': 'houses.csv',
                'path': 'data'
            },
            {
                'filename': 'tumor_data_two_var.csv',
                'path': 'data'
            }
        ]

    def get_lib_files(self):

        return [
            {
                'name': 'utils.py',
                'content': self.utils_code,
                'targetPathInBackend': './'
            },
            {
                'name': 'JsonEncoder.py',
                'content': self.json_encoder_code,
                'targetPathInBackend': './'
            }
        ]

   

    def check_quality(self, path):

        from pylint import epylint as lint
        pylint_stdout, pylint_stderr = lint.py_run(path, return_std=True)

        return pylint_stdout

"""
class MultifilePythonRunner(MultifileCodeRunner, PythonRunner):

    def __init__(self):

        self.picture_folder = "pictures"
        self.utils_code = get_util_function_code()
        self.json_encoder_code = get_json_encoder_code()
    
    def _prepare_main_file(self, user_id, main_file):
        pass

"""

class OneFilePythonRunner(OneFileCodeRunner, PythonRunner):

    def __init__(self):

        self.picture_folder = "pictures"
        self.utils_code = get_util_function_code()
        self.json_encoder_code = get_json_encoder_code()


    def run_external_check(self, yaml_path, exercice_data):
        
        user_id = exercice_data['studentId']
        commands = exercice_data['testCommand']
        files = {}
        
        cwd = os.path.join(os.getcwd(), os.path.dirname(yaml_path))
        
        user_picture_folder =  os.path.join(cwd, "pictures")
        
        if not os.path.isdir(user_picture_folder):
            os.mkdir(user_picture_folder)

        return run_exercice_code(cwd, commands, user_picture_folder)

    def _get_default_command(self, files):
       
        return 'PYSPARK_PYTHON="$(which python3)" python3 main.py'

    def _prepare_main_file(self, user_id, user_files):

        user_folder = self._get_user_folder(user_id)

        main_file = user_files[-1]

        user_picture_folder = os.path.join(user_folder, self.picture_folder)
        plot_saving_code = get_plot_code(user_picture_folder)
        
        updated_main = (
            """import warnings; warnings.filterwarnings('ignore')""",
            'from JsonEncoder import CustomEncoder',
            user_files[0]['content'],
            main_file['content'],
            plot_saving_code,
        )

        if 'result_status' in main_file['content']:
            updated_main = updated_main + ('print(CustomEncoder.to_json(result_status))',)
        else: 
            updated_main = updated_main + ('result_status= tester.get_test_output()\nprint(CustomEncoder.to_json(result_status))',)

        user_files[-1]['content'] = "\n".join(updated_main)

    def _prepare_answer_file(self, user_files, code_to_run_before_student_file):
        answer_file = user_files[0]
        answer_code = answer_file['content']
    
        if "was_function_called_with" in user_files[1]['content']:

            updated_student_code = (
                function_redefinition,
                'from utils import AnswerTester',
                'tester = AnswerTester()',
                code_to_run_before_student_file,
                
                'tester.watch_function_calls()',
                answer_code,
                'tester.stop_watch_function_calls()'
            )

            n_line_injected = function_redefinition.count('\n') + code_to_run_before_student_file.count('\n') + 4

        else:
            updated_student_code = (
                function_redefinition,
                'from utils import AnswerTester',
                'tester = AnswerTester()',
                code_to_run_before_student_file,
                answer_code,
            )
            n_line_injected = function_redefinition.count('\n') + code_to_run_before_student_file.count('\n') + 6

        user_files[0]['content'] = "\n".join(updated_student_code)
        
        return n_line_injected
    
    def after_exercice_code_was_run(self, user_id, files, output, n_line_injected):
        print(n_line_injected)
        if output['status'] == 0:
            return
        
        print("la")
        filename = "main"
        stderr = output['stderr']
        pattern = r'{}\.py.* line (\d+)'.format(filename)

        replacer = lambda m: '{}.py" line {}'.format(filename, str(int(m.group(1)) - n_line_injected))

        updated_stderr = re.sub(pattern, replacer, stderr)

        output['stderr'] = updated_stderr



def line_contains_variable(line):

    g = re.match("^(\w+)$", line)

    if not g:
        return (False, None)
    groups = g.groups()

    return (True, groups[0]) if len(groups) > 0 else (False, None)


def prepare_submission(code):

    last_line = code.split("\n")[-1]

    #is_a_variable, variable_name = line_contains_variable(last_line)

    #if is_a_variable:
    #    return code + "\nprint({})".format(variable_name)

    function_tracer_code = ""
    #code = function_tracer_code + code


    return code



def get_util_function_code():

    import os

    current_folder = os.path.dirname(os.path.realpath(__file__))
    
    
    return read_file_content(current_folder + '/utils.py')


def get_json_encoder_code():

    import os

    current_folder = os.path.dirname(os.path.realpath(__file__))
    return read_file_content(current_folder + '/JsonEncoder.py')


def get_plot_code(picture_folder):

    code ="""

import matplotlib.pyplot as plt
if len(plt.get_fignums()) > 0:
    
    for i in plt.get_fignums():
        plt.figure(i)
        path = '{}/figure_%d.png' % i
        
        plt.savefig(path)
    

""".format(picture_folder)

    return code


function_redefinition = """
__open = open; __print = print; __sum = sum; __sorted = sorted; __max = max; __min = min; __abs = abs; __type = type;
def open(file, model='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None): 
               return __open(file, model, buffering, encoding, errors, newline, closefd, opener)
def print(*args): __print(*args);
def sum(v): return __sum(v)
def sorted(l, *args, **kwargs): return __sorted(l, *args, **kwargs)
def max(values, *args, **kwargs): return __max(values, *args, **kwargs)
def min(values, *args, **kwargs): return __min(values, *args, **kwargs)
def abs(x): return __abs(x)
def type(object): return __type(object)"""
"""



        def open(file, model='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
            return __open(file, model, buffering, encoding, errors, newline, closefd, opener)

        def print(*args):
            __print(*args);

        def sum(v):
            return __sum(v)

        def sorted(l, *args, **kwargs):
            return __sorted(l, *args, **kwargs)

        def max(values, *args, **kwargs):
            return __max(values, *args, **kwargs)

        def min(values, *args, **kwargs):
            return __min(values, *args, **kwargs)

        def abs(x):
            return __abs(x)

        def type(object):
            return __type(object)



"""



"""
    scope = {
        'compare_results': compare_results
    }
    try:

        exec(code_to_run, globals(), scope)

    except BaseException as err:

        error = {
            'message': str(err)
        }
        return error
    except SyntaxError as err:

        error = {
            'text': err.text,
            'line': err.lineno,
            'message': err.msg
        }
        return {
            'error': error
        }
    except NameError as err:
        error = {
            'message': err.args
        }
        return {
            'error': error
        }

    if 'result_status' in scope:
        return {
            'error': error,
            'output': scope['result_status']
        }

    return {
        'error': {
            'message': 'result_status variable does not exists'
    }
    
    
 
   
   
class Capturing(list):

    """"""
	with Capturing() as outpout:
             func_call()
	src: https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call

       can be stack by adding previous output in next with Capturint(output)
	see also second answer for pyton>=3.4
	""""""
    def __enter__(self):
         self._stdout = sys.stdout
         sys.stdout = self._stringio = StringIO()
         return self
    
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

 


def evaluate_jupyter_notebook_cell():

    pass

def evaluate_script(str_script, output_variable_to_test, expected_value):

    exec(str_script)

    exec("submitted_value = {}".format(output_variable_to_test))

    output = compare_results(submitted_value, expected_value)

    return output 
 

def evaluate_code_on_inputs(inputs, function_to_test):

    results = []
    for input_arguments in inputs:
        exec("ouput = function_to_test(*input_arguments)")
        results.append(ouput)
    return results


def test_exercice_submission(solution_function_name, str_solution_code, input_generator_name, str_test_code):

    try:
        exec(str_test_code)
        exec("arguments = input_generator()")
        outputs = evaluate_code_on_inputs(arguments, solution)
        
    except(e):
        pass
        
 



def append_fonction_name(function_code, suffix):

    def repl(match, s=suffix):

        return "def {}{}{}".format(match.group(1), s, match.group(2))

    r = re.sub("\w+\s+(\w*)(.*)", repl, function_code)
    return r

def dynamic_python_test(function_name,
                        str_submited_answer,
                        str_solution,
                        str_input_generator,
                        available_files=[]):

    scope = {}

    exec(str_input_generator, scope)
    arguments = scope['input_generator']()

    solution_scope = {}
    exec(str_solution, solution_scope)
    solution_function = solution_scope[function_name]

    submission_scope = {}
    exec(str_submited_answer, submission_scope)
    submission_function = submission_scope[function_name]

    return compare_results(solution_function, submission_function, arguments)



def build_function_call_str(nomFonction, listeArguments):

    appelFonction = nomFonction + "("
    for i in range(len(listeArguments)):
        appelFonction += str(listeArguments[i])
        appelFonction += "," if i != len(listeArguments) - 1 else ""
    appelFonction += ")"

    return appelFonction

 
 
def PythonCodeRunner():

    def __init__(self): pass

    def one_file_exercice_run(self, user_id, solution_checking_code, student_submission):

        return python_one_file_exercice_run(user_id, solution_checking_code, student_submission) 
 
"""
