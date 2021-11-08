import numpy as np
from bilby.core.utils import logger

from gwpopulation.cupy_utils import xp
from gwpopulation.vt import GridVT, ResamplingVT

N_EVENTS = np.nan


def dummy_selection(*args, **kwargs):
    return 1


def mass_only_scalar_calibrated_grid_vt(vt_file, model):
    selection = _mass_only_calibrated_grid_vt(
        vt_file=vt_file,
        model=model,
        calibration="scalar",
    )
    return selection


def mass_only_linear_calibrated_grid_vt(vt_file, model):
    selection = _mass_only_calibrated_grid_vt(
        vt_file=vt_file,
        model=model,
        calibration="linear",
    )
    return selection


def mass_only_quadratic_calibrated_grid_vt(vt_file, model):
    selection = _mass_only_calibrated_grid_vt(
        vt_file=vt_file,
        model=model,
        calibration="quadratic",
    )
    return selection


gaussian_mass_only_scalar_calibrated_grid_vt = mass_only_scalar_calibrated_grid_vt
gaussian_mass_only_linear_calibrated_grid_vt = mass_only_linear_calibrated_grid_vt
gaussian_mass_only_quadratic_calibrated_grid_vt = mass_only_quadratic_calibrated_grid_vt
broken_mass_only_scalar_calibrated_grid_vt = mass_only_scalar_calibrated_grid_vt
broken_mass_only_linear_calibrated_grid_vt = mass_only_linear_calibrated_grid_vt
broken_mass_only_quadratic_calibrated_grid_vt = mass_only_quadratic_calibrated_grid_vt


def _mass_only_calibrated_grid_vt(vt_file, model, calibration=None):
    import deepdish as dd

    model = model
    _vt_data = dd.io.load(vt_file)
    vt_data = dict()
    vt_data["vt"] = _vt_data["vt_early_high"]
    if calibration is not None:
        vt_data["vt"] *= _vt_data[f"{calibration}_calibration"]
    vt_data["vt"] = xp.asarray(vt_data["vt"])
    vt_data["mass_1"] = xp.asarray(_vt_data["m1"])
    vt_data["mass_ratio"] = xp.asarray(_vt_data["q"])

    selection = GridVT(model=model, data=vt_data)
    return selection


def load_injection_data(vt_file, ifar_threshold=1, snr_threshold=11):
    """
    Load the injection file in the O3 injection file format.

    For mixture files and multiple observing run files we only
    have the full `sampling_pdf`.

    We use a different parameterization than the default so we require a few
    changes.

    - we parameterize the model in terms of primary mass and mass ratio and
      the injections are generated in primary and secondary mass. The Jacobian
      is `primary mass`.
    - we parameterize spins in spherical coordinates, neglecting azimuthal
      parameters. The injections are parameterized in terms of cartesian
      spins. The Jacobian is `1 / (2 pi magnitude ** 2)`.

    For O3 injections we threshold on FAR.
    For O1/O2 injections we threshold on SNR as there is no FAR
    provided by the search pipelines.

    Parameters
    ----------
    vt_file: str
        The path to the hdf5 file containing the injections.
    ifar_threshold: float
        The threshold on inverse false alarm rate in years. Default=1.
    snr_threshold: float
        The SNR threshold when there is no FAR. Default=11.

    Returns
    -------
    gwpop_data: dict
        Data required for evaluating the selection function.

    """
    logger.info(f"Loading VT data from {vt_file}.")
    import h5py

    with h5py.File(vt_file, "r") as ff:
        data = ff["injections"]
        found = np.zeros_like(data["mass1_source"][()], dtype=bool)
        for key in data:
            if "ifar" in key.lower():
                found = found | (data[key][()] > ifar_threshold)
            if "name" in data.keys():
                gwtc1 = (data["name"][()] == b"o1") | (data["name"][()] == b"o2")
                found = found | (gwtc1 & (data["optimal_snr_net"][()] > snr_threshold))
        n_found = sum(found)
        gwpop_data = dict(
            mass_1=xp.asarray(data["mass1_source"][found]),
            mass_ratio=xp.asarray(
                data["mass2_source"][found] / data["mass1_source"][found]
            ),
            redshift=xp.asarray(data["redshift"][found]),
            total_generated=int(data.attrs["total_generated"][()]),
            analysis_time=data.attrs["analysis_time_s"][()] / 365.25 / 24 / 60 / 60,
        )
        for ii in [1, 2]:
            gwpop_data[f"a_{ii}"] = (
                xp.asarray(
                    data.get(f"spin{ii}x", np.zeros(n_found))[found] ** 2
                    + data.get(f"spin{ii}y", np.zeros(n_found))[found] ** 2
                    + data[f"spin{ii}z"][found] ** 2
                )
                ** 0.5
            )
            gwpop_data[f"cos_tilt_{ii}"] = (
                xp.asarray(data[f"spin{ii}z"][found]) / gwpop_data[f"a_{ii}"]
            )
        gwpop_data["prior"] = (
            xp.asarray(data["sampling_pdf"][found])
            * xp.asarray(data["mass1_source"][found])
            * (2 * np.pi * gwpop_data["a_1"] ** 2)
            * (2 * np.pi * gwpop_data["a_2"] ** 2)
        )
    return gwpop_data


_load_injection_data = load_injection_data


def injection_resampling_vt(vt_file, model, ifar_threshold=1, snr_threshold=11):

    data = load_injection_data(
        vt_file=vt_file, ifar_threshold=ifar_threshold, snr_threshold=snr_threshold
    )

    return ResamplingVT(model=model, data=data, n_events=N_EVENTS)


def injection_resampling_vt_no_redshift(
    vt_file, model, ifar_threshold=1, snr_threshold=11
):

    data = load_injection_data(
        vt_file=vt_file, ifar_threshold=ifar_threshold, snr_threshold=snr_threshold
    )
    data["prior"] = data["mass_1"] ** (-2.35 + 1) * data["mass_ratio"] ** 2

    return ResamplingVT(model=model, data=data, n_events=N_EVENTS)
