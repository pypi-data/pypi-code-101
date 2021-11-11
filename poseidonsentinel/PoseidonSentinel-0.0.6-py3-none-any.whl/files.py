import os.path

__all__ = ['File',]

    
class RawFile():
    """
    Accepts a file from OS module to create an 
    encompassing class for easy manipulations
    """

    PATHS = None

    def __init__(self, f):
        self.file = f
        self.name = self.file.name
        self.stats = self.file.stat()
        self.size = self.stats.st_size
        self.local_path = self.file.path      
        self.path = os.path.abspath(self.local_path)


    @property
    def mod_date(self):
        """
        returns the last time modified in a datetime object
        """
        from datetime import datetime
        return datetime.fromtimestamp(self.stats.st_mtime)


    @property
    def acc_date(self):
        """
        returns the last time accessed in a datetime object
        """
        from datetime import datetime
        return datetime.fromtimestamp(self.stats.st_atime)


    @property
    def tree(self):
        """
        returns the abs path as a list
        """
        return self.path.split('\\')


    @property
    def ext(self):
        """
        returns the extention of a file
        """
        return self.name.split('.')[-1]


    @property
    def file_name(self):
        """
        returns the file name, allows for periods 
        in the filename
        """
        name = self.name.split('.')
        name.pop()
        return '.'.join(name)


    @property
    def _lines(self):
        """
        A simple list return of the File
        """
        if self.ext.lower() in ('csv', 'txt'):
            with open(self.path, 'r') as f:
                _lines = f.readlines()
            return _lines
        else:
            return []


    @property
    def count(self):
        return 0


    @property
    def total(self):
        return 0

    @property
    def save_name(self):
        """
        Returns the save name
        """
        return self.file_name
    

    @property
    def save_date(self):
        """
        Returns the save date
        """
        return self.mod_date


    def rawfile_type(self, f):
        return any(t in self.tree for t in self.PATHS)


    def __gt__(self, instance):
        """
        lexiographical comparison based on filename
        """
        return self.file_name.lower() > instance.file_name.lower()


    def __eq__(self, instance):
        """
        lexiographical comparison based on filename
        """
        return self.file_name.lower() == instance.file_name.lower()


    def __str__(self):
        return (
            f'file type: {self.__class__.__name__}\n'
            f'file: {self.file_name}\n'
            f'size: {self.size}\n'
        )    

class File:
    """
    Factory class for creating subclasses if criteria is met
    """
    def __new__(cls, f):
        for subcls in RawFile.__subclasses__():
            if subcls(f).rawfile_type(f):
                return subcls(f)
        return RawFile(f)

