# pylint: disable=too-few-public-methods, import-error, wrong-import-order, broad-except

# module-level docstring
__doc__='''
Path tools
==========

Easy to use tool to collect files matching a pattern.

Note: both class and function versions should be euivalent, both kept
just in case. Class may be usefull for repeated calls to `collect` method.

'''

from typing import Union, Iterable, List
from pathlib import Path
from os import popen
import re
import sys
import win32api
from .os_detect import Os
from .execute import execute
import logging
log = logging.getLogger( __file__ )

MAKE_FS_SAFE_PATTERN = re.compile( pattern=r'[\\/*?:"<>|]' )


class FileCollector:
    ''' Easy to use tool to collect files matching a pattern (recursive or not), using pathlib.glob. 
    Reasoning for making it a class: Making cohexist an initial check/processing on root with a recursive
    main function was not straightforward. I did it anyway, so feel free to use the function alternative. '''

    def __init__( self, root: Path ) -> None:
        assert root.is_dir()
        root.resolve()
        self.root = root
        self.log = logging.getLogger( __file__ )
        self.log.debug( "root=%s", root )

    def collect( self, pattern: Union[str,Iterable[str]] = '**/*.*' ) -> List[Path]:
        ''' Collect files matching given pattern(s) '''
        files = []
        
        if isinstance( pattern, str ):
            # 11/11/2020 BUGFIX : was collecting files in trash like a cyber racoon
            files = [
                item.resolve() 
                for item in self.root.glob( pattern )
                if item.is_file() and (not '$RECYCLE.BIN' in item.parts)
            ]

            self.log.debug( "\t'%s': Found %s files in %s", pattern, len(files), self.root )
        elif isinstance( pattern, Iterable ):
            patterns = pattern
            assert 0 < len(patterns)
            for p in patterns:
                files.extend( self.collect(p) )
        else:
            raise ValueError(f"FileCollector: 'pattern' ({pattern}) must be an Iterable or a string, but is a {type(pattern)}")

        return files
        

def file_collector( root: Path, pattern: Union[str,Iterable[str]] = '**/*.*' ) -> List[Path]:
    ''' Easy to use tool to collect files matching a pattern (recursive or not), using pathlib.glob.
    Collect files matching given pattern(s) '''
    assert root.is_dir()
    root.resolve()
    log.debug( "root=%s", root )

    def collect( _pattern: str ) -> List[Path]:
        # 11/11/2020 BUGFIX : was collecting files in trash like a cyber racoon
        _files = [
            item.resolve() 
            for item in root.glob( pattern )
            if item.is_file() and (not '$RECYCLE.BIN' in item.parts)
        ]
        log.debug( "\t'%s': Found %s files in %s", pattern, len(_files), root )
        return _files

    files = []
    if isinstance( pattern, str ):
        files = collect( pattern )
    elif isinstance( pattern, Iterable ):
        patterns = pattern
        assert 0 < len(patterns)
        for p in patterns:
            files.extend( collect(p) )
    else:
        raise ValueError(f"FileCollector: 'pattern' ({pattern}) must be an Iterable or a string, but is a {type(pattern)}")

    return files


def make_FS_safe( s: str ) -> str:
    ''' File Systems don't accept all characters on file/directory names.

    Return s with illegal characters stripped

    Note: OS/FS agnostic, applies a simple filter on characters: ``\\, /, *, ?, :, ", <, >, |``
    '''
    return re.sub(
        pattern=MAKE_FS_SAFE_PATTERN,
        repl="",
        string=s
    )

def find_available_path( root: Path, base_name, file: bool ) -> Path:
    ''' Returns a path to a file/directory that DOESN'T already exist.
    The file/dir the user wishes to make a path for is referred as X.

    `root`: where X must be created. Can be a list of path parts
    `base_name`: the base name for X. May be completed with '(index)' if name already exists.
    `file`: True if X is a file, False if it is a directory
    '''
    # Helper function: makes suffixes for already existing files/directories
    def suffixes():
        yield ''
        idx=0
        while True:
            idx+=1
            yield f" ({idx})"
    
    # Iterate over candidate paths until an unused one is found
    safe_base_name = make_FS_safe( base_name )
    if file:
        # name formatting has to keep the extension at the end of the name !
        ext_idx = safe_base_name.rfind('.')
        assert ext_idx!=-1
        f_name, f_ext = safe_base_name[:ext_idx], safe_base_name[ext_idx:]
        for suffix in suffixes():
            _object = root / ( f_name + suffix + f_ext )
            if not _object.is_file():
                return _object
    else:
        for suffix in suffixes():
            _object = root / ( safe_base_name + suffix )
            if not _object.is_dir():
                return _object


