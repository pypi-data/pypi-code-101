from __future__ import print_function
import csv
import logging
import multiprocessing
import os
import os.path as op
import shutil
import six
import sys
import tarfile

from collections import Counter, OrderedDict
from glob import glob

import click
import click_config
import pandas
import parmap

from genologics.lims import Lims
from scgc import apps, classifier, fastx, utils


class config(object):
    """
    Define default values that may be missing in the configuration file.
    """

    class shared(object):
        data = ""
        results = ""
        deliverables = ""
        cores = 10
        min_score = 150
        top_fraction = 0.9
        min_length = 100
        cores = 10
        baseuri = "https://scgc-clarity.bigelow.org"
        username = "apiuser"
        password = "meantdiagramcreateprize"
        version = "v2"
        layouts_dir = "/mnt/scgc_raw/clarity/static/layout"

    class assemble(object):
        logs = "/mnt/scgc_raw/results/nextseq/logs/"
        bcl_queue = "scgc-route"
        queue = "route"
        time = "20:00:00"
        qsub_cpus = 8
        qsub_mem = "50G"
        job_name = "assembly"
        subsample = 0
        cores = 10
        skip_qc = False
        ignore_low_coverage = False
        trim_opts = "-phred33 LEADING:0 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:36"
        complexity_threshold = 0.05
        norm_opts = "-k 21 -t 30 -c 3"
        reference = ""
        reference_threshold = 0.05
        assembly_opts = "--careful --sc --phred-offset 33"
        passing_length = 2200
        left_trim = 100
        right_trim = 100
        blast_db = ""
        blast_opts = "-num_alignments 100"
        contamination_terms = "homo sapiens,human dna sequence"
        contamination_length = 100
        contamination_identity = 95.0
        pca_script = ""
        pca_opts = "--window 1600 --step 200"
        ssu_min_length = 500
        # SSU reference DB
        ssu_blast_db = ""
        ssu_blast_map = ""
        ssu_blast_tre = ""
        prokka_proteins = ""

    class classify(object):
        blast_db = ""
        function_map = ""

    class join(object):
        # could move some to shared space
        cores = 10
        skip_qc = False
        trim_opts = "-phred33 LEADING:0 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:75"
        complexity_threshold = 0.05
        mismatch_density = 0.05
        min_overlap = 35
        max_overlap = 150
        blast_opts = ""
        contamination_terms = ""
        contamination_length = 75
        contamination_identity = 95.0

    class deliverables(object):
        cores = 10

    class coassemble(object):
        outdir = "./results"


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option("0.4.3")
@click.pass_context
def cli(obj):
    """SCGC sequencing packages."""
    pass


def print_stats(out_file, stats_dict):
    # TODO "notes" placed ahead of checkM 'checkM_classification'
    with open(out_file, "w") as fh:
        print(*list(stats_dict.keys()), sep=",", file=fh)
        print(*list(stats_dict.values()), sep=",", file=fh)


def stop_processing(msg, stats=None, log_file=None, exit_code=0):
    logging.error(msg)
    if stats:
        stats["notes"] = msg
    if log_file:
        print_stats(log_file, stats)
    sys.exit(exit_code)


def process_samplesheet(
    samplesheet, new_samplesheet, reverse_complement=False, determine=False
):
    """Fix hidden characters in sample names and optional reverse complement
    the second index.

    Args:
        samplesheet (str): file path to SampleSheet.csv
        reverse_complement (bool): to reverse complement 'Index2'

    Returns:
        list
    """
    if not determine:
        logging.info("Processing %s", samplesheet)

    samples = []
    start = False
    index2_idx = None

    with open(samplesheet, "rU" if six.PY2 else "r") as ifh, open(
        new_samplesheet, "w"
    ) as ofh:
        for line in ifh:
            toks = line.strip().split(",")
            if not start:
                # table header processing
                if toks[0] == "Sample_ID":
                    start = True
                    if reverse_complement:
                        if "index2" in toks:
                            index2_idx = toks.index("index2")
                        elif "Index2" in toks:
                            index2_idx = toks.index("Index2")
                        else:
                            logging.warn("There is no Index2 to reverse complement")

            elif toks[0]:
                # convert underscores to dashes
                toks[0] = toks[0].replace("_", "-").replace(".", "-")
                toks[1] = toks[0]
                samples.append(toks[0])

                # only adjust on known index
                if reverse_complement and index2_idx:
                    toks[index2_idx] = complement(toks[index2_idx])[::-1]

            # remove blank lines at end of table
            else:
                break
            print(*[t.strip() for t in toks], sep=",", file=ofh)

    run = os.path.basename(os.path.dirname(samplesheet))
    if not determine:
        logging.info("Found %d samples for run %s", len(samples), run)
    return samples


@cli.command("annotate", short_help="run prokka with optional references")
@click.argument("fasta", type=click.Path(exists=True))
@click.argument("outdir")
@click.argument("prefix")
@click.option("--cores", help="number of cores used by prokka")
@click_config.wrap(module=config, sections=["assemble", "shared"])
def cli_run_prokka(fasta, outdir, prefix, cores):
    """Annotate FASTA and write files to OUTDIR where output files begin with
    PREFIX. Additional annotations from PROTEINS is written to
    PREFIX-extra.tsv
    """
    log = utils.logger(log_name="Annotate")
    log.info("Annotation started on %s" % fasta)
    utils.safe_makedir(outdir)
    log.info("Output is being written to %s/%s" % (outdir, prefix))
    if cores:
        config.assemble.cores = cores
    apps.run_prokka(
        fasta,
        outdir,
        prefix,
        proteins=config.assemble.prokka_proteins,
        cores=config.assemble.cores,
    )
    log.info("Annotation complete.")


