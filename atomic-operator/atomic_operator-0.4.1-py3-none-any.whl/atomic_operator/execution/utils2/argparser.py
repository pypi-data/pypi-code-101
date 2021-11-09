from ...base import Base


class ArgumentParser(Base):

    _replacement_strings = [
        '#{{{0}}}',
        '${{{0}}}'
    ]

    def __init__(self, test_name, input_arguments):
        self.name = test_name
        self.input_arguments = input_arguments

    def parse(self, command, remote=False):
        if remote:
            path = '/tmp'
        else:
            path = self.CONFIG.atomics_path
        args_dict = self.CONFIG.kwargs
        if self.CONFIG.prompt_for_input_args:
            #Formatting commands based on user input at prompt
            for input in self.input_arguments:
                args_dict[input.name] = self.prompt_user_for_input(self.test.name, input)
        if self.input_arguments:
            for arguments in self.input_arguments:
                if arguments.type.lower() != 'integer':
                    if args_dict and args_dict.get(arguments.name):
                        arguments.value = args_dict[arguments.name]
                    else:
                        arguments.value = self.replace_command_string(arguments.default, path)
        return self.replace_command_string(command, path)
