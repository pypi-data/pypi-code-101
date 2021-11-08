"""
Functions for collecting input samples from a range of sources and computing
the fiducial prior for the appropriate parameters.

The module provides the `gwpopulation_pipe_collection` executable.

In order to use many of the other functions you will need a class that provides
various attributes specified in the `gwpopulation_pipe` parser.
"""

#!/usr/bin/env python3

# !/usr/bin/env python3
import glob
import json
import os
import re
from copy import deepcopy

import h5py
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units
from astropy.cosmology import Planck15
from bilby.core.utils import logger
from scipy.interpolate import interp1d

from .data_simulation import simulate_posteriors
from .parser import create_parser

matplotlib.rcParams["text.usetex"] = False


def euclidean_distance_prior(samples):
    r"""
    Evaluate the redshift prior assuming a Euclidean universe.

    See Appendix C of `Abbott et al. <https://arxiv.org/pdf/1811.12940.pdf>`_.

    .. math::

        p(z) \propto d^2_L \left( \frac{d_{L}}{1 + z} + (1 + z) \frac{d_{H}}{E(z)} \right)

    This uses the `astropy.cosmology.Planck15` cosmology.

    Parameters
    ----------
    samples: dict
        The samples to use, must contain `redshift` as a key.

    """
    redshift = samples["redshift"]
    luminosity_distance = Planck15.luminosity_distance(redshift).to(units.Gpc).value
    return luminosity_distance ** 2 * (
        luminosity_distance / (1 + redshift)
        + (1 + redshift)
        * Planck15.hubble_distance.to(units.Gpc).value
        / Planck15.efunc(redshift)
    )


def replace_keys(posts):
    """
    Map the keys from legacy names to the `GWPopulation` standards.

    Parameters
    ----------
    posts: dict
        Dictionary of `pd.DataFrame` objects

    Returns
    -------
    new_posts: dict
        Updated posteriors.

    """
    _mapping = dict(
        mass_1="m1_source",
        mass_2="m2_source",
        mass_ratio="q",
        a_1="a1",
        a_2="a2",
        cos_tilt_1="costilt1",
        cos_tilt_2="costilt2",
        redshift="redshift",
    )
    new_posts = dict()
    for name in posts:
        post = posts[name]
        new = pd.DataFrame()
        for key in _mapping:
            if _mapping[key] in post:
                new[key] = post[_mapping[key]]
            elif key in post:
                new[key] = post[key]
            else:
                new[key] = 0
        new_posts[name] = new
    return new_posts


def evaluate_prior(posts, args):
    """
    Evaluate the prior distribution for the input posteriors.

    Parameters
    ----------
    posts: dict
        Dictionary of `pd.DataFrame` objects containing the posteriors.
    args:
        Input args containing the prior specification.

    Returns
    -------
    posts: dict
        The input dictionary, modified in place.
    """
    max_redshift = max(
        args.max_redshift, max([max(posts[key]["redshift"]) for key in posts])
    )
    zs_ = np.linspace(0, max_redshift * 1.01, 1000)
    if args.distance_prior.lower() == "comoving":
        logger.info(
            f"Using uniform in the comoving source frame distance prior for all events."
        )
        p_z = Planck15.differential_comoving_volume(zs_).value * 4 * np.pi / (1 + zs_)
    else:
        logger.info("Using Euclidean distance prior for all events.")
        p_z = euclidean_distance_prior(dict(redshift=zs_))
    p_z /= np.trapz(p_z, zs_)
    interpolated_p_z = interp1d(zs_, p_z)

    for name in posts:
        post = posts[name]
        post["prior"] = 1
        if "redshift" in post:
            post["prior"] *= interpolated_p_z(post["redshift"])
        else:
            logger.warning(
                f"No redshift present for {name}, cannot evaluate distance prior weight"
            )
        if args.mass_prior.lower() == "flat-detector":
            logger.info(f"Assuming flat in detector frame mass prior for {name}")
            post["prior"] *= post["mass_1"] * (1 + post["redshift"]) ** 2
        else:
            raise ValueError(f"Mass prior {args.mass_prior} not recognized.")
        if args.spin_prior.lower() == "component":
            logger.info(f"Assuming uniform in component spin prior for {name}")
            post["prior"] /= 4
        elif args.spin_prior.lower() == "gaussian":
            raise NotImplementedError(
                f"Prior for gaussian spin has not yet been implemented."
            )
        else:
            raise ValueError(f"Spin prior {args.spin_prior} not recognized.")
    return posts


