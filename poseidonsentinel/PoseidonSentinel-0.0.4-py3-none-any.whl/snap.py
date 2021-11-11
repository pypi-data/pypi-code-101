from sentinel.path import Path
from sentinel.files import File

__all__ = ['Snapshot']

class Snapshot:
    """
    A current list of files within a specified directory
    """

    def __init__(self, path:Path):
        self.files = self.snap(path)


    def list_snap(self):
        """ 
        Prints a list of File objects from a snapshot
        """
        for f in self.files:
            print(f)


    def snap(self, path:Path):
        """
        Returns a list of File objects found in a directory
        """
        from os import scandir
        return [File(f) for f in scandir(path.path())]


    def snap_set(self):
        """
        Converts the snap into a set 
        """
        return set(f.file_name for f in self.files)


    def compare(self, instance):
        """
        Compares two snaps
        If new files are found in the second, add to the compare dictionary as created
        If new files are found in the initial, add to the compare dictionary as deleted
        Returns the dictionary 
        """
        compare = {}
        created = instance.snap_set() - self.snap_set()
        deleted = self.snap_set() - instance.snap_set()

        if created:
            compare['created'] = [f for f in instance.files if f.file_name in created]
        if deleted:
            compare['deleted'] = [f for f in self.files if f.file_name in deleted]

        return compare
