#!/usr/bin/env python3
import sys
import numpy as np
from os.path import join, basename
from copy import deepcopy as copy

from pyFIT3D.common.constants import __c__
from pyFIT3D.common.tools import radial_sum_cube_e
from pyFIT3D.common.io import ReadArguments, get_data_from_fits, get_wave_from_header, output_spectra

class ReadArgumentsLocal(ReadArguments):
    """
    Argument parser for the emission-lines fit scripts.

    To add an argument to the script:
        Argument name in `__mandatory__` or `__optional__` list.
        Argument conversion function in `__mandatory_conv_func___` or `__optional_conv_func___` list.
        Argument default value (if not mandatory) in `__def_optional__`
    """
    # class static configuration:
    # arguments names and conversion string to number functions
    __script_name__ = basename(sys.argv[0])
    __mandatory__ = ['cube_filename', 'name', 'x0', 'y0', 'output_path']
    __optional__ = ['delta_R', 'badpix_ext', 'badpix_val', 'badpix_coll_threshold_frac']
    __arg_names__ = __mandatory__ + __optional__
    __N_tot_args__ = len(__arg_names__)
    # default values of optional arguments with __optional__ as keys
    __def_optional__ = {
        'delta_R': 2.5, 'badpix_ext': 3, 'badpix_val': 1, 'badpix_coll_threshold_frac': 0.75
    }

    # parse functions
    __conv_func_mandatory__ = {'cube_filename': str, 'name': str, 'output_path': str}
    __conv_func_optional__ = {'badpix_ext': int}
    __conv_func__ = __conv_func_mandatory__.copy()
    __conv_func__.update(__conv_func_optional__)

    # usage message
    __usage_msg__ = 'usage: {} FILENAME NAME X0 Y0 OUTPUT_PATH '.format(__script_name__)
    __usage_msg__ += ' [DELTA_R={}]'.format(__def_optional__['delta_R'])
    __usage_msg__ += ' [BADPIX_EXT={}]'.format(__def_optional__['badpix_ext'])
    __usage_msg__ += ' [BADPIX_VAL={}]'.format(__def_optional__['badpix_val'])
    __usage_msg__ += ' [BADPIX_COLL_THRESHOLD_FRACTION={}]'.format(__def_optional__['badpix_coll_threshold_frac'])

    def __init__(self, args_list=None, verbose=False):
        ReadArguments.__init__(self, args_list, verbose=verbose)

def collapse_badpixels_mask(mask__wyx, threshold_fraction=1, mask_value=1):
    """
    Performs the bad pixels mask collapse, i.e., generates a 2D map from a 3D
    (wavelengths, y, x) masking spaxels with a fraction of masked pixels equal
    or above `threshold`.

    Parameters
    ----------
    mask__wyx : array like
        Bad pixels mask cube (3 dimensions, NWAVE, NY, NX).

    threshold_fraction : float
        Sets the threshold to be considered a bad spaxel, i.e. spaxels with a
        fraction of masked pixels equal or above this threshold will be masked.
        threshold = NWAVE * threshold_fraction.

    Returns
    -------
    array like
        2D bad spaxels map.
    """
    nw, ny, nx = mask__wyx.shape
    threshold = nw*threshold_fraction
    badspaxels__yx = np.zeros((ny, nx), dtype=mask__wyx.dtype)
    badpixels_total__yx = mask__wyx.sum(axis=0)
    badspaxels__yx[badpixels_total__yx/nw >= threshold] == 1
    return badspaxels__yx

if __name__ == '__main__':
    pa = ReadArgumentsLocal()

    # Central and integrated spec extraction
    org_cube__wyx, org_h, n_ext = get_data_from_fits(pa.cube_filename, header=True, return_n_extensions=True)
    org_wave__w = get_wave_from_header(org_h, wave_axis=3)
    h_set_rss = {'CRVAL1': org_h['CRVAL3'], 'CDELT1': org_h['CDELT3'], 'CRPIX1': org_h['CRPIX3']}
    h_set_cube = {'CRVAL3': org_h['CRVAL3'], 'CDELT3': org_h['CDELT3'], 'CRPIX3': org_h['CRPIX3']}
    med_vel = org_h.get('MED_VEL')
    org_badpix__wyx = None
    org_error__wyx = None
    org_badspaxels__yx = None
    if org_h['EXTEND']:
        org_error__wyx = get_data_from_fits(pa.cube_filename, extension=1)
        org_badpix__wyx = get_data_from_fits(pa.cube_filename, extension=pa.badpix_ext)
        if pa.badpix_val != 1:
            _tmp_org_badpix__wyx = np.ones_like(org_badpix__wyx)
            _tmp_org_badpix__wyx[org_badpix__wyx != pa.badpix_val] = 0
            org_badpix__wyx = _tmp_org_badpix__wyx
        org_badspaxels__yx = collapse_badpixels_mask(org_badpix__wyx,
                                                     threshold_fraction=pa.badpix_coll_threshold_frac,
                                                     mask_value=1)
    r = radial_sum_cube_e(copy(org_cube__wyx), x0=pa.x0, y0=pa.y0, delta_R=pa.delta_R,
                          input_mask=org_badpix__wyx, input_error=org_error__wyx)
    output__rw, e_output__rw, _ = r
    f_cen__w = copy(output__rw[0])
    f_cen__w[~np.isfinite(f_cen__w)] = 0
    sqrt_f_cen__w = np.sqrt(np.abs(f_cen__w))
    e_f_cen__w = copy(e_output__rw[0])
    e_f_cen__w[~np.isfinite(e_f_cen__w)] = 1e12
    e_f_cen__w = np.where(e_f_cen__w > sqrt_f_cen__w, sqrt_f_cen__w, e_f_cen__w)
    cen_spec_filename = f'{pa.name}.spec_5.txt'
    output_spectra(org_wave__w, [f_cen__w, e_f_cen__w], join(pa.output_path, cen_spec_filename))
    f_int__w = copy(output__rw[5])
    f_int__w[~np.isfinite(f_int__w)] = 0
    sqrt_f_int__w = np.sqrt(np.abs(f_int__w))
    e_f_int__w = copy(e_output__rw[5])
    e_f_int__w[~np.isfinite(e_f_int__w)] = 1e12
    e_f_int__w = np.where(e_f_int__w > sqrt_f_int__w, sqrt_f_int__w, e_f_int__w)
    int_spec_filename = f'{pa.name}.spec_30.txt'
    output_spectra(org_wave__w, [f_cen__w, e_f_cen__w], join(pa.output_path, int_spec_filename))
