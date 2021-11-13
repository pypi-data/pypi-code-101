from .base import BaseCog

try:
    from . import orm
except ImportError:
    pass
