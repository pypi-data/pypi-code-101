import logging
import os
import shutil


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    return shutil.which(name) is not None


def path_exist(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        logging.error("Out path (%s) doesn't exist or is not a directory." % path)
        # RETURN
        return False
    else:
        # RETURN
        return True


def cmd_src_on_success_failure(config, on_success_failure: 'success, failure'):
    """
    Return shell cmd to execute on success or failure for the src file.
    :param config:
    :param on_success_failure:
    :return:
    """
    src_on_keyword = 'src_on_' + on_success_failure
    src_on_keyword_dest = src_on_keyword + '_dest'
    if src_on_keyword not in config:
        logging.info("%s is not defined, default back to 'keep'" % src_on_keyword)
        config[src_on_keyword] = 'keep'

    on_success_failure = config[src_on_keyword]
    cmd_on_success_failure = ""
    if on_success_failure == 'keep':
        pass
    elif on_success_failure == 'move':
        if src_on_keyword_dest not in config:
            logging.warning("%s was defined as 'move' but not %s was defined. Default back to 'keep'." %
                            (src_on_keyword, src_on_keyword_dest))

        dest = config[src_on_keyword_dest]
        if not path_exist(dest):
            logging.warning("Default back to keep for %s" % on_success_failure)
        else:
            cmd_on_success_failure = "mv {0} " + str(dest) + "/{1}"
    elif on_success_failure == 'delete':
        cmd_on_success_failure = "rm {0}"

    return cmd_on_success_failure


def do_src_on_done(exit_code: int, file, local_config):
    """
    Launch shell cmd to execute on success or failure, to move, delete ... src file.
    :param local_config:
    :param exit_code:
    :param file:
    :return:
    """

    if exit_code == 0:
        cmd = cmd_src_on_success_failure(config=local_config, on_success_failure='success')
        logging.debug("Exit code was successful.")
    else:
        cmd = cmd_src_on_success_failure(config=local_config, on_success_failure='failure')
        logging.debug("Exit code was not successful %s" % str(exit_code))

    cmd = cmd.format(file, os.path.basename(file))
    logging.debug("Execute post convert (empty if 'keep'): %s" % cmd)
    os.system(cmd)

    return None