@cli.command("assemble", short_help="paired-end assembly pipeline")
@click.argument("r1")
@click.argument("run_id")
@click.option("--data", help="directory of raw sequence data; the parent of run data")
@click.option(
    "--results",
    help="parent directory for all result files; the parent of run result data",
)
@click.option(
    "--output",
    help="output path to overwrite configuration settings for results location",
)
@click.option("--cores", type=int, help="number of multithreading tasks where possible")
@click.option(
    "--ignore-low-coverage",
    is_flag=True,
    help="set to allow samples with fewer than 1k reads to be processed",
)
@click.option(
    "--subsample",
    type=int,
    default=0,
    help="subsample original fastq prior to executing pipeline; 0 disables",
)
@click.option("--trim-opts", help="trimmomatic options")
@click.option(
    "--complexity-threshold", type=float, help="sequence complexity threshold"
)
@click.option("--norm-opts", help="kmernorm options")
@click.option(
    "--contamination-reference", help="contamination reference fasta file path"
)
@click.option(
    "--reference-threshold",
    type=float,
    help="allowable mismatch fraction to contamination reference",
)
@click.option("--assembly-opts", help="spades options")
@click.option("--passing-length", type=int, help="passing contig length")
@click.option("--left-trim", type=int, help="bases to trim from 5' end")
@click.option("--right-trim", type=int, help="bases to trim from 3' end")
@click.option(
    "--blast-db",
    help="blast database; multiple can be specified as comma separated list of paths",
)
@click.option("--blast-opts", help="blast options")
@click.option("--contamination-terms", help="blast contamination filter terms")
@click.option(
    "--contamination-length",
    type=int,
    help="minimum length of a hit to be considered; overlapping hits are merged",
)
@click.option(
    "--contamination-identity",
    type=float,
    help="minimum percentage of identical matches across alignment to be considered",
)
@click.option("--pca-script", help="tetramerPCA script path")
@click.option("--pca-opts", help="tetramerPCA options")
@click.option(
    "--ssu-min-length",
    type=int,
    default=500,
    help="SSU minimum sequence length of reported assignments",
)
@click.option("--ssu-blast-db", help="SSU annotation DB")
@click.option(
    "--ssu-blast-map", help="organism map with ID corresponding to ssu-blast-db"
)
@click.option(
    "--ssu-blast-tre", help="newick tree of ID corresponding to ssu-blast-map"
)
@click.option(
    "--prokka-proteins",
    help="fasta file of priority protein sequences for prokka annotation",
)
@click.option(
    "--seqtk-seed", default=11, show_default=True, help="seqtk random sample seed"
)
@click.option("--with-interproscan", is_flag=True, help="run interproscan across genes")
@click_config.wrap(module=config, sections=["assemble", "shared"])
def scgc_assemble(
    r1,
    run_id,
    data,
    results,
    output,
    cores,
    ignore_low_coverage,
    subsample,
    trim_opts,
    complexity_threshold,
    norm_opts,
    contamination_reference,
    reference_threshold,
    assembly_opts,
    passing_length,
    left_trim,
    right_trim,
    blast_db,
    blast_opts,
    contamination_terms,
    contamination_length,
    contamination_identity,
    pca_script,
    pca_opts,
    ssu_min_length,
    ssu_blast_db,
    ssu_blast_map,
    ssu_blast_tre,
    prokka_proteins,
    seqtk_seed,
    with_interproscan,
):
    """Assembly protocol. Any options specified on the command line overwrite
    defaults and any configuration file.
    """
    assert (
        "_R1"
    ) in r1, (
        "We're operating under the assumption of Illumina's file naming convention."
    )
    r2 = r1.replace("_R1", "_R2")
    sample = op.basename(r1).partition("_")[0]
    log = utils.logger(log_name="Assemble")
    log.info("Assembly started on %s" % sample)
    # we're going to rename "sample" to "sample-<subsample number>"
    try:
        subsample_n = int(max([config.assemble.subsample, subsample]))
    except ValueError:
        log.exception("Subsampling parameter should be an integer")
        raise

    # rename sample to include the subsample number if requested
    if subsample_n:
        sample = "%s-%d" % (sample, subsample_n)
    if data:
        config.shared.data = data
    if results:
        config.shared.results = results
    # create proper output directory structure
    if not output:
        output_dir = op.join(config.shared.results, run_id, sample)
    else:
        output_dir = op.abspath(output)
    if cores:
        config.assemble.cores = cores
    if ignore_low_coverage:
        config.assemble.ignore_low_coverage = True
    if trim_opts:
        config.assemble.trim_opts = trim_opts
    if complexity_threshold:
        config.assemble.complexity_threshold = complexity_threshold
    if norm_opts:
        config.assemble.norm_opts = norm_opts
    if contamination_reference:
        config.assemble.reference = contamination_reference
    if reference_threshold:
        config.assemble.reference_threshold = reference_threshold
    if assembly_opts:
        config.assemble.assembly_opts = assembly_opts
    if passing_length:
        config.assemble.passing_length = passing_length
    if left_trim:
        config.assemble.left_trim = left_trim
    if right_trim:
        config.assemble.right_trim = right_trim
    if blast_db:
        config.assemble.blast_db = blast_db
    if blast_opts:
        config.assemble.blast_opts = blast_opts
    if contamination_terms:
        config.assemble.contamination_terms = contamination_terms
    if contamination_length:
        config.assemble.contamination_length = contamination_length
    if contamination_identity:
        config.assemble.contamination_identity = contamination_identity
    if pca_script:
        config.assemble.pca_script = pca_script
    if pca_opts:
        config.assemble.pca_opts = pca_opts
    if ssu_min_length:
        config.assemble.ssu_min_length = ssu_min_length
    if ssu_blast_db:
        config.assemble.ssu_blast_db = ssu_blast_db
    if ssu_blast_map:
        config.assemble.ssu_blast_map = ssu_blast_map
    if ssu_blast_tre:
        config.assemble.ssu_blast_tre = ssu_blast_tre
    if prokka_proteins:
        config.assemble.prokka_proteins = prokka_proteins
    utils.safe_makedir(output_dir)
    log.info("Writing results to %s" % output_dir)
    # the final stats file we're writing out upon completion
    run_stats_file = op.join(output_dir, "%s_assembly_info.csv" % sample)
    run_stats = OrderedDict({"well": sample})

    sample_name_parts = sample.split("-")
    plate = "-".join(sample_name_parts[0:2])
    try:
        # sample well will fail with their "custom" samples
        sample_well = sample_name_parts[2]
        lims = Lims(
            config.shared.baseuri,
            config.shared.username,
            config.shared.password,
            config.shared.version,
        )

        # lets just fail for now
        # cp contents
        artifact_id = lims.get_containers(plate)[0].placements["A:1"].id
        mda_process = lims.get_processes(
            type="rtMDA-1", inputartifactlimsid=artifact_id
        )[0]
        cp_data = dict()
        for artifact in mda_process.shared_result_files():
            if artifact.name.endswith(".csv"):
                # can raise requests.exceptions.HTTPError
                try:
                    contents = lims.get_file_contents(artifact.files[0].id).split("\n")
                    plate_id = contents[0].split(" ")[1]
                    sample_ids = contents[contents.index("[Fit Parameters]") + 1].split(
                        ","
                    )[1:]
                    cp_values = contents[contents.index("[Fit Parameters]") + 3].split(
                        ","
                    )[1:]
                    cp_data = {
                        "{}-{}".format(plate_id, k): v
                        for k, v in six.moves.zip(sample_ids, cp_values)
                    }
                except Exception:
                    cp_data[sample] = "error connecting to LIMS"
                break

        # facs contents
        facs_process = lims.get_processes(type="FACS", inputartifactlimsid=artifact_id)[
            0
        ]
        layout_file = op.join(
            config.shared.layouts_dir,
            op.basename(facs_process.udf["Plate Layout File"]),
        )
        plate_contents = dict()
        with open(layout_file) as fh:
            lines = fh.readlines()
            if len(lines) == 1:
                lines = lines[0].split("\r")

            for y_index, line in enumerate(lines):
                if y_index == 0:
                    continue
                toks = line.strip().split("\t")
                row = toks[0]
                for x_index, row_value in enumerate(toks[1:], start=1):
                    well = "{row}{number}".format(row=row, number="%02d" % (x_index,))
                    plate_contents[well] = row_value
        run_stats["well_type"] = plate_contents[sample_well]
        run_stats["wga_cp"] = cp_data[sample]
    except:
        pass
    run_stats["wgs_run_id"] = run_id

    # log from the run's conversion from .bcl to .fastq
    # bcl2fastq_log = op.join(config.shared.data, run_id, "bcl2fastq.log")
    # if op.exists(bcl2fastq_log):
    #     run_stats['bcl2fastq_version'], run_stats[
    #         'bcl2fastq_parameters'
    #     ] = apps.parse_bcl2fastq_log(
    #         bcl2fastq_log
    #     )

    if not op.exists(r2):
        stop_processing("zero starting reads", run_stats, run_stats_file)

    run_stats["raw_read_count"] = fastx.read_count(r1)
    current_read_count = run_stats["raw_read_count"]
    # stop operating on samples that had very low read counts
    if current_read_count < 1000 and not config.assemble.ignore_low_coverage:
        stop_processing("too few starting reads", run_stats, run_stats_file)
    # create sub folders
    qc_dir = utils.safe_makedir(op.join(output_dir, sample + "_WGS_QC"))
    ssu_dir = utils.safe_makedir(op.join(qc_dir, "SSU_rRNA_recovery"))
    reads_dir = utils.safe_makedir(op.join(output_dir, sample + "_WGS_reads"))
    blast_dir = op.join(qc_dir, sample + "_all_contigs_blastn")
    checkm_dir = op.join(qc_dir, sample + "_final_contigs_checkm")
    prokka_dir = op.join(output_dir, sample + "_functional_annotation", "Prokka")
    if with_interproscan:
        interproscan_dir = utils.safe_makedir(
            op.join(output_dir, sample + "_functional_annotation", "InterProScan")
        )
    swissprot_dir = utils.safe_makedir(
        op.join(output_dir, sample + "_functional_annotation", "Swiss-Prot")
    )
    pca_dir = op.join(qc_dir, sample + "_final_contigs_tetramer_pca")
    # subsample
    if subsample_n:
        r1, r2 = apps.run_seqtk_sample(
            [r1, r2],
            [
                op.join(reads_dir, sample + "_R1.fastq.gz"),
                op.join(reads_dir, sample + "_R2.fastq.gz"),
            ],
            subsample_n,
            seed=seqtk_seed,
        )
        # run_stats['subsampled_to'] = subsample_n
        current_read_count = fastx.read_count(r1)
    # fastqc
    if not config.assemble.skip_qc:
        fastqc = apps.run_fastqc(
            [r1, r2], op.join(qc_dir, sample + "_fastqc"), config.assemble.cores
        )
    # trim
    if config.assemble.trim_opts:
        out_files = apps.trimmomatic(
            [r1, r2],
            [
                op.join(reads_dir, sample + "_trimmed_R1.fastq.gz"),
                op.join(reads_dir, sample + "_orphan_R1.fastq.gz"),
                op.join(reads_dir, sample + "_trimmed_R2.fastq.gz"),
                op.join(reads_dir, sample + "_orphan_R2.fastq.gz"),
            ],
            config.assemble.trim_opts,
            config.assemble.cores,
        )
        # run_stats['trimmer'] = apps.trimmomatic_version()
        # run_stats['trim_parameters'] = '"%s"' % config.assemble.trim_opts
        # run_stats['trimmed_read_count'] = fastx.read_count(out_files[0])
        # current_read_count = run_stats['trimmed_read_count']
        next_r1 = out_files[0]
        next_r2 = out_files[2]
    else:
        next_r1 = r1
        next_r2 = r2
    if not current_read_count:
        stop_processing("no reads survived trimming", run_stats, run_stats_file)
    # complexity filter
    pe_reads, complexity_read_count = fastx.complexity_filter(
        next_r1,
        next_r2,
        op.join(reads_dir, sample + "_pe.fastq.gz"),
        config.assemble.complexity_threshold,
        config.assemble.cores,
    )
    # run_stats['complexity_filter_threshold'] = "%0.02f%%" % (
    #     config.assemble.complexity_threshold * 100
    # )
    # run_stats['complexity_filtered_read_count'] = complexity_read_count
    current_read_count = complexity_read_count
    if not current_read_count:
        stop_processing("no reads after complexity filter", run_stats, run_stats_file)
    # digital normalization
    if config.assemble.norm_opts and current_read_count > 0:
        normed_reads = apps.run_kmernorm(
            pe_reads,
            op.join(reads_dir, sample + "_normalized_pe.fastq.gz"),
            config.assemble.norm_opts,
            config.assemble.cores,
        )
        next_pe = normed_reads
        # run_stats['normalizer'] = apps.kmernorm_version()
        # run_stats['normalization_parameters'] = '"%s"' % config.assemble.norm_opts
        # over 2 due to the reads being interleaved
        # run_stats['normalized_read_count'] = fastx.read_count(normed_reads) / 2
        current_read_count = fastx.read_count(normed_reads) / 2
    else:
        next_pe = pe_reads
    if not current_read_count:
        stop_processing("no reads after normalization", run_stats, run_stats_file)
    # contamination filter against bwa indexes
    if config.assemble.reference:
        # this should likely be a loop
        # for ref_fasta in config.assemble.reference.split(","):
        #     # needs to accommodate temp output file
        #     cfilter_reads = apps.reference_filter(next_pe, ref_fasta,
        #                                           op.join(reads_dir, sample + "_contamfiltered_pe.fastq.gz"),
        #                                           hits_file=None,
        #                                           threshold=config.assemble.reference_threshold,
        #                                           cores=config.assemble.cores)
        cfilter_reads = apps.reference_filter(
            next_pe,
            config.assemble.reference,
            op.join(reads_dir, sample + "_contamfiltered_pe.fastq.gz"),
            hits_file=None,
            threshold=config.assemble.reference_threshold,
            cores=config.assemble.cores,
        )
        # loop ends here
        # run_stats['contamination_reference'] = ";".join(
        #     op.basename(i) for i in config.assemble.reference.split(",")
        # )
        # run_stats['contamination_identity_threshold'] = "%0.02f%%" % (
        #     100 - (100 * config.assemble.reference_threshold)
        # )
        # over 2 due to the reads being interleaved
        # run_stats['passed_contamination_filter'] = fastx.read_count(cfilter_reads) / 2
        current_read_count = fastx.read_count(cfilter_reads) / 2
        next_pe = cfilter_reads
    if not current_read_count:
        stop_processing(
            "no reads after contamination filtering", run_stats, run_stats_file
        )
    # assemble
    if config.assemble.assembly_opts:
        # run_stats['assembler'] = apps.spades_version()
        # run_stats['assembly_parameters'] = '"%s"' % config.assemble.assembly_opts
        # run_stats['passing_contig_length'] = config.assemble.passing_length
        all_contigs = apps.spades(
            sample,
            next_pe,
            op.join(qc_dir, sample + "_all_contigs.fasta"),
            config.assemble.assembly_opts,
            config.assemble.cores,
        )
        if utils.file_exists(all_contigs):
            stats = fastx.fasta_stats(all_contigs)
            # run_stats['all_contigs_count'] = stats[2]
            # run blast against all_contigs
            if config.assemble.blast_db and config.assemble.blast_opts:
                blast_tabular = []
                for blast_db in config.assemble.blast_db.split(","):
                    db_name = os.path.basename(blast_db)
                    blast_archive = apps.blastn(
                        all_contigs,
                        op.join(
                            blast_dir, sample + "_" + db_name + "_all_contigs.ASN1"
                        ),
                        blast_db,
                        config.assemble.blast_opts,
                        config.assemble.cores,
                    )
                    blast_html = apps.blast_formatter(
                        blast_archive,
                        op.join(
                            blast_dir, sample + "_" + db_name + "_all_contigs.html"
                        ),
                        "-html -max_target_seqs 10",
                    )
                    blast_tabular_db = apps.blast_formatter(
                        blast_archive,
                        op.join(blast_dir, sample + "_" + db_name + "_all_contigs.tsv"),
                        "-max_target_seqs 10",
                        (
                            "6 qseqid sseqid pident length mismatch gapopen qstart "
                            "qend sstart send evalue bitscore sallseqid score nident "
                            "positive gaps ppos qframe sframe qseq sseq qlen slen "
                            "salltitles"
                        ),
                    )
                    blast_tabular.append(blast_tabular_db)
            # length filter the contigs
            l_pass, l_fail = fastx.length_filter(
                all_contigs,
                op.join(qc_dir, sample + "_length_passing_contigs.fasta"),
                op.join(qc_dir, sample + "_length_failing_contigs.fasta"),
                length=config.assemble.passing_length,
            )
            if utils.file_exists(l_pass):
                stats = fastx.fasta_stats(l_pass)
                # run_stats['length_passing_contigs_count'] = stats[2]
                # trim then run blast contamination filter
                if (
                    config.assemble.contamination_terms
                    and config.assemble.blast_db
                    and config.assemble.blast_opts
                ):
                    raw_trimmed_contigs = fastx.trim_fastx(
                        l_pass,
                        op.join(qc_dir, sample + "_raw_trimmed_contigs.fasta"),
                        config.assemble.left_trim,
                        config.assemble.right_trim,
                    )
                    final_contigs = apps.blast_results_filter(
                        blast_tabular,
                        raw_trimmed_contigs,
                        op.join(output_dir, sample + "_contigs.fasta"),
                        [
                            i.strip()
                            for i in config.assemble.contamination_terms.split(",")
                        ],
                        contaminated_contigs=op.join(
                            qc_dir, sample + "_contaminated_contigs.fasta"
                        ),
                        length=config.assemble.contamination_length,
                        identity=config.assemble.contamination_identity,
                    )
                    tmp_stats = fastx.fasta_stats(final_contigs)
                    # run_stats['contamination_databases'] = ";".join(
                    #     [
                    #         os.path.basename(i)
                    #         for i in config.assemble.blast_db.split(",")
                    #     ]
                    # )
                    # run_stats['contaminated_contigs'] = run_stats[
                    #     'length_passing_contigs_count'
                    # ] - tmp_stats[
                    #     2
                    # ]
                    # run_stats[
                    #     'contamination_terms'
                    # ] = '"%s"' % config.assemble.contamination_terms
                    # run_stats[
                    #     'contamination_alignment_length'
                    # ] = config.assemble.contamination_length
                    # run_stats[
                    #     'contamination_identity_threshold'
                    # ] = config.assemble.contamination_identity
                    # BLAST has filtered everything
                    if fastx.read_count(final_contigs) == 0:
                        stop_processing(
                            "no contigs survived blast results filtering",
                            run_stats,
                            run_stats_file,
                        )
                # or just trim the contigs by length
                else:
                    final_contigs = fastx.trim_fastx(
                        l_pass,
                        op.join(output_dir, sample + "_contigs.fasta"),
                        config.assemble.left_trim,
                        config.assemble.right_trim,
                    )
                stats = fastx.fasta_stats(final_contigs)
                # FIXME
                if stats[0] < 20000:
                    # run_stats['final_contigs_count'] = 0
                    run_stats["final_assembly_length"] = "NA"
                    run_stats["max_contig_length"] = 0
                    run_stats["gc_content"] = "NA"
                    # FIXME
                    stop_processing(
                        "assembled length less than 20kbp threshold",
                        run_stats,
                        run_stats_file,
                    )
                    os.remove(final_contigs)
                else:
                    # run_stats['final_contigs_count'] = stats[2]
                    run_stats["final_assembly_length"] = stats[0]
                    run_stats["max_contig_length"] = stats[1]
                    run_stats["gc_content"] = stats[3]
                # if run_stats['final_contigs_count'] > 0:
                if stats[2] > 0:
                    # completeness, number_unique_markers, number_multi_copy, taxonomy_contained, taxonomy_sister_lineage
                    checkm_vals = apps.run_checkm(
                        final_contigs, checkm_dir, config.assemble.cores
                    )
                    run_stats["checkM_estimated_completeness"] = checkm_vals[0]
                    # run_stats['unique_marker_genes'] = checkm_vals[1]
                    # run_stats['number_multi_copy'] = checkm_vals[2]
                    # run_stats['checkM_classification'] = ";".join(
                    #     [checkm_vals[3], checkm_vals[4]]
                    # )
                    # functional annotation on final contigs
                    prokka_files = apps.run_prokka(
                        final_contigs,
                        prokka_dir,
                        sample,
                        proteins=config.assemble.prokka_proteins,
                        protein_out=op.join(
                            swissprot_dir, sample + "_prokka-swissprot.tsv"
                        ),
                        cores=config.assemble.cores,
                    )

                    prokka_merged_proteins = op.join(
                        swissprot_dir, sample + "_prokka-swissprot.tsv"
                    )
                    if utils.file_exists(prokka_merged_proteins):
                        cds_stats = apps.parse_prokka_output(prokka_merged_proteins)
                        run_stats["total_CDS_count"] = cds_stats["count"]
                        run_stats["hypothetical_cds_fraction"] = cds_stats[
                            "hypothetical_fraction"
                        ]
                        run_stats["average_cds_length"] = cds_stats["average_length"]
                    run_stats["number_multi_copy"] = checkm_vals[2]
                    run_stats["checkM_classification"] = ";".join(
                        [checkm_vals[3], checkm_vals[4]]
                    )
                    if with_interproscan:
                        apps.run_interproscan(
                            final_contigs,
                            op.join(interproscan_dir, sample + "_interproscan.tsv"),
                            cores=config.assemble.cores,
                        )
                    if (
                        config.assemble.ssu_blast_db
                        and config.assemble.ssu_blast_map
                        and config.assemble.ssu_blast_tre
                    ):
                        ssu_tax = classifier.classify_by_ssu(
                            final_contigs,
                            config.assemble.ssu_blast_db,
                            config.assemble.ssu_blast_map,
                            config.assemble.ssu_blast_tre,
                            op.join(ssu_dir, sample + "_SSU_blast.tsv"),
                            op.join(ssu_dir, sample + "_SSU.fasta"),
                            op.join(ssu_dir, sample + "_SSU.tsv"),
                            min_score=100,
                            top_fraction=0.98,
                            min_length=ssu_min_length,
                            threads=config.assemble.cores,
                        )
                        if isinstance(ssu_tax, six.string_types):
                            run_stats["SSU_classification_1"] = ssu_tax
                            # run_stats['SSU_contig_1'] = "NA"
                        else:
                            for i, (name, length, annotation) in enumerate(
                                ssu_tax, start=1
                            ):
                                run_stats["SSU_classification_%d" % i] = annotation
                                # run_stats['SSU_contig_%d' % i] = "%s (%d bp)" % (
                                # name, length
                                # )
                # run tetramer PCA
                # if config.assemble.pca_script and run_stats['final_contigs_count'] > 1:
                if config.assemble.pca_script and stats[2] > 1:
                    pca_status = apps.tetramer_pca(
                        final_contigs,
                        pca_dir,
                        config.assemble.pca_script,
                        config.assemble.pca_opts,
                        config.assemble.cores,
                    )
                    if not pca_status:
                        run_stats["notes"] = "Tetramer PCA failed"
            else:
                run_stats["notes"] = "no contigs passed length filter"
        else:
            run_stats["notes"] = "assembly failed"
    if "notes" not in run_stats:
        run_stats["notes"] = ""
    print_stats(run_stats_file, run_stats)
    log.info("Assembly of %s is complete." % sample)