def make_valid_path( 
    root: Union[Path, List],
    base_name: str,
    file: bool = True,
    create: bool = False ) -> Path:
    ''' Returns a path to a file/directory that DOESN'T already exist.
    The file/dir the user wishes to make a path for is referred as X.

    `root`: where X must be created. Can be a list of path parts
    `base_name`: the base name for X. May be completed with '(index)' if name already exists.
    `file`: True if X is a file, False if it is a directory
    `create`: True instantiates X (empty file or dir), False doesn't

    Build upon `find_available_path`, adding:
    - root path construction
    - root mkdir
    - ability to initialize returned file/dir
    '''

    # make root path
    if isinstance(root, List):
        if isinstance(root[0], str):
            _root = Path(make_FS_safe(root[0]))
        elif isinstance(root[0], Path):
            _root = root[0]
        else:
            raise TypeError(f"root[0]={root[0]} is of unexpected type {type(root[0])}, not str or Path !")
        
        for path_part in root[1:]:
            assert isinstance(path_part, str), f"path part in root '{path_part}' is of unexpected type {type(path_part)}, not str !"
            safe_path_part = make_FS_safe(path_part)
            assert safe_path_part
            _root = _root / safe_path_part
    elif isinstance(root, Path):
        _root = root
    else:
        raise TypeError(f"root={root} is of unexpected type {type(root)}, not str or Path !")
            
    # make root directory
    ensure_dir_exists( _root )

    # Find valid path
    valid_path = find_available_path(
        _root,
        base_name,
        file
    )

    # Optionally create file/dir
    if create:
        if file:
            valid_path.touch()
        else:
            valid_path.mkdir()

    return valid_path


def ensure_dir_exists( folder: Path ) -> None:
    ''' Tests whether `folder` exists, creates it (and its whole path) if it doesn't.
    '''
    if folder.is_file():
        raise ValueError(f"Given path '{folder}' is a file !")
    if not folder.is_dir():
        folder.mkdir( parents=True )


def folder_get_file_count( _root: Path, use_fallback: bool = False ) -> int:
    ''' Uses built-in platform-specific ways to recursively count the number of files in a given directory.
    Reason for using CLI calls to platform-specific external tools : they typically offer superior performance (because optimised)

    `use_fallback` : if True, use Path.glob instead of platform-specific CLI calls (mainly for testing puposes)
    '''
    _root = _root.resolve()

    def fallback() -> int:
        return sum( 1 for x in _root.glob('**/*') if x.is_file() )

    if use_fallback:
        return fallback()

    current_os = Os()
    command = None
    if current_os.windows:
        # Windows CMD
        log.debug("Crawler from '%s'", _root)
        command = f"dir \"{_root}\" /A:-D /B /S | find \".\" /C"
    elif current_os.wsl or current_os.linux:
        # Linux
        log.debug("Crawler from '%s'", _root)
        command = f"find \"{_root}\" -type f|wc -l"
    else:
        log.warning( "OS not recognised or has no specific command set (%s); fallback method used.", current_os )
        return fallback()

    
    return int(popen( command ).read().strip())


def folder_get_subdirs( root_dir: Path ) -> List[Path]:
    ''' Return a list of first level subdirectories '''
    assert root_dir.is_dir()
    return [ 
        item
        for item in root_dir.resolve().iterdir()
        if item.is_dir() and (not '$RECYCLE.BIN' in item.parts)
    ]


def windows_list_logical_drives() -> List[Path]:
    ''' Uses windows-specific methods to retrieve a list of logical drives.

    Both methods have been developped and tested to give equivalent output and be interchangeable
    '''
    
    def method1():
        ''' uses a windows shell command to list drives '''
        try:

            def filter_drives( l ):
                for item in l:
                    if not item:
                        continue
                    try:
                        yield Path(item).resolve()
                    except Exception:
                        continue

            drives = list( 
                filter_drives( win32api.GetLogicalDriveStrings().split('\x00') ) 
            )
            return drives
        except ImportError as e:
            print(f"windows_list_logical_drives: ImportError raised, so you may have tried using this function on a non-windows system, or the `pypiwin32` package is missing : {e}")
            exit(1)
    
    def method2():
        ''' uses a windows shell command to list drives '''
        command = [ 'wmic', 'logicaldisk', 'get', 'name' ]
        stdout = execute( command )['stdout']

        def return_cleaned( l ):
            for item in l:
                if len(item) < 2:
                    continue
                if item[0].isupper() and item[1] == ':':
                    try:
                        # Bugfix : the '<driveletter>:' format was resolving to CWD when driveletter==CWD's driveletter. 
                        # This seems to be an expected Windows behavior. Fix: switch to '<driveletter>:\\' format, whis is more appropriate.
                        yield Path(item[:2]+'\\').resolve()
                    except Exception:
                        continue
        
        drives = list( return_cleaned(stdout.splitlines()) )
        return drives
    
    # Test
    # assert all( [ x.samefile(y) for x,y in zip(method1(),method2()) ] )
    
    try:
        return method1()
    except Exception:
        try:
            return method2()
        except Exception as e:
            print(f"windows_list_logical_drives: something went wrong : {e}")
            sys.exit(1)
