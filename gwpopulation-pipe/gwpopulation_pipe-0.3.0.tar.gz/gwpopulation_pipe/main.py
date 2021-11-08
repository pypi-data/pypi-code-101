#!/usr/bin/env python3

import itertools
import os
import shutil
import sys

from bilby_pipe.utils import logger, strip_quotes

from .parser import create_parser

MASS_MODELS = dict(
    a="gwpopulation.models.mass.power_law_primary_mass_ratio",
    b="gwpopulation.models.mass.power_law_primary_mass_ratio",
    c="SinglePeakSmoothedMassDistribution",
    d="BrokenPowerLawSmoothedMassDistribution",
    e="MultiPeakSmoothedMassDistribution",
    f="BrokenPowerLawPeakSmoothedMassDistribution",
)

REDSHIFT_MODELS = dict(
    powerlaw="gwpopulation.models.redshift.PowerLawRedshift",
    madaudickinson="gwpopulation.models.redshift.MadauDickinsonRedshift",
)

analysis_template = """universe = vanilla
executable = {analysis_executable}
log = {log_dir}/population-analysis-$(label).log
error = {log_dir}/population-analysis-$(label).err
output = {log_dir}/population-analysis-$(label).out
arguments = {ini_file} --label $(label) $(models) $(vt_models)
accounting_group = ligo.dev.o3.cbc.pe.lalinference
accounting_group_user = {user}
notification = error
request_memory = 1024
getenv = True
request_gpus = {gpu}
queue
"""
collection_template = """universe = local
executable = {collection_executable}
log = {log_dir}/population-collection-$(label).log
error = {log_dir}/population-collection-$(label).err
output = {log_dir}/population-collection-$(label).out
arguments = {ini_file}
accounting_group = ligo.dev.o3.cbc.pe.lalinference
accounting_group_user = {user}
notification = error
request_memory = 1024
getenv = True
queue
"""
format_template = """universe = vanilla
executable = {format_executable}
log = {log_dir}/population-format-$(label).log
error = {log_dir}/population-format-$(label).err
output = {log_dir}/population-format-$(label).out
arguments = --injection-file {injection_file} --result-file $(run_dir)/result/$(label)_result.json --samples-file $(run_dir)/result/$(label)_samples.hdf5 $(models) $(vt_models) --n-samples {n_post_samples} --max-redshift {max_redshift} --minimum-mass {minimum_mass} --maximum-mass {maximum_mass} --filename $(run_dir)/result/$(label)_full_posterior.hdf5 --vt-ifar-threshold {ifar_threshold} --vt-snr-threshold {snr_threshold}
accounting_group = ligo.dev.o3.cbc.pe.lalinference
accounting_group_user = {user}
notification = error
request_memory = 1024
getenv = True
request_gpus = {gpu}
queue
"""
plot_template = """universe = vanilla
executable = {plot_executable}
log = {log_dir}/population-post-$(label).log
error = {log_dir}/population-post-$(label).err
output = {log_dir}/population-post-$(label).out
arguments = {ini_file} --result-file $(run_dir)/result/$(label)_result.json --samples $(run_dir)/$(label)_samples.hdf5
accounting_group = ligo.dev.o3.cbc.pe.lalinference
accounting_group_user = {user}
notification = error
request_memory = 1024
getenv = True
request_gpus = {gpu}
queue
"""
summary_template = """universe = vanilla
executable = {summary_executable}
log = {log_dir}/population-summary.log
error = {log_dir}/population-summary.err
output = {log_dir}/population-summary.out
arguments = {ini_file} --samples $(result_files) --labels $(labels) --webdir {run_dir}/summary
accounting_group = ligo.dev.o3.cbc.pe.lalinference
accounting_group_user = {user}
notification = error
request_memory = 1024
getenv = True
queue
"""


def check_user(user=None):
    if user is None:
        if "USER" in os.environ:
            user = os.environ.get["USER"]
        else:
            raise ValueError(
                "Argument 'user' must be provided or set in environment variables!"
            )
    return user


