# -----------------------------------------------------------------------------
# BEGIN driver.py
# -----------------------------------------------------------------------------

import os
import sys
import time
from optparse import OptionParser
from src.sheng.compile import *
from src.sheng.utils import *


LOG_DIRECTORY = './log/'

SYSTEM_STREAMS = {
    'stdin': sys.stdin,
    'stdout': sys.stdout,
    'stderr': sys.stderr,
}


def default(str):
    return str + ' [Default: %default]'

def read_command(argv):
    usage_str = 'sheng [option] [file]'
    parser = OptionParser(usage_str)

    parser.add_option(
        '-d', '--debug', action='store_true', dest='debug',
        help=default('debug mode'), default=False
    )
    
    parser.add_option(
        '-i', '--input-stream', dest='input_stream',
        help=default('input stream'), default='stdin'
    )

    parser.add_option(
        '-o', '--output-stream', dest='output_stream',
        help=default('output stream'), default='stdout'
    )

    parser.add_option(
        '-l', '--log-stream', dest='log_stream',
        help=default('log stream, applicable only if debug mode is on'), 
        default=f'sheng_{time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())}.log'
    )

    options, other = parser.parse_args(argv[1:])
    if (len(other) == 0):
        parser.error('no input file')
    if (len(other) > 1):
        parser.error('Command line input not understood: ' + str(other[1:]))

    args = dict()
    args['file'] = other[0]

    # Debug, write logs to log stream
    if (options.debug):
        Global().is_debug = options.debug
        log_stream = None
        if (options.log_stream in SYSTEM_STREAMS):
            log_stream = SYSTEM_STREAMS[options.log_stream]
        else:
            log_stream_path = LOG_DIRECTORY + options.log_stream
            os.makedirs(os.path.dirname(log_stream_path), exist_ok=True)
            log_stream = open(log_stream_path, 'w')
        Global().log_stream = log_stream

    # Input stream
    input_stream = None
    if (options.input_stream in SYSTEM_STREAMS):
        input_stream = SYSTEM_STREAMS[options.input_stream]
    else:
        input_stream = open(options.input_stream, 'r')
    Global().input_stream = input_stream

    # Output stream
    output_stream = None
    if (options.output_stream in SYSTEM_STREAMS):
        output_stream = SYSTEM_STREAMS[options.output_stream]
    else:
        output_stream = open(options.output_stream, 'w')
    Global().output_stream = output_stream

    return args

def read_file(file):
    f = open(file, "r", encoding='utf-8')
    data = f.read()
    f.close()
    return data

def main():
    args = read_command(sys.argv)
    data = read_file(**args)
    return execute(data)


# -----------------------------------------------------------------------------
# END driver.py
# -----------------------------------------------------------------------------
