
class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CalcError(Exception):
    def __init__(self, text, o=None, argv=None):
        self.info = {
            'name': o.name if o else '',
            'argc': o.argc if o else '',
            'argv': argv
        }
        super().__init__(text)