def make_archive(tar, file_tuples, overwrite=False):
    """
    tar - name of archive file
    file_tuples - list of (input_path, output_path) tuples
    overwrite - clobber existing tars
    """
    log = logging.getLogger(__name__)
    if op.exists(tar):
        if op.getsize(tar) == 0 or overwrite:
            os.remove(tar)
        else:
            log.info("%s already exists." % tar)
            return tar

    utils.safe_makedir(op.dirname(tar))
    with tarfile.open(tar, "w:gz") as tf:
        for fin, fout in file_tuples:
            if not op.exists(fin) or op.getsize(fin) == 0:
                log.warn("Skipping missing file %s of archive %s" % (fin, tar))
            else:
                tf.add(fin, arcname=fout)
    return tar


def process_sample(sample_meta, input_dir, output_dir, overwrite):
    """
    sample_meta - (customer id, run id, sample name)
    input_dir
    output_dir
    overwrite
    """
    log = logging.getLogger(__name__)
    customer, run_id, sample = sample_meta
    customer = customer.strip("/")
    # assert run_id.count("_") >= 3
    log.info("Processing sample %s of %s" % (sample, run_id))
    files = [
        (
            op.join(input_dir, run_id, sample, sample + "_WGS_QC"),
            op.join(sample, sample + "_WGS_QC"),
        ),
        (
            op.join(input_dir, run_id, sample, sample + "_functional_annotation"),
            op.join(sample, sample + "_functional_annotation"),
        ),
        (
            op.join(input_dir, run_id, sample, sample + "_assembly_info.csv"),
            op.join(sample, sample + "_assembly_info.csv"),
        ),
        (
            op.join(input_dir, run_id, sample, sample + "_contigs.fasta"),
            op.join(sample, sample + "_contigs.fasta"),
        ),
        (
            op.join(
                input_dir,
                run_id,
                sample,
                sample + "_WGS_reads",
                sample + "_pe.fastq.gz",
            ),
            op.join(sample, sample + "_WGS_reads", sample + "_pe.fastq.gz"),
        ),
    ]
    if output_dir.startswith("remote:"):
        with utils.tmp_dir() as tdir:
            dst = "{output_dir}/{customer}/{run_id}/{sample}.tar.gz".format(
                output_dir=output_dir.rstrip("/"),
                customer=customer,
                run_id=run_id,
                sample=sample,
            )
            tar = make_archive(
                op.join(tdir, run_id, customer, sample + ".tar.gz"), files, overwrite
            )
            if utils.cp(tar, dst):
                log.info("archive uploaded")
            else:
                log.error("failed to upload to remote {dst}".format(dst=dst))
    else:
        tar = make_archive(
            op.join(output_dir, run_id, customer, sample + ".tar.gz"), files, overwrite
        )
        log.info("archive created for %s" % sample)
    return tar


