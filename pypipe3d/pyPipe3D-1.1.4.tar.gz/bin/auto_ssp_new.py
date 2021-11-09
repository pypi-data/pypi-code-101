#!/usr/bin/env python3
import io
import sys
import numpy as np
from copy import deepcopy as copy
from os.path import join, basename, isfile, exists
from astropy.io import fits

from pyFIT3D.modelling.dust import spec_apply_dust
from pyFIT3D.modelling.stellar import StPopSynt, SSPModels

from pyFIT3D.common.io import array_to_fits, write_img_header, ReadArguments
from pyFIT3D.common.io import read_spectra, print_time, clean_preview_results_files
from pyFIT3D.common.io import get_wave_from_header, readFileArgumentParser, print_verbose
from pyFIT3D.common.stats import shift_convolve
from pyFIT3D.common.constants import __selected_R_V__, __selected_extlaw__
from pyFIT3D.common.auto_ssp_tools import auto_ssp_elines_single_main

def _spec_model(wlo, wlm, fm, z, losvd, inst_disp, av, rv, extlaw):
    return spec_apply_dust(
        wlo/(1 + z),
        shift_convolve(wlo, wlm, fm, z, losvd, sigma_inst=inst_disp),
        av, R_V=rv, extlaw=extlaw
    )

class new_SSPModels(SSPModels):
    """
    A helper class to deal with SSP models. It reads the models directly
    from FITS file.
    """
    def __init__(self, filename):
        """
        Parameters
        ----------
        filename : str
            FITS filename of the SSP models spectral library.
        """
        # XXX: To the future (2019-10-18 EADL) selects initial models instead
        # load another FITS file.
        self._t = fits.open(filename)
        self._ot = copy(self._t)
        self.new_ver = False
        if len(self._t) > 1:
            self.new_ver = True
        self.filename = filename
        self._parse_data()

    def _parse_data(self):
        self.wavelength = self._parse_wavelength()
        self.n_wave = self.wavelength.size
        self.n_models = self._t[0].header.get('NAXIS2')
        self.flux_models = self._t[0].data
        if self.new_ver:
            self._parse_new()
        else:
            SSPModels.__init__(self, self.filename)
            # self._parse_old()
            self._t = copy(self._ot)
            self._convert_to_new()

        # deprecated variables in order to keep working the code at first instance:
        self.wavenorm = self.normalization_wavelength
        if 'AGE' in self.parameters.keys():
            self.age_models = self.parameters['AGE']
        if 'MET' in self.parameters.keys():
            self.metallicity_models = self.parameters['MET']

    def get_mtol(self):
        mtol = 1/self.parameters['FNORM']
        return mtol

    def _convert_to_new(self):
        self.parameters = {}
        self.parameters_units = {}
        self.parameters['AGE'] = copy(self.age_models)
        self.parameters['MET'] = copy(self.metallicity_models)
        self.parameters['FNORM'] = np.asarray([self._t[0].header.get(f'NORM{i}')
                                               for i in range(self._t[0].header.get('NAXIS2'))])
        self.parameters_units['AGE'] = 'Gyr'
        self.parameters_units['MET'] = ''
        self.parameters_units['FNORM'] = ''
        self.normalization_half_window = 45

    def _parse_old(self):
        self.normalization_wavelength = self._parse_normalization_wavelength()
        self.age_models, self.metallicity_models, self.mass_to_light = self._parse_tZ_models()

    def _parse_normalization_wavelength(self):
        """ Search for the normalization wavelength at the FITS header.
        If the key WAVENORM does not exists in the header, sweeps all the
        models looking for the wavelengths where the flux is closer to 1,
        calculates the median of those wavelengths and return it.

        Returns
        -------
        float
            The normalization wavelength.
        """
        try:
            wave_norm = self._t[0].header['WAVENORM']
        except Exception as ex:
            _closer = 1e-6
            probable_wavenorms = np.hstack([self.wavelength[(np.abs(self.flux_models[i] - 1) < _closer)]
                                            for i in range(self.n_models)])
            wave_norm = np.median(probable_wavenorms)
            # wave_norm = self._parse_wavelength()[int(self.n_wave/2)]
            print(f'[SSPModels] {ex}')
            print(f'[SSPModels] setting normalization wavelength to {wave_norm} A')
        return wave_norm

    def _parse_wavelength(self, mask=None):
        """ Creates wavelength array from FITS header. Applies a mask to
        wavelengths if `mask` is set.

        Parameters
        ----------
        mask : array like, optional
            Masked wavelengths.

        Returns
        -------
        array like
            Wavelenght array from FITS header.

        See also
        --------
        :func:`pyFIT3D.common.io.get_wave_from_header`
        """
        # crval = self._header['CRVAL1']
        # cdelt = self._header['CDELT1']
        # crpix = self._header['CRPIX1']
        # pixels = np.arange(self.n_wave) + 1 - crpix
        # w = crval + cdelt*pixels
        w = get_wave_from_header(self._t[0].header, wave_axis=1)
        if mask is None:
            mask = np.ones_like(w).astype('bool')
        return w[mask]

    def _parse_tZ_models(self):
        """ Reads the values of age, metallicity and mass-to-light at the
        normalization flux from the SSP models FITS file.

        Returns
        -------
        array like
            Ages, in Gyr, in the sequence as they appear in FITS data.

        array like
            Metallicities in the sequence as they appear in FITS data.

        array like
            Mass-to-light value at the normalization wavelength.
        """
        hdr = self._t[0].header
        ages = np.zeros(self.n_models, dtype='float')
        Zs = ages.copy()
        mtol = ages.copy()
        for i in range(self.n_models):
            mult = {'Gyr': 1, 'Myr': 1/1000}
            name_read_split = hdr.get(f'NAME{i}').split('_')
            # removes 'spec_ssp_' from the name
            name_read_split = name_read_split[2:]
            _age = name_read_split[0]
            if 'yr' in _age:
                mult = mult[_age[-3:]]  # Gyr or Myr
                _age = _age[:-3]
            else:
                mult = 1  # Gyr
            age = mult*np.float(_age)
            _Z = name_read_split[1].split('.')[0]
            Z = np.float(_Z.replace('z', '0.'))
            ages[i] = age
            Zs[i] = Z
            mtol[i] = 1/np.float(hdr.get(f'NORM{i}'))
        return ages, Zs, mtol

    def _parse_new(self):
        self.parameters = {}
        self.parameters_units = {}
        for i, par in enumerate(self._t[1].data.names):
            self.parameters[par] = self._t[1].data[par]
            self.parameters_units[par] = self._t[1].header.get(f'TUNIT{i}', '')
        self.mass_to_light = self.get_mtol()
        self.normalization_wavelength = self._t[0].header.get(f'WAVENORM', '')
        self.normalization_half_window = self._t[0].header.get(f'NORMHWIN', '')

    def get_par_average_from_coeffs(self, coeffs, par_name, log_avg=False):
        '''
        Return the value from the age and metallicity weighted by light and mass
        from the age and metallicity of each model weighted by the `coeffs`.

        Parameters
        ----------
        coeffs : array like
            Coefficients of each SSP model.

        par_name : str
            Name of parameter to be averaged.

        Returns
        -------
        float
            Parameter average.

        float
            Parameter average weighted by mass.
        '''
        coeffs = np.array(coeffs)
        coeffs[~np.isfinite(coeffs)] = 0
        avpar, avpar_m = 0, 0
        try:
            par = self.parameters[par_name]
            if log_avg:
                par = np.log10(par)
            if not (coeffs == 0).all():
                norm_C = coeffs.sum()
                coeffs_normed = coeffs/norm_C
                avpar = np.dot(coeffs_normed, par)
                avpar_m = np.dot(self.mass_to_light*coeffs_normed, par)
        except KeyError:
            print(f'[SSPModels] parameter {par_name} do not exists.')
        except Exception as ex:
            print(f'[SSPModels] {ex}')
        return avpar, avpar_m

    def get_models_extincted_obs_frame(self, wavelength, sigma, redshift, AV, sigma_inst, R_V=3.1, extlaw='CCM', coeffs=None):
        """
        Shift and convolves SSP model fluxes (i.e. `self.flux_models`) to `wavelength`
        using the observed kinetic parameters `redshift` and `sigma` (velocity
        dispersion). The convolution considers the instrumental dispersion of the
        observed data if `sigma_inst` is not None. After the shift and convolution
        of the models, it applies dust extinction to the SSPs following the extinction
        law `extlaw`  with `AV` attenuance. It uses the vector population `coeffs`
        in order to accelerate the process only performing the calculation over
        the models where coeffs != 0.

        Parameters
        ----------
        wavelength : array like
            Wavelenghts at observed frame.

        sigma : float
            Velocity dispersion (i.e. sigma) at observed frame.

        redshift : float
            Redshift of the Observed frame.

        AV : float or array like
            Dust extinction in mag.
            TODO: If AV is an array, will create an (n_AV, n_wave) array of dust spectra.

        sigma_inst : float or None
            Sigma instrumental.

        R_V : float, optional
            Selective extinction parameter (roughly "slope"). Default value 3.1.

        extlaw : str {'CCM', 'CAL'}, optional
            Which extinction function to use.
            CCM will call `Cardelli_extlaw`.
            CAL will call `Calzetti_extlaw`.
            Default value is CCM.

        coeffs : array like
            Coefficients of each SSP model.

        Returns
        -------
        array like
            SSP spectra shift and convolved at the observed frame extincted by dust.
            Has the same dimension as (SSPModels.n_models, wavelenght.size).

        See also
        --------
        :func:`pyFIT3D.common.stats.shift_convolve`, :func:`pyFIT3D.modelling.dust.spec_apply_dust`
        """
        flux_models_obsframe_dust = np.zeros((self.n_models, wavelength.size))
        if coeffs is None:
            models_iter = range(self.n_models)
        else:
            models_iter = [i for i, c in enumerate(coeffs) if c != 0]
        for i in models_iter:
            flux_models_obsframe_dust[i] = _spec_model(  # _fast(
                wlo=wavelength, wlm=self.wavelength, fm=self.flux_models[i],
                z=redshift, losvd=sigma, inst_disp=sigma_inst, av=AV, rv=R_V,
                extlaw=extlaw)
        return flux_models_obsframe_dust

    def get_model_from_coeffs(self, coeffs, wavelength, sigma, redshift, AV, sigma_inst, R_V=3.1, extlaw='CCM'):
        """
        Shift and convolves SSP model fluxes (i.e. `self.flux_models`) to
        wavelengths `wave_obs` using `sigma` and `sigma_inst`. After this,
        applies dust extinction to the SSPs following the extinction law
        `extlaw` with `AV` attenuance. At the end, returns the SSP model
        spectra using `coeffs`.

        Parameters
        ----------
        coeffs : array like
            Coefficients of each SSP model.

        wavelength : array like
            Wavelenghts at observed frame.

        sigma : float
            Velocity dispersion (i.e. sigma) at observed frame.

        redshift : float
            Redshift of the Observed frame.

        AV : float or array like
            Dust extinction in mag.
            TODO: If AV is an array, will create an (n_AV, n_wave) array of dust spectra.

        sigma_inst : float or None
            Sigma instrumental.

        R_V : float, optional
            Selective extinction parameter (roughly "slope"). Default value 3.1.

        extlaw : str {'CCM', 'CAL'}, optional
            Which extinction function to use.
            CCM will call `Cardelli_extlaw`.
            CAL will call `Calzetti_extlaw`.
            Default value is CCM.

        Returns
        -------
        array like
            SSP model spectrum created by coeffs.

        See also
        --------
        :func:`pyFIT3D.common.stats.shift_convolve`, :func:`pyFIT3D.modelling.dust.spec_apply_dust`
        """
        coeffs = np.array(coeffs)
        coeffs[~np.isfinite(coeffs)] = 0
        if (coeffs == 0).all():
            model = np.zeros(wavelength.size)
        else:
            fl_of_d = self.get_models_extincted_obs_frame(wavelength, sigma,
                                                          redshift, AV, sigma_inst,
                                                          R_V=R_V, extlaw=extlaw,
                                                          coeffs=coeffs)
            model = np.dot(coeffs, fl_of_d)
        return model

    def output_new_FITS(self, label='new', path='.'):
        old_hdr = self._t[0].header
        hdu = fits.PrimaryHDU(
            data=self.flux_models,
            header=fits.Header([
                ('CRVAL1', old_hdr.get('CRVAL1', self.wavelength[0])),
                ('CDELT1', old_hdr.get('CDELT1', np.diff(self.wavelength)[0])),
                ('CRPIX1', old_hdr.get('CRPIX1', 1)),
                ('CTYPE1', 'wavelength'),
                ('CUNIT1', 'AA'),
                ('CTYPE2', 'flux'),
                ('CUNIT2', ''),
                ('WAVENORM', self.normalization_wavelength),
                ('NORMHWIN', self.normalization_half_window),
            ])
        )
        columns = self.parameters.keys()
        units = [self.parameters_units[k] for k in columns]
        fmts = {column: 'E' for column in columns}
        _units = dict(zip(columns, units))
        _columns = []
        for k, v in self.parameters.items():
            _columns.append(fits.Column(name=k, array=v, format=fmts[k], unit=_units[k]))
        table_hdu = fits.BinTableHDU.from_columns(_columns)
        table_hdu.name = 'PARAMETERS'
        hdu_list = fits.HDUList([hdu, table_hdu])
        basis_name = f'SSPModels-{label}.fits.gz'
        hdu_list.writeto(join(path, basis_name), overwrite=True)

