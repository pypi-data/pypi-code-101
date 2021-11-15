
from io import StringIO
import sys
import functools
import os
import re
import time

from lib.executeCode import *
from lib.OneFileCodeRunner import OneFileCodeRunner
from .PythonRunner import *
import tensorflow
__open = open
__print = print
__sum = sum
__sorted = sorted
__max = max
__min = min
__abs = abs
__type = type

class InMemoryOneFileExercicePythonRunner(OneFilePythonRunner):

    def __init__(self):
        self.picture_folder = "pictures"
        self.utils_code = get_util_function_code()
        self.json_encoder_code = get_json_encoder_code()
       
    def _run_exercice_cmd(self, user_id, commands, files):

        from .utils import AnswerTesterB, AnswerTester
        from .JsonEncoder import CustomEncoder
        import matplotlib.pyplot as plt

        local_data={
            'AnswerTester': AnswerTester,
            'CustomEncoder': CustomEncoder,
            'plt': plt,
            'tensorflow': tensorflow
        }
        concat_files = files[1]['content']
        
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        os.chdir(self._get_user_folder(user_id))

        
        try:
            
            exec(concat_files, {}, local_data)
            print_data = redirected_output

        except Exception as e:
            import traceback
            return {
                "status": 1,
                "stderr": traceback.format_exc(),
                "assesments": {
                    'isRight': False
                }
            }
        
        sys.stdout = old_stdout
        tester = local_data['tester']
        
        
        assesments = tester.get_test_output()


        user_folder = self._get_user_folder(user_id)
        picture_folder = os.path.join(user_folder, self.picture_folder)
        picture_data = get_output_pictures_as_base_64(picture_folder)

        AnswerTesterB._instance.__init__()
        return {
            'status': 0,
            'assesments': assesments,
            'stdout': print_data.getvalue(),
            'pictures': picture_data,
        }


    def _prepare_main_file(self, user_id, user_files):
        """ concatenates all files in the main no need to do it in _run_exercice_cmd ! """
        user_folder = self._get_user_folder(user_id)

        main_file = user_files[-1]

        user_picture_folder = os.path.join(user_folder, self.picture_folder)
        plot_saving_code = get_plot_code(user_picture_folder)
        
        updated_main = (
            """import warnings; warnings.filterwarnings('ignore')""",
            user_files[0]['content'],
            main_file['content'],
            plot_saving_code,
        )

        user_files[-1]['content'] = "\n".join(updated_main)


    def _prepare_answer_file(self, user_files, code_to_run_before_student_file):
        answer_file = user_files[0]
        answer_code = answer_file['content']
    
        if "was_function_called_with" in user_files[1]['content']:
            
            updated_student_code = (
                function_redefinition,
                'tester = AnswerTester()',
                code_to_run_before_student_file,
                
                'tester.watch_function_calls()',
                answer_code,
                'tester.stop_watch_function_calls()'
            )

            n_line_injected = function_redefinition.count('\n') + code_to_run_before_student_file.count('\n') + 3

        else:
            updated_student_code = (
                function_redefinition,

                'tester = AnswerTester()',
                code_to_run_before_student_file,
                answer_code,
            )
            n_line_injected = function_redefinition.count('\n') + code_to_run_before_student_file.count('\n')

        user_files[0]['content'] = "\n".join(updated_student_code)
        
        return n_line_injected


    def save_files(self, user_id, files):
        pass #no need to save the code files as it is in memory
        
