from lib.executeCode import run_cmd

class CommandTester():

    def run_output_tests(self, exercice_data):


        tests = []
        isRight = True
        for test in exercice_data['outputTests']:
 
            output = self.check_output(test)
            
            assesments = output['assesments']
            isRight = assesments['isRight']

            if not isRight:
                output['assesments']['isRight'] = False

            tests = tests + output['assesments']['tests']

        output['assesments']['tests'] = tests

        return {
            'status': 0,
            'assesments': {
                'tests': tests,
                'isRight': isRight
            }
        }


    def check_output(self, command_test):

        command = command_test['command']
        includes = command_test['includes'] if 'includes' in command_test else []
        excludes = command_test['excludes'] if 'excludes' in command_test else []
        output = self.test_command_output(command, excludes=excludes, includes=includes)

        return output

    def test_command_output(self, command, includes = None, excludes = None):


        print("running command '{}'...".format(command))
        output, err = run_cmd(command, ".")

        if err:
            print("error occured:")
            print(err)
            return {'status': 1, 'isRight': False, 'assesments': {'isRight': 0, 'tests': [{'name': 'command {} run without error'.format(command), "isRight": False}]}}

        print(output)

        is_right = True
        tests = []

        tests.append({
            'name': 'command "{}" run without error'.format(command),
            'isRight': not err
        })

        if not includes is None:
            for contain in includes:
                if not contain in output:
                    is_right = False

                tests.append({
                    'name': 'output countains {}'.format(contain),
                    'isRight': contain in output
                })

        if not excludes is None:
            for exclude in excludes :

                if exclude in output:

                    is_right = False
                    tests.append({
                        'name': 'output does not contain {}'.format(exclude),
                        'isRight': is_right
                    })

        return {
            'status' : 0,
            'isRight': is_right,
            'assesments': {
                'isRight': is_right,
                'tests': tests
            }
        }