def load_gwtc_1_events(args):
    """
    Load GWTC-1 posteriors dowloaded from `<https://dcc.ligo.org/LIGO-P1800370/public>`_.

    Parameters
    ----------
    args

    Returns
    -------
    posteriors: dict
        Dictionary of `pd.DataFrame` objects

    """
    files = glob.glob(args.gwtc1_samples_regex)
    z_array = np.expm1(np.linspace(np.log(1), np.log(10 + 1), 1000))
    distance_array = Planck15.luminosity_distance(z_array).to(units.Mpc).value
    z_of_d = interp1d(distance_array, z_array)
    approximant = "Overall"
    posteriors = dict()
    meta_data = dict()
    for filename in files:
        posterior = pd.DataFrame()
        with h5py.File(filename, "r") as ff:
            try:
                data = np.array(ff[f"{approximant}_posterior"])
            except KeyError as e:
                logger.info(f"Failed to load {filename} with KeyError: {e}")
                continue
            posterior["redshift"] = z_of_d(data["luminosity_distance_Mpc"])
            for ii in [1, 2]:
                posterior[f"mass_{ii}"] = data[f"m{ii}_detector_frame_Msun"] / (
                    1 + posterior["redshift"]
                )
                posterior[f"a_{ii}"] = data[f"spin{ii}"]
                posterior[f"cos_tilt_{ii}"] = data[f"costilt{ii}"]
            posterior["mass_ratio"] = posterior["mass_2"] / posterior["mass_1"]
        posteriors[filename] = posterior
        meta_data[filename] = dict(label="GWTC-1", approximant=approximant)
        logger.info(f"Loaded {approximant} from {filename}.")
    return posteriors


def load_posterior_from_meta_file(filename, labels=None):
    """
    Load a posterior from a `PESummary` meta file.

    Parameters
    ----------
    filename: str
    labels: list
        The labels to search for in the file in order of precedence.

    Returns
    -------
    posterior: pd.DataFrame
    meta_data: dict
        Dictionary containing the run label that was loaded.

    """
    _mapping = dict(
        mass_1="mass_1_source",
        mass_2="mass_2_source",
        mass_ratio="mass_ratio",
        redshift="redshift",
        a_1="a_1",
        a_2="a_2",
        cos_tilt_1="cos_tilt_1",
        cos_tilt_2="cos_tilt_2",
    )
    load_map = dict(
        json=load_meta_file_from_json,
        h5=load_meta_file_from_hdf5,
        dat=load_samples_from_csv,
    )
    if labels is None:
        labels = ["PrecessingSpinIMRHM", "PrecessingSpin"]
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist")
    extension = os.path.splitext(filename)[1][1:]
    _posterior, label = load_map[extension](filename=filename, labels=labels)
    posterior = pd.DataFrame({key: _posterior[_mapping[key]] for key in _mapping})
    meta_data = dict(label=label)
    logger.info(f"Loaded {label} from {filename}.")
    return posterior, meta_data


def load_meta_file_from_hdf5(filename, labels):
    """
    Load the posterior from a `hdf5` `PESummary` file.
    See `load_posterior_from_meta_file`.
    """
    new_style = True
    with h5py.File(filename, "r") as data:
        if "posterior_samples" in data.keys():
            new_style = False
            data = data["posterior_samples"]
        label = list(data.keys())[0]
        for _label in labels:
            if _label in data.keys():
                label = _label
                break
        if new_style:
            posterior = pd.DataFrame(data[label]["posterior_samples"][:])
        elif hasattr(data[label], "keys"):
            posterior = pd.DataFrame(
                data[label]["samples"][:],
                columns=[key.decode() for key in data[label]["parameter_names"][:]],
            )
        else:
            posterior = pd.DataFrame(data[label][:])
        return posterior, label