@cli.command("deliverables", short_help="create archives from results")
@click.argument("csvfile", type=click.Path(exists=True))
@click.option("--cores", type=int)
@click.option("--overwrite", is_flag=True, help="overwrite existing archives")
@click_config.wrap(module=config, sections=["deliverables", "shared"])
def scgc_deliverables(csvfile, cores, overwrite):
    """
    Takes CSV file with customer, runid, sampleid and creates archives
    in the deliverables folder.

    Setting deliverables to a remote location will trigger an upload, e.g.

    \b
        deliverables: remote:scgc_drive/deliverables/
    """
    log = utils.logger(log_name="Deliverables")
    if not cores:
        cores = config.deliverables.cores
    with open(csvfile, "rU") as fh:
        csvreader = csv.reader(fh)
        samples_meta = [i for i in csvreader]
    log.info("The input file includes %d samples" % len(samples_meta))
    p = multiprocessing.Pool(cores)
    archives = parmap.map(
        process_sample,
        samples_meta,
        config.shared.results,
        config.shared.deliverables,
        overwrite,
        pool=p,
    )
    log.info("Successfully created %d archives" % len(archives))
    out_dirs = [op.dirname(i) for i in archives]
    out_dirs = set(out_dirs)
    log.info("It's recommended that destination directories exist prior to uploading.")
    log.info("To share deliverables, upload the following:")
    for d in out_dirs:
        log.info("rclone sync -v %s remote:scgc_drive/deliverables/etc." % d)


