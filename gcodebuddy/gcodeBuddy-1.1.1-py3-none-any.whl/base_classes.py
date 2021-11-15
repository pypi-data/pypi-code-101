import sys
import numpy as np
from gcodeBuddy import angle, Arc, centers_from_params
from gcodeBuddy.marlin import marlin_commands


class BaseCommand:
    """
    represents line of g-code

    :param init_string: line of g-code
    :type init_string: str
    """

    def __init__(self, init_string):
        """
        initialization method
        """

        self.flavor = "<flavor>"
        self.command = "<command>"
        self.params = dict()

        err_msg = "Error in Command.__init__(): "

        # removing extraneous spaces
        command_string = init_string
        while command_string[0] == " ":
            command_string = command_string[1:]
        while command_string[-1] == " ":
            command_string = command_string[:-1]
        ind = 0
        while (ind + 1) < len(command_string):
            if command_string[ind] == " " and command_string[ind + 1] == " ":
                command_string = command_string[:ind] + command_string[(ind + 1):]
            else:
                ind += 1

        # ensuring valid command
        command_list = command_string.split(" ")
        if command_list[0] in marlin_commands():
            self.command = command_list[0]
            command_list = command_list[1:]
        else:
            print(err_msg + "Unrecognized" + self.flavor + "command passed in argument 'init_string'")
            sys.exit(1)

        self.params = dict()
        for parameter_str in command_list:
            if parameter_str[0].isalpha():
                try:
                    float(parameter_str[1:])
                except ValueError:
                    print(err_msg + self.flavor + " parameter passed in argument 'init_string' of non-int/non-float type")
                    sys.exit(1)
                else:
                    self.params[parameter_str[0].upper()] = float(parameter_str[1:])
            else:
                print(err_msg + "Unrecognized" + self.flavor + "parameter passed in argument 'init_string'")
                sys.exit(1)

    def get_command(self):
        """
        :return: g-code command
        :rtype: str
        """
        return self.command

    def has_param(self, param_char):
        """
        :param param_char: parameter character to search for in g-code command
        :type param_char: str
        :return: whether the Command object has the given parameter
        :rtype: bool
        """
        err_msg = "Error in Command.has_param(): "
        # ensuring string passed
        if isinstance(param_char, str):
            return param_char.upper() in self.params
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def get_param(self, param_char):
        """
        :param param_char: parameter character to search for in g-code command
        :type param_char: str
        :return: value of parameter character stored in g-code command
        :rtype: float
        """
        err_msg = "Error in Command.get_param(): "
        # ensuring param_char is string, and is in self.params
        if isinstance(param_char, str):
            if param_char in self.params:
                return self.params[param_char]
            else:
                print(err_msg + "Command does not contain" + self.flavor + "parameter given in argument 'param_char'")
                sys.exit(1)
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def set_param(self, param_char, param_val):
        """
        sets parameter value

        :param param_char: parameter character to change value
        :type param_char: str
        :param param_val: parameter value to set
        :type param_val: int, float
        """
        err_msg = "Error in Command.set_param(): "
        # ensuring param_char is string and is in self.params and param_val is number
        if isinstance(param_char, str):
            if isinstance(param_val, (int, float)):
                if param_char in self.params:
                    self.params[param_char] = param_val
                else:
                    print(err_msg + "Command does not contain" + self.flavor + "parameter given in argument 'param_char'")
                    sys.exit(1)
            else:
                print(err_msg + "Argument 'param_val' of non-int/non-float type")
                sys.exit(1)
        else:
            print(err_msg + "Argument 'param_char' of non-string type")
            sys.exit(1)

    def get_string(self):
        """
        :return: entire g-code command in line form
        :rtype: string
        """
        ret_val = self.command
        for param_key in self.params:
            ret_val += " " + param_key + str(self.params[param_key])
        return ret_val
