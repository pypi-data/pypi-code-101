from . import errors


class Element:
    '''
    Base of all OpenTraining artifacts (Topic, Exercise, Task, Person, ...)
    '''
    def __init__(self, title, path, docname, userdata):
        ''':param title: string that is sometimes (?) displayed somewhere (?)

        :param docname: leaks out from sphinx/docutils. Sometimes (?)
        used to display error messages. Should be removed in favor of
        ``userdata``

        :param userdata: during sphinx/docutils processing, we try to
        create OpenTraining elements as early as possible while
        keeping reference to the original docutils elements. For
        debugging and error messages only.

        :param path: the requested path across the hierarchy that this
        element should be placed under. Note that the hierarchy is not
        yet in place when an Element is create - this is just a
        request for a later step: when the soup is committed, Group
        elements are created, and is that point where the ``path``
        argument is used to add this Element to a *parent* group.

        '''

        _verify_is_path(path)

        self.title = title
        self.docname = docname
        self.userdata = userdata
        if path:
            self._requested_path = path
        else:   # root group; no parent
            self.parent = None

    def __str__(self):
        if hasattr(self, '_requested_path'):
            return f'{self._requested_path} (uncommitted)'
        else:
            return f'{self.path}'

    @property
    def path(self):
        if hasattr(self, '_requested_path'):
            raise errors.OpenTrainingError(f'{self} is not yet committed (path not known)')
        if self.parent:
            return self.parent.path + [self.parent.element_name(self)]
        else:
            return []

    def resolve_paths(self, soup):
        pass


def _verify_is_path(path):
    if type(path) not in (list, tuple):
        raise errors.BadPath(f'Not a valid path: {path} is neither list nor tuple')
        
    for elem in path:
        if type(elem) is not str:
            raise errors.BadPath(f'Not a valid path: {path} ({elem} is not str)')
        if not elem.isidentifier():
            raise errors.BadPath(f'Not a valid path: {path} ({elem} is not an identifier)')
    
