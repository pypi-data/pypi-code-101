import bilby
import gwpopulation
from bilby_pipe.bilbyargparser import BilbyArgParser
from bilby_pipe.parser import StoreBoolean
from bilby_pipe.utils import noneint, nonestr


def create_parser():
    from . import __version__

    parser = BilbyArgParser(
        usage=__doc__, ignore_unknown_config_file_keys=False, allow_abbrev=False
    )
    parser.add("ini", type=str, is_config_file=True, help="Configuration ini file")
    parser.add("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add(
        "--version",
        action="version",
        version="%(prog)s={version}\nbilby={bilby_version}\ngwpopulation={gwpopulation_version}".format(
            version=__version__,
            bilby_version=bilby.__version__,
            gwpopulation_version=gwpopulation.__version__,
        ),
    )

    base_parser = parser.add_argument_group(
        title="Generic arguments", description="Generic arguments"
    )

    base_parser.add_argument(
        "--run-dir",
        type=str,
        default="outdir",
        help="Output directory for posterior samples",
    )
    base_parser.add_argument(
        "--log-dir",
        type=str,
        default="logs",
        help="Output directory for writing log files",
    )
    base_parser.add_argument("--label", type=str, default="label", help="Run label")
    base_parser.add_argument("--user", type=str, help="User name", default=None)
    base_parser.add_argument("--vt-file", type=str, help="File to load VT data from.")
    base_parser.add_argument(
        "--vt-ifar-threshold",
        type=float,
        default=1,
        help="IFAR threshold for resampling injections",
    )
    base_parser.add_argument(
        "--vt-snr-threshold",
        type=float,
        default=11,
        help="IFAR threshold for resampling injections. "
        "This is only used for O1/O2 injections",
    )
    base_parser.add_argument(
        "--vt-function",
        type=str,
        default="injection_resampling_vt",
        help="Function to generate selection function from.",
    )
    base_parser.add_argument(
        "--prior-file",
        type=str,
        help="Prior file containing priors for all considered parameters",
    )
    base_parser.add_argument(
        "--request-gpu",
        default=True,
        action=StoreBoolean,
        help="Whether to request a GPU for the relevant jobs.",
    )

    model_parser = parser.add_argument_group(
        title="Analysis models", description="Analysis models"
    )
    model_parser.add_argument(
        "--mass-models", action="append", help="Mass distribution models"
    )
    model_parser.add_argument(
        "--magnitude-models", action="append", help="Spin magnitude distribution models"
    )
    model_parser.add_argument(
        "--tilt-models", action="append", help="Spin tilt distribution models"
    )
    model_parser.add_argument(
        "--redshift-models", action="append", help="Redshift distribution models"
    )

    collection_parser = parser.add_argument_group(
        title="Data collection arguments", description="Data collection arguments"
    )
    collection_parser.add_argument(
        "--parameters",
        action="append",
        help="Parameters to load posteriors for.",
    )
    collection_parser.add_argument(
        "--ignore", action="append", help="Events to ignore."
    )
    collection_parser.add_argument(
        "--gwtc1", action=StoreBoolean, default=False, help="Use GWTC1 events"
    )
    collection_parser.add_argument(
        "--o3a", action=StoreBoolean, default=False, help="Use O3a events"
    )
    collection_parser.add_argument(
        "--o3b", action=StoreBoolean, default=False, help="Use O3b events"
    )
    collection_parser.add_argument(
        "--gwtc1-samples-regex",
        type=str,
        default="",
        help="Pattern to match for O3a events",
    )
    collection_parser.add_argument(
        "--o3a-samples-regex",
        type=str,
        default="",
        help="Pattern to match for O3a events",
    )
    collection_parser.add_argument(
        "--preferred-labels",
        action="append",
        help="Run labels to search for in sample files",
    )
    collection_parser.add_argument(
        "--o3b-samples-regex",
        type=str,
        default="",
        help="Pattern to match for O3b events",
    )
    collection_parser.add_argument(
        "--plot",
        default=True,
        action=StoreBoolean,
        help="Whether to generate diagnostic plots",
    )
    collection_parser.add_argument(
        "--n-simulations", type=noneint, help="Number of posteriors to simulate"
    )
    collection_parser.add_argument(
        "--samples-per-posterior",
        type=int,
        default=1000,
        help="Number of samples per posterior.",
    )
    collection_parser.add_argument(
        "--data-label", default="posteriors", help="Label for data product."
    )
    collection_parser.add_argument(
        "--distance-prior",
        default="euclidean",
        help="Distance prior format, e.g., euclidean, comoving",
    )
    collection_parser.add_argument(
        "--mass-prior",
        default="flat-detector",
        help="Mass prior, only flat-detector is implemented",
    )
    collection_parser.add_argument(
        "--spin-prior",
        default="component",
        help="Spin prior, this should be either component or gaussian",
    )

    analysis_parser = parser.add_argument_group(
        title="Arguments describing analysis jobs", description="Analysis arguments"
    )
    analysis_parser.add_argument(
        "--max-redshift",
        default=2.3,
        type=float,
        help="The maximum redshift considered, this should match the injections.",
    )
    analysis_parser.add_argument(
        "--minimum-mass",
        default=2,
        type=float,
        help="The minimum mass considered, this should match the injections "
        "and is important for smoothed mass models.",
    )
    analysis_parser.add_argument(
        "--maximum-mass",
        default=100,
        type=float,
        help="The maximum mass considered, this should match the injections "
        "and is important for smoothed mass models.",
    )
    analysis_parser.add_argument(
        "--sampler",
        default="dynesty",
        type=str,
        help="The sampler to use, the default is dynesty",
    )
    analysis_parser.add_argument(
        "--sampler-kwargs",
        type=str,
        default="Default",
        help=(
            "Dictionary of sampler-kwargs to pass in, e.g., {nlive: 1000} OR "
            "pass pre-defined set of sampler-kwargs {Default, FastTest}"
        ),
    )
    analysis_parser.add_argument(
        "--vt-parameters",
        action="append",
        help=(
            "Which parameters to include in the VT estimate, should be some "
            "combination of mass, redshift, spin"
        ),
    )
    analysis_parser.add_argument(
        "--enforce-minimum-neffective-per-event",
        action=StoreBoolean,
        default=True,
        help=(
            "Require that all Monte Carlo integrals for the single event "
            "marignalizaed likleihoods have at least as many effective samples"
            " as the number of events."
        ),
    )

    injection_parser = parser.add_argument_group(
        title="Arguments describing injections", description="Injection arguments"
    )
    injection_parser.add_argument(
        "--injection-file",
        default=None,
        type=nonestr,
        help="JSON file containing population parameters, should be pandas readable.",
    )
    injection_parser.add_argument(
        "--injection-index", type=noneint, help="Index in injection file to use."
    )
    injection_parser.add_argument(
        "--sample-from-prior",
        action=StoreBoolean,
        help="Simulate posteriors from prior.",
    )

    post_parser = parser.add_argument_group(
        title="Post processing arguments", description="Post arguments"
    )
    post_parser.add_argument(
        "--post-plots",
        action=StoreBoolean,
        default=True,
        help="Whether to make post-processing plots.",
    )
    post_parser.add_argument(
        "--make-summary",
        action=StoreBoolean,
        default=True,
        help="Whether to make a summary page.",
    )
    post_parser.add_argument(
        "--n-post-samples",
        default=5000,
        type=int,
        help="Number of samples to use in the common format script",
    )

    return parser