def files_to_df(files):
    df = None
    for f in files:
        if df is None:
            df = pandas.read_csv(f)
            continue

        tdf = pandas.read_csv(f)
        df = pandas.concat([df, tdf])
        del tdf
    return df


@cli.command(
    "compile-stats", short_help="create data table for assembly stats across run IDs"
)
@click.argument("runs", nargs=-1)
@click.option(
    "--out-dir",
    help="override config output directory; prefix path before plate or run ID",
)
@click.option(
    "--out-file", default=None, help="if specified, STDOUT is redirected into this file"
)
@click_config.wrap(module=config, sections=["shared"])
def scgc_compile_stats(runs, out_dir, out_file):
    """
    Create a data table given a run ID or multiple run IDs.
    """
    log = utils.logger(log_name="Stats")
    # stats files from the assembly pipeline
    stats_files = []
    for run in runs:
        if out_dir:
            p = op.join(out_dir, run)
        else:
            p = op.join(config.shared.results, run)
        log.info("Checking %s for stats files." % run)
        if op.exists(p):
            stats_files.extend(glob(op.join(p, "*", "*_*_info.csv")))
        else:
            log.info("Skipping %s as it does not exist." % run)
    if len(stats_files) == 0:
        log.error("No stats files were found.")
        sys.exit(1)
    log.info("Found %d total files." % len(stats_files))
    # take header with most values
    cols = []
    for f in stats_files:
        with open(f) as fh:
            h = fh.readline()
            c = h.strip().split(",")
            if len(c) > len(cols):
                cols = c
    df = files_to_df(stats_files)
    df.sort_values(by=["wgs_run_id", "well"]).to_csv(
        sys.stdout if not out_file else out_file,
        na_rep="NA",
        index=False,
        quoting=csv.QUOTE_NONNUMERIC,
        columns=cols,
    )


@cli.command("coassemble-sample", short_help="coassemble a sample across multiple runs")
@click.argument("output")
@click.argument("samples", nargs=-1)
@click.option(
    "--concatenated-prefix",
    default=None,
    help="optional prefix for concatenated R1 and R2 across runs; should be everything up to _R1.fastq.gz",
)
@click.option(
    "--coassembly-id",
    default="coassembly",
    show_default=True,
    help="affects `scgc assemble` output location",
)
@click.option(
    "--with-interproscan",
    is_flag=True,
    help="run interproscan across genes after assembly",
)
@click_config.wrap(module=config, sections=["assemble", "shared"])
def scgc_coassemble(
    output, samples, concatenated_prefix, coassembly_id, with_interproscan
):
    """
    Samples are defined as run_id:sample_id pairs on the command line and more
    than one is required.
    """
    if len(samples) < 2:
        sys.exit("Specify more than one sample.")
    log = utils.logger(log_name="coassemble")
    r1_paths = []
    r2_paths = []
    for sample in sorted(samples):
        run_id, sample_id = sample.split(":")
        r1 = "{results}/{run}/{sample}/{sample}_WGS_reads/{sample}_trimmed_R1.fastq.gz".format(
            results=config.shared.results,
            run=run_id,
            sample=sample_id,
        )
        if not op.exists(r1):
            log.critical("%s does not exist. Exiting." % r1)
            sys.exit(1)
        r2 = r1.replace("_R1.fastq.gz", "_R2.fastq.gz")
        if not op.exists(r2):
            log.critical("%s does not exist. Exiting." % r2)
            sys.exit(1)
        r1_paths.append(r1)
        r2_paths.append(r2)
    log.info("Using:\n%s" % "\n".join(r1_paths + r2_paths))
    if concatenated_prefix:
        prefix_dir = os.path.dirname(concatenated_prefix)
        utils.safe_makedir(prefix_dir)
        with open(os.path.join(prefix_dir, "info.txt"), "w") as fh:
            print(*samples, sep="\n", file=fh)
        result_r1 = os.path.join("%s_R1.fastq.gz" % concatenated_prefix)
        result_r2 = os.path.join("%s_R2.fastq.gz" % concatenated_prefix)
    else:
        utils.safe_makedir(output)
        with open(os.path.join(output, "info.txt"), "w") as fh:
            print(*samples, sep="\n", file=fh)
        result_r1 = os.path.join(output, "%s_R1.fastq.gz" % os.path.basename(output))
        result_r2 = os.path.join(output, "%s_R2.fastq.gz" % os.path.basename(output))
    log.info("Writing:\n%s\n%s" % (result_r1, result_r2))
    if not os.path.exists(result_r1):
        utils.run("cat %s > %s" % (" ".join(r1_paths), result_r1))
    if not os.path.exists(result_r2):
        utils.run("cat %s > %s" % (" ".join(r2_paths), result_r2))
    utils.run(
        "scgc assemble %s %s %s --output=%s"
        % (
            "--with-interproscan" if with_interproscan else "",
            result_r1,
            coassembly_id,
            output,
        )
    )