class new_StPopSynt(StPopSynt):
    def __init__(self, config, wavelength, flux, eflux, ssp_file, out_file,
                 ssp_nl_fit_file=None, sigma_inst=None, min=None, max=None,
                 w_min=None, w_max=None, nl_w_min=None, nl_w_max=None,
                 elines_mask_file=None, mask_list=None,
                 R_V=3.1, extlaw='CCM', spec_id=None, guided_errors=None,
                 plot=None, verbose=False, ratio_master=None, fit_gas=True):
        StPopSynt.__init__(self, config, wavelength, flux, eflux, ssp_file,
                           out_file,ssp_nl_fit_file, sigma_inst, min, max,
                           w_min, w_max, nl_w_min, nl_w_max, elines_mask_file,
                           mask_list, R_V, extlaw, spec_id, guided_errors,
                           plot, verbose, ratio_master, fit_gas)

    def _load_ssp_fits(self):
        self.models = new_SSPModels(self.filename)

        # deprecated the use of self.ssp.
        # in order to keep working the code at first instance:
        self.ssp = self.models

        if self.filename_nl_fit:
            self.models_nl_fit = new_SSPModels(self.filename_nl_fit)

            # deprecated the use of self.ssp_nl_fit
            # in order to keep working the code at first instance:
            self.ssp_nl_fit = self.models_nl_fit

    def _MC_averages(self):
        """
        Calc. of the mean age, metallicity and AV weighted by light and mass.
        """
        ssp = self.models

        coeffs_input_zero = self.coeffs_input_MC
        _coeffs = self.coeffs_ssp_MC
        # print(_coeffs)
        norm = _coeffs.sum()
        _coeffs_norm = _coeffs/norm
        _sigma = self.coeffs_ssp_MC_rms
        _sigma_norm = np.divide(_sigma*_coeffs_norm, _coeffs, where=_coeffs > 0.0, out=np.zeros_like(_coeffs))
        _min_coeffs = self.orig_best_coeffs
        _min_coeffs_norm = _min_coeffs/norm
        # _sigma_norm = np.where(_coeffs > 0, _sigma*(_coeffs_norm/_coeffs), 0)

        l_age_min, l_age_min_mass = ssp.get_par_average_from_coeffs(_coeffs, 'AGE', log_avg=True)
        l_met_min, l_met_min_mass = ssp.get_par_average_from_coeffs(_coeffs, 'MET', log_avg=True)
        AV_min, AV_min_mass = ssp.get_par_average_from_coeffs(_coeffs, 'AV', log_avg=False)
        e_l_age_min, e_l_age_min_mass = ssp.get_par_average_from_coeffs(_sigma, 'AGE', log_avg=True)
        e_l_met_min, e_l_met_min_mass = ssp.get_par_average_from_coeffs(_sigma, 'MET', log_avg=True)
        e_AV_min, e_AV_min_mass = ssp.get_par_average_from_coeffs(_sigma, 'AV', log_avg=False)

        self.mass_to_light = np.dot(ssp.mass_to_light, _coeffs_norm)

        self.age_min = 10**l_age_min
        self.met_min = 10**l_met_min
        self.AV_min = AV_min
        if self.mass_to_light == 0:
            self.mass_to_light = 1
        self.age_min_mass = 10**(l_age_min_mass/self.mass_to_light)
        self.met_min_mass = 10**(l_met_min_mass/self.mass_to_light)
        self.AV_min_mass = AV_min_mass/self.mass_to_light

        # propagate std of coeffs in order to calculate error in age and met.
        _f = np.log10(np.e)
        self.e_age_min = np.abs(_f*e_l_age_min*self.age_min)
        self.e_met_min = np.abs(_f*e_l_met_min*self.met_min)
        self.e_AV_min = np.abs(_f*e_AV_min*self.AV_min)
        self.e_age_min_mass = np.abs(_f*e_l_age_min*self.age_min_mass)
        self.e_met_min_mass = np.abs(_f*e_l_met_min*self.met_min_mass)
        self.e_AV_min_mass = np.abs(_f*e_AV_min*self.AV_min_mass)

    def output_coeffs_MC_to_screen(self):
        cols = 'ID,AGE,MET,COEFF,Min.Coeff,log(M/L),AV,N.Coeff,Err.Coeff'
        fmt_cols = '| {0:^4} | {1:^7} | {2:^6} | {3:^6} | {4:^9} | {5:^8} | {6:^4} | {7:^7} | {8:^9} |'
        fmt_numbers = '| {:=04d} | {:=7.4f} | {:=6.4f} | {:=6.4f} | {:=9.4f} | {:=8.4f} | {:=4.2f} | {:=7.4f} | {:=9.4f} | {:=6.4f} | {:=6.4f}'
        # fmt_numbers_out_coeffs = '{:=04d},{:=7.4f},{:=6.4f},{:=6.4f},{:=9.4f},{:=8.4f},{:=4.2f},{:=7.4f},{:=9.4f},{:=6.4f},{:=6.4f}'
        cols_split = cols.split(',')
        tbl_title = fmt_cols.format(*cols_split)
        ntbl = len(tbl_title)
        tbl_border = ntbl*'-'
        print(tbl_border)
        print(tbl_title)
        print(tbl_border)
        for i in range(self.models.n_models):
            try:
                C = self.coeffs_ssp_MC[i]
            except (IndexError,TypeError):
                C = 0
            if np.isnan(C):
                C = 0
            if C < 1e-5:
                continue
        # for i, C in enumerate(_coeffs):
            tbl_row = []
            tbl_row.append(i)
            tbl_row.append(self.models.parameters['AGE'][i])
            tbl_row.append(self.models.parameters['MET'][i])
            tbl_row.append(self.coeffs_norm[i])  # a_coeffs_N
            tbl_row.append(self.min_coeffs_norm[i])  # a_min_coeffs
            tbl_row.append(np.log10(self.models.mass_to_light[i]))
            tbl_row.append(self.models.parameters['AV'][i])  # deprecated. better usage self.AV.best['value']
            tbl_row.append(C)  # a_coeffs
            tbl_row.append(self.coeffs_ssp_MC_rms[i])  # a_e_coeffs
            tbl_row.append(self.coeffs_input_MC[i])  # ???
            tbl_row.append(self.coeffs_input_MC_rms[i])  # ???
            print(fmt_numbers.format(*tbl_row))
        print(tbl_border)

    def output_coeffs_MC(self, filename, write_header=True):
        """
        Outputs the SSP coefficients table to the screen and to the output file `filename`.

        Parameters
        ----------
        filename : str
            The output filename to the coefficients table.
        """

        if isinstance(filename, io.TextIOWrapper):
            f_out_coeffs = filename
        else:
            f_out_coeffs = open(filename, 'a')

        cols = 'ID,AGE,MET,COEFF,Min.Coeff,log(M/L),AV,N.Coeff,Err.Coeff'
        cols_out_coeffs = cols.replace(',', '\t')
        fmt_numbers_out_coeffs = '{:=04d}\t{:=7.4f}\t{:=6.4f}\t{:=6.4f}\t{:=9.4f}\t{:=8.4f}\t{:=4.2f}\t{:=7.4f}\t{:=9.4f}'

        if write_header:
            print(f'#{cols_out_coeffs}', file=f_out_coeffs)

        for i in range(self.models.n_models):
            try:
                C = self.coeffs_ssp_MC[i]
            except (IndexError,TypeError):
                C = 0
            if np.isnan(C):
                C = 0
        # for i, C in enumerate(_coeffs):
            tbl_row = []
            tbl_row.append(i)
            tbl_row.append(self.models.parameters['AGE'][i])
            tbl_row.append(self.models.parameters['MET'][i])
            tbl_row.append(self.coeffs_norm[i])  # a_coeffs_N
            tbl_row.append(self.min_coeffs_norm[i])  # a_min_coeffs
            tbl_row.append(np.log10(self.models.mass_to_light[i]))
            tbl_row.append(self.models.parameters['AV'][i])  # deprecated. better usage self.AV.best['value']
            tbl_row.append(C)  # a_coeffs
            tbl_row.append(self.coeffs_ssp_MC_rms[i])  # a_e_coeffs
            print(fmt_numbers_out_coeffs.format(*tbl_row), file=f_out_coeffs)

        if not isinstance(filename, io.TextIOWrapper):
            f_out_coeffs.close()

    def output_fits(self, filename):
        """
        Writes the FITS file with the output spectra (original, model, residual and joint).

        Parameters
        ----------
        filename : str
            Output FITS filename.
        """
        s = self.spectra
        table = np.array(self.output_spectra_list)
        array_to_fits(filename, table, overwrite=True)
        h = {}
        h['CRPIX1'] = 1
        h['CRVAL1'] = s['raw_wave'][0]
        h['CDELT1'] = s['raw_wave'][1] - s['raw_wave'][0]
        h['NAME0'] = 'org_spec'
        h['NAME1'] = 'model_spec'
        h['NAME2'] = 'mod_joint_spec'
        h['NAME3'] = 'gas_spec'
        h['NAME4'] = 'res_joint_spec'
        h['NAME5'] = 'no_gas_spec'
        h['COMMENT'] = f'OUTPUT {basename(sys.argv[0])} FITS'
        columns_pars_data = {
            'MINCHISQ': self.output_results[0],
            'LWAGE': self.output_results[1],
            'E_LWAGE': self.output_results[2],
            'LWMET': self.output_results[3],
            'E_LWMET': self.output_results[4],
            'AV': self.output_results[5],
            'E_AV': self.output_results[6],
            'REDSHIFT': self.output_results[7],
            'E_REDSHI': self.output_results[8],
            'VELDISP': self.output_results[9],
            'E_VELDIS': self.output_results[10],
            'SUM_ORFL': self.output_results[11],
            'MEDFLNW': self.output_results[13],
            'STDRES': self.output_results[14],
            'MWAGE': self.output_results[15],
            'E_MWAGE': self.output_results[16],
            'MWMET': self.output_results[17],
            'E_MWMET': self.output_results[18],
            'SYSVEL': self.output_results[19],
            'LML': self.output_results[20],
            'LMASS': self.output_results[21],
            # 'min_chisq': self.output_results[0],
            # 'LW_age': self.output_results[1],
            # 'e_LW_age': self.output_results[2],
            # 'LW_met': self.output_results[3],
            # 'e_LW_met': self.output_results[4],
            # 'AV': self.output_results[5],
            # 'e_AV': self.output_results[6],
            # 'redshift': self.output_results[7],
            # 'e_redshift': self.output_results[8],
            # 'vdisp': self.output_results[9],
            # 'e_vdisp': self.output_results[10],
            # 'sum_orig_flux': self.output_results[11],
            # 'median_flux_norm_window': self.output_results[13],
            # 'std_res': self.output_results[14],
            # 'MW_age': self.output_results[15],
            # 'e_MW_age': self.output_results[16],
            # 'MW_met': self.output_results[17],
            # 'e_MW_met': self.output_results[18],
            # 'sys_vel': self.output_results[19],
            # 'lML': self.output_results[20],
            # 'lMass': self.output_results[21],
        }
        h.update(columns_pars_data)
        write_img_header(filename, list(h.keys()), list(h.values()))

        ssp = self.models
        t = fits.open(filename)
        #
        # columns = [
        #     'min_chisq', 'LW_age', 'e_LW_age', 'LW_met', 'e_LW_met', 'AV', 'e_AV',
        #     'redshift', 'e_redshift', 'vdisp', 'e_vdisp', 'sum_orig_flux',
        #     'median_flux_norm_window', 'std_res', 'MW_age', 'e_MW_age', 'MW_met', 'e_MW_met',
        #     'sys_vel', 'lML', 'lMass',
        # ]
        # units = [
        #     '', 'Gyr', 'Gyr', '', '', 'mag', 'mag',
        #     '', '', 'km/s', 'km/s', 'flux',
        #     'flux', 'flux', 'Gyr', 'Gyr', '', '',
        #     'km/s', '', '',
        # ]
        # fmts = {column: 'E' for column in columns}
        # _units = dict(zip(columns, units))
        # print(len(columns), len(units), len(columns_pars_data.keys()))
        # _columns = []
        # for k, v in columns_pars_data.items():
        #     print(v, type(v))
        #     _columns.append(fits.Column(name=k, array=v, format=fmts[k], unit=_units[k]))
        # table_hdu_pars = fits.BinTableHDU.from_columns(_columns)
        # table_hdu_pars.name = 'PARAMETERS'

        # OUTPUT SFH
        columns = ['AGE', 'MET', 'AV', 'coeffs_norm', 'min_coeffs_norm', 'logML', 'coeffs_ssp_MC_rms']
        units = [ssp.parameters_units['AGE'], ssp.parameters_units['MET'],
                 ssp.parameters_units['AV'], '', '', '', '']
        fmts = {column: 'E' for column in columns}
        _units = dict(zip(columns, units))
        columns_SFH_data = {
            'AGE': ssp.parameters['AGE'],
            'MET': ssp.parameters['MET'],
            'AV': ssp.parameters['AV'],
            'coeffs_norm': self.coeffs_norm,
            'min_coeffs_norm': self.min_coeffs_norm,
            'logML': np.log10(self.models.mass_to_light),
            'coeffs_ssp_MC_rms': self.coeffs_ssp_MC_rms,
            }
        _columns = []
        for k, v in columns_SFH_data.items():
            _columns.append(fits.Column(name=k, array=v, format=fmts[k], unit=_units[k]))
        table_hdu_SFH = fits.BinTableHDU.from_columns(_columns)
        table_hdu_SFH.name = 'SFH'
        # deprecated variable names
        table_hdu_SFH.header['SSP_SFH'] = self.filename
        table_hdu_SFH.header['SSP_KIN'] = self.filename_nl_fit
        table_hdu_SFH.header['NORMWSFH'] = self.ssp.wavenorm
        table_hdu_SFH.header['NORMWKIN'] = self.ssp_nl_fit.wavenorm

        # hdu_list = fits.HDUList([t[0], table_hdu_pars, table_hdu_SFH])
        hdu_list = fits.HDUList([t[0], table_hdu_SFH])
        hdu_list.writeto(filename, overwrite=True)

    def output(self, filename, write_header=True, block_plot=True):
        """
        Summaries the run in a csv file.

        Parameters
        ----------
        filename : str
            Output filename.
        """
        s = self.spectra
        spectra_list = self.output_spectra_list
        chi_joint = self.output_results[0]
        FLUX = self.output_results[11]
        delta_wl_range = self.models.wavelength[-1] - self.models.wavelength[0]
        mass = self.mass_to_light*self.med_flux*0.5*delta_wl_range
        lmass = self.output_results[-1]
        lml = self.output_results[-2]
        if isinstance(filename, io.TextIOWrapper):
            if write_header:
                self._print_header(filename)
            f_outfile = filename
        else:
            if not exists(filename):
                self._print_header(filename)
            f_outfile = open(filename, 'a')
        outbuf = f'{chi_joint},'
        outbuf = f'{outbuf}{self.age_min},{self.e_age_min},{self.met_min},{self.e_met_min},'
        outbuf = f'{outbuf}{self.AV_min},{self.e_AV_min},{self.best_redshift},{self.e_redshift},'
        outbuf = f'{outbuf}{self.best_sigma},{self.e_sigma},{FLUX},{self.best_redshift},'
        outbuf = f'{outbuf}{self.med_flux},{self.rms},{self.age_min_mass},{self.e_age_min_mass},'
        outbuf = f'{outbuf}{self.met_min_mass},{self.e_met_min_mass},{self.systemic_velocity},'
        outbuf = f'{outbuf}{lml},{lmass}'
        print(outbuf, file=f_outfile)
        if not isinstance(filename, io.TextIOWrapper):
            f_outfile.close()