def load_meta_file_from_json(filename, labels):
    """
    Load the posterior from a `json` `PESummary` file.
    See `load_posterior_from_meta_file`.
    """
    with open(filename, "r") as ff:
        data = json.load(ff)
    samples = data["posterior_samples"]
    del data
    label = list(samples.keys())[0]
    for _label in labels:
        if _label in samples:
            label = _label
            break
    posterior = pd.DataFrame(
        samples[label]["samples"], columns=samples[label]["parameter_names"]
    )
    return posterior, label


def load_samples_from_csv(filename, *args, **kwargs):
    """
    Load posterior samples from a csd file.
    This is just a wrapper to `pd.read_csv` assuming tab separation.

    Parameters
    ----------
    filename: str
    args: unused
    kwargs: unused

    Returns
    -------
    posterior: `pd.DataFrame`
    meta_data: None
    """
    posterior = pd.read_csv(filename, sep="\t")
    return posterior, None


def load_o3a_events(args):
    """
    Load posteriors for the O3a events using the `o3a_samples_regex` attribute.

    Parameters
    ----------
    args

    Returns
    -------
    posteriors: dict
        Dictionary of `pd.DataFrame` posteriors.
    """
    posteriors, meta_data = _load_batch_of_meta_files(
        regex=args.o3a_samples_regex, label="O3a", labels=args.preferred_labels
    )
    with open(os.path.join(args.run_dir, "data", "event_data.json"), "w") as ff:
        json.dump(meta_data, ff)
    return posteriors


def load_o3b_events(args):
    """
    Load posteriors for the O3b events using the `o3b_samples_regex` attribute.

    Parameters
    ----------
    args

    Returns
    -------
    posteriors: dict
        Dictionary of `pd.DataFrame` posteriors.
    """
    posteriors, meta_data = _load_batch_of_meta_files(
        regex=args.o3b_samples_regex, label="O3b", labels=args.preferred_labels
    )
    return posteriors


def _load_batch_of_meta_files(regex, label, labels=None):
    keys = [
        "mass_1",
        "mass_ratio",
        "a_1",
        "a_2",
        "cos_tilt_1",
        "cos_tilt_2",
        "redshift",
    ]
    posteriors = dict()
    meta_data = dict()
    all_files = glob.glob(regex)
    logger.info(f"Found {len(all_files)} {label} events in standard format.")
    for posterior_file in all_files:
        try:
            new_posterior, data = load_posterior_from_meta_file(
                posterior_file, labels=labels
            )
        except TypeError as e:
            logger.info(f"Failed to load {posterior_file} with TypeError: {e}.")
            continue
        if all([key in new_posterior for key in keys]):
            meta_data[posterior_file] = data
            new_posterior = new_posterior[keys]
            if min(new_posterior["mass_ratio"]) >= 1:
                new_posterior["mass_ratio"] = 1 / new_posterior["mass_ratio"]
            posteriors[posterior_file] = new_posterior
        else:
            logger.info(f"Posterior has keys {new_posterior.keys()}.")
    return posteriors, meta_data


def load_all_events(args, funcs=None):
    """
    Load posteriors for some/all events.

    Parameters
    ----------
    args
    funcs: list
        The load functions to use, the default will look for all data from O1-O3.

    Returns
    -------
    posteriors: dict
        Dictionary of `pd.DataFrame` posteriors.
    """
    if funcs is None:
        funcs = [load_gwtc_1_events, load_o3a_events, load_o3b_events]
    elif not isinstance(funcs, list):
        funcs = [funcs]
    posteriors = dict()
    logger.info("Loading posteriors...")
    for func in funcs:
        posteriors.update(func(args))
    posteriors = replace_keys(posteriors)
    posteriors = evaluate_prior(posteriors, args=args)
    for key in args.parameters:
        for name in posteriors:
            if key not in posteriors[name]:
                raise KeyError(f"{key} for found for {name}")
    logger.info(f"Loaded {len(posteriors)} posteriors.")
    return posteriors


