# _pyLaCroix_module.py

__module_name__ = "_pyLaCroix_module.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])

# package imports #
# --------------- #
import os


# local imports #
# ------------- #
from ._supporting_functions import _fetch_palette_from_csv as fetch_module
from ._supporting_functions._fetch_palette_from_csv import _fetch_palette_from_csv
from ._supporting_functions._create_color_gradient import _create_color_gradient
from ._supporting_functions._update_parameter import _update_parameter


class _pyLaCroix:
    
    def __init__(self, n_points):
                         
        for key, value in _fetch_palette_from_csv(os.path.dirname(fetch_module.__file__)).items():
            _update_parameter(self, "_{}_palette".format(key), value)
            _update_parameter(self, key, _create_color_gradient(n_points, value, key))