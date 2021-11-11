import os
import re
import json
import glob
import shutil

from . import util


class DiskHashTree:
    def __init__(self, root: str, min_prefix_size: int=2):
        '''
        :param root: The root directory where the hash tree is stored.
        :param min_prefix_size: The minimum amount of characters to include as
            subdirectory names. eg, a value of 2 means aa/ ab/ ac/ ...
        '''
        # Validate the bucket size
        if isinstance(min_prefix_size, int):
            if min_prefix_size < 1:
                raise ValueError('Incorrect min_prefix_size (must be >0)')
        else:
            raise TypeError('Incorrect type for min_prefix_size (expected int)')

        self.root = root
        self.min_prefix_size = min_prefix_size
        self.cardinality = 0

        # Validate the root directory
        if os.path.isdir(self.root):
            # Check if the directory is empty or not
            if bool(os.listdir(self.root)):
                # If the directory has things, try loading the metadata file
                try:
                    self.load_meta()
                except FileNotFoundError:
                    raise FileNotFoundError('Meta file not found. Ensure that you have set root to an empty directory')
            else:
                # See if the directory is writable by initialising the metadata
                self.write_meta()
        else:
            raise ValueError('Invalid root directory provided')


    def __getstate__(self):
        '''
        Will return a dict of the metadata of this object.
        '''
        return {
            'root' : self.root,
            'cardinality' : self.cardinality,
            'min_prefix_size' : self.min_prefix_size
        }


    def __iter__(self, current_root=None):
        '''
        Will descend the entire tree in no particular order.

        WARNING: For large sets and converting to a list/set object,
        this will perform a large read operation and may take a very long time.
        If you are checking for set membership or using the `in` directive,
        use DiskHashTree.contains() instead.
        '''
        if current_root is None:
            current_root = self.root

        glob_results = glob.glob(os.path.join(current_root, '*'))

        dir_list = list(util.filter_valid_directories(glob_results))

        for d in dir_list:
            yield from self.__iter__(os.path.join(current_root, d))

        file_list = list(util.filter_valid_files(glob_results))

        for f in file_list:
            yield f


    def load_meta(self):
        '''
        Loads the metadata values from the .meta file in the root directory
        of the hash tree into this structure's variables.
        '''
        with open(os.path.join(self.root, '.meta'), 'r', encoding='utf-8') as fp:
            meta = json.load(fp)

            if meta.get('cardinality', False):
                self.cardinality = meta.get('cardinality')

            if meta.get('min_prefix_size', False):
                self.min_prefix_size = meta.get('min_prefix_size')


    def write_meta(self):
        '''
        Writes all the variables of this structure into a JSON meta file called
        .meta which is located at the root of the hash tree.
        '''
        meta = self.__getstate__()

        with open(os.path.join(self.root, '.meta'), 'w', encoding='utf-8') as fp:
            json.dump(meta, fp)


    def collapse_subdir(self, directory: str):
        '''
        Strips all slashes from the directory and removes any reference to the
        root directory of the structure.

        This is so that we can calculate how far we have recursed relative to
        a provided key by producing the first portion of it based on the depth
        of recursion.
        '''
        return ''.join(util.safe_str_replace(directory, self.root, '').split('/'))


    def key_to_prefix(self, key, from_subdir=''):
        '''
        Converts the key to the appropriately sized prefix as configured.
        If from_subdir is provided, then it will pick the prefix relative to the
        provided directory instead of from the front of the key.

        :param key: The provided key/hash.
        :param from_subdir: The current subdirectory that is being recursed.
            If provided, the returned prefix will be relative to the directory.
        '''
        # Calculate the part of the key that has already been used in the directory
        recursed_key = self.collapse_subdir(from_subdir)
        # And then remove it safely
        temp_key = util.safe_str_replace(key, recursed_key, '')
        idx = 0
        prefix = ''

        # While the prefix is smaller than the min size and is not a valid file name
        while len(prefix) < self.min_prefix_size or not bool(re.match(util.FILE_NAME_REGEX, prefix)):
            prefix += temp_key[idx]
            idx += 1

        return prefix


    def add(self, key: str, current_root: str=None):
        '''
        Recursively adds a hash to the set.
        '''
        assert bool(re.match(util.FILE_NAME_REGEX, key)), 'Provided key is illegal'

        if current_root is None:
            current_root = self.root

        glob_results = glob.glob(os.path.join(current_root, '*'))
        # This is a string with the first n characters of the key that have been recursed
        key_progress = self.collapse_subdir(current_root)

        try:
            # This is what the next subdirectory will be called if it were to be created
            # It is the next prefix after key_progress
            key_prefix_rel = self.key_to_prefix(key, from_subdir=current_root)
            # This will be the absolute path of the next subdirectory
            next_root = os.path.join(current_root, key_prefix_rel)
        except IndexError:
            # If we reached the limit of subdirectories for the length of the
            # key, then we simply store the key here.
            with open(os.path.join(current_root, key), 'w', encoding='utf-8') as fp:
                return os.path.join(current_root, key)

        # First check if the key is in the current directory
        file_list = list(util.filter_valid_files(glob_results))

        if key in file_list:
            return os.path.join(current_root, key)

        # Then check to see if there is a branch we can follow
        dir_list = list(util.filter_valid_directories(glob_results))

        if key_prefix_rel in dir_list:
            # Recurse to the subdirectory that matches the key
            return self.add(
                key,
                current_root=next_root
            )

        # Else see if there is a prefix collision in this directory
        colliding_files = [f for f in file_list if f.startswith(key_progress + key_prefix_rel)]

        if bool(colliding_files):
            # Then move all files to a subdirectory
            new_subdir = next_root
            os.mkdir(new_subdir)

            for f in colliding_files:
                os.rename(
                    os.path.join(current_root, f),
                    os.path.join(new_subdir, f)
                )

            # And finally, emplace the key
            with open(os.path.join(new_subdir, key), 'w', encoding='utf-8') as fp:
                return os.path.join(new_subdir, key)
        else:
            # Emplace the key
            with open(os.path.join(current_root, key), 'w', encoding='utf-8') as fp:
                return os.path.join(current_root, key)


    def remove(self, key: str, current_root: str=None):
        '''
        Removes a hash from the set and raises a KeyError if it doesn't exist.
        '''
        assert bool(re.match(util.FILE_NAME_REGEX, key)), 'Provided key is illegal'

        if current_root is None:
            current_root = self.root

        glob_results = glob.glob(os.path.join(current_root, '*'))
        file_list = list(util.filter_valid_files(glob_results))
        dir_list = list(util.filter_valid_directories(glob_results))

        # First check if the key is here
        if key in file_list:
            # If it is the last item in here with no subdirs, then remove the subdir
            if len(file_list) == 1 and len(dir_list) == 0 and current_root != self.root:
                shutil.rmtree(current_root)
            else: # Otherwise just remove the key
                os.remove(os.path.join(current_root, key))
            return key

        try:
            # Try to get the relative prefix.
            # If we can, then recurse normally, else there is nowhere else to go
            key_prefix_rel = self.key_to_prefix(key, from_subdir=current_root)
            # Prepare the next directory
            next_root = os.path.join(current_root, key_prefix_rel)
        except IndexError:
            raise KeyError

        # Otherwise check for a new subdir
        if key_prefix_rel in dir_list:
            # Recurse to the subdirectory that matches the key prefix
            return self.remove(
                key,
                current_root=next_root
            )

        # If all else fails, the key is not in here
        raise KeyError


    def discard(self, key: str):
        '''
        Idempotent version of DiskHashTree.remove(). Removes the hash with no
        error whether or not it is in the set or not.

        :returns: A boolean which is True if something was removed
        '''
        try:
            return self.remove(key)
        except KeyError:
            return False


    def is_empty(self):
        '''
        Returns whether or not there are elements in the set.
        '''
        glob_results = glob.glob(os.path.join(self.root, '*'))
        file_list = list(util.filter_valid_files(glob_results))
        dir_list = list(util.filter_valid_directories(glob_results))

        return len(file_list) + len(dir_list) == 0


    def pop(self, reverse=False):
        '''
        Returns the first hash in alphabetical order and removes it. This
        function iterates depth-first.
        '''
        current_root = self.root
        glob_results = glob.glob(os.path.join(current_root, '*'))
        dir_list = list(util.filter_valid_directories(glob_results))

        # Keep going until there are no more subdirs
        while len(dir_list) > 0:
            # Although this looks like it should be outside the loop, it needs
            # to be here because dir_list is redefined at the end of it.
            dir_list.sort(reverse=reverse)
            current_root = os.path.join(current_root, dir_list[0])
            glob_results = glob.glob(os.path.join(current_root, '*'))
            dir_list = list(util.filter_valid_directories(glob_results))

        file_list = list(util.filter_valid_files(glob_results))
        file_list.sort(reverse=reverse)

        # Let the rest of the library do all the work and give it a hint as to
        # where to remove from.
        return self.remove(file_list[0], current_root=current_root)



    def pop_back(self):
        '''
        Returns the last hash in alphabetical order and removes it.
        '''
        return self.pop(reverse=True)


    def contains(self, key: str, current_root: str=None):
        '''
        Whether or not the key is contained in the set.

        This function exists because the python implementation of the `in`
        directive requires __iter__ to be defined and is far less performant
        than descending the tree in this algorithm.
        '''
        assert bool(re.match(util.FILE_NAME_REGEX, key)), 'Provided key is illegal'

        if current_root is None:
            current_root = self.root

        glob_results = glob.glob(os.path.join(current_root, '*'))
        file_list = list(util.filter_valid_files(glob_results))

        try:
            # Try to get the relative prefix.
            # If we can, then recurse normally, else check the current directory
            # and return the containment status.
            key_prefix_rel = self.key_to_prefix(key, from_subdir=current_root)
            # Prepare the next directory
            next_root = os.path.join(current_root, key_prefix_rel)
        except IndexError:
            return key in file_list

        # First check if the key is here
        if key in file_list:
            return True

        # Otherwise check for a new subdir
        dir_list = list(util.filter_valid_directories(glob_results))
        if key_prefix_rel in dir_list:
            # Recurse to the subdirectory that matches the key prefix
            return self.contains(
                key,
                current_root=next_root
            )

        # If all else fails, the key is not in here
        return False



    def issubset(self, other: set):
        '''
        Returns True if all of the elements in other are present in this hash
        tree.
        '''
        holds = True

        for elem in other:
            holds = holds and self.contains(elem)
            if not holds:
                break

        return holds


    def isdisjoint(self, other: set):
        '''
        Returns True if all of the elements in other are not present in this
        hash tree.
        '''
        holds = True

        for elem in other:
            holds = holds and not self.contains(elem)
            if not holds:
                break

        return holds