@cli.command("join", short_help="cleanup and join PE reads")
@click.argument("r1", type=click.Path(exists=True))
@click.argument("run_id")
@click_config.wrap(module=config, sections=["join", "shared"])
def scgc_join(r1, run_id):
    log = utils.logger(log_name="Join")
    r1 = op.abspath(r1)
    r2 = r1.replace("_R1", "_R2")
    if not op.exists(r2):
        stop_processing("File Not Found: %s" % r2, exit_code=1)
    sample = op.basename(r1).partition("_")[0]
    out_dir = op.join(config.shared.results, run_id, sample)
    utils.safe_makedir(out_dir)
    job_log = op.join(out_dir, "%s_join_info.csv" % sample)
    job_stats = OrderedDict({"sample": sample})
    job_stats["run_id"] = run_id
    job_stats["raw_read_count"] = fastx.read_count(r1)
    current_read_count = job_stats["raw_read_count"]
    if current_read_count < 200:
        stop_processing("too few starting reads", job_stats, job_log)
    qc_dir = utils.safe_makedir(op.join(out_dir, sample + "_QC"))
    reads_dir = utils.safe_makedir(op.join(out_dir, sample + "_reads"))
    blast_dir = op.join(qc_dir, sample + "_joined_reads_blastn")
    if not config.join.skip_qc:
        fastqc = apps.run_fastqc(
            [r1, r2], op.join(qc_dir, sample + "_fastqc"), config.join.cores
        )
    if config.join.trim_opts:
        out_files = apps.trimmomatic(
            [r1, r2],
            [
                op.join(reads_dir, sample + "_trimmed_R1.fastq.gz"),
                op.join(reads_dir, sample + "_orphan_R1.fastq.gz"),
                op.join(reads_dir, sample + "_trimmed_R2.fastq.gz"),
                op.join(reads_dir, sample + "_orphan_R2.fastq.gz"),
            ],
            config.join.trim_opts,
            config.join.cores,
        )
        job_stats["trimmer"] = apps.trimmomatic_version()
        job_stats["trim_parameters"] = '"%s"' % config.join.trim_opts
        job_stats["trimmed_read_count"] = current_read_count = fastx.read_count(
            out_files[0]
        )
        next_r1 = out_files[0]
        next_r2 = out_files[2]
    else:
        next_r1 = r1
        next_r2 = r2
    if not current_read_count:
        stop_processing("no reads survived trimming", job_stats, job_log)
    pe_reads, complexity_read_count = fastx.complexity_filter(
        next_r1,
        next_r2,
        op.join(reads_dir, sample + "_compf_pe.fastq.gz"),
        config.join.complexity_threshold,
        config.join.cores,
    )
    job_stats["complexity_filter_threshold"] = "%0.02f%%" % (
        config.join.complexity_threshold * 100
    )
    job_stats["passed_complexity_filtered"] = current_read_count = complexity_read_count
    if not current_read_count:
        stop_processing("no reads survived complexity filter", job_stats, job_log)
    if config.join.references and len(list(config.join.references.keys())) > 0:
        job_stats["contamination_identity_threshold"] = "%0.02f%%" % (
            100 - (100 * config.assemble.reference_threshold)
        )
        for i, (ref, meta) in enumerate(config.join.references.items()):
            if i > 0 and not current_read_count:
                stop_processing(
                    "all reads were filtered out as contamination", job_stats, job_log
                )
            if meta["save_filtered"]:
                parts = op.basename(pe_reads).split(".")
                # should we incorporate reference name into the pe reads file?
                hits_file = ".".join(
                    ["%s/%s_%s" % (op.dirname(pe_reads), parts[0], ref)] + parts[1:]
                )
                pe_reads, hits_file = apps.reference_filter(
                    pe_reads,
                    meta["prefix"],
                    op.join(reads_dir, sample + "_contf_pe.fastq.gz"),
                    hits_file=hits_file,
                    threshold=config.join.reference_threshold,
                    cores=config.join.cores,
                )
            else:
                pe_reads = apps.reference_filter(
                    pe_reads,
                    meta["prefix"],
                    op.join(reads_dir, sample + "_contf_pe.fastq.gz"),
                    threshold=config.join.reference_threshold,
                    cores=config.join.cores,
                )
            job_stats["passed_%s_filter" % ref] = current_read_count = (
                fastx.read_count(pe_reads) / 2
            )
    if not current_read_count:
        stop_processing("no reads survived contamination filter", job_stats, job_log)
    # could encode params into file name to simplify parameter sweepss
    joined_reads = apps.run_bbmerge(
        pe_reads,
        op.join(reads_dir, sample + "_joined.fastq.gz"),
        k=40,
        extend2=60,
        iterations=5,
        loose="t",
        qtrim2="t",
    )
    job_stats["joined_reads"] = fastx.read_count(joined_reads)
    current_read_count = job_stats["joined_reads"]
    if not current_read_count:
        stop_processing("no reads were joined", job_stats, job_log)
    if "notes" not in job_stats:
        job_stats["notes"] = "Completed Successfully"
    print_stats(job_log, job_stats)


@cli.command("archive", short_help="create a BCL archive")
@click.argument("run_id")
@click.option("--overwrite", is_flag=True, help="overwrite existing archive")
@click_config.wrap(module=config, sections=["shared"])
def archive(run_id, overwrite):
    """Does not perform any integrity checks on the run folder.

    Overwrite to force a new archive to be built.
    """
    log = utils.logger(log_name="Archive")
    run_data = op.join(config.shared.data, run_id)
    archive = op.join(config.shared.archive, run_id + ".tar.gz")
    if op.exists(archive) and not overwrite:
        log.error(
            "An archive already exists for %s; use --overwrite to force rebuilding"
            % run_id
        )
        sys.exit(1)
    if not op.exists(run_data):
        log.error("%s does not exist" % run_data)
        sys.exit(1)
    with utils.file_transaction(archive) as tx:
        cmd = (
            "tar -zcf %s --exclude='*.fastq.gz' --exclude='*.count' --exclude='SAMPLES' --exclude='bcl2fastq.log' %s"
            % (tx, run_data)
        )
        utils.run(cmd, description="Archiving %s" % run_data)
    log.info("Archiving complete for %s" % run_id)


@cli.command("restore", short_help="restore existing BCL archive")
@click.argument("run_id")
@click.option("--overwrite", is_flag=True, help="write into existing directory")
@click_config.wrap(module=config, sections=["shared"])
def restore(run_id, overwrite):
    """If an archive exists for RUN_ID, extract it to shared data directory.

    Overwrite will extract data into an existing folder.
    """
    log = utils.logger(log_name="Restore")
    out_dir = op.join(config.shared.data, run_id)
    archive = op.join(config.shared.archive, run_id + ".tar.gz")
    if not op.exists(archive):
        log.error("No archive exists for %s; checked %s" % (run_id, archive))
        sys.exit(1)
    if op.exists(out_dir) and not overwrite:
        log.error("%s exists and we're not overwriting" % out_dir)
        sys.exit(1)
    cmd = "tar -zxf %s --directory %s" % (archive, config.shared.data)
    utils.run(cmd, description="Extracting %s" % archive)
    log.info("Archive restored for %s" % run_id)


@cli.command("remove-archived", short_help="remove directory if archive exists")
@click.argument("dir_loc")
@click.option("--dev", is_flag=True)
def scgc_remove_archived(dir_loc, dev):
    """removes directory if archive exists, archive location currently hard-coded.
    Args:
        dir_loc (path): path to directory to be deleted
    """

    arch = op.join("/mnt/scgc/simon/archive/", "{}.tar.gz".format(op.basename(dir_loc)))
    assert op.exists(
        arch
    ), "Archive does not exist for {}, make sure all files are archived before attempting to delete.".format(
        dir_loc
    )

    if op.exists(arch):
        if dev:
            print(
                "If dev had been 'False', would be DELETING {} because {} exists".format(
                    dir_loc, arch
                )
            )
        else:
            print("DELETING {} because {} exists".format(dir_loc, arch))
            shutil.rmtree(dir_loc)


