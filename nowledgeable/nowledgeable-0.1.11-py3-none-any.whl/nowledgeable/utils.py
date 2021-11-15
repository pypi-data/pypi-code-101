#! /usr/bin/python3
# -*- coding:utf-8 -*-


import sys
import json
import copy
import matplotlib

import collections

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def plot_1D_functions(submitted, expected, inputs):

    submitted_outputs = submitted(inputs)
    expected_outputs = expected(inputs)

    plt.plot(inputs, expected_outputs, c="green")
    try:
        plt.plot(inputs, submitted_outputs, c="black")
    except:
        print('Error: The output of your function does not have the good size. Could not be plotted')
    plt.legend(['Good solution', 'Your solution'])

    plt.show()


class Tracer():

    """"""

    def __init__(self):
        self.calls = {}
        self.returns = {}

    def function_was_called(self, function_name, arguments):

        call = {
            'function_name': function_name,
            'arguments': arguments
        }

        if function_name in self.calls:
            self.calls[function_name].append(call)
        else:
            self.calls[function_name] = [call]

    def function_returned(self, function_name, return_value):

        return_data = {
            'function_name' : function_name,
            'return_value': return_value
        }

        if function_name in self.returns:
            self.returns[function_name].append(return_data)
        else:
            self.returns[function_name] = [return_data]


    def get_function_calls(self):

        return self.calls



def tracefunc(frame, event, arg, func_calls, max_level, restrict_to, level=[0]):

    """
        tracefun

        collects function calls
        usefull to check that the student used a function properly

    """
    if level[0] > max_level:
        return tracefunc

    if event in ["call"]: #including c_call make go too much deep

        level[0] += 1

        func_name = frame.f_code.co_name

        if "import_module" in func_name:
            return tracefunc

        if len(restrict_to)>0:
            if not func_name in restrict_to:
                return tracefunc

        arguments = collections.OrderedDict(sorted(frame.f_locals.items()))

        func_calls.append({
            'name': func_name,
            'arguments': arguments
        })


    if event in ["return"]:
        level[0] -= 1

    return tracefunc


def AnswerTester():
    """
        Singleton pattern

    :param tracer:
    :return:
    """

    if AnswerTesterB._instance is None:
        AnswerTesterB._instance = AnswerTesterB()


    return AnswerTesterB._instance