def parse_arguments(default_args_file=None):
    """
    Parse the command line args.

    With fromfile_pidxrefix_chars=@ we can read and parse command line args
    inside a file with @file.txt.
    default args inside default_args_file
    """
    default_args = {
        'error_file': None, 'error_flux_variance': False, 'single_ssp': False,
        'nl_ssp_models_file': None, 'out_file': 'auto_ssp.out',
        'mask_list': None, 'elines_mask_file': None,
        'plot': 0,  # TODO: 'plot': False, 'plot_to_file': '',
        'min_flux_plot': None, 'max_flux_plot': None,
        'instrumental_dispersion': None, 'wl_range': None, 'nl_wl_range': None,
        'redshift_set': None, 'losvd_set': None, 'AV_set': None,
        'fit_sigma_nnls': False, 'no_eml_fit': False, 'sigma_in_AA': False,
        'losvd_rnd_medres_merit': False,
        'extlaw': __selected_extlaw__, 'R_V': __selected_R_V__,
    }

    help_args = {
        'spec_file': 'A file containing the spectrum information (columns should be: ID WAVELENGTH FLUX [ERROR_FLUX])',
        'error_file': 'An optional file with the error (std-dev) of the obseved spectrum',
        'ssp_models_file': 'Stellar population synthesis models. For more information about ssp_models file see README.txt.',
        'nl_ssp_models_file': 'Stellar population models used for the fit of the non-linear parameters (redshift, sigma and AV). If not used, the program uses SSP_MODELS_FILE by default',
        'config_file': 'Auto-SSP config file',
        'mask_list': 'Rest-frame wavelength ranges to be masked',
        'elines_mask_file': 'File with rest-frame emission lines central wavelength masked during the non-linear fit and stellar population synthesis',
        'out_file': 'The output parameters file. Also will set the filename prefix for other produced files',
        'instrumental_dispersion': 'The instrumental dispersion of the observed spectra. Unit in Angstroms.',
        'min_flux_plot': 'Used when plot != 0. Set the min flux used in plots',
        'max_flux_plot': 'Used when plot != 0. Set the max flux used in plots',
        'wl_range': 'Stellar population synthesis wavelength range',
        'nl_wl_range': 'Non-linear parameters fit wavelength range (only used in redshift and sigma fit)',
        'plot': '0 = no plot | 1 = plot in screen | 2 = plot to file',
        # TODO: 'plot_to_file': 'All plots to files.'
        'redshift_set': 'Redshift fit setup. The inputs are GUESS DELTA MIN MAX',
        'losvd_set': 'Line-of-sight velocity dispersion fit setup. The inputs are in the same way as the redshift fit setup. The used unit is Angstrom when --sigma_in_AA active, otherwise in km/s.',
        'AV_set': 'Dust extinction parameter fit setup. The inputs are in the same way as the redshift fit setup. The used unit is mag.',
        'no_eml_fit': 'Do not perform the emission lines fit',
        'sigma_in_AA': 'Set the line-of-sight velocity dispersion unit as Angstroms',
        'error_flux_variance': 'Treat the optional ERROR_FLUX column of spec_file as variance',
        'force_seed': 'Force the seed of the random number generator',
        'fit_sigma_nnls': 'Fit sigma using non-negative least squares (faster but less precise)',
        'single_ssp': 'Run the stellar population synthesis looking for a single SSP as an answer',
        'losvd_rnd_medres_merit': 'When using the default losvd fit, uses the median of the residual spectrum (obs - mod) instead the Chi-squared as the merit function',
        'R_V': 'R_V extinction factor: R_V=A_V/E(B-V)',
        'extlaw': 'Extinction law used. Cardelli, Clayton & Mathis (CCM) or Calzetti (CAL)',
    }

    parser = readFileArgumentParser(fromfile_prefix_chars='@')

    parser.add_argument('--error_file', metavar='FILE', type=str, default=default_args['error_file'], help=help_args['error_file'])
    parser.add_argument('-n','--nl_ssp_models_file', metavar='FILE', type=str, default=default_args['nl_ssp_models_file'], help=help_args['nl_ssp_models_file'])
    parser.add_argument('--mask_list', metavar='FILE', type=str, default=default_args['mask_list'], help=help_args['mask_list'])
    parser.add_argument('--elines_mask_file', metavar='FILE', type=str, default=default_args['elines_mask_file'], help=help_args['elines_mask_file'])
    parser.add_argument('--out_file', '-o', metavar='FILE', type=str, default=default_args['out_file'], help=help_args['out_file'])
    parser.add_argument('--instrumental_dispersion', '-d', metavar='FLOAT', type=float, default=default_args['instrumental_dispersion'], help=help_args['instrumental_dispersion'])
    parser.add_argument('--min_flux_plot', metavar='FLOAT', type=float, default=default_args['min_flux_plot'], help=help_args['min_flux_plot'])
    parser.add_argument('--max_flux_plot', metavar='FLOAT', type=float, default=default_args['max_flux_plot'], help=help_args['max_flux_plot'])
    parser.add_argument('--wl_range', nargs=2, metavar='INT', type=int, help=help_args['wl_range'])
    parser.add_argument('--nl_wl_range', nargs=2, metavar='INT', type=int, help=help_args['nl_wl_range'])
    parser.add_argument('--force_seed', metavar='INT', help=help_args['force_seed'])
    parser.add_argument('--R_V', metavar='FLOAT', type=float, default=default_args['R_V'], help=help_args['R_V'])
    parser.add_argument('--extlaw', type=str, choices=['CCM', 'CAL'], default=default_args['extlaw'], help=help_args['extlaw'])
    # TODO: plot to file
    parser.add_argument('--plot', '-p', type=int, choices=[0, 1, 2], help=help_args['plot'])
    # parser.add_argument('--plot', '-p', action='store_true', default=default_args['plot'], help=help_args['plot'])
    # parser.add_argument('--plot_to_file', metavar='FILE_PREFIX', type=str, default=default_args['plot_to_file'], help=help_args['plot_to_file'])
    parser.add_argument('--redshift_set', '-R', type=float, nargs=4, metavar='FLOAT', help=help_args['redshift_set'])
    parser.add_argument('--losvd_set', '-S', type=float, nargs=4, metavar='FLOAT', help=help_args['losvd_set'])
    parser.add_argument('--AV_set', '-A', type=float, nargs=4, metavar='FLOAT', help=help_args['AV_set'])
    parser.add_argument('--single_ssp', action='store_true', default=default_args['single_ssp'], help=help_args['single_ssp'])
    parser.add_argument('--no_eml_fit', action='store_true', default=default_args['no_eml_fit'], help=help_args['no_eml_fit'])
    parser.add_argument('--sigma_in_AA', action='store_true', default=default_args['sigma_in_AA'], help=help_args['sigma_in_AA'])
    parser.add_argument('--error_flux_variance', action='store_true', default=default_args['error_flux_variance'], help=help_args['error_flux_variance'])
    parser.add_argument('--fit_sigma_nnls', action='store_true', default=default_args['fit_sigma_nnls'], help=help_args['fit_sigma_nnls'])
    parser.add_argument('--losvd_rnd_medres_merit', action='store_true', default=default_args['losvd_rnd_medres_merit'], help=help_args['losvd_rnd_medres_merit'])

    # positional arguments
    parser.add_argument('spec_file', metavar='SPEC_FILE', type=str, help=help_args['spec_file'])
    parser.add_argument('ssp_models_file', metavar='SSP_MODELS_FILE', type=str, help=help_args['ssp_models_file'])
    parser.add_argument('config_file', metavar='CONFIG_FILE', type=str, help=help_args['config_file'])

    parser.add_argument('--verbose', '-v', action='count', default=0)

    args_list = sys.argv[1:]
    # if exists file default.args, load default args
    if default_args_file is not None and isfile(default_args_file):
        args_list.insert(0, '@%s' % default_args_file)
    args = parser.parse_args(args=args_list)
    # TREAT ARGUMENTS HERE
    print(f'ef={args.error_file} sp={args.spec_file}')
    print(f'sspnlf={args.nl_ssp_models_file} sspf={args.ssp_models_file}')
    return args