@cli.command(
    "classify-seqs", short_help="classify short sequences using SCGC SAGs reference"
)
@click.argument("fastx", type=click.Path(exists=True, resolve_path=True))
@click.argument("db", type=click.Path(exists=True, resolve_path=True))
@click.argument("crestnodes", type=click.Path(exists=True, resolve_path=True))
@click.argument("ncbinodes", type=click.Path(exists=True, resolve_path=True))
@click.argument("outhits", type=click.Path(exists=False, resolve_path=True))
@click.argument("outtsv", type=click.Path(exists=False, resolve_path=True))
@click.option("--min-pid", type=float, default=90)
@click.option("--min-length", type=int, default=100)
@click.option("--top-fraction", type=float, default=0.90)
@click.option("--cores", type=int, default=1)
def run_classify_reads(
    fastx,
    db,
    crestnodes,
    ncbinodes,
    outhits,
    outtsv,
    min_pid,
    min_length,
    top_fraction,
    cores,
):
    """
    Run bbmap using the input FAST(A,Q) against an annotated FASTA database and
    determine the least common taxonomic ancestor among HSPs.
    """
    log = utils.logger(log_name="Classify-SAG")
    log.info("Alignment results are being written to: %s" % outhits)
    log.info("Annotations are being written to: %s" % outtsv)
    classifier.classify_reads(
        fastx,
        db,
        crestnodes,
        ncbinodes,
        outhits,
        outtsv,
        min_pid,
        min_length,
        top_fraction,
        cores,
    )


def samples_from_samplesheet(path):
    samples = []
    start = False
    with open(path, "rU") as fh:
        for line in fh:
            toks = line.strip().split(",")
            if not start:
                # table header processing
                if toks[0] == "Sample_ID":
                    start = True
            elif toks[0]:
                # convert underscores to dashes
                samples.append(toks[0].replace("_", "-").replace(".", "-"))
            else:
                break

    return samples


@cli.command(
    "easy", short_help="run bcl2fastq, assemblies, and stats for a sequence run"
)
@click.argument("run_id")
@click.option(
    "--conversion-threads",
    type=int,
    default=40,
    show_default=True,
    help="bcl2fastq processing threads",
)
@click.option("--subsample", type=int, help="number of reads")
@click.option("--queue", help="qsub queue")
@click.option(
    "--skip-assembly", is_flag=True, help="convert BCL to FASTQ and archive only"
)
@click_config.wrap(module=config, sections=["assemble", "shared"])
def scgc_easy(run_id, conversion_threads, subsample, queue, skip_assembly):
    """Process NextSeq runs through stats compilation. To simultaneously run
    sub-sampled sequences, use --subsample.
    """
    if queue:
        config.assemble.queue = queue
    log = utils.logger(log_name="Easy")
    pfx = op.join(config.shared.data, run_id)
    fq_pfx = op.join(pfx, "Data", "Intensities", "BaseCalls")
    samplesheet = op.join(pfx, "SampleSheet.csv")
    if not op.exists(samplesheet):
        log.error("No SampleSheet was found. Tried %s." % samplesheet)
        sys.exit(1)
    jobs = []
    samples = samples_from_samplesheet(samplesheet)
    if op.exists(op.join(pfx, "bcl2fastq.log")):
        log.info(
            "A log for .BCL conversion exists in the data directory, "
            "so we're skipping that step. To restart entirely, delete "
            "the following:"
        )
        log.info(op.join(pfx, "bcl2fastq.log"))
        # double checking that all fastqs are present
        # for sample in samples:
        #     for idx in ["R1", "R2"]:
        #         assert op.exists(
        #             op.join(
        #                 fq_pfx, "{sample}_{idx}.fastq.gz".format(sample=sample, idx=idx)
        #             )
        #         )
    else:
        cmd = (
            "bcl_to_fastq --determine --overwrite "
            "--processing {threads} "
            "--runfolder-dir {runfolder}"
        ).format(threads=conversion_threads, runfolder=pfx)
        jobs.append(
            utils.submit(
                cmd,
                config.assemble.bcl_queue,
                "bcl-conversion",
                conversion_threads,
                "160:00:00",
                config.assemble.qsub_mem,
                config.assemble.logs,
            )
        )
    conversion = "" if len(jobs) == 0 else jobs[0]
    if not op.exists(op.join(pfx, "{run}_multiqc_report.html".format(run=run_id))):
        report_jobs = []
        cmd = "interop_index-summary {run} --csv=1 > {pfx}/InterOp/index-summary.csv".format(
            run=run_id, pfx=pfx
        )
        report_jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name="bcl-idx-sum",
                cpus=1,
                time="1:00:00",
                log_dir=config.assemble.logs,
                mem="2G",
                depends=[conversion],
            )
        )
        cmd = "interop_summary {run} --csv=1 > {pfx}/InterOp/summary.csv".format(
            run=run_id, pfx=pfx
        )
        report_jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name="bcl-sum",
                cpus=1,
                time="1:00:00",
                mem="2G",
                log_dir=config.assemble.logs,
                depends=[conversion],
            )
        )
        cmd = (
            'multiqc --cl_config "max_table_rows: 2000" --module interop '
            "--no-data-dir --outdir {pfx} --interactive "
            "--title {run} {pfx}"
        ).format(pfx=pfx, run=run_id)
        utils.submit(
            cmd,
            queue=config.assemble.queue,
            job_name="multiqc",
            cpus=1,
            time="1:00:00",
            mem="1G",
            log_dir=config.assemble.logs,
            depends=report_jobs,
        )
    # create a bcl archive
    utils.submit(
        "scgc archive {run}".format(run=run_id),
        config.assemble.queue,
        "bcl-archive",
        config.assemble.qsub_cpus,
        config.assemble.time,
        "2G",
        config.assemble.logs,
        [conversion],
    )

    if skip_assembly:
        log.info(
            "All jobs have been submitted. Per sample assemblies have been skipped."
        )
        return

    for sample in samples:
        cmd = "scgc assemble {r1} {run_id}".format(
            r1=op.join(fq_pfx, "{sample}_R1.fastq.gz".format(sample=sample)),
            run_id=run_id,
        )
        jobs.append(
            utils.submit(
                cmd,
                config.assemble.queue,
                sample,
                config.assemble.qsub_cpus,
                config.assemble.time,
                config.assemble.qsub_mem,
                config.assemble.logs,
                [conversion],
            )
        )
        if subsample:
            cmd = ("scgc assemble --subsample {count} " "{r1} {run_id}").format(
                count=subsample,
                r1=op.join(fq_pfx, "{sample}_R1.fastq.gz".format(sample=sample)),
                run_id=run_id,
            )
            jobs.append(
                utils.submit(
                    cmd,
                    config.assemble.queue,
                    sample,
                    config.assemble.qsub_cpus,
                    config.assemble.time,
                    config.assemble.qsub_mem,
                    config.assemble.logs,
                    [conversion],
                )
            )
    cmd = ("scgc compile-stats --out-file {out_file} " "{run}").format(
        out_file=op.join(
            config.shared.results,
            run_id,
            "{run_id}_assembly_stats.csv".format(run_id=run_id),
        ),
        run=run_id,
    )
    utils.submit(
        cmd,
        config.assemble.queue,
        "compile-stats",
        1,
        "1:00:00",
        "2G",
        config.assemble.logs,
        jobs,
    )
    log.info("All jobs have been submitted. Check status using `qstat`.")


def compile_samples(path):
    samples = set()
    plates = list()
    for fastq_file in glob("%s/*_trimmed_R1.fastq.gz" % path):
        if "_R2" in fastq_file:
            continue
        sample = os.path.basename(fastq_file).partition("_")[0]
        plate = sample.rpartition("-")[0]
        samples.update([sample])
        plates.append(plate)
    return samples, plates