class AnswerTesterB():

    """
        Test class generating exercice report


    """

    _instance = None

    TESTS = {
        'compare_object_attributes': 'compare_object_attributes',
        'function_called': 'function_called'
    }

    def __init__(self):

        self.tests = []
        self.func_to_watch = []

        self.func_calls = []
        self.max_level = 200

    def set_max_watch_depth(self, level):
        self.max_level = level

    def watch_function_calls(self, restrict_to=[]):

        import functools

        tracer = functools.partial(tracefunc, restrict_to=restrict_to, max_level=self.max_level, func_calls=self.func_calls)
        sys.setprofile(tracer)


    def stop_watch_function_calls(self):

        sys.setprofile(None)

    def compare_object_attributes(self, test_name, submitted_object, expected_object, message=""):

        self.tests.append({
            'name': test_name,
            'type': self.TESTS['compare_object_attributes'],
            'submitted': submitted_object,
            'expected': expected_object,
            'message': message
        })


    def was_function_called_with(self, test_name, function_name, arguments, message=""):

        self.func_to_watch.append(function_name)
        self.tests.append({
            'name': test_name,
            'type': 'function_called',
            'function_name': function_name,
            'arguments': arguments,
            'message': ""
        })


    def compare_keras_architecture(self, submitted, expected):

        self.tests.append({
            'name': 'keras arch',
            'type': 'keras_architecture',
            'submitted': submitted,
            'expected': expected
        })
        

    def compare_functions(self, test_name, submitted, expected, inputs, message="", precision=None):

        self.tests.append({
            "name": test_name,
            "type": "function",
            "expected": expected,
            "submitted": submitted,
            "inputs": inputs,
            "message": message,
            "precision": precision
        })

    def compare_variables(self, test_name, submitted, expected, message = ""):

        self.tests.append({
            "name": test_name,
            "type": "variable",
            "expected": expected,
            "submitted": submitted,
            "message": message
        })

    def compare_files(self, test_name, submitted_path, expected_path, message):

        self.tests.append({
            "name": test_name,
            "type": "file",
            "expected": expected_path,
            "submitted": submitted_path,
            "message": message
        })


    def assert_almost_equal(self, test_name, submited, expected, precision=1e-4, message=""):

        self.tests.append({
            "name": test_name,
            "type": "assert_almost_equal",
            "expected": expected,
            "submitted": submited,
            "precision": precision,
            "message": message
        })


    def or_test(self, test_name):
        self.or_test_start = len(self.tests) - 1

    def end_or_test(self):


        self.tests.append({
            "name"
        })

    def assert_(self, test_name, assertion, message):
        self.add_assert(test_name, assertion, message)

    def add_assert(self, test_name, assertion, message=""):

        self.tests.append({
            "name": test_name,
            "type": "assert",
            "assertion": assertion,
            "message": message
        })

    def print_json_output(self):

        from python_utils.JsonEncoder import CustomEncoder

        output = self.get_test_output()
        print(CustomEncoder.to_json(output))


    def get_test_output(self):

        self.stop_watch_function_calls()
        self.output = {
            "isRight": True,
            "tests": []
        }

        for test in self.tests:

            t = test['type']

            name = test['name']

            if 'submitted' in test:
                submitted = test['submitted']

            if 'expected' in test:
                expected = test['expected']

            if 'message' in test:
                message = test['message']

            if t == "file":
                compare_files(name, test['submitted'], test['expected'], message)

            elif t == "function":
                self._compare_functions(name, submitted, expected, test['inputs'], message)

            elif t == "assert":
                self._assert(name, test['assertion'], message)

            elif t == "variable":
                self._compare_variables(name, submitted, expected, message)

            elif t == "function_called":
                self._function_called(test)

            elif t == self.TESTS['compare_object_attributes']:

                self._compare_object_attributes(name, submitted, expected, message)

            elif t == "assert_almost_equal":

                self._assert_almost_equal(name, submitted, expected, test['precision'], message)

            elif t == 'keras_architecture':

                compare_keras_architecture(submitted, expected, self.output.tests)

            else:
                print('test not supported')
                continue

        return self.output


    def _assert_almost_equal(self, name, submited, expected, precision, message):

        test = {
            'isRight': are_variable_almost_equal(submited, expected, precision)
        }
        test['message'] = message
        test['name'] = name
        test['expected'] = expected
        test['submitted'] = submited

        self.output['tests'].append(test)
        self._update_answer_status(test)


    def get_called_functions(self, name=None):
        """
            get functions called by the student
            optionnally filtered by a function name
        """

        if name is None:
            return self.func_calls

        calls = self.func_calls
        good_calls = list(filter(lambda call: name in call['name'] , calls))
        return good_calls

    def _function_called(self, test):

        function_to_be_called = test['function_name']
        if isinstance(function_to_be_called, dict):
            function_to_be_called = list(function_to_be_called.values())[0]

        expected_arguments = test['arguments']

        good_calls = self.get_called_functions(function_to_be_called)

        if len(good_calls) == 0:
            test_output = {
                'name': test['name'],
                'message': "function {} was not called and should be".format(function_to_be_called),
                'isRight': False
            }

        else:
            test_output = self._check_argument_call(good_calls, function_to_be_called,  expected_arguments)
            test_output['name'] = test['name']

        test_output['name'] = test['name']
        
        self.output['tests'].append(test_output)
        self._update_answer_status(test_output)

    def _check_argument_call(self, good_calls, function_to_be_called, expected_arguments):


        for call in good_calls:

            output = self._analyse_arguments(call, function_to_be_called, expected_arguments)

            if output['isRight']:
                return output

        return output


    def _analyse_arguments(self, call, function_to_be_called, expected_arguments):


        """
        plusieurs cas : args et kwargs
        si on utilise {'args': bla} ou pas
        """

        test_output = {}
        called_arguments = {**call}['arguments']

        if isinstance(expected_arguments, (list,)):

            return self._analyse_array_arguments(function_to_be_called, expected_arguments, called_arguments)

        if 'args' in called_arguments:

             if 'args' in expected_arguments:

                 expected_args = expected_arguments['args']
                 submitted_args = list(called_arguments['args'])


                 if are_variable_equal(expected_args, submitted_args):
                     return {'isRight': True}
                 else:
                     return {
                         'isRight': False,
                         'expected': expected_args,
                         'submitted': submitted_args,
                         'message': "function not called with good arguments"
                     }

             import pandas as pd
             import numpy as np

             def tolist(v):

                 if isinstance(v, (np.ndarray,)):
                     return v.tolist()

                 if isinstance(v, (pd.DataFrame,)):
                     return v.values.tolist()

                 return v

             args_arguments = list(called_arguments.pop('args'))
             args_arguments = [tolist(v) for v in args_arguments]

             expected_arguments = list(expected_arguments.values())
             expected_arguments = [tolist(v) for v in expected_arguments]


             #'args' order is not deterministic
             for expected_arg in expected_arguments:

                 if not expected_arg in args_arguments:
                     test_output['isRight'] = False
                     test_output['message'] = "{} function was not called with the good arguments".format(function_to_be_called)

                     return test_output

             test_output['isRight'] = True


             return test_output


        if 'kwargs' in called_arguments :

            if len(called_arguments['kwargs']) > 0:

                kwargs_arguments = called_arguments.pop('kwargs')

                for arg in kwargs_arguments:

                    called_arguments[arg] = kwargs_arguments[arg]


        for name, value in expected_arguments.items():

            if not name in called_arguments:

                test_output['isRight'] = False
                test_output['message'] = "{} function was not called with {} and should be".format(
                    function_to_be_called, name)

                return test_output

            called_value = called_arguments[name]
            expected_value = value

            if not are_variable_equal(called_value, expected_value):
                test_output['isRight'] = False
                test_output['expected'] = expected_value
                test_output['submitted'] = called_value
                test_output['message'] = "function parameter {} was not called with the good value".format(name)
                return test_output

        test_output['isRight'] = True
        return test_output


    def _analyse_array_arguments(self, function_to_be_called, expected_arguments, called_arguments):
        test_output = {}

        if 'args' in called_arguments:

            args_arguments = list(called_arguments.pop('args'))

            if are_variable_equal(args_arguments, expected_arguments):
                test_output['isRight'] = True

            else:
                test_output['isRight'] = False
                test_output['expected'] = expected_arguments
                test_output['message'] = "{} function was not called with the good arguments".format(
                    function_to_be_called)

            return test_output

        called_arguments #is a an orderedDict (argName, value)
        if are_variable_equal(list(called_arguments.values()), expected_arguments):
            test_output['isRight'] = True

        else:
            test_output['isRight'] = False
            test_output['expected'] = expected_arguments
            test_output['message'] = "{} function was not called with the good arguments".format(
                function_to_be_called)

        return test_output

    def _assert(self, name, assertion, message):

        test_output = {
            'name': name,
            "isRight": assertion,
            "message": message
        }
        self.output['tests'].append(test_output)
        self._update_answer_status(test_output)


    def _compare_files(self, name, submitted_path, expected_path, message):

        test = compare_files(submitted_path, expected_path)

        test['message'] = message

        self.output['tests'].append(test)

        self._update_answer_status(test)

    def _compare_functions(self, name, submitted, expected, inputs, messages):

        function_tests = compare_functions(submitted, expected, inputs)

        for test in function_tests['tests']:

            self.output['tests'].append(test)
            self._update_answer_status(test)

    def _compare_object_attributes(self, name, submitted, expected, message):

        tests = compare_object_attributes(submitted, expected)

        for test in tests['tests']:

            self.output['tests'].append(test)
            self._update_answer_status(test)


    def _compare_variable_types(self, submitted, expected):

        test = {
            'name': "Checking variable types",
            'isRight': are_variable_equal(type(submitted), type(expected)),
            'expected': str(type(expected)),
            'submitted': str(type(submitted)),
            'message': "the type of variable is not good"
        }

        self.output['tests'].append(test)
        self._update_answer_status(test)


    def _compare_variables(self, name, submitted, expected, message):

        self._compare_variable_types(submitted, expected)

        test = compare_variables(submitted, expected)

        test['message'] = message
        test['name'] = name
        test['expected'] = expected
        test['submitted'] = submitted

        self.output['tests'].append(test)
        self._update_answer_status(test)

    def _update_answer_status(self, test):

        if not test['isRight']:
            self.output['isRight'] = False


