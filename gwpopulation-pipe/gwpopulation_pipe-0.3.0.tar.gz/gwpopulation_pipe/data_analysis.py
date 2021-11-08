"""
Functions for running stochastic sampling with Bilby for pre-collected posteriors.

The module provides the `gwpopulation_pipe_analysis` executable.

In order to use many of the other functions you will need a class that provides
various attributes specified in the `gwpopulation_pipe` parser.
"""

#!/usr/bin/env python3

import inspect
import os
import sys
from importlib import import_module

import matplotlib

matplotlib.use("agg")  # noqa

import deepdish as dd
import numpy as np
import pandas as pd
from bilby import run_sampler
from bilby.core.prior import Constraint, LogUniform, PriorDict
from bilby.core.utils import infer_args_from_function_except_n_args, logger
from bilby.hyper.model import Model
from bilby_pipe.utils import convert_string_to_dict
from gwpopulation.conversions import convert_to_beta_parameters
from gwpopulation.cupy_utils import to_numpy
from gwpopulation.hyperpe import HyperparameterLikelihood, RateLikelihood
from gwpopulation.models.mass import (
    BrokenPowerLawPeakSmoothedMassDistribution,
    BrokenPowerLawSmoothedMassDistribution,
    MultiPeakSmoothedMassDistribution,
    SinglePeakSmoothedMassDistribution,
    two_component_primary_mass_ratio,
)
from gwpopulation.models.spin import (
    iid_spin,
    iid_spin_magnitude_beta,
    iid_spin_orientation_gaussian_isotropic,
    independent_spin_magnitude_beta,
    independent_spin_orientation_gaussian_isotropic,
)
from scipy.stats import gamma
from tqdm.auto import trange

from . import vt_helper
from .parser import create_parser as create_main_parser
from .utils import prior_conversion, KNOWN_ARGUMENTS, MinimumEffectiveSamplesLikelihood


def create_parser():
    parser = create_main_parser()
    parser.add_argument("--prior", help="Prior file readable by bilby.")
    parser.add_argument(
        "--models",
        type=str,
        action="append",
        help="Model functions to evaluate, default is "
        "two component mass and iid spins.",
    )
    parser.add_argument(
        "--vt-models",
        type=str,
        action="append",
        help="Model functions to evaluate for selection, default is no model",
    )
    parser.add_argument(
        "--max-samples",
        default=1e10,
        type=int,
        help="Maximum number of posterior samples per event",
    )
    parser.add_argument(
        "--rate", default=False, type=bool, help="Whether to sample in the merger rate."
    )
    return parser


def load_prior(args):
    hyper_prior = PriorDict(filename=args.prior_file)
    hyper_prior.conversion_function = prior_conversion
    if args.rate:
        hyper_prior["rate"] = LogUniform(
            minimum=1e-1,
            maximum=1e3,
            name="rate",
            latex_label="$R$",
            boundary="reflective",
        )
    return hyper_prior


MODEL_MAP = {
    "two_component_primary_mass_ratio": two_component_primary_mass_ratio,
    "iid_spin": iid_spin,
    "iid_spin_magnitude": iid_spin_magnitude_beta,
    "ind_spin_magnitude": independent_spin_magnitude_beta,
    "iid_spin_orientation": iid_spin_orientation_gaussian_isotropic,
    "two_comp_iid_spin_orientation": iid_spin_orientation_gaussian_isotropic,
    "ind_spin_orientation": independent_spin_orientation_gaussian_isotropic,
    "SmoothedMassDistribution": SinglePeakSmoothedMassDistribution,
    "SinglePeakSmoothedMassDistribution": SinglePeakSmoothedMassDistribution,
    "BrokenPowerLawSmoothedMassDistribution": BrokenPowerLawSmoothedMassDistribution,
    "MultiPeakSmoothedMassDistribution": MultiPeakSmoothedMassDistribution,
    "BrokenPowerLawPeakSmoothedMassDistribution": BrokenPowerLawPeakSmoothedMassDistribution,
}


def load_model(args):
    if args.models is None:
        args.models = [
            "two_component_primary_mass_ratio",
            "iid_spin",
            "gwpopulation.models.redshift.PowerLawRedshift",
        ]
    model = Model([_load_model(model, args) for model in args.models])
    return model


def load_vt(args):
    if args.vt_function == "" or args.vt_file == "None":
        return vt_helper.dummy_selection
    vt_model = Model([_load_model(model, args) for model in args.vt_models])
    try:
        vt_func = getattr(vt_helper, args.vt_function)
        return vt_func(
            args.vt_file,
            model=vt_model,
            ifar_threshold=args.vt_ifar_threshold,
            snr_threshold=args.vt_snr_threshold,
        )
    except AttributeError:
        return vt_helper.injection_resampling_vt(
            vt_file=args.vt_file,
            model=vt_model,
            ifar_threshold=args.vt_ifar_threshold,
            snr_threshold=args.vt_snr_threshold,
        )


