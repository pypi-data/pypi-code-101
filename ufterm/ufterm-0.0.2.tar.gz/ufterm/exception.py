
class NoCommandSelectedError(RuntimeError):
    def __init__(self):
        super().__init__("No command are selected")


class CommandAlreadyPresentError(RuntimeError):
    def __init__(self, name):
        super().__init__("The command: %s is already present" % name)


class CommandNameAlreadyUsedError(RuntimeError):
    def __init__(self, name):
        super().__init__("The command name: %s is already used" % name)


class ValidationError(RuntimeError):
    pass


class ConversionError(ValidationError):
    pass


class MenuExitException(RuntimeError):
    pass