def compare_files(submitted_path, expected_path):

    with open(submitted_path, 'r') as submitted_file:
        submitted = submitted_file.readlines()

    with open(expected_path, 'r') as expected_file:
        expected = expected_file.readlines()

    return compare_variables(submitted, expected)


def compare_object_attributes(submited_obj, expected_obj):

    tests = []
    isRight = True

    submited_attributes = submited_obj.__dict__
    expected_attributes = expected_obj.__dict__

    for expected_attribute, expected_value in expected_attributes.items():

        test = {}
        if not expected_attribute in submited_attributes:

            test['isRight'] = False
            test['expected'] = {'attribute': expected_attribute, 'value': expected_value}
            test['submitted'] = 'attribute {} is None'.format(expected_attribute)
            tests.append(test)
            isRight = False
            continue

        submited_value = submited_attributes[expected_attribute]
        equals = are_variable_equal(submited_value, expected_value)
        tests.append({
            'isRight': equals,
            'expected': {'attribute': expected_attribute, 'value': expected_value},
            'submitted': {'attribute': expected_attribute, 'value': submited_value},
        })

        if not equals:
            isRight = False

        return {
            'isRight': isRight,
            'tests': tests
        }



def compare_keras_architecture(model, expected_layers, tests):
    
    if len(model.layers) != len(expected_layers):

        tests.append({
            "name": 'number of layers',
            'expected': len(expected_struct),
            'submitted' : len(model.layers),
            'isRight': False
        })

        return 
        
    layers = model.layers
    for i_layer, layer in enumerate():

        real_layer_conf = layer.get_config()
        expected_layer_conf = expected_layers[i_layer]

        real_layer_name = real_layer_conf['name'].split('_')[0]
        real_unit_count = real_layer_conf['units']
        real_activation_function = real_layer_conf['activation']

        if 'name' in expected_layer_conf:

            expected_name = expected_layer_conf['name']
            same_name = real_layer_name == expected_name

            tests.append({
                "name": 'layer_name of layer {}'.format(i_layer),
                'expected': len(expected_struct),
                'submitted' : len(model.layers),
                'isRight': same_name
            })

        if 'units' in expected_layer_conf:

            expected_units = expected_conf['units']
            same_units = (expected_units == real_unit_count)

            tests.append({
                "name": 'number of neurones of layer named {} (i={})'.format(name, i_layer),
                'expected': len(expected_struct),
                'submitted' : len(model.layers),
                'isRight': same_units
            })


        if 'activation' in expected_layer_conf:
            expected_activation = expected_layer_conf['activation']
            same_conf = real_activation_function == expected_activation

            tests.append({
                "name": 'activation function of layer n°{} ({})'.format(i_layer, layer_name),
                'expected': expected_activation,
                'submitted' : real_activation_function,
                'isRight': same_conf
            })

        if 'kernel_size' in expected_layer_conf:
            expected = expected_layer_conf['kernel_size']
            real = real_layer_conf['kernel_size']

            tests.append({
                "name": 'kernel_size of layer n°{} ({})'.format(i_layer, layer_name),
                'expected': expected,
                'submitted' : real,
                'isRight': real == expected
            })




        