def _load_model(model, args):
    if "." in model:
        split_model = model.split(".")
        module = ".".join(split_model[:-1])
        function = split_model[-1]
        _model = getattr(import_module(module), function)
        logger.info(f"Using {function} from {module}.")
    elif model in MODEL_MAP:
        _model = MODEL_MAP[model]
        logger.info(f"Using {model}.")
    else:
        raise ValueError(f"Model {model} not found.")
    if inspect.isclass(_model):
        if "redshift" in model.lower():
            kwargs = dict(z_max=args.max_redshift)
        elif "mass" in model.lower():
            kwargs = dict(mmin=args.minimum_mass, mmax=args.maximum_mass)
        else:
            kwargs = dict()
        try:
            _model = _model(**kwargs)
        except TypeError:
            logger.warning(f"Failed to instantiate {model} with arguments {kwargs}")
            _model = _model()
    return _model


def create_likelihood(args, posteriors, model, selection):
    if args.rate:
        if args.enforce_minimum_neffective_per_event:
            raise ValueError(
                "No likelihood available to enforce convergence of Monte Carlo integrals "
                "while sampling over rate."
            )
        likelihood_class = RateLikelihood
    elif args.enforce_minimum_neffective_per_event:
        likelihood_class = MinimumEffectiveSamplesLikelihood
    else:
        likelihood_class = HyperparameterLikelihood
    likelihood = likelihood_class(
        posteriors,
        model,
        conversion_function=convert_to_beta_parameters,
        selection_function=selection,
        max_samples=args.max_samples,
    )

    return likelihood


def get_sampler_kwargs(args):
    sampler_kwargs = dict(nlive=500, nact=2, walks=5)
    if args.sampler_kwargs == "Default":
        sampler_kwargs = dict()
    elif not isinstance(args.sampler_kwargs, dict):
        sampler_kwargs.update(convert_string_to_dict(args.sampler_kwargs))
    else:
        sampler_kwargs = args.sampler_kwargs
    if args.sampler == "cpnest" and "seed" not in sampler_kwargs:
        sampler_kwargs["seed"] = np.random.randint(0, 1e6)
    return sampler_kwargs


def compute_rate_posterior(posterior, selection):
    r"""
    Compute the rate posterior as a post-processing step.

    This method is the same as described in https://dcc.ligo.org/T2000100.
    To get the rate at :math:`z=0` we stop after step four.

    The total surveyed four-volume is given as

    .. math::

        V_{\rm tot}(\Lambda) = T_{\rm obs} \int dz \frac{1}{1+z} \frac{dVc}{dz} \psi(z|\Lambda)

    Note that :math:`\psi(z=0|\Lambda) = 1`

    The sensitive four-volume is then :math:`\mu V_{\rm tot}` where :math:`\mu` is the
    fraction of injections which are found.

    We draw samples from the gamma distribution with mean N_EVENTS + 1

    These samples of this are then divided by the sensitive four-volume to
    give the average rate over the surveyed volume with units :math:`Gpc^{-3}yr^{-1}`.

    Parameters
    ----------
    posterior: pd.DataFrame
        DataFrame containing the posterior samples
    selection: vt_helper.InjectionResamplingVT
        Object that computes:
          - the mean and variance of the survey completeness
          - the total surveyed 4-volume weighted by the redshift distribution
    """
    if selection == vt_helper.dummy_selection:
        posterior["log_10_rate"] = np.log10(
            gamma(a=vt_helper.N_EVENTS).rvs(len(posterior))
        )
        return
    else:
        efficiencies = list()
        n_effective = list()
        surveyed_hypervolume = list()
        for ii in trange(len(posterior), file=sys.stdout):
            parameters = dict(posterior.iloc[ii])
            efficiency, variance = selection.detection_efficiency(parameters)
            efficiencies.append(efficiency)
            n_effective.append(efficiency ** 2 / variance)
            surveyed_hypervolume.append(
                float(selection.surveyed_hypervolume(parameters))
            )
        posterior["selection"] = efficiencies
        posterior["pdet_n_effective"] = n_effective
        posterior["surveyed_hypervolume"] = surveyed_hypervolume
        posterior["log_10_rate"] = np.log10(
            gamma(a=vt_helper.N_EVENTS).rvs(len(posterior))
            / posterior["surveyed_hypervolume"]
            / posterior["selection"]
        )
    posterior["rate"] = 10 ** posterior.log_10_rate