if __name__ == '__main__':
    pa = parse_arguments()

    spec_file = pa.spec_file
    ssp_models_file = pa.ssp_models_file
    config_file = pa.config_file
    out_file = pa.out_file
    error_file = pa.error_file
    nl_ssp_models_file = pa.nl_ssp_models_file
    mask_list = pa.mask_list
    elines_mask_file = pa.elines_mask_file
    instrumental_dispersion = pa.instrumental_dispersion
    wl_range = pa.wl_range
    nl_wl_range = pa.nl_wl_range
    plot = pa.plot
    min = pa.min_flux_plot
    max = pa.max_flux_plot
    redshift_set = pa.redshift_set
    losvd_set = pa.losvd_set
    AV_set = pa.AV_set
    fit_gas = (not pa.no_eml_fit)
    variance_error_column = pa.error_flux_variance
    fit_sigma_rnd = (not pa.fit_sigma_nnls)
    seed = pa.force_seed
    single_ssp = pa.single_ssp
    losvd_rnd_medres_merit = pa.losvd_rnd_medres_merit
    verbose = pa.verbose
    # TODO: this option need to be implemented in StPopSynt class
    losvd_in_AA = pa.sigma_in_AA
    R_V = pa.R_V
    extlaw = pa.extlaw
    sps_class = new_StPopSynt
    SN_window_reference_wavelength = None
    SN_window_half_range = 45
    norm_window_reference_wavelength = None
    norm_window_half_range = 45
    ratio = None
    gas_fit_correct_wl_range = 2

    time_ini_run = print_time(print_seed=False, get_time_only=True)
    # initial time in seconds since Epoch.
    seed = print_time() if seed is None else print_time(time_ini=seed)
    # initial time used as the seed of the random number generator.
    np.random.seed(seed)
    ratio = True if ratio is None else ratio
    nl_ssp_models_file = ssp_models_file if nl_ssp_models_file is None else nl_ssp_models_file
    out_file_elines = 'elines_' + out_file
    out_file_single = 'single_' + out_file
    out_file_coeffs = 'coeffs_' + out_file
    out_file_fit = 'output.' + out_file + '.fits'
    out_file_ps = out_file
    w_min = None if wl_range is None else wl_range[0]
    w_max = None if wl_range is None else wl_range[1]
    nl_w_min = None if nl_wl_range is None else nl_wl_range[0]
    nl_w_max = None if nl_wl_range is None else nl_wl_range[1]
    if redshift_set is not None:
        input_redshift, delta_redshift, min_redshift, max_redshift = redshift_set
    else:
        input_redshift, delta_redshift, min_redshift, max_redshift = None, None, None, None
    if losvd_set is not None:
        input_sigma, delta_sigma, min_sigma, max_sigma = losvd_set
    else:
        input_sigma, delta_sigma, min_sigma, max_sigma = None, None, None, None
    if AV_set is not None:
        input_AV, delta_AV, min_AV, max_AV = AV_set
    else:
        input_AV, delta_AV, min_AV, max_AV = None, None, None, None

    # remove old files
    clean_preview_results_files(out_file, out_file_elines, out_file_single, out_file_coeffs, out_file_fit)

    # read spectrum
    wl__w, f__w, ef__w = read_spectra(spec_file, f_error=lambda x: 0.1*np.sqrt(np.abs(x)), variance_column=variance_error_column)

    input_SN = np.divide(f__w, ef__w, where=ef__w!=0)
    print_verbose(f'-> mean input S/N: {input_SN[np.isfinite(input_SN)].mean()}', verbose=verbose)

    cf, SPS = auto_ssp_elines_single_main(
        wl__w, f__w, ef__w, ssp_models_file,
        config_file=config_file,
        ssp_nl_fit_file=nl_ssp_models_file, sigma_inst=instrumental_dispersion, out_file=out_file,
        mask_list=mask_list, elines_mask_file=elines_mask_file,
        min=min, max=max, w_min=w_min, w_max=w_max, nl_w_min=nl_w_min, nl_w_max=nl_w_max,
        input_redshift=input_redshift, delta_redshift=delta_redshift,
        min_redshift=min_redshift, max_redshift=max_redshift,
        input_sigma=input_sigma, delta_sigma=delta_sigma, min_sigma=min_sigma, max_sigma=max_sigma,
        input_AV=input_AV, delta_AV=delta_AV, min_AV=min_AV, max_AV=max_AV,
        plot=plot, single_ssp=single_ssp, ratio=ratio, fit_sigma_rnd=fit_sigma_rnd,
        fit_gas=fit_gas, losvd_rnd_medres_merit=losvd_rnd_medres_merit,
        verbose=verbose, R_V=R_V, extlaw=extlaw,
        sps_class=sps_class,
        SN_window_reference_wavelength=SN_window_reference_wavelength,
        SN_window_half_range=SN_window_half_range,
        norm_window_reference_wavelength=norm_window_reference_wavelength,
        norm_window_half_range=norm_window_half_range,
        # TODO: need to be implemented in StPopSynth
        # sigma_in_AA=losvd_in_AA,
        gas_fit_subtrcont_ratio_range=None, gas_fit_subtrcont_ratio_std=None,
        gas_fit_half_range_sysvel=None, gas_fit_correct_wl_range=gas_fit_correct_wl_range,
        gas_fit_guide_vel=True
    )

    # write outputs
    if fit_gas:
        SPS.output_gas_emission(filename=out_file_elines)
    if not single_ssp:
        SPS.output_fits(filename=out_file_fit)
        SPS.output_coeffs_MC(filename=out_file_coeffs)
        SPS.output(filename=out_file, block_plot=False)
    else:
        SPS.output_single_ssp(filename=out_file_coeffs.replace('coeffs', 'chi_sq'))

    time_end = print_time(print_seed=False)
    time_total = time_end - time_ini_run
    print(f'# SECONDS = {time_total}')