def assert_keras_model_match_structure(model, expected_struct):

    if len(model.layers) != len(expected_struct):
        return False

    for i, layer in enumerate(model.layers):
        conf = layer.get_config()
        same_conf = True
        
        expected_conf = expected_struct[i]
        
        if 'name' in expected_conf:
            name = conf['name'].split('_')[0]

            same_conf = same_conf and (name == expected_conf['name'])

        if 'units' in expected_conf:
            same_conf = same_conf and (expected_conf['units'] == expected_conf['units'])

        if 'activation' in expected_conf:
            same_conf = same_conf and (conf['activation'] == expected_conf['activation'])

        if not same_conf:
            return False

    return True


def compare_variables(submitted, expected):

    is_right = are_variable_equal(submitted, expected)

    return {
        "isRight": is_right,
        "tests": [
            {
                "isRight": is_right,
                "submitted": submitted,
                "expected": expected,
            }
        ],
    }


def format_long_string(long_string, max_len=300):

    if len(long_string) <= max_len:
        return long_string

    return long_string[: int(max_len / 2)] + "..." + long_string[- int(max_len / 2):]


def csr_matrix_equal(a1, a2):
    #ref https://github.com/haasad/PyPardisoProject/issues/1
    #https://stackoverflow.com/questions/30685024/check-if-two-scipy-sparse-csr-matrix-are-equal
    import numpy as np
    return all((np.array_equal(a1.indptr, a2.indptr),
                np.array_equal(a1.indices, a2.indices),
                np.array_equal(a1.data, a2.data)))


