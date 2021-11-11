from .jobdesc import load_jobs
from .soccer import soccer

# Module-level doc string
"""
SOCcer allows convenvient vectorized querying of the SOCcer API
and returns results in a structured tabular format (pandas df).
"""

# Indicate exported function
__all__ = [
    "load_jobs",
    "soccer"
]