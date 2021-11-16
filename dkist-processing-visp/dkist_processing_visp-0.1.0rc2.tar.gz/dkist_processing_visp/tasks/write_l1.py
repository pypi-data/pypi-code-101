from typing import Literal

import dkist_fits_specifications
from astropy.io import fits
from dkist_processing_common.tasks.write_l1 import WriteL1Frame

from dkist_processing_visp.visp_base import VispScienceTask


class VispWriteL1Frame(WriteL1Frame, VispScienceTask):
    def add_dataset_headers(
        self, header: fits.Header, stokes: Literal["I", "Q", "U", "V"]
    ) -> fits.Header:
        """
        Add the VISP specific dataset headers to L1 FITS files
        """
        if stokes.upper() not in self.stokes_params:
            raise ValueError("The stokes parameter must be one of I, Q, U, V")
        header["DNAXIS"] = 5  # spectral, spatial, spatial, temporal, stokes
        # ---Spectral---
        header["DNAXIS1"] = header["NAXIS1"]
        header["DTYPE1"] = "SPECTRAL"
        header["DPNAME1"] = "wavelength"
        header["DWNAME1"] = "wavelength"
        header["DUNIT1"] = header["CUNIT1"]
        # ---Spatial 1---
        header["DNAXIS2"] = header["NAXIS2"]
        header["DTYPE2"] = "SPATIAL"
        header["DPNAME2"] = "helioprojective latitude of point on slit"
        header["DWNAME2"] = "helioprojective latitude"
        header["DUNIT2"] = header["CUNIT2"]
        # ---Spatial 2---
        header["DNAXIS3"] = self.num_raster_steps
        header["DTYPE3"] = "SPATIAL"
        header["DPNAME3"] = "helioprojective longitude of point on slit"
        header["DWNAME3"] = "helioprojective longitude"
        header["DUNIT3"] = header["CUNIT3"]
        # ---Temporal---
        # Total number of input observe frames
        header["DNAXIS4"] = self.num_dsps_repeats  # total number of raster scans in the dataset
        header["DTYPE4"] = "TEMPORAL"
        header["DPNAME4"] = "time"
        header["DWNAME4"] = "time"
        header["DUNIT4"] = "s"
        # ---Stokes---
        header["DNAXIS5"] = 4  # I, Q, U, V
        header["DTYPE5"] = "STOKES"
        header["DPNAME5"] = "polarization state"
        header["DWNAME5"] = "polarization state"
        header["DUNIT5"] = ""

        header["DAAXES"] = 2  # Spectral, spatial
        header["DEAXES"] = 3  # Spatial, temporal, stokes

        # Raster position in dataset
        header["DINDEX3"] = header["VSPSTP"]  # Current position in raster scan
        # Temporal position in dataset
        header["DINDEX4"] = header["DSPSNUM"]  # Current raster scan
        # Stokes position in dataset - stokes axis goes from 1-4
        header["DINDEX5"] = self.stokes_params.index(stokes.upper()) + 1

        # VISP has a wavelength axis in the frame and so FRAMEWAV is hard to define. Use LINEWAV.
        header["FRAMEWAV"] = header["LINEWAV"]
        header["LEVEL"] = 1
        header["HEADVERS"] = dkist_fits_specifications.__version__
        header["HEAD_URL"] = ""  # TODO Need a link to put in here
        header["INFO_URL"] = ""  # TODO Need a link to put in here
        header[
            "CALVERS"
        ] = "dkist_processing_visp.__version__"  # TODO need versioned releases of instrument pipelines
        header["CAL_URL"] = ""  # TODO Need a link to put in here
        header["WAVEBAND"] = self.spectral_line
        header["WAVEUNIT"] = -9  # nanometers
        header["WAVEREF"] = "Air"
        # The wavemin and wavemax assume that all frames in a dataset have identical wavelength axes
        header["WAVEMIN"] = header["CRVAL1"] - (header["CRPIX1"] * header["CDELT1"])
        header["WAVEMAX"] = header["CRVAL1"] + (
            (header["NAXIS1"] - header["CRPIX1"]) * header["CDELT1"]
        )

        # Binning headers
        header["NBIN1"] = 1
        header["NBIN2"] = 1
        header["NBIN3"] = 1
        header["NBIN"] = header["NBIN1"] * header["NBIN2"] * header["NBIN3"]

        return header