def are_variable_almost_equal(submited, expected, eps=1e-4):

    import numpy as np
    return np.allclose(submited, expected, eps, equal_nan=True)



def are_variable_equal(v1, expected):

    import numpy as np
    import pandas as pd
    from scipy.sparse import csr_matrix, csc_matrix

    if isinstance(v1, (csc_matrix, csr_matrix)) or isinstance(expected, (csc_matrix, csr_matrix)):
        if isinstance(v1, (csr_matrix)) and isinstance(expected, (csr_matrix)):
            return csr_matrix_equal(v1, expected)
        if isinstance(v1, (csc_matrix)) and isinstance(expected, (csc_matrix)):
            return csr_matrix_equal(v1, expected)
        return False

    if isinstance(v1, np.ndarray) or isinstance(expected, np.ndarray):

        try:
            return np.allclose(v1, expected, equal_nan=True)
        except:
            return np.array_equal(v1, expected)

    if isinstance(v1, pd.DataFrame):
        return v1.equals(expected)

    if isinstance(expected, pd.DataFrame):
        return expected.equals(v1)

    if isinstance(v1, pd.Series):
        try:
            return np.allclose(v1, expected, equal_nan=True)
        except:
            return np.array_equal(v1, expected)

    if isinstance(expected, pd.Series):
        try:
            return np.allclose(v1, expected, equal_nan=True)
        except:
            return np.array_equal(v1, expected)

    return v1 == expected


def assert_are_dataframes_equal(submitted_df, expected_df):

    tests = []
    tests.append(compare_variables(submitted_df[:5], expected_df[:5]))
    tests.append(compare_variables(submitted_df[-5:], expected_df[-5:]))

    n_row = len(expected_df)

    random_lines = np.random.choice(np.arange(0, n_row, 10))

    tests.append(compare_variables(submitted_df.iloc[random_lines], expected_df.iloc[random_lines]))

    return tests

def compare_functions(submission_function, solution_function, test_data, precision=None):

    tests = []
    is_right = True

    for argument_list in test_data:

        copy_argument_list = copy.deepcopy(argument_list) #some function can modify args and will make test fail

        expected_answer = solution_function(*argument_list)
        submission_answer = submission_function(*copy_argument_list)

        test = {
            "expected": expected_answer,
            "submitted": submission_answer,
            "arguments": argument_list
        }

        if precision:
            is_output_identical = are_variable_almost_equal(submission_answer, expected_answer, precision)
        else:
            is_output_identical = are_variable_equal(submission_answer, expected_answer)

        if not is_output_identical:
            test["isRight"] = False
            is_right = False
        else:
            test["isRight"] = True

        tests.append(test)

    return {
        'isRight': is_right,
        'tests': tests
    }




def compare_variable_list(submited_variables, expected_variables):

    differences = []

    for submited, expected in zip(submited_variables, expected_variables):
        if not are_variable_equal(submited, expected):

            differences.append(
                {
                    'arguments': [expected['name']],
                    'expected': expected['value'],
                    'submited': submited
                }
            )

    if len(differences) == 0:

        return {
            "isRight": True,
        }

    else:
        return {
            "isRight": False,
            "differences": differences
        }