def make_submit_files(args):
    format_args = dict(
        log_dir=args.log_dir,
        run_dir=args.run_dir,
        user=args.user,
        ini_file=args.ini_file,
        injection_file=args.vt_file,
        analysis_executable=shutil.which("gwpopulation_pipe_analysis"),
        collection_executable=shutil.which("gwpopulation_pipe_collection"),
        format_executable=shutil.which("gwpopulation_pipe_to_common_format"),
        plot_executable=shutil.which("gwpopulation_pipe_plot"),
        summary_executable=shutil.which("summarypages"),
        custom_plotting=os.path.join(os.path.dirname(__file__), "pesummary_plot.py"),
        gpu=int(args.request_gpu),
        max_redshift=args.max_redshift,
        minimum_mass=args.minimum_mass,
        maximum_mass=args.maximum_mass,
        n_post_samples=args.n_post_samples,
        ifar_threshold=args.vt_ifar_threshold,
        snr_threshold=args.vt_snr_threshold,
    )
    subfiles = ["analysis", "collection", "common_format"]
    templates = dict(
        analysis=analysis_template,
        collection=collection_template,
        common_format=format_template,
        plot=plot_template,
        summary=summary_template,
    )
    if args.post_plots:
        subfiles.append("plot")
    if args.make_summary:
        subfiles.append("summary")
    for label in subfiles:
        submit_filename = os.path.join(
            args.run_dir, "submit", f"{args.label}_{label}.sub"
        )
        with open(submit_filename, "w") as ff:
            ff.write(templates[label].format(**format_args))


