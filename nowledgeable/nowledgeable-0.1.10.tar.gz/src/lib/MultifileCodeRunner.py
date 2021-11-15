from lib.CodeRunner import CodeRunner

class MultifileCodeRunner(CodeRunner):

    def _prepare_main_file(self, main_file):
        pass

    def _assert_answer_contain_forbidden_expressions(self, files, forbidden_expressions):

        for file in files:

            if code_has_forbiden_expression(file['content'], forbidden_expressions):
                return True
        return False

    def run_exercice_code(self, 
                          user_id, data_files, user_files, main_file, forbidden_expressions,                      
                          commands, 
                          expected_output, 
                          timeout = 30):

        if self._assert_answer_contain_forbidden_expressions(user_files, forbidden_expressions):
            return self._answer_has_forbidden_expression_output()
            
        self._setup_environment(user_id, data_files, "picture/")        
        self._prepare_main_file(user_id, main_file)

        lib_files = self.get_lib_files()
        files = user_files + lib_files
        self._save_files(user_id, files)

        answer_status = self._run_exercice_cmd(user_id, commands, files)
      
        self.after_exercice_code_was_run(answer_status)
        self._assert_program_output_is(answer_status, expected_output)
        
        return answer_status


