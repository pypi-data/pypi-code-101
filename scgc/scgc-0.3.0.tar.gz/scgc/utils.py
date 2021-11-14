import contextlib
import fnmatch
import itertools
import logging
import parmap
import os
import os.path as op
import shutil
import six
import subprocess
import tempfile
import time
from io import TextIOWrapper
from sarge import capture_stdout, capture_stderr
from six.moves import zip_longest


utils_logger = logging.getLogger(__name__)


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def multiprocess(f, iterable, *args, **kwargs):
    """
    Map an iterable to a function. Default key function chunks iterable by
    1000s.

    parameters
        f : callable
        iterable : any iterable where each item is sent to f
        args : arguments passed to mapped function
        kwargs : additional arguments for parmap.map

    returns
        mapped function result
    """
    chunksize = kwargs.pop('chunksize', 1000)
    key = kwargs.pop('key', lambda k, l=itertools.count(): next(l)//chunksize)
    for k, g in itertools.groupby(iterable, key=key):
        yield parmap.map(f, g, *args, **kwargs)


def find_files(directory, pattern):
    """
    returns all files (recursively) under directory that match pattern or
    patterns.

    parameters
        directory : where to start searching
        pattern : string pattern(s) to search; wildcards are accepted

    returns
        file paths : list
    """
    found_files = []
    pattern = [pattern] if isinstance(pattern, six.string_types) else pattern
    for root, dirs, files in os.walk(directory):
        for p in pattern:
            for filename in fnmatch.filter(files, p):
                found_files.append(os.path.join(root, filename))
    return found_files


@contextlib.contextmanager
def file_transaction(*rollback_files):
    """
    Wrap file generation in a transaction, moving to output if finishes.
    """
    exts = {".vcf": ".idx", ".bam": ".bai", "vcf.gz": ".tbi", ".fastq.gz": ".count"}
    safe_names, orig_names = _flatten_plus_safe(rollback_files)
    # remove any half-finished transactions
    remove_files(safe_names)
    try:
        if len(safe_names) == 1:
            yield safe_names[0]
        else:
            yield tuple(safe_names)
    # failure -- delete any temporary files
    except:
        remove_files(safe_names)
        remove_tmpdirs(safe_names)
        raise
    # worked -- move the temporary files to permanent location
    else:
        for safe, orig in zip(safe_names, orig_names):
            if os.path.exists(safe):
                shutil.move(safe, orig)
                for check_ext, check_idx in six.iteritems(exts):
                    if safe.endswith(check_ext):
                        safe_idx = safe + check_idx
                        if os.path.exists(safe_idx):
                            shutil.move(safe_idx, orig + check_idx)
        remove_tmpdirs(safe_names)


def remove_tmpdirs(fnames):
    for x in fnames:
        xdir = os.path.dirname(os.path.abspath(x))
        if xdir and os.path.exists(xdir):
            shutil.rmtree(xdir, ignore_errors=True)


def remove_files(fnames):
    for x in fnames:
        if x and os.path.exists(x):
            if os.path.isfile(x):
                os.remove(x)
            elif os.path.isdir(x):
                shutil.rmtree(x, ignore_errors=True)


def _flatten_plus_safe(rollback_files):
    """
    Flatten names of files and create temporary file names.
    """
    tx_files, orig_files = [], []
    for fnames in rollback_files:
        if isinstance(fnames, six.string_types):
            fnames = [fnames]
        for fname in fnames:
            basedir = safe_makedir(os.path.dirname(fname))
            tmpdir = safe_makedir(tempfile.mkdtemp(dir=basedir))
            tx_file = os.path.join(tmpdir, os.path.basename(fname))
            tx_files.append(tx_file)
            orig_files.append(fname)
    return tx_files, orig_files


def safe_makedir(dname):
    """
    Make a directory if it doesn't exist, handling concurrent race conditions.
    """
    if not dname:
        return dname
    num_tries = 0
    max_tries = 5
    while not os.path.exists(dname):
        try:
            os.makedirs(dname)
        except OSError:
            if num_tries > max_tries:
                raise
            num_tries += 1
            time.sleep(2)
    return dname


def file_exists(fnames):
    """
    Check if a file or files exist and are non-empty.

    parameters
        fnames : file path as string or paths as list; if list, all must exist

    returns
        boolean
    """
    if isinstance(fnames, six.string_types):
        fnames = [fnames]
    for f in fnames:
        if not os.path.exists(f) or os.path.getsize(f) == 0:
            return False
    return True


def stdout_iter(cmd):
    p = capture_stdout(cmd)
    for line in TextIOWrapper(p.stdout):
        yield line


def run(cmd, description=None, iterable=None, retcodes=[0]):
    """Runs a command using check_call.

    Args:
        cmd (str): shell command as a string
        description (Optional[str]):
        iterable (Optional[str]):
    """
    if description:
        utils_logger.info(description)
    utils_logger.info("$> %s" % cmd)
    if iterable:
        return stdout_iter(cmd)
    else:
        p = capture_stderr(cmd)
        if p.returncode not in retcodes:
            for line in TextIOWrapper(p.stderr):
                utils_logger.error(line.strip())
            raise subprocess.CalledProcessError(p.returncode, cmd=cmd)
        else:
            return p


def submit(cmd, queue="normal", job_name="scgcpy", cpus=8, time="24:00:00", mem='5G',
           log_dir="logs", depends=[], umask="0002"):
    log_dir = os.path.realpath(os.path.expanduser(log_dir))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    depends = [i for i in depends if i]
    qsub_cmd = ("qsub -N {job_name} -q {queue} "
                "-l walltime={time},ncpus={cpus},mem={mem} "
                "-W umask={umask} -j oe -o {log_dir} "
                "{dependencies}").format(job_name=job_name,
                                         queue=queue,
                                         time=time,
                                         cpus=cpus,
                                         umask=umask,
                                         mem=mem,
                                         log_dir=log_dir,
                                         dependencies="" if not depends else "-W depend=afterany:%s" % ":".join(depends[-50:]))
    cmd = '''echo \"{cmd}\" | {qsub_cmd}'''.format(cmd=cmd, qsub_cmd=qsub_cmd)
    utils_logger.info(cmd)
    p = capture_stdout(cmd, shell=True)
    job_id = ""
    for line in TextIOWrapper(p.stdout):
        job_id = line.strip()
        break
    return job_id


def cp(src, dst):
    """
    will transfer to rclone's 'remote' if either src or dst starts with 'remote:'.
    """
    if src.startswith("remote:") or dst.startswith("remote:"):
        try:
            run("rclone copy {src} {dst}".format(src=src, dst=dst))
        except subprocess.CalledProcessError:
            utils_logger.warn("failed transferring {src} to {dst}".format(src=src, dst=dst))
            return False
    else:
        shutil.copyfile(src, dst)
    return True


def mv(src, dst):
    shutil.move(src, dst)


def logger(log_file=None, log_name=None, log_level=logging.INFO,
           log_format="[%(asctime)s %(name)s %(levelname)s] %(message)s"):
    # dict(info=logging.INFO, debug=logging.DEBUG) and then map to proper level
    logging.basicConfig(level=log_level, format=log_format)
    log = logging.getLogger(log_name)
    if log_file:
        logfile = logging.FileHandler(log_file)
        logfile.setLevel(log_level)
        logfile.setFormatter(logging.Formatter(log_format))
        log.addHandler(logfile)
    return log


@contextlib.contextmanager
def tmp_dir():
    d = None
    try:
        d = tempfile.mkdtemp()
        yield d
    finally:
        if d:
            shutil.rmtree(d)


def is_plain(input_file):
    """Use `file` to verify input is plain text.

    Args:
        input_file (str): path to file

    Returns:
        boolean

    Raises:
        IOError
    """
    if not op.exists(input_file):
        raise IOError(2, "No such file:", input_file)
    for output in run("file -b --mime-type " + input_file, iterable=True):
        if "plain" in output:
            return True
    return False


def pigz_file(fname, cores=1):
    if not op.exists(fname):
        raise IOError(2, "No such file:", fname)
    file_path = ""
    out_file = ""
    if fname.endswith('.gz'):
        out_file = fname
        if is_plain(fname):
            # need to rename the file
            file_path = op.splitext(fname)[0]
            shutil.move(fname, file_path)
    else:
        out_file = fname + '.gz'
        file_path = fname
    if file_path:
        try:
            run("pigz -f --best -p %d %s" % (cores, file_path))
        except:
            run("gzip -f --best %s" % file_path)
    return out_file


def gunzip_file(fname):
    """Decompress fname using `gzip -d`.

    Args:
        fname (str): file path to decompress

    Returns:
        str
    """
    out_file, ext = op.splitext(fname)
    run("gzip -d -f %s" % fname)
    return out_file


def touch(fname, times=None):
    """https://stackoverflow.com/questions/1158076/implement-touch-using-python"""
    with open(fname, 'a'):
        os.utime(fname, times)