def fill_minimum_n_effective(posterior, likelihood):
    """
    Compute the minimum per event n effective for each posterior sample.
    This is added to the posterior in place.

    Parameters
    ----------
    posterior: pd.DataFrame
        DataFrame containing posterior distribution
    likelihood: gwpopulation.hyperpe.HyperparameterLikelihood
        The likelihood used in the analysis.

    Returns
    -------

    """
    if not hasattr(likelihood, "per_event_bayes_factors_and_n_effective"):
        logger.info(
            "Likelihood has no method 'per_event_bayes_factors_and_n_effective'"
            " skipping n_effective calculation."
        )
        return
    all_n_effectives = list()
    for ii in trange(len(posterior), file=sys.stdout):
        parameters = dict(posterior.iloc[ii])
        parameters, _ = likelihood.conversion_function(parameters)
        likelihood.parameters.update(parameters)
        likelihood.hyper_prior.parameters.update(parameters)
        _, n_effectives = likelihood.per_event_bayes_factors_and_n_effective()
        all_n_effectives.append(float(min(n_effectives)))
    posterior["min_event_n_effective"] = all_n_effectives
    return


def resample_single_event_posteriors(likelihood, result, save=True):
    """
    Resample the single event posteriors to use the population-informed prior.

    Parameters
    ----------
    likelihood: gwpopulation.hyperpe.HyperparameterLikelihood
        The likelihood object to use.
    result: bilby.core.result.Result
        The result whose posterior should be used for the reweighting.
    save: bool
        Whether to save the samples to file. If `False` the samples will be returned.

    Returns
    -------
    original_samples: dict
        The input samples with the new prior weights in a new `weights` entry.
    reweighted_samples: dict
        The input samples resampled in place according to the new prior weights.
        Note that this will cause samples to be repeated.
    """
    original_samples = {key: to_numpy(likelihood.data[key]) for key in likelihood.data}
    original_samples["prior"] = to_numpy(likelihood.sampling_prior)
    reweighted_samples, weights = likelihood.posterior_predictive_resample(
        result.posterior, return_weights=True
    )
    original_samples["weights"] = to_numpy(weights)
    reweighted_samples = {
        key: to_numpy(reweighted_samples[key]) for key in reweighted_samples
    }
    if save:
        dd.io.save(
            os.path.join(result.outdir, f"{result.label}_samples.hdf5"),
            dict(
                original=original_samples,
                reweighted=reweighted_samples,
                names=result.meta_data["event_ids"],
                label=result.label,
            ),
        )
    else:
        return original_samples, reweighted_samples


def main():
    parser = create_parser()
    args, unknown_args = parser.parse_known_args(sys.argv[1:])
    posterior_file = os.path.join(args.run_dir, "data", f"{args.data_label}.pkl")
    posteriors = pd.read_pickle(posterior_file)
    for ii, post in enumerate(posteriors):
        posteriors[ii] = post[post["redshift"] < args.max_redshift]
    vt_helper.N_EVENTS = len(posteriors)
    logger.info(f"Loaded {len(posteriors)} posteriors")
    event_ids = list()
    with open(
        os.path.join(args.run_dir, "data", f"{args.data_label}_posterior_files.txt"),
        "r",
    ) as ff:
        for line in ff.readlines():
            event_ids.append(line.split(":")[0])

    hyper_prior = load_prior(args)
    model = load_model(args)
    selection = load_vt(args)

    search_keys = list()
    ignore = ["dataset", "self", "cls"]
    for func in model.models:
        param_keys = infer_args_from_function_except_n_args(func, n=0)
        param_keys += KNOWN_ARGUMENTS.get(func, list())
        for key in param_keys:
            if key in search_keys or key in ignore:
                continue
            search_keys.append(key)

    logger.info(f"Identified keys: {', '.join(search_keys)}")
    for key in list(hyper_prior.keys()):
        if (
            key not in search_keys
            and key != "rate"
            and not isinstance(hyper_prior[key], Constraint)
        ):
            del hyper_prior[key]

    likelihood = create_likelihood(args, posteriors, model, selection)
    likelihood.parameters.update(hyper_prior.sample())
    likelihood.log_likelihood_ratio()

    if args.injection_file is not None:
        injections = pd.read_json(args.injection_file)
        injection_parameters = dict(injections.iloc[args.injection_index])
    else:
        injection_parameters = None

    result = run_sampler(
        likelihood=likelihood,
        priors=hyper_prior,
        label=args.label,
        sampler=args.sampler,
        outdir=os.path.join(args.run_dir, "result"),
        injection_parameters=injection_parameters,
        **get_sampler_kwargs(args),
    )
    result.meta_data["models"] = args.models
    result.meta_data["event_ids"] = event_ids

    logger.info("Computing rate posterior")
    compute_rate_posterior(posterior=result.posterior, selection=selection)
    logger.info("Computing n effectives")
    fill_minimum_n_effective(posterior=result.posterior, likelihood=likelihood)

    result.save_to_file(extension="json", overwrite=True)

    logger.info("Resampling single event posteriors")
    resample_single_event_posteriors(likelihood, result, save=True)

    plot_parameters = result.search_parameter_keys + ["log_10_rate"]
    if injection_parameters is not None:
        plot_parameters = {
            key: injection_parameters.get(key, np.nan) for key in plot_parameters
        }
    result.plot_corner(parameters=plot_parameters)
