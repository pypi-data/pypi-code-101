"""CIOSkeleton Relax NG."""

from os.path import dirname, join


RELAXNG_CIOSKELETON = {
    'namespace': 'http://ns.chrysal.io/cioskeleton',
    'root': 'cioskeleton', 'version': '1.0',
    'file': join(dirname(__file__), 'RelaxNG', 'cioskeleton.rng')}