def plot_summary(posteriors: list, events: list, args):
    """
    Plot a summary of the posteriors for each parameter.

    Parameters
    ----------
    posteriors: list
        List of `pd.DataFrame` posteriors.
    events: list
        Names for each event.
    args
    """
    posteriors = deepcopy(posteriors)
    plot_dir = os.path.join(args.run_dir, "data")
    plot_chi = True
    for posterior in posteriors:
        if all(
            [
                key in posterior
                for key in ["a_1", "a_2", "cos_tilt_1", "cos_tilt_2", "mass_ratio"]
            ]
        ):
            posterior["chi_eff"] = (
                posterior["a_1"] * posterior["cos_tilt_1"]
                + posterior["a_2"] * posterior["cos_tilt_2"] * posterior["mass_ratio"]
            ) / (1 + posterior["mass_ratio"])
            posterior["chi_p"] = np.maximum(
                posterior["a_1"] * (1 - posterior["cos_tilt_1"] ** 2) ** 0.5,
                posterior["mass_ratio"]
                * (3 + 4 * posterior["mass_ratio"])
                / (4 + 3 * posterior["mass_ratio"])
                * posterior["a_2"]
                * (1 - posterior["cos_tilt_2"] ** 2) ** 0.5,
            )
        else:
            plot_chi = False
    plot_mass_2 = True
    for posterior in posteriors:
        try:
            posterior["mass_2"] = posterior["mass_1"] * posterior["mass_ratio"]
        except KeyError:
            plot_mass_2 = False
    for parameter in posteriors[0].keys():
        if parameter in ["chi_eff", "chi_p"] and not plot_chi:
            continue
        elif parameter == "mass_2" and not plot_mass_2:
            continue
        logger.info(f"Making box plot for {parameter}")
        file_name = os.path.join(plot_dir, parameter)
        data = [post[parameter] for post in posteriors]
        fig = plt.figure(figsize=(len(posteriors), 5))
        plt.violinplot(data)
        plt.ylabel(parameter.replace("_", " "))
        plt.xticks(np.arange(1, len(events) + 1), events, rotation=90)
        if parameter == "prior":
            plt.yscale("log")
        plt.tight_layout()
        plt.savefig(file_name + ".png")
        plt.close(fig)


def gather_posteriors(args):
    """
    Load in posteriors from files according to the command-line arguments.

    Parameters
    ----------
    args:
        Command-line arguments

    Returns
    -------
    posts: list
        List of `pd.DataFrame` posteriors.
    events: list
        Event labels
    """
    if args.ignore is None:
        args.ignore = list()
    logger.info(f"Outdir is {args.run_dir}")
    load_funcs = list()
    if args.gwtc1:
        load_funcs.append(load_gwtc_1_events)
    if args.o3a:
        load_funcs.append(load_o3a_events)
    if args.o3b:
        load_funcs.append(load_o3b_events)
    if len(load_funcs) == 0:
        logger.info("No events specified, loading all events.")
        posteriors = load_all_events(args)
    else:
        posteriors = load_all_events(args, funcs=load_funcs)
    posts = list()
    events = list()
    with open(f"{args.run_dir}/data/{args.data_label}_posterior_files.txt", "w") as ff:
        for filename in posteriors.keys():
            ignore = False
            for label in args.ignore:
                if label in filename:
                    ignore = True
            if ignore:
                logger.info(f"Ignoring {filename}.")
                continue
            event = re.findall(r"(\w*\d{6}[a-z]*)", filename)[0]
            if event in events:
                continue
            posts.append(posteriors[filename])
            events.append(event)
            ff.write(f"{event}: {filename}\n")
    return posts, events


def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.injection_file is not None or args.sample_from_prior:
        posts = simulate_posteriors(args=args)
        events = [str(ii) for ii in range(len(posts))]
    else:
        posts, events = gather_posteriors(args=args)
    logger.info(f"Using {len(posts)} events, final event list is: {', '.join(events)}.")
    posterior_file = f"{args.data_label}.pkl"
    logger.info(f"Saving posteriors to {posterior_file}")
    filename = os.path.join(args.run_dir, "data", posterior_file)
    pd.to_pickle(posts, filename)
    if args.plot:
        plot_summary(posts, events, args)
