class SyntaxException(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


class RuntimeException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
