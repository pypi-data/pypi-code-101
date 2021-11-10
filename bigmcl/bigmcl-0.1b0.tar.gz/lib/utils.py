#! /usr/bin/env python3

import glob, os, datetime, re, shutil, sys


def collect_files( directory = './', filetype = '*', recursive = False ):
    '''
    Inputs: directory path, file extension (no "."), recursivity bool
    Outputs: list of files with `filetype`
    If the filetype is a list, split it, else make a list of the one entry.
    Parse the environment variable if applicable. Then, obtain a clean, full
    version of the input directory. Glob to obtain the filelist for each
    filetype based on whether or not it is recursive.
    '''

    if type(filetype) == list:
        filetypes = filetype.split()
    else:
        filetypes = [filetype]

    directory = formatPath( directory )
    filelist = []
    for filetype in filetypes:
        if recursive:
            filelist.extend(
                glob.glob( directory + "/**/*." + filetype, recursive = recursive )
            )
        else:
            filelist.extend(
                glob.glob( directory + "/*." + filetype, recursive = recursive )
            )

    return filelist


def expandEnvVar( path ):
    '''Expands environment variables by regex substitution'''

    if path.startswith( '/$' ):
        path = '/' + path
    env_comp = re.compile( r'/\$([^/]+)' )
    if not env_comp.search( path ):
        env_comp = re.compile( r'^\$([^/]+)' )
    var_search = env_comp.search( path )
    if var_search:
        var = var_search[1]
        pathChange = os.environ[ var ]
        path = env_comp.sub( pathChange, path )

    return path


def formatPath( path, isdir = None ):
    '''Goal is to convert all path types to absolute path with explicit dirs'''
   
    if path:
        path = os.path.expanduser( path )
        path = expandEnvVar( path )
        path = os.path.abspath( path )
        if isdir:
            if not path.endswith('/'):
                path += '/'
        else:
            if path.endswith( '/' ):
                if path.endswith( '//' ):
                    path = path[:-1]
                if not os.path.isdir( path ):
                    path = path[:-1]
            elif not path.endswith( '/' ):
                if os.path.isdir( path ):
                    path += '/'

    return path


def zprint(out_str, log = None, flush = True):
    fprint(out_str, log)
    print(out_str, flush = flush)

def vprint( toPrint, v = False, e = False , flush = True):
    '''Boolean print option to stdout or stderr (e)'''

    if v:
        if e:
            eprint( toPrint, flush = True)
        else:
            print( toPrint, flush = True)


def intro( script_name, args_dict, credit='', log = False, stdout = True):
    '''
    Inputs: script_name string, args_dict dictionary of arguments,
    credit string bool / path for output log
    Outputs: prints an introduction, returns start_time in YYYYmmdd format
    Creates a string to populate and format for the introduction using
    keys as the left-most descriptor and arguments (values) as the right
    most. Optionally outputs a log according to `log` path.
    '''

    start_time = datetime.datetime.now()
    date = start_time.strftime( '%Y%m%d' )

    out_str = '\n' + script_name + '\n' + credit + \
        '\nExecution began: ' + str(start_time)

    for arg in args_dict:
        out_str += '\n' + '{:<30}'.format(arg.upper() + ':') + \
            str(args_dict[ arg ])

    if log:
        zprint(out_str, log)
    elif stdout:
        print(out_str, flush = True)
    else:
        eprint( out_str, flush = True )

    return start_time

def outro( start_time, log = False, stdout = True ):
    '''
    Inputs: start time string formatted YYYYmmdd, log path
    Outputs: prints execution time and exits with 0 status
    '''


    end_time = datetime.datetime.now()
    duration = end_time - start_time
    dur_min = duration.seconds/60
    out_str = '\nExecution finished: ' + str(end_time) + '\t' + \
            '\n\t{:.2}'.format(dur_min) + ' minutes\n'

    if log:
        zprint(out_str, log)
    elif not stdout:
        eprint(out_str, flush = True)
    else:
        print(out_str, flush = True)

    sys.exit(0)


def findExecs( deps, exit = set(), verbose = True ):
    '''
    Inputs list of dependencies, `dep`, to check path.
    If dependency is in exit and dependency is not in path,
    then exit.
    '''

    vprint('\nDependency check:', v = verbose, e = True, flush = True)
    checks = []
    if type(deps) is str:
        deps = [deps]
    for dep in deps:
        check = shutil.which( dep )
        vprint('{:<15}'.format(dep + ':', flush = True) + \
            str(check), v = verbose, e = True)
        if not check and dep in exit:
            eprint('\nERROR: ' + dep + ' not in PATH', flush = True)
            sys.exit(300)
        else:
            checks.append(check)

    return checks