@cli.command(
    "coassemble-plate", short_help="coassemble a plate across multiple sequencing runs"
)
@click.argument("runs", nargs=-1)
@click.option("--with-interproscan", is_flag=True, help="run interproscan across genes")
@click.option("--outdir", help="alternate output location from the config")
@click_config.wrap(module=config, sections=["assemble", "shared", "coassemble"])
def submit_coassembly(runs, with_interproscan, outdir):
    """Specify the runs for LoCoS and the runs of the deep sequencing
    (order independent). Plate IDs are verified before submitting jobs.
    """
    # also verifies all samples of this run are from the same plate
    sample_defs = dict()
    all_plates = list()

    if not outdir:
        outdir = config.coassemble.outdir

    for run in runs:
        # peer into processed data for these reads
        samples, plates = compile_samples(
            os.path.join(config.shared.results, run, "*", "*_WGS_reads")
        )
        all_plates.extend(plates)
        click.echo(
            "Found %d samples in %s across %d plate(s)"
            % (len(samples), run, len(set(plates)))
        )
        sample_defs[run] = samples

    all_samples = Counter()
    for run, samples in six.iteritems(sample_defs):
        for sample in samples:
            all_samples.update([sample])

    intersection_set = []
    either_set = []
    for sample, count in six.iteritems(all_samples):
        if count > 1:
            intersection_set.append(sample)
        else:
            either_set.append(sample)

    click.echo("Preparing to submit %d jobs for coassembly" % len(intersection_set))
    click.echo("and %d jobs for re-assembly" % len(either_set))

    jobs = []

    # coassemblies
    for sample in intersection_set:

        plate = sample.rpartition("-")[0]

        sample_lst = []
        for run, samples in six.iteritems(sample_defs):
            if sample in samples:
                sample_lst.append("%s:%s" % (run, sample))
        sample_str = " ".join(sample_lst)
        prefix = os.path.join(outdir, plate, sample, "%s_WGS_reads" % sample, sample)

        cmd = (
            "scgc coassemble-sample {interproscan} "
            "--coassembly-id {plate} --concatenated-prefix {prefix} "
            "{outdir}/{plate}/{sample} "
            "{samples}"
        ).format(
            interproscan="--with-interproscan" if with_interproscan else "",
            plate=plate,
            prefix=prefix,
            outdir=outdir,
            sample=sample,
            samples=sample_str,
        )

        jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name=sample,
                cpus=config.assemble.qsub_cpus,
                time=config.assemble.time,
                mem=config.assemble.qsub_mem,
                log_dir=config.coassemble.logs,
            )
        )
        # click.echo("run: %s" % cmd)

    # assemblies
    for sample in either_set:

        plate = sample.rpartition("-")[0]

        # figure out which run this sample belongs to
        runid = ""
        for run, samples in six.iteritems(sample_defs):
            if sample in samples:
                runid = run
                # no need to continue checking
                break

        if not runid:
            sys.exit("Unable to determine Run ID for %s" % sample)

        cmd = (
            "scgc assemble {interproscan} " "--output {out_dir} {r1} " "{runid}"
        ).format(
            interproscan="--with-interproscan" if with_interproscan else "",
            out_dir=os.path.join(outdir, plate, sample),
            r1=os.path.join(
                config.shared.results,
                runid,
                "*",
                "*_WGS_reads",
                sample + "_trimmed_R1.fastq.gz",
            ),
            runid=runid,
        )
        jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name=sample,
                cpus=config.assemble.qsub_cpus,
                time=config.assemble.time,
                mem=config.assemble.qsub_mem,
                log_dir=config.assemble.logs,
            )
        )
        # click.echo("run: %s" % cmd)

    for plate in set(all_plates):

        cmd = (
            "scgc compile-stats --out-dir {outdir} "
            "--out-file {outdir}/{plate}_assembly_stats.csv "
            "{plate}"
        ).format(outdir=outdir, plate=plate)
        utils.submit(
            cmd,
            queue=config.assemble.queue,
            job_name="stats-%s" % plate,
            cpus=1,
            time="2:00:00",
            log_dir=config.assemble.logs,
            depends=jobs,
        )
        # click.echo("Stats: %s" % cmd)

    click.echo("All jobs submitted.")


@cli.command("join-all", short_help="run bcl2fastq then bbmerge across all samples")
@click.argument("run_id")
@click.option(
    "--conversion-threads",
    type=int,
    default=40,
    show_default=True,
    help="bcl2fastq processing threads",
)
@click.option("--queue", help="qsub queue")
@click_config.wrap(module=config, sections=["assemble", "shared", "join"])
def scgc_join_all(run_id, conversion_threads, queue):
    if queue:
        config.assemble.queue = queue
    log = utils.logger(log_name="join-all")
    pfx = op.join(config.shared.data, run_id)
    fq_pfx = op.join(pfx, "Data", "Intensities", "BaseCalls")
    samplesheet = op.join(pfx, "SampleSheet.csv")
    if not op.exists(samplesheet):
        log.error("No SampleSheet was found. Tried %s." % samplesheet)
        sys.exit(1)
    jobs = []
    samples = samples_from_samplesheet(samplesheet)
    if op.exists(op.join(pfx, "bcl2fastq.log")):
        log.info(
            "A log for .BCL conversion exists in the data directory, "
            "so we're skipping that step. To restart entirely, delete "
            "the following:"
        )
        log.info(op.join(pfx, "bcl2fastq.log"))
    else:
        cmd = (
            "bcl_to_fastq --determine --overwrite "
            "--processing {threads} "
            "--runfolder-dir {runfolder}"
        ).format(threads=conversion_threads, runfolder=pfx)
        jobs.append(
            utils.submit(
                cmd,
                config.assemble.bcl_queue,
                "bcl-conversion",
                conversion_threads,
                "160:00:00",
                config.assemble.qsub_mem,
                config.assemble.logs,
            )
        )
    conversion = "" if len(jobs) == 0 else jobs[0]
    if not op.exists(op.join(pfx, "{run}_multiqc_report.html".format(run=run_id))):
        report_jobs = []
        cmd = "interop_index-summary {run} --csv=1 > {pfx}/InterOp/index-summary.csv".format(
            run=run_id, pfx=pfx
        )
        report_jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name="bcl-idx-sum",
                cpus=1,
                time="1:00:00",
                log_dir=config.assemble.logs,
                mem="2G",
                depends=[conversion],
            )
        )
        cmd = "interop_summary {run} --csv=1 > {pfx}/InterOp/summary.csv".format(
            run=run_id, pfx=pfx
        )
        report_jobs.append(
            utils.submit(
                cmd,
                queue=config.assemble.queue,
                job_name="bcl-sum",
                cpus=1,
                time="1:00:00",
                mem="2G",
                log_dir=config.assemble.logs,
                depends=[conversion],
            )
        )
        cmd = (
            'multiqc --cl_config "max_table_rows: 2000" --module interop '
            "--no-data-dir --outdir {pfx} --interactive "
            "--title {run} {pfx}"
        ).format(pfx=pfx, run=run_id)
        utils.submit(
            cmd,
            queue=config.assemble.queue,
            job_name="multiqc",
            cpus=1,
            time="1:00:00",
            mem="1G",
            log_dir=config.assemble.logs,
            depends=report_jobs,
        )
    # create a bcl archive
    utils.submit(
        "scgc archive {run}".format(run=run_id),
        config.assemble.queue,
        "bcl-archive",
        config.assemble.qsub_cpus,
        config.assemble.time,
        "2G",
        config.assemble.logs,
        [conversion],
    )

    for sample in samples:
        cmd = "scgc join {r1} {run_id}".format(
            r1=op.join(fq_pfx, "{sample}_R1.fastq.gz".format(sample=sample)),
            run_id=run_id,
        )
        jobs.append(
            utils.submit(
                cmd,
                config.assemble.queue,
                sample,
                1,
                "40:00:00",
                config.assemble.qsub_mem,
                config.assemble.logs,
                [conversion],
            )
        )
    log.info("All jobs have been submitted. Check status using `qstat`.")


@cli.command(
    "complexity-filter", short_help="run nucleotide complexity filter on fastqs"
)
@click.argument("r1")
@click.argument("r2")
@click.argument("pe")
@click.option(
    "--threshold",
    default=0.05,
    type=float,
    help="nucleotide threshold",
)
@click.option(
    "--cores",
    default=1,
    type=int,
    help="cores to utilize",
)
def scgc_complexity_filter(r1, r2, pe, threshold=0.05, cores=1):
    fastx.complexity_filter(r1, r2, pe, threshold, cores)


if __name__ == "__main__":
    cli()