def make_dag(args):
    args.user = check_user(user=args.user)
    args.run_dir = os.path.abspath(args.run_dir)
    args.log_dir = os.path.abspath(args.log_dir)
    condor_dir = os.path.join(args.run_dir, "submit")
    result_dir = os.path.join(args.run_dir, "result")
    summary_dir = os.path.join(args.run_dir, "summary")
    data_dir = os.path.join(args.run_dir, "data")
    args.ini_file = os.path.abspath(args.ini_file)
    for directory in [
        args.run_dir,
        args.log_dir,
        condor_dir,
        result_dir,
        data_dir,
        summary_dir,
    ]:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        elif not os.path.isdir(directory):
            raise IOError(f"{directory} exists and is not a directory.")

    dag_file = f"{condor_dir}/{args.label}.dag"
    bash_file = f"{condor_dir}/{args.label}.sh"

    bash_str = "#! /bin/bash\n\n"

    dag_str = (
        f"JOB collection {os.path.join(condor_dir, f'{args.label}_collection.sub')}\n"
    )
    dag_str += f'VARS collection label="{args.label}"\n\n'

    bash_str += f"gwpopulation_pipe_collection {args.ini_file}\n\n"

    collection_dependencies = "PARENT collection CHILD"
    post_dependencies = "PARENT"
    dependencies = list()
    job_names = list()
    result_files = list()

    for mass, mag, tilt, redshift in itertools.product(
        args.mass_models,
        args.magnitude_models,
        args.tilt_models,
        args.redshift_models,
    ):
        mass_model = MASS_MODELS[mass]
        mag_model = f"{mag}_spin_magnitude"
        tilt_model = f"{tilt[-3:]}_spin_orientation"
        redshift_model = REDSHIFT_MODELS[redshift]
        models = "--models " + " --models ".join(
            [
                mass_model,
                mag_model,
                tilt_model,
                redshift_model,
            ]
        )
        vt_models = list()
        if "mass" in args.vt_parameters:
            vt_models.append(mass_model)
        if "redshift" in args.vt_parameters:
            vt_models.append(redshift_model)
        if "spin" in args.vt_parameters:
            vt_models.append(tilt_model)
            vt_models.append(mag_model)
        if len(vt_models) == 0:
            vt_models = [mass_model, redshift_model]
        vt_models = "--vt-models " + " --vt-models ".join(vt_models)
        prior_name = f"mass_{mass}_{mag}_mag_{tilt}_tilt_{redshift}_redshift"
        job_name = f"{args.label}_{prior_name}"
        job_names.append(job_name)
        result_files.append(f"{args.run_dir}/result/{job_name}_result.json")
        collection_dependencies += f" {job_name}"
        post_dependencies += f" {job_name}"
        dependencies.append(f"PARENT {job_name} CHILD {job_name}_post\n")
        dependencies.append(f"PARENT {job_name} CHILD {job_name}_format\n")

        dag_str += (
            f"JOB {job_name} {os.path.join(condor_dir, f'{args.label}_analysis.sub')}\n"
            f'VARS {job_name} label="{job_name}" models="{models}" '
            f'vt_models="{vt_models}" prior="{prior_name}"\n\n'
        )
        dag_str += (
            f"JOB {job_name}_post {os.path.join(condor_dir, f'{args.label}_plot.sub')}\n"
            f'VARS {job_name}_post run_dir="{args.run_dir}" label="{job_name}"\n\n'
        )
        dag_str += (
            f"JOB {job_name}_format {os.path.join(condor_dir, f'{args.label}_common_format.sub')}\n"
            f'VARS {job_name}_format run_dir="{args.run_dir}" label="{job_name}" models="{models}" '
            f'vt_models="{vt_models}" prior="{prior_name}"\n\n'
        )

        bash_str += (
            f"gwpopulation_pipe_analysis {args.ini_file} "
            f"--label {job_name} {models} {vt_models}\n\n"
        )
        bash_str += (
            f"gwpopulation_pipe_plot {args.ini_file} "
            f"--result-file {result_dir}/{job_name}_result.json "
            f"--samples {result_dir}/{job_name}_samples.hdf5\n\n"
        )
        bash_str += (
            f"gwpopulation_pipe_to_common_format "
            f"--result-file {result_dir}/{job_name}_result.json "
            f" {models} {vt_models} --n-samples {args.n_post_samples} --max-redshift {args.max_redshift} "
            f"--minimum-mass {args.minimum_mass} --maximum-mass {args.maximum_mass} "
            f"--injection-file {args.vt_file} "
            f"--filename {result_dir}/{job_name}_full_posterior.hdf5 "
            f"--samples-file {result_dir}/{job_name}_samples.hdf5 "
            f"--vt-ifar-threshold {args.vt_ifar_threshold} "
            f"--vt-snr-threshold {args.vt_snr_threshold}\n\n"
        )

    job_names = " ".join(job_names)
    result_files = " ".join(result_files)

    if args.make_summary:
        dag_str += (
            f"JOB all_post {os.path.join(condor_dir, f'{args.label}_summary.sub')}\n"
            f'VARS all_post rundir="{summary_dir}" '
            f'labels="{job_names}" result_files="{result_files}"\n\n'
        )
        bash_str += (
            f"summarypages --samples {result_files} --webdir {summary_dir} "
            f"--labels {job_names}\n"
        )

    with open(dag_file, "w") as ff:
        ff.write(dag_str)
        ff.write(collection_dependencies + "\n")
        for dependency in dependencies:
            ff.write(dependency)
        if args.post_plots:
            post_dependencies += " CHILD all_post"
            ff.write(post_dependencies)

    with open(bash_file, "w") as ff:
        ff.write(bash_str)

    logger.info(f"dag file written to {dag_file}")
    logger.info(f"shell script written to {bash_file}")
    logger.info(f"Now run condor_submit_dag {dag_file}")


def main():
    parser = create_parser()
    args, _ = parser.parse_known_args(sys.argv[1:])

    complete_ini_file = f"{args.run_dir}/{args.label}_config_complete.ini"
    args.ini_file = complete_ini_file
    make_dag(args)
    make_submit_files(args)
    parser.write_to_file(
        filename=complete_ini_file,
        args=args,
        overwrite=True,
        include_description=False,
    )
    with open(complete_ini_file, "r") as ff:
        content = ff.readlines()
    for ii, line in enumerate(content):
        content[ii] = strip_quotes(line)
    with open(complete_ini_file, "w") as ff:
        ff.writelines(content)
