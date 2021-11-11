"""Chrysalio main Relax NG."""

from os.path import join, dirname

from pyramid.config import Configurator


RELAXNG = {
    'root': 'chrysalio', 'version': '1.0',
    'file': join(dirname(__file__), 'RelaxNG', 'chrysalio.rng')}


# =============================================================================
def includeme(configurator):
    """Function to include Relax NG.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.

    ``configurator.registry['relaxng']`` is a dictionary describing the main
    Relax NG with the following keys:

    * ``'root'``: the name of the root element, possibly with namespace
    * ``'version'``:  the value of attribute version
    * ``'file'``: the path to the Relax NG file
    """
    if isinstance(configurator, Configurator):
        configurator.registry['relaxng'] = RELAXNG
