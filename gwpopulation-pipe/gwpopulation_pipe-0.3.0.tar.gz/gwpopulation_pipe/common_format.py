import os
from argparse import ArgumentParser

import deepdish as dd
import h5py
import numpy as np
import pandas as pd
from bilby.core.result import read_in_result
from bilby.core.utils import logger
from gwpopulation.cupy_utils import to_numpy, xp
from tqdm import tqdm

from .data_analysis import load_model
from .data_collection import evaluate_prior
from .utils import prior_conversion
from .vt_helper import load_injection_data


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("-r", "--result-file", help="Bilby result file")
    parser.add_argument(
        "-s", "--samples-file", help="File containing single event samples"
    )
    parser.add_argument("--injection-file", help="File containing injections")
    parser.add_argument("-f", "--filename", default=None, help="Output file name")
    parser.add_argument("--models", type=str, action="append")
    parser.add_argument("--vt-models", type=str, action="append")
    parser.add_argument("--max-redshift", default=2.3, type=float)
    parser.add_argument("--minimum-mass", default=2, type=float)
    parser.add_argument("--maximum-mass", default=100, type=float)
    parser.add_argument(
        "--n-events", type=int, default=None, help="Number of events to draw"
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=5000,
        help="The number of population samples to use, default=5000",
    )
    parser.add_argument(
        "--vt-ifar-threshold",
        type=float,
        default=1,
        help="IFAR threshold for resampling injections",
    )
    parser.add_argument(
        "--vt-snr-threshold",
        type=float,
        default=11,
        help="IFAR threshold for resampling injections. "
        "This is only used for O1/O2 injections",
    )
    parser.add_argument(
        "--distance-prior",
        default="euclidean",
        help="Distance prior format, e.g., euclidean, comoving",
    )
    parser.add_argument(
        "--mass-prior",
        default="flat-detector",
        help="Mass prior, only flat-detector is implemented",
    )
    parser.add_argument(
        "--spin-prior",
        default="component",
        help="Spin prior, this should be either component or gaussian",
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    result = read_in_result(args.result_file)
    n_samples = min(args.n_samples, len(result.posterior))
    all_samples = dict()
    posterior = result.posterior.sample(n_samples, replace=False)
    posterior = do_spin_conversion(posterior)
    all_samples["posterior"] = posterior

    samples = dd.io.load(args.samples_file)
    if "prior" not in samples["original"]:
        samples["original"]["prior"] = evaluate_prior(samples["original"], args)
    for key in samples["original"]:
        samples["original"][key] = xp.asarray(samples["original"][key])

    if args.n_events:
        n_draws = args.n_events
        logger.info(f"Number of draws set to {n_draws}.")
    else:
        n_draws = len(samples["names"])
        logger.info(f"Number of draws equals number of events, {n_draws}.")

    logger.info("Generating observed populations.")
    model = load_model(args)
    observed_dataset = resample_events_per_population_sample(
        posterior=posterior,
        samples=samples["original"],
        model=model,
        n_draws=len(samples["names"]),
    )

    for ii, name in enumerate(samples["names"]):
        new_posterior = pd.DataFrame()
        for key in observed_dataset:
            new_posterior[f"{name}_{key}"] = to_numpy(observed_dataset[key][:, ii])
        all_samples[name] = new_posterior

    if args.injection_file is None:
        logger.info("Can't generate predicted populations without VT file.")
    else:
        logger.info("Generating predicted populations.")
        args.models = args.vt_models
        vt_data = load_injection_data(
            args.injection_file,
            ifar_threshold=args.vt_ifar_threshold,
            snr_threshold=args.vt_snr_threshold,
        )
        model = load_model(args)
        synthetic_dataset = resample_injections_per_population_sample(
            posterior=posterior,
            data=vt_data,
            model=model,
            n_draws=n_draws,
        )

        for ii in range(n_draws):
            new_posterior = pd.DataFrame()
            for key in synthetic_dataset:
                new_posterior[f"synthetic_{key}_{ii}"] = to_numpy(
                    synthetic_dataset[key][:, ii]
                )
            all_samples[f"synthetic_{ii}"] = new_posterior

    if args.filename is None:
        filename = os.path.join(result.outdir, f"{result.label}_full_posterior.hdf5")
    else:
        filename = args.filename
    save_to_common_format(
        posterior=all_samples, events=samples["names"], filename=filename
    )


def do_spin_conversion(posterior):
    """Utility function to convert between beta distribution parameterizations."""
    original_keys = list(posterior.keys())
    posterior = prior_conversion(posterior)
    for key in ["amax", "amax_1", "amax_2"]:
        if key not in original_keys and key in posterior:
            del posterior[key]
    return posterior


def save_to_common_format(posterior, events, filename):
    """
    Save the data to the common hdf5 format.

    Parameters
    ----------
    posterior: [np.ndarray, pd.DataFrame]
        The posterior to be saved.
    events: list
        The names of each of the events in the dataset.
    filename: str
        the output filename

    """
    for key in posterior:
        if isinstance(posterior[key], pd.DataFrame):
            posterior[key] = data_frame_to_sarray(posterior[key])
    events = [event.encode() for event in events]
    logger.info(f"Writing data to {filename}")
    with h5py.File(filename, "w") as ff:
        for key in posterior:
            ff[f"samples/{key}"] = posterior[key]
        ff["events"] = events


def read_common_format(filename, data_format="numpy"):
    """
    Read a posterior file in the common format

    Parameters
    ----------
    filename: str
        The path to the file to read.
    data_format: str
        The format to return the data in, can be either `numpy` or `pandas`.

    Returns
    -------
    output: [np.ndarray, pd.DataFrame]
        The posterior in the requested format.
    events: list
        The event names.
    """
    with h5py.File(filename, "r") as ff:
        data = {key: ff["samples"][key][:] for key in ff["samples"]}
        events = [event.decode() for event in ff["events"]]
    if data_format == "numpy":
        return data, events
    elif data_format == "pandas":
        output = dict()
        for key in data:
            data_frame = pd.DataFrame()
            for name in data[key].dtype.names:
                data_frame[name] = data[key][name]
            output[key] = data_frame
        return output, events
    else:
        raise ValueError(f"Data format {data_format} not implemented.")


def resample_events_per_population_sample(posterior, samples, model, n_draws):
    """
    Resample the input posteriors with a fiducial prior to the population
    informed distribution. This returns a single sample for each event for
    each passed hyperparameter sample.

    See, e.g., section IIIC of `Moore and Gerosa <https://arxiv.org/abs/2108.02462>`_
    for a description of the method.

    Parameters
    ----------
    posterior: pd.DataFrame
        Hyper-parameter samples to use for the reweighting.
    samples: dict
        Posterior samples with the fiducial prior.
    model: bilby.hyper.model.Model
        Object that implements a `prob` method that will calculate the population
        probability.
    n_draws: int
        The number of samples to draw. This should generally be the number of events.
        This will return one sample per input event.

    Returns
    -------
    observed_dataset: dict
        The observed dataset of the events with the population informed prior.
    """
    all_choices = list()

    for ii in tqdm(range(len(posterior))):
        parameters = dict(posterior.iloc[ii])
        model.parameters.update(parameters)
        weights = to_numpy(model.prob(samples) / samples["prior"])
        weights = (weights.T / np.sum(weights, axis=-1)).T
        choices = [
            np.random.choice(
                len(weights[ii]),
                p=weights[ii],
            )
            for ii in range(n_draws)
        ]
        all_choices.append(choices)
    observed_dataset = dict()
    for key in samples:
        observed_dataset[key] = xp.array(
            [
                xp.asarray(
                    [samples[key][ii, choice] for ii, choice in enumerate(choices)]
                )
                for choices in all_choices
            ]
        )
    return observed_dataset


def resample_injections_per_population_sample(posterior, data, model, n_draws):
    """
    Resample the input data with a fiducial prior to the population
    informed distribution. This returns a fixed number of samples for
    each passed hyperparameter sample.

    This is designed to be used with found injections.

    See, e.g., section IIIC of `Moore and Gerosa <https://arxiv.org/abs/2108.02462>`_
    for a description of the method.

    Parameters
    ----------
    posterior: pd.DataFrame
        Hyper-parameter samples to use for the reweighting.
    data: dict
        Input data samples to be reweighted.
    model: bilby.hyper.model.Model
        Object that implements a `prob` method that will calculate the population
        probability.
    n_draws: int
        The number of samples to draw. This should generally be the number of events.
        This will return one sample per input event.

    Returns
    -------
    observed_dataset: dict
        The observed dataset of the input data with the population informed prior.
    """
    all_choices = list()
    for ii in tqdm(range(len(posterior))):
        parameters = dict(posterior.iloc[ii])
        model.parameters.update(parameters)
        weights = to_numpy(model.prob(data) / data["prior"])
        weights /= sum(weights)
        choices = np.random.choice(len(weights), p=weights, size=n_draws, replace=False)
        all_choices.append(choices)
    synthetic_dataset = dict()
    for key in data:
        if not isinstance(data[key], xp.ndarray):
            continue
        synthetic_dataset[key] = xp.asarray(
            [data[key][choices] for choices in all_choices]
        )
    return synthetic_dataset


def data_frame_to_sarray(data_frame):
    """
    Convert a pandas DataFrame object to a numpy structured array.
    This is functionally equivalent to but more efficient than
    `np.array(df.to_array())`.

    lifted from https://stackoverflow.com/questions/30773073/save-pandas-dataframe-using-h5py-for-interoperabilty-with-other-hdf5-readers

    Parameters
    -----------
    data_frame: pd.DataFrame
        the data frame to convert

    Returns
    -------
    output: np.ndarray
        a numpy structured array representation of df
    """

    types = [
        (data_frame.columns[index], data_frame[key].dtype.type)
        for (index, key) in enumerate(data_frame.columns)
    ]
    dtype = np.dtype(types)
    output = np.zeros(data_frame.values.shape[0], dtype)
    for (index, key) in enumerate(output.dtype.names):
        output[key] = data_frame.values[:, index]
    return output
