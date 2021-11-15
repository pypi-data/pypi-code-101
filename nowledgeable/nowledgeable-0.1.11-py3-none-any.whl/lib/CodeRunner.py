import os
import functools

from lib.utils import *
from lib.executeCode import *

class CodeRunner():

    """
        Runner 

        Base class managing user code submission and code exercice submissions

        implments Template method pattern, should be subclassed and 
        some methods must be overidden
    """

    def get_datasets(self):
        """ a list of datasets to be linked into the user environment """


        return []

    def after_exercice_code_was_run(self, user_id, files, output, n_line_injected):
        """ function called after the student code was run"""
        pass

    def setup_library_files(self, user_id):
        pass

    def run_code(self, user_id, data_files, user_files, commands, timeout=30):
        
        """ run code without any tests : saves files and execute the command"""

        working_directory = self._get_user_folder(user_id)
        self._setup_environment(working_directory, data_files, self.picture_folder)
        self.save_files(user_id, user_files)

        stdout, stderr = run_cmd(commands, working_directory, timeout)

        return {
            'status': 1 if stderr else 0,
            'stdout': stdout,
            'stderr': stderr
        }    

    def _setup_environment(self, user_id, data_files, picture_folder = "pictures/"):

        user_folder = self._get_user_folder(user_id)

        setup_user_folder(user_folder, picture_folder)
        
        data_file_paths = save_data_files(user_folder, data_files)
        
        setup_links_to_datasets(user_folder, self.get_datasets())
        
        self.setup_library_files(user_id)

        return data_file_paths

    def _answer_has_forbidden_expression_output(self):

        found_forbidden = ", ".join(self.forbidden_expressions_found)

        return {
            'status': 1,
            'stderr': 'answer.forbiden_expression: ' + found_forbidden,
            'assesments': {
                'isRight': False,
            }
        }

    def _get_user_folder(self, user_id):

        return get_user_folder(user_id)

    def _get_user_picture_folder(self, user_id):
        user_folder = self._get_user_folder(user_id)
        return os.path.join(user_folder, self.picture_folder)

    def _run_command(self, working_dir, command):

        return run_cmd(command, working_dir)

    def _run_exercice_cmd(self, user_id, commands, files):

        cwd = self._get_user_folder(user_id)
        user_picture_folder = self._get_user_picture_folder(user_id)

        return run_exercice_code(cwd, commands, user_picture_folder)

    def _get_file_content(self, path):

        with open(path, 'r') as f:
            content = f.read()

        return content

    def _save_files(self, user_id, files):

        """
        saves code files in the folder of the code submitter (using user_id)
    
        :param base_path string
        :param files: list
    
        """
        base_path = self._get_user_folder(user_id)
        for file in files:
            
            targetFileInBackend = file['targetPathInBackend'] if 'targetPathInBackend' in file else ''
            folder_path = os.path.join(base_path, targetFileInBackend)

            targetPath = os.path.join(
                folder_path,
                file['name']
            )
            
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)

            with open(targetPath, 'w') as f:
                f.write(file['content'])

    def _assert_program_output_is(self, answer_status, expected_output):

        if (len(expected_output) == 0 or answer_status['status'] == 1):
            return 

        print_output = answer_status['stdout']
        
        tests = answer_status['assesments']['tests']
        tests.append({
            'isRight': print_output ==  expected_output,
            'message': 'exercice.invalid_program_output'
        })

