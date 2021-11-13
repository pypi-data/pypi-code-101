class OpenTrainingError(Exception):
    '''Base class for all OpenTraining errors'''

class BadPath(OpenTrainingError):
    pass

class ElementError(OpenTrainingError):
    '''Base class for errors tied to a single element'''
    def __init__(self, msg, element):
        super().__init__(msg)
        self.element = element

class DependencyError(ElementError):
    pass

class PathNotFound(ElementError):
    pass

class NotCommitted(ElementError):
    pass

class AlreadyCommitted(ElementError):
    pass

class CompoundError(OpenTrainingError):
    '''An error that *contains* multiple errors. Used in situations where
    we do not bail out early, but rather continue, and represent the
    user with a list of collected error messages.  '''

    def __init__(self, msg, errors):
        super().__init__(msg)
        self.errors = errors
