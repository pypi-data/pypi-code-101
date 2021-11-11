"""CIOLDAP Relax NG."""

from os.path import dirname, join


RELAXNG_CIOLDAP = {
    'namespace': 'http://ns.chrysal.io/cioldap',
    'root': 'cioldap', 'version': '1.0',
    'file': join(dirname(__file__), 'RelaxNG', 'cioldap.rng')}
