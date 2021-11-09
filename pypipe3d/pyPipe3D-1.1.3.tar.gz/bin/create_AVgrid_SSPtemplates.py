#!/usr/bin/env python3
import sys
import numpy as np
from os.path import basename
from pyFIT3D.common.io import ReadArguments
from auto_ssp_new import new_SSPModels, _spec_model

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
    __mandatory__ = ['filename']
    __optional__ = [
        'AVmin', 'AVmax', 'n', 'RV', 'extlaw', 'label', 'output_path'
    ]
    __arg_names__ = __mandatory__ + __optional__
    __N_tot_args__ = len(__arg_names__)
    # default values of optional arguments with __optional__ as keys
    __def_optional__ = {
        'AVmin': 0, 'AVmax': 2, 'n': 5, 'RV': 3.1, 'extlaw': 'CCM', 'label': 'new', 'output_path': '.',
    }

    # parse functions
    __conv_func_mandatory__ = {'filename': str}
    __conv_func_optional__ = {'n': int, 'extlaw': str, 'label': str, 'output_path': str}
    __conv_func__ = __conv_func_mandatory__.copy()
    __conv_func__.update(__conv_func_optional__)

    # usage message
    __usage_msg__ = 'usage: {} SSP_FILENAME'.format(__script_name__)
    __usage_msg__ += ' [MIN_AV={}]'.format(__def_optional__['AVmin'])
    __usage_msg__ += ' [MAX_AV={}]'.format(__def_optional__['AVmax'])
    __usage_msg__ += ' [N_AV={}]'.format(__def_optional__['n'])
    __usage_msg__ += ' [R_V={}]'.format(__def_optional__['RV'])
    __usage_msg__ += ' [EXTINCT_LAW={}]'.format(__def_optional__['extlaw'])
    __usage_msg__ += ' [OUTPUT_LABEL={}]'.format(__def_optional__['label'])
    __usage_msg__ += ' [OUTPUT_PATH={}]'.format(__def_optional__['output_path'])

    def __init__(self, args_list=None, verbose=False):
        ReadArguments.__init__(self, args_list, verbose=verbose)
        self.check_AV()

    def check_AV(self):
        if (self.AVmin == self.AVmax):
            print('{}: MIN_AV need to be different from MAX_AV.'.format(self.__script_name__))
            sys.exit()
        if (self.n == 0):
            print('{}: N_AV should be greater than 0.'.format(self.__script_name__))
            sys.exit()

class SSPModels_AVgrid(new_SSPModels):
    def __init__(self, filename, AV_min=0, AV_max=2, n=10, R_V=3.1, extlaw='CCM', label='new_', path='.'):
        new_SSPModels.__init__(self, filename)
        self.create_AV_grid(AV_min, AV_max, n, R_V, extlaw)
        self.output_new_FITS(label=label, path=path)

    def create_AV_grid(self, AV_min=0, AV_max=2, n=10, R_V=3.1, extlaw='CCM'):
        '''
        Create a grid of dust extincted models with AV values::

            AV_grid = np.linspace(AV_min, AV_max, n)

        It will change the `self.parameters` scheme, adding a AV as a new parameter of the SSP template.

        Parameters
        ----------
        AV_min : float, optional
            The lowest value of the AV grid (in mag). Defaults to 0.

        AV_max : float, optional
            The highest value of the AV grid (in mag). Defaults to 2.

        n : int, optional
            The number of bins to divide the AV between `AV_min` and `AV_max`. Defaults to 10.

        R_V : float, optional
            Selective extinction parameter. Defaults to 3.1.

        extlaw : str {'CCM', 'CAL'}, optional
            Which extinction function to use.
            CCM will call :func:`pyFIT3D.modelling.dust.Cardelli_extlaw`.
            CAL will call :func:`pyFIT3D.modelling.dust.Calzetti_extlaw`.
            Default value is CCM.
        '''
        new_parameters = {}
        parameters_names = list(self.parameters.keys())
        parameters_names.append('AV')
        for name in parameters_names:
            new_parameters[name] = []
        # unnormalize models in order to self.get_models_extincted_obs_frame to work uppon unnormalized spectra.
        flux_models_unorm = (self.flux_models.T * 1/self.mass_to_light).T
        # new models
        new_n_models = n*self.n_models
        new_models = np.zeros((new_n_models, self.n_wave), dtype=self.flux_models.dtype)
        for i, AV in enumerate(np.linspace(AV_min, AV_max, n)):
            _models = np.zeros((self.n_models, self.wavelength.size))
            for i_mod, model in enumerate(flux_models_unorm):
                _models[i_mod] = _spec_model(wlo=self.wavelength, wlm=self.wavelength, fm=model,
                                             z=0, losvd=0, inst_disp=0, av=AV, rv=R_V, extlaw=extlaw)
            j = i*self.n_models
            new_models[j:j + self.n_models] = _models
            new_parameters['AV'] += [AV]*self.n_models
        for k, v in self.parameters.items():
            new_parameters[k] = np.asarray(n*v.tolist())
        new_parameters['AV'] = np.asarray(new_parameters['AV'])
        # new values
        self.parameters_units['AV'] = 'mag'
        self.parameters = new_parameters
        norm_wl = self.normalization_wavelength
        norm_hwin = self.normalization_half_window
        sel = (self.wavelength > norm_wl - norm_hwin) & (self.wavelength < norm_wl + norm_hwin)
        new_norm = (new_models[:, sel]).mean(axis=1)
        self.parameters['FNORM'] = new_norm
        new_models_norm = (new_models.T*1/new_norm).T
        self.n_models = new_n_models
        self.flux_models = new_models_norm
        self.mass_to_light = self.get_mtol()

if __name__ == '__main__':
    pa = ReadArgumentsLocal()
    SSPModels_AVgrid(pa.filename, AV_min=pa.AVmin, AV_max=pa.AVmax, n=pa.n, R_V=pa.RV, extlaw=pa.extlaw, label=pa.label, path=pa.output_path)
