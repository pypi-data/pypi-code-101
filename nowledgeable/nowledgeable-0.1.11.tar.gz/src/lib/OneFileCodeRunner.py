from lib.utils import * 
from lib.CodeRunner import CodeRunner


class OneFileCodeRunner(CodeRunner):

    """ 

    OneFileCodeRunner

    Runner for exercice which consists in being a single file exercice
    """

    def _assert_answer_contain_forbidden_expressions(self, file, forbidden_expressions):

        forbiden = get_forbidden_expressions(file, forbidden_expressions)    
        
        self.forbidden_expressions_found = forbiden

        return len(forbiden) > 0

    def _get_default_command(self, files):
        raise "override"

    def run_exercice_code(self, 
                          user_id, 
                          data_files, 
                          user_files, 
                          code_to_run_before_student_file,
                          forbidden_expressions,                      
                          commands = "", 
                          expected_output = "", 
                          timeout = 30):
        
        if self._assert_answer_contain_forbidden_expressions(user_files[0]['content'], forbidden_expressions):
            return self._answer_has_forbidden_expression_output()
            
        self._setup_environment(user_id, data_files, self.picture_folder)
        
        n_line_added = self._prepare_answer_file(user_files, code_to_run_before_student_file)
        self._prepare_main_file(user_id, user_files)

        lib_files = self.get_lib_files()
        files = user_files + lib_files
        self._save_files(user_id, files)

        commands = commands if commands != "" else self._get_default_command(files)
        answer_status = self._run_exercice_cmd(user_id, commands, files)
      
        self.after_exercice_code_was_run(user_id, files, answer_status, n_line_added)
        self._assert_program_output_is(answer_status, expected_output)
        
        return answer_status