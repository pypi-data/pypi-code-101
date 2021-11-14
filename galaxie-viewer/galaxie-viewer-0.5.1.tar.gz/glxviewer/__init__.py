from glxviewer.viewer import Viewer

APPLICATION_AUTHORS = ["Tuuuux"]
APPLICATION_NAME = "galaxie-viewer"
APPLICATION_COPYRIGHT = """Copyright (C) 2018-2021 Galaxie Viewer Project.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
"""
APPLICATION_VERSION = "0.5.1"

__all__ = ['Viewer', 'viewer']

viewer = Viewer()
