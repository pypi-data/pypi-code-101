__all_ = ['Path']

class Path:
    """
    Simple string concantenation to create
    a path name
    """
    def __init__(self, path_dir, *subdirs):
        self.dir = path_dir
        self.subdirs = subdirs

    def path(self):
        """
        Appends any additional args as subdirectories
        """
        path = self.dir
        for sub in self.subdirs:
            path += '/' + sub
        return path

    def __str__(self):
        return self.path()