from urllib.request import pathname2url
import posixpath

def path_to_local_file_uri(path):
    """
    Convert local filesystem path to local file uri.
    """
    path = pathname2url(path)
    if path == posixpath.abspath(path):
        return "file://{path}".format(path=path)
    else:
        return "file:{path}".format(path=path)