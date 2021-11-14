from __future__ import print_function
import csv
import fileinput
import logging
import os
import os.path as op
import random
import re
import shutil
import six
import tempfile
from contextlib import contextmanager
from interlap import InterLap
from itertools import groupby
from toolshed import nopen, reader

# local imports
from .fastx import (
    length_sort,
    munge_header,
    tmp_split_reads,
    readfx,
    check_sync,
    print_fasta_record,
)
from .utils import (
    file_exists,
    file_transaction,
    run,
    safe_makedir,
    grouper,
    tmp_dir,
    gunzip_file,
    pigz_file,
    touch,
)


logger = logging.getLogger(__name__)


def index_bam(bam_file):
    """
    Build an index for a bam file.

    parameters
        bam_file : alignment file path

    returns
        index file name : string
    """
    bam_index = bam_file + ".bai"
    if not file_exists(bam_index):
        with file_transaction(bam_index) as tx_out_file:
            run("samtools index %s %s" % (bam, tx_out_file))
    return bam_index


def _remove_option(options, item, flag=False):
    """
    remove item from options. item is assumed to not be a flag, therefore
    two sequential args are removed from options.

    parameters
        options : list of args
        item : string to search for among options
        flag : whether for not item is boolean

    returns
        options : list
    """
    if item in options:
        x = options.index(item)
        options.pop(x)
        if not flag:
            options.pop(x)
    return options


def filter_options(options, predefined_options):
    """
    filter predefined options from user-specified options.

    parameters
        options : string or list of options for application
        predefined_options : list of tuples specifying option and whether or
            not the option is a boolean flag

    returns
        options : list
    """
    options = options.split() if isinstance(options, six.string_types) else options
    for option, flag in predefined_options:
        options = _remove_option(options, option, flag)
    return options


def run_fastqc(fastq, out_dir, cores=1):
    """
    runs fastqc on fastq or fastqs as a space-delimited single string.

    parameters
        fastq : single file path or list of file paths
        out_dir : directory to write output files
        cores : cpu cores to utilize

    returns
        output directory : string
    """
    if not op.exists(out_dir):
        safe_makedir(out_dir)
    if isinstance(fastq, six.string_types):
        fastq = [fastq]
    for fq in fastq:
        fname, ext = op.splitext(op.basename(fq))
        if ext == ".gz":
            # fastqc only strips ".fastq"; variants like .fq will remain
            tfname, ext = op.splitext(fname)
            if ext == ".fastq":
                fname = tfname
        fname += "_fastqc.zip"
        out_file = op.join(out_dir, fname)
        if file_exists(out_file):
            continue
        with file_transaction(out_file) as tx:
            run(
                "fastqc --outdir %s --noextract -f fastq -t %d -q %s"
                % (op.dirname(tx), cores, fq),
                description="Running FastQC",
            )
    return out_dir


def trimmomatic(fastq, out_file, options, cores=1):
    """
    runs trimmomatic and returns path of out_file. if your reads are paired-end,
    fastq should be a list of [R1 path, R2 path].

    parameters
        fastq : file path or list of R1, R2 file paths
        out_file : file path if single-end, list otherwise (trimmed_R1,
            trimmed_orphan_R1, trimmed_R2, trimmed_orphan_R2)
        options : trimmomatic options

    returns
        output files : list
    """
    predefined_options = [
        ("-threads", False),
        ("-trimlog", False),
        ("PE", True),
        ("SE", True),
    ]
    if isinstance(fastq, six.string_types):
        fastq = [fastq]
    if len(fastq) > 1:
        assert len(out_file) == 4
    if file_exists(out_file):
        return out_file
    options = filter_options(options, predefined_options)
    flag_options = []
    trimmers = []
    for option in options:
        if option.startswith("-"):
            flag_options.append(option)
        else:
            trimmers.append(option)
    flag_options.extend(["-threads", str(cores)])

    with file_transaction(out_file) as tx_out_file:
        if len(fastq) == 1:
            cmd = "trimmomatic.sh SE {opts} {fastq} {out} {trimmers}".format(
                opts=" ".join(flag_options),
                fastq=fastq[0],
                out=tx_out_file,
                trimmers=" ".join(trimmers),
            )
        else:
            cmd = "trimmomatic.sh PE {opts} {fastq} {out} {trimmers}".format(
                opts=" ".join(flag_options),
                fastq=" ".join(fastq),
                out=" ".join(tx_out_file),
                trimmers=" ".join(trimmers),
            )
        run(cmd, description="Trimming")
    return out_file


def trimmomatic_version():
    """returns the version string for Trimmomatic."""
    return "Trimmomatic v0.32"


def run_kmernorm(fastq, out_file, options, cores=1):
    """
    perform digital normalization using kmernorm. unzip input file if gzipped
    and gzip input file after kmernorm.

    parameters
        fastq : file path; gzipped input will be decompressed and recompressed
        out_file : file path; file ending with '.gz' will be compressed
        options : kmernorm options
        cores : cpu cores to utilize

    returns
        normalized file path and surviving read pairs : tuple (string, int)
    """
    if file_exists(out_file):
        return out_file

    gzip_result = True if out_file.endswith(".gz") else False
    out_file = out_file.rsplit(".gz", 1)[0]
    if fastq.endswith(".gz"):
        fastq = gunzip_file(fastq)
    with file_transaction(out_file) as tx:
        run(
            "kmernorm %s %s > %s" % (options, fastq, tx),
            description="Normalizing with kmernorm",
        )
    if gzip_result:
        out_file = pigz_file(out_file, cores)
    # compress input file regardless
    fastq = pigz_file(fastq, cores)
    return out_file


def kmernorm_version():
    """
    Executes `kmernorm` and parses output for version info.

    returns
        version : string
    """
    version = ""
    for line in run("kmernorm 2>&1", iterable=True):
        line = line.strip()
        # 'Version' is misspelled in the software.
        if line.startswith("Ver"):
            line = line.split()
            version = line[1]
            break
    return "kmernorm " + version


def spades(sample, fastq, out_file, options, cores=1):
    """
    runs spades assembler on interleaved, PE fastq.

    parameters
        sample : name of sample being processed; will be prepended to contig name
        fastq : file path
        out_file : file path of assembled contigs
        options : spades options
        cores : cpu cores to utilize

    returns
        assembled contigs file path
    """
    if file_exists(out_file):
        return out_file
    predefined_options = [
        ("-o", False),
        ("--pe1-12", False),
        ("--12", False),
        ("-t", False),
        ("--threads", False),
    ]
    options = filter_options(options, predefined_options)
    with file_transaction(out_file) as tx:
        tx_dir = op.dirname(tx)
        contigs = tx_dir + "/contigs.fasta"
        cmd = "spades.py --12 {fq} --threads {cores} -o {out} {options}".format(
            fq=fastq, cores=cores, out=tx_dir, options=" ".join(options)
        )
        try:
            run(cmd)
        except:
            return out_file

        # sort the contigs
        sorted_contigs = os.path.join(tx_dir, sample + "_all_sorted_contigs.fasta")
        sorted_contigs = length_sort(contigs, sorted_contigs)
        # prepend sample name to contig header
        renamed_contigs = op.join(tx_dir, sample + "_all_contigs.fasta")
        renamed_contigs = munge_header(
            sorted_contigs, renamed_contigs, sample, intent="prepend-and-split", sep="_"
        )

        # need to rename spades output to match out_file
        shutil.move(renamed_contigs, tx)

    return out_file


def spades_version():
    """
    Executes `spades.py` and parses output for version info.

    returns
        version : string
    """
    version = ""
    for line in run("spades.py 2>&1 | head -1", iterable=True):
        version = line.rstrip("\r\n")
        break
    return version


def parse_bcl2fastq_log(log):
    """
    parses bcl2fastq log generated from bcl2fastq.py.

    returns
        version and run parameters : tuple (string, string)
    """
    version = ""
    parameters = ""
    if file_exists(log):
        for i, line in enumerate(nopen(log)):
            if i < 5 and line.startswith("bcl2fastq"):
                version = line.strip("\r\n")
                continue
            if "Command-line invocation" in line:
                parameters = (
                    '"%s"' % line.strip("\r\n").rsplit(": bcl2fastq", 1)[1].strip()
                )
            if version and parameters:
                break
    version = version if version else "Unable to detect"
    parameters = parameters if parameters else "Unable to detect"
    return version, parameters


def bwa_mem(fastq, out_file, index, options, cores=1):
    """
    align reads using bwa mem.

    parameters
        fastq : path to reads
        out_file : path to aligned reads bam
        index : path to bwa index
        options : bwa mem options
        cores : int

    returns
        output file path : string
    """
    if file_exists(out_file):
        return out_file
    predefined_options = [("-t", False)]
    options = filter_options(options, predefined_options)
    logger.info("Mapping %s using bwa mem" % bam)

    # TODO bwa index...
    with file_transaction(out_file) as tx_out_file:
        cmd = (
            "bwa mem -t {cores} {options} {index} {fastq} | samtools view "
            "-ShuF4q2 - | samtools sort -o -m 8G - tmp > {result}"
        ).format(
            cores=cores,
            options=" ".join(options),
            index=index,
            fastq=fastq,
            result=tx_out_file,
        )
        run(cmd)
        index_bam(tx_out_file)

    return out_file


def blastn(fasta, out_file, blast_db, options, cores=1):
    """
    align sequences using blastn, creating blast archive format (ASN1).

    fasta : file path as string
    out_file : result file path with extension ASN1
    options : blastn options except for db, num_threads, query, out, and outfmt

    returns ASN1 result path
    """
    if file_exists(out_file):
        return out_file
    predefined_options = [
        ("-num_threads", False),
        ("-out", False),
        ("-query", False),
        ("-outfmt", False),
        ("-db", False),
    ]
    options = filter_options(options, predefined_options)
    logger.info("Aligning %s using blastn" % fasta)

    with file_transaction(out_file) as tx_out_file:
        cmd = (
            "blastn -db {db} -outfmt 11 {options} -num_threads {cores} "
            "-out {result} -query {fasta}"
        ).format(
            db=blast_db,
            options=" ".join(options),
            cores=cores,
            result=tx_out_file,
            fasta=fasta,
        )
        run(cmd)

    return out_file


def blastn_fastq(fastq, out_file, blast_db, options, cores=1):
    """Align FASTQ sequences using blastn, creating a blast ASN1 archive.

    bioawk -c fastx '{print ">"$name"\n"$seq}' AD-782-J14_R1.fastq.gz | blastn -db nt -outfmt 11 -num_threads 80

    Args:
        fastq (str): fastq file path
        out_file (str): out file path to ASN1 archive
        blast_db (str): path or name of blast db
        options (str): blast options as you define them on the command line
        cores (Optional[int]): number of threads used by blast

    Returns:
        str

    Note:
        Adds `bioawk` dependency that should be removed in the future.

    """
    if file_exists(out_file):
        return out_file
    predefined_options = [
        ("-num_threads", False),
        ("-out", False),
        ("-query", False),
        ("-outfmt", False),
        ("-db", False),
    ]
    options = filter_options(options, predefined_options)
    logger.info("Aligning %s using blastn" % fastq)

    with file_transaction(out_file) as tx_out_file:
        cmd = r"""bioawk -c fastx '{print ">"$name"\n"$seq}' """
        cmd += (
            "{fastq} | blastn -db {db} -outfmt 11 {options} "
            "-num_threads {cores} -out {result} "
        ).format(
            fastq=fastq,
            db=blast_db,
            options=" ".join(options),
            cores=cores,
            result=tx_out_file,
        )
        run(cmd)

    return out_file


def blast_formatter(archive, out_file, options, out_fmt=None):
    """"""
    if file_exists(out_file):
        return out_file
    # gzipped somewhere outside, but after this method and the pipeline
    # is being re-run
    if file_exists(out_file + ".gz"):
        return out_file + ".gz"

    predefined_options = [("-archive", False), ("-outfmt", False)]
    options = filter_options(options, predefined_options)

    logger.info("Converting %s to %s" % (archive, out_file))

    blast_header = {
        "qseqid": "Query Seq-id",
        "qgi": "Query GI",
        "qacc": "Query accesion",
        "qaccver": "Query accesion.version",
        "qlen": "Query sequence length",
        "sseqid": "Subject Seq-id",
        "sallseqid": "All subject Seq-id(s)",
        "sgi": "Subject GI",
        "sallgi": "All subject GIs",
        "sacc": "Subject accession",
        "saccver": "Subject accession.version",
        "sallacc": "All subject accessions",
        "slen": "Subject sequence length",
        "qstart": "Start of alignment in query",
        "qend": "End of alignment in query",
        "sstart": "Start of alignment in subject",
        "send": "End of alignment in subject",
        "qseq": "Aligned part of query sequence",
        "sseq": "Aligned part of subject sequence",
        "evalue": "Expect value",
        "bitscore": "Bit score",
        "score": "Raw score",
        "length": "Alignment length",
        "pident": "Percentage of identical matches",
        "nident": "Number of identical matches",
        "mismatch": "Number of mismatches",
        "positive": "Number of positive-scoring matches",
        "gapopen": "Number of gap openings",
        "gaps": "Total number of gaps",
        "ppos": "Percentage of positive-scoring matches",
        "frames": "Query and subject frames",
        "qframe": "Query frame",
        "sframe": "Subject frame",
        "btop": "Blast traceback operations (BTOP)",
        "staxids": "unique Subject Taxonomy ID(s)",
        "sscinames": "unique Subject Scientific Name(s)",
        "scomnames": "unique Subject Common Name(s)",
        "sblastnames": "unique Subject Blast Name(s)",
        "sskingdoms": "unique Subject Super Kingdom(s)",
        "stitle": "Subject Title",
        "salltitles": "All Subject Title(s)",
        "sstrand": "Subject Strand",
        "qcovs": "Query Coverage Per Subject",
        "qcovhsp": "Query Coverage Per HSP",
    }

    with file_transaction(out_file) as tx_out_file:
        if out_fmt:
            n = out_fmt[0]
            if n == "6" or n == "10":
                hdr = [blast_header[k] for k in out_fmt[1:].split()]
                if n == "6":
                    sep = "\t"
                else:
                    sep = ","
                with open(tx_out_file, "w") as fh:
                    print(*hdr, sep=sep, file=fh)

            cmd = (
                "blast_formatter -archive {archive} {options} "
                "-outfmt '{fmt}' >> {result}"
            ).format(
                archive=archive,
                options=" ".join(options),
                fmt=out_fmt,
                result=tx_out_file,
            )
        else:
            cmd = (
                "blast_formatter -archive {archive} {options} " ">> {result}"
            ).format(archive=archive, options=" ".join(options), result=tx_out_file)
        run(cmd)
    return out_file


def tetramer_pca(fasta, out_dir, script_path, options, cores=1):
    sample_id = os.path.basename(fasta).rpartition(".")[0]
    # out_dir/sample_id + -<window size>-<step size>-PC.pdf
    out_files = [
        os.path.join(out_dir, sample_id + "-outliers.fasta"),
        os.path.join(out_dir, sample_id + "-outliers.xml"),
        os.path.join(out_dir, sample_id + "-tetramer-counts.csv"),
        os.path.join(out_dir, sample_id + "-tetramer-fail.csv"),
        os.path.join(out_dir, sample_id + "-tetramer-loading.csv"),
        os.path.join(out_dir, sample_id + "-tetramer-PC.csv"),
    ]

    if file_exists(out_files):
        return out_dir

    predefined_options = [
        ("--input", False),
        ("--output_dir", False),
        ("--num_threads", False),
    ]
    options = filter_options(options, predefined_options)

    logger.info("Running Tetramer PCA on %s" % fasta)

    # out_files = []
    # with file_transaction(out_files) as tx_out_files:
    cmd = (
        "Rscript --vanilla {script} --input {fasta} "
        "--output_dir {out_dir} --num_threads {cores} "
        "{options}"
    ).format(
        script=script_path,
        fasta=fasta,
        out_dir=out_dir,
        cores=cores,
        options=" ".join(options),
    )
    try:
        run(cmd, description="Running Tetramer PCA")
    except:
        return False
    return out_dir


@contextmanager
def bwa_index(reference, options=None):
    """Builds an index using `bwa index`.

    Args:
        reference (str): file path of reference fasta
        options (Optional[str]): options passed to bwa index, eg. "-a is"

    Yields:
        str: file path of reference as it's used as the prefix in `bwa index`
    """
    ref = op.abspath(reference)
    idx_files = [ref + x for x in [".amb", ".ann", ".bwt", ".pac", ".sa"]]
    if not file_exists(idx_files):
        logger.debug("Creating BWA index for %s" % ref)
        cmd = "bwa index {options} {ref}".format(
            options=options if options else "", ref=ref
        )
        run(cmd, "Building BWA index")
    yield reference


def _aln(ref, fastq, tmp="/tmp", threads=1, threshold=0.05):
    sai = os.path.join(tmp, "%09d.sai" % random.randrange(0, 1e10))
    with file_transaction(sai) as tx:
        cmd = ("bwa aln -n {threshold} -t {threads} " "{ref} {fastq} > {tx}").format(
            **locals()
        )
        run(cmd)
    return sai


def _sampe(ref, reads, tmp="/tmp", threads=1, threshold=0.05):
    r1, r2 = tmp_split_reads(reads, tmp)
    with bwa_index(ref) as bwaidx:
        r1_sai = _aln(bwaidx, r1, tmp, threads, threshold)
        r2_sai = _aln(bwaidx, r2, tmp, threads, threshold)
        sampe = (
            "bwa sampe {ref} {r1_sai} {r2_sai} {r1} {r2} " "| samtools view -SF0x0004 -"
        ).format(ref=bwaidx, r1_sai=r1_sai, r2_sai=r2_sai, r1=r1, r2=r2)
        for a in run(sampe, iterable=True):
            yield a


def reference_filter(fastq, fasta, out_file, hits_file=None, threshold=0.05, cores=1):
    """Align FASTQ file against a reference FASTA file generating a filtered
    FASTQ file. Optionally, if a file path is specified for alignment hits,
    reads are removed from FASTQ and written to hits.

    Args:
        fastq (str): path to interleaved fastq file
        fasta (str): path to reference fasta file
        out_file (str): path of output FASTQ with hits removed
        hits_file (Optional[str]): path of output FASTQ containing contamination hits only
        threshold (Optional[float]): allowable mismatch threshold of mapped reads
        cores (Optional[int]): bwa processing threads

    Returns:
        str or list: output file path or output file path and hits file path
    """
    if not hits_file and file_exists(out_file):
        return out_file
    # okay to have a 0 byte hits_file
    if hits_file and os.path.exists(hits_file) and file_exists(out_file):
        return out_file, hits_file

    logger.info("Filtering %s based on %s" % (fastq, fasta))
    if hits_file:
        out_files = [out_file, hits_file]
    else:
        out_files = [out_file]

    # file_transaction will yield a list when hits_file is used
    with file_transaction(out_files) as tx_files:
        hits = set()
        observed = 0
        survived = 0

        # this makes things easier if no hits_file is specified
        if isinstance(tx_files, six.string_types):
            tx_files = [tx_files]
        txdir = os.path.dirname(tx_files[0])

        for hit in _sampe(fasta, fastq, txdir, cores, threshold):
            hits.add(hit.partition("\t")[0])

        if len(hits) == 0:
            # still want to have an intermediate file here
            logger.info("No observed contamination.")
            # need to add .gz on output file if input file also has it
            shutil.copy(fastq, tx_files[0])
            if hits_file:
                touch(tx_files[1])
                return out_files
            else:
                return out_files[0]

        if hits_file:
            with open(tx_files[0], "w") as fq_fh, open(tx_files[1], "w") as ht_fh:
                for (n1, s1, q1), (n2, s2, q2) in grouper(2, readfx(fastq)):
                    check_sync(n1, n2)
                    observed += 1
                    # bwa strips read number from name so this works on R1 and R2
                    read_name = n1.partition("/")[0]
                    if read_name in hits:
                        print(
                            "@" + n1,
                            s1,
                            "+",
                            q1,
                            "@" + n2,
                            s2,
                            "+",
                            q2,
                            sep="\n",
                            file=ht_fh,
                        )
                    else:
                        survived += 1
                        print(
                            "@" + n1,
                            s1,
                            "+",
                            q1,
                            "@" + n2,
                            s2,
                            "+",
                            q2,
                            sep="\n",
                            file=fq_fh,
                        )
        else:
            with open(tx_files[0], "w") as fq_fh:
                for (n1, s1, q1), (n2, s2, q2) in grouper(2, readfx(fastq)):
                    check_sync(n1, n2)
                    observed += 1
                    # bwa strips read number from name so this works on R1 and R2
                    read_name = n1.partition("/")[0]
                    if read_name in hits:
                        continue
                    survived += 1
                    print(
                        "@" + n1,
                        s1,
                        "+",
                        q1,
                        "@" + n2,
                        s2,
                        "+",
                        q2,
                        sep="\n",
                        file=fq_fh,
                    )

        logger.info("Pairs observed: %d" % observed)
        logger.info("Pairs survived: %d" % survived)

        if tx_files[0].endswith(".gz"):
            pigz_file(tx_files[0], cores)
        if hits_file and tx_files[1].endswith(".gz"):
            pigz_file(tx_files[1], cores)

        count_file = tx_files[0].rsplit(".gz")[0] + ".count"
        with open(count_file, "w") as fh:
            print(survived * 2, file=fh)

    if hits_file:
        return out_files
    else:
        return out_file


def overlap_distance(coords):
    """
    >>> coords = [(1,3),(2,6),(8,9)]
    >>> overlap_distance(coords)
    8
    """
    overlap = InterLap()
    joined_intervals = InterLap()
    coords.sort(key=lambda x: x[0])
    overlap.add(coords)
    seen = set()
    for iset in coords:
        if iset in seen:
            continue
        seen.add(iset)
        start = iset[0]
        end = iset[1]
        for jset in overlap.find(iset):
            if jset in seen:
                continue
            seen.add(jset)
            start = min(start, jset[0])
            end = max([end, jset[1]])
        joined_intervals.add((start, end))
    return sum([j - i + 1 for (i, j) in joined_intervals])


def blast_results_filter(
    blast_tsv,
    fastx_file,
    out_file,
    terms,
    contaminated_contigs=None,
    length=1000,
    identity=95.0,
):
    """Filter FASTX based on intervals matching terms within BLAST results.

    Args:
        blast_tsv (str or list): tsv of BLAST results. See note
        fastx_file (str): file path to existing file
        out_file (str): file path to be written
        terms (str or list): search terms to be considered a hit, e.g. ["Homo sapiens genomic DNA"]
        contaminated_contigs (str): path to file to store contigs marked as contaminants
        length (Optional[int]): required match length to be considered a hit
        identity (Optional[float]): required matched identity to be filtered

    Returns:
        str

    Note:
        blast tsv requires a header with at least the following fields:
            Query Seq-id
            Percentage of identical matches
            Alignment length
            All Subject Title(s)
    """
    if file_exists(out_file):
        return out_file
    if file_exists(out_file + ".gz"):
        return out_file + ".gz"

    # _csv.Error: field larger than field limit (131072)
    import sys
    import csv

    max_int = sys.maxsize
    decrement = True

    while decrement:
        # decrease the max_int value by factor 10
        # as long as the OverflowError occurs.
        decrement = False
        try:
            csv.field_size_limit(max_int)
        except OverflowError:
            max_int = int(max_int / 10)
            decrement = True

    # start the filter
    if isinstance(blast_tsv, six.string_types):
        blast_tsv = [blast_tsv]
    for btsv in blast_tsv:
        if not file_exists(btsv):
            logger.critical("%s not found." % btsv)
            return ""
    if not file_exists(fastx_file):
        logger.critical("%s not found." % fastx_file)
        return ""

    logger.info("Filtering %s based on BLAST results." % fastx_file)
    if isinstance(terms, six.string_types):
        terms = [terms.lower()]
    else:
        terms = [t.lower() for t in terms]
    # pull out IDs of contaminated entries from blast results
    contaminated = set()
    for btsv in blast_tsv:
        for qseq_id, alignments in groupby(
            reader(btsv, header=True, sep="\t"), key=lambda x: x["Query Seq-id"]
        ):
            # get the coordinates of passing hits
            coords = set()
            for alignment in alignments:
                if float(
                    alignment["Percentage of identical matches"]
                ) > identity and any(
                    t in alignment["All Subject Title(s)"].lower() for t in terms
                ):
                    coords.add(
                        (
                            int(alignment["Start of alignment in query"]),
                            int(alignment["End of alignment in query"]),
                        )
                    )
            # sum potentially overlapping coordinates
            if coords and overlap_distance(list(coords)) > length:
                contaminated.add(qseq_id)

    # writes empty file when every contig is contaminated
    # filter the contig into out_file
    if contaminated_contigs:
        contaminated_contigs_fh = open(contaminated_contigs, "w")
    with file_transaction(out_file) as tx:
        with open(tx, "w") as fh:
            for name, seq, qual in readfx(fastx_file):
                if name in contaminated:
                    print_fasta_record(name, seq, contaminated_contigs_fh)
                else:
                    if qual is None:
                        print_fasta_record(name, seq, fh)
                    else:
                        print("@" + name, seq, "+", qual, sep="\n", file=fh)
    if contaminated_contigs:
        contaminated_contigs_fh.close()
    return out_file


def run_checkm(fasta, out_dir, cores):
    logger.info("Running checkm on %s and writing to %s" % (fasta, out_dir))

    prefix = op.basename(fasta).split(".")[0]
    fasta = op.abspath(fasta)
    completeness = 0.0
    number_unique_markers = 0
    number_multi_copy = 0
    taxonomy_contained = "NA"
    taxonomy_sister_lineage = "NA"

    # we want the fasta in a directory by itself
    with tmp_dir() as bin_path:
        tmp_fasta = op.join(bin_path, op.basename(fasta))
        shutil.copy(fasta, tmp_fasta)

        plot_path = op.join(out_dir, "plots")

        # lineage workflow
        if not file_exists(op.join(out_dir, "completeness.tsv")):
            # clear any existing output directory and create
            shutil.rmtree(out_dir, ignore_errors=True)
            safe_makedir(out_dir)
            # run lineage workflow
            logger.info("Running lineage workflow on %s" % fasta)
            run(
                (
                    "checkm lineage_wf -f {outdir}/completeness.tsv --tab_table "
                    "-q -x fasta -t {cores} {binpath} {outdir}"
                ).format(outdir=out_dir, cores=cores, binpath=bin_path)
            )
        try:
            for l in reader(out_dir + "/completeness.tsv", header=True, sep="\t"):
                completeness = l["Completeness"]
                break
        except IOError:
            logger.warning("Lineage workflow failed for %s" % fasta)
            pass

        # tree (has better output than workflow)
        if not file_exists(op.join(out_dir, "taxonomy.tsv")):
            logger.info("Getting taxonomy")
            # checkm tree -t 30 -x fasta --tmpdir /dev/shm fastas checkm_o
            # checkm tree_qa --tab_table -o 2 checkm_o > taxonomy.tsv
            # Bin Id	# unique markers (of 43)	# multi-copy	Insertion branch UID	Taxonomy (contained)	Taxonomy (sister lineage)	GC	Genome size (Mbp)	Gene counCoding density	Translation table	# descendant genomes	Lineage: GC mean	Lineage: GC std	Lineage: genome size (Mbp) mean	Lineage: genome size (Mbp) std	Lineage: gene count mean	Lineage: gene count std
            # AG-323-G20_contigs	1	0	UID2169	k__Bacteria;p__Cyanobacteria;c__Chroococcales;o__Chroococcales;f__Cyanobium	f__Synechococcus;g__Synechococcus;s__	43.97247688	0.398356	453	0.773782747091	11	2	53.2604384148	0.813097897058	2.656719	0.049971	2998.5	47.5
            run(
                (
                    "checkm tree_qa --tab_table -o 2 {outdir} "
                    "-f {outdir}/taxonomy.tsv"
                ).format(outdir=out_dir)
            )
        try:
            for l in reader("%s/taxonomy.tsv" % out_dir, header=True, sep="\t"):
                number_unique_markers = l["# unique markers (of 43)"]
                number_multi_copy = l["# multi-copy"]
                taxonomy_contained = l["Taxonomy (contained)"]
                taxonomy_sister_lineage = l["Taxonomy (sister lineage)"]
                break
        except IOError:
            logger.warning("Failed to retrieve taxonomy info")
            pass

        # try to make these plots:
        try:
            # bin_qa_plot
            if not file_exists(op.join(plot_path, "bin_qa_plot.pdf")):
                logger.info("Running bin_qa_plot on %s" % fasta)
                run(
                    (
                        "checkm bin_qa_plot -x fasta -q --image_type pdf {outdir} "
                        "{binpath} {plotpath}"
                    ).format(outdir=out_dir, binpath=bin_path, plotpath=plot_path)
                )
            # marker_plot
            if not file_exists(op.join(plot_path, prefix + ".marker_pos_plot.pdf")):
                logger.info("Running marker_plot on %s" % fasta)
                run(
                    (
                        "checkm marker_plot -x fasta -q --image_type pdf {outdir} "
                        "{binpath} {plotpath}"
                    ).format(outdir=out_dir, binpath=bin_path, plotpath=plot_path)
                )
            # dist_plot
            if not file_exists(op.join(plot_path, prefix + ".ref_dist_plots.pdf")):
                logger.info("Running dist_plot on %s" % fasta)
                tns = os.path.join(out_dir, "tetranucleotide_signatures.tsv")
                run(
                    "checkm tetra -q -t {cores} {fa} {tns}".format(
                        cores=cores, fa=fasta, tns=tns
                    )
                )
                run(
                    (
                        "checkm dist_plot -q -x fasta --image_type pdf {outdir} "
                        "{binpath} {plotpath} {tns} 95"
                    ).format(
                        outdir=out_dir, binpath=bin_path, plotpath=plot_path, tns=tns
                    )
                )
        # subprocess.CalledProcessError
        except:
            pass
    return (
        completeness,
        number_unique_markers,
        number_multi_copy,
        taxonomy_contained,
        taxonomy_sister_lineage,
    )


def classify_fasta(
    fasta,
    blastdb,
    rrna_file,
    min_score=150,
    num_alignments=10,
    min_rrna_length=75,
    threads=8,
):
    cmd = (
        "blastn -task megablast -query {q} -db {db} "
        "-num_alignments {na} -outfmt {fmt} -out {o} "
        "-num_threads {nt}"
    )
    with tmp_dir() as tmp:
        blast_hits = True
        xml = os.path.join(tmp, op.basename(fasta) + ".xml")
        run(
            cmd.format(
                q=fasta, db=blastdb, na=num_alignments, fmt=5, o=xml, nt=threads
            ),
            description="BLAST against %s" % blastdb,
        )
        crest_dir = os.path.join(tmp, op.basename(fasta) + ".crest")
        # should include a DB option for CREST call...
        try:
            run(
                "classify {xml} -o {cd} --minscore={ms}".format(
                    xml=xml, cd=crest_dir, ms=min_score
                )
            )
        except:
            blast_hits = False
            pass

        # skip if the other blast search yielded nothing; determined by classification failure
        if blast_hits:
            with open(rrna_file, "w") as rrna_fh:
                for qseq_id, alignments in groupby(
                    run(
                        cmd.format(
                            q=fasta,
                            db=blastdb,
                            na=num_alignments,
                            fmt='"6 std qseq"',
                            o="-",
                            nt=threads,
                        ),
                        iterable=True,
                    ),
                    key=lambda x: x.strip().split("\t")[0],
                ):
                    for alignment in alignments:
                        # take best hit only per contig; no gaps in seq
                        alignment = alignment.strip().split("\t")
                        if not int(alignment[3]) >= min_rrna_length:
                            continue
                        print_fasta_record(qseq_id, alignment[-1], rrna_fh)
                        break

        # Level	Taxonpath	Taxon	xxxAG-459-P16
        # base	root;No hits	No hits	30355
        # base	root;Cellular organisms	Cellular organisms	0
        # domain	root;Cellular organisms;Bacteria	Bacteria	0
        # phylum	root;Cellular organisms;Bacteria;Cyanobacteria	Cyanobacteria	0

        taxonpath = "root;No hits"
        count = 0
        if file_exists(op.join(crest_dir, "All_Assignments.tsv")):
            with open(op.join(crest_dir, "All_Assignments.tsv")) as fh:
                for line in fh:
                    toks = line.strip().split("\t")
                    if "root;No hits" in toks[1] or "Taxonpath" in toks[1]:
                        continue
                    if int(toks[3]) > count:
                        count = int(toks[3])
                        taxonpath = toks[1]
        return taxonpath


def run_seqtk_sample(fastqs, out_files, n, seed=37):
    """Subsample incoming paired-end fastqs to `n` reads (serially).

    Args:
        fastqs (list): list of fastq paths
        out_files (list): list of output fastq paths; output files are always gzipped
        n (int): number of subsampled reads
        seed (int): for random selection of reads

    Returns:
        list: subsampled r1, r2 file paths
    """
    if file_exists(out_files):
        return out_files

    logger.info("Subsampling to %d reads" % n)
    with file_transaction(out_files) as tx:
        cmd = "seqtk sample -s {seed} {fastq} {number} | gzip > {out}".format(
            seed=seed, fastq=fastqs[0], number=n, out=tx[0]
        )
        run(cmd)
        cmd = "seqtk sample -s {seed} {fastq} {number} | gzip > {out}".format(
            seed=seed, fastq=fastqs[1], number=n, out=tx[1]
        )
        run(cmd)
    return out_files


def run_flash(
    fastq, out_file, mismatch_density=0.05, min_overlap=35, max_overlap=150, cores=1
):
    """Joins interleaved FASTQ file using `flash`.

    Args:
        fastq (str): file path to fastq
        out_file (str): path of desired gzip compressed fastq
        mismatch_density (Optional[float]): mismatch density of overlapping region
        min_overlap (Optional[int]): minimum expected read overlap
        max_overlap (Optional[int]): maximum expected read overlap
        cores (Optional[int]): threads allocated to flash

    Returns:
        str
    """
    # in case we switch what the current config looks like
    # predefined_options = [('--interleaved-input', True),
    #                       ('--interleaved', True), ('-I', True),
    #                       ('-Ti', True), ('--tab-delimited-input', True),
    #                       ('-To', True), ('--tab-delimited-output', True),
    #                       ('-o', False), ('--output-prefix', False),
    #                       ('-d', False), ('--output-directory', False),
    #                       ('-c', True), ('--to-stdout', True),
    #                       ('-z', True), ('--compress', True),
    #                       ('--compress-prog', True),
    #                       ('--compress-prog-args', True), ('--suffix', True),
    #                       ('--output-suffix', True), ('-t', False),
    #                       ('--threads', False), ('-m', False),
    #                       ('--min-overlap', False), ('-M', False),
    #                       ('--max-overlap', False), ('-x', False),
    #                       ('--max-mismatch-density', False)]
    # options = filter_options(options, predefined_options)

    if file_exists(out_file):
        return out_file
    if not out_file.endswith(".gz"):
        out_file = out_file + ".gz"
        if file_exists(out_file):
            return out_file

    logger.info("Joining %s using flash" % fastq)

    with file_transaction(out_file) as tx:
        cmd = (
            "flash --interleaved-input -x {mismatch} -m {min} "
            "-M {max} -t {threads} --to-stdout {fastq} "
            "| gzip > {tx}"
        ).format(
            mismatch=mismatch_density,
            min=min_overlap,
            max=max_overlap,
            threads=cores,
            fastq=fastq,
            tx=tx,
        )
        run(cmd, description="Joining reads with flash")
    return out_file


def flash_version():
    """Get the version from `flash --version`.

    Returns:
        str
    """
    for line in run("flash --version", iterable=True):
        return line.strip()


def run_prokka(fasta, out_dir, prefix, proteins=None, protein_out=None, cores=1):
    """prefix is used for the file name and the locus tag

    outputs: .err .faa .ffn .fna .fsa .gbk .gff .log .sqn .tbl .tsv .txt
    """

    prokka_exts = [
        ".err",
        ".faa",
        ".ffn",
        ".fsa",
        ".gff",
        ".log",
        ".tbl",
        ".tsv",
        ".txt",
        ".fna",
    ]
    out_files = [op.join(out_dir, prefix + x) for x in prokka_exts]
    if proteins:
        if not protein_out:
            protein_out = op.join(out_dir, prefix + "_prokka-swissprot.tsv")
        out_files.append(protein_out)
    if file_exists(out_files):
        logger.info("Prokka is complete for %s" % prefix)
        return out_files

    # with file_transaction(out_files) as tx:
    cmd = (
        "prokka --force --outdir {out} --prefix {prefix} --locustag {prefix}"
        " --cpus {cores} {fasta}"
    ).format(out=out_dir, prefix=prefix, cores=cores, fasta=fasta)
    prokka_gff = op.join(out_dir, prefix + ".gff")
    try:
        run(cmd, description="Annotation with Prokka")
    except:
        logger.warning("Annotation with Prokka of %s failed" % prefix)
        pass

    if proteins:
        out_dir = op.dirname(op.abspath(protein_out))
        prot_files = [op.join(out_dir, prefix + "-proteins" + x) for x in prokka_exts]
        cmd = (
            "prokka --force --outdir {out} --prefix {prefix}-proteins --locustag {prefix}"
            " --cpus {cores} --rawproduct --proteins {proteins}"
            " {fasta}"
        ).format(
            out=out_dir, prefix=prefix, cores=cores, proteins=proteins, fasta=fasta
        )

        try:
            run(cmd, description="Secondary annotation with Prokka")

            gff = op.join(out_dir, prefix + "-proteins.gff")

            locus_tag_re = re.compile(r"locus_tag=(.*?)(?:;|$)")
            ec_re = re.compile(r"eC_number=(.*?)(?:;|$)")
            gene_re = re.compile(r"gene=(.*?)(?:;|$)")
            product_re = re.compile(r"product=(.*?)(?:;|$)")

            prokka_annotation = dict()
            # needs a gff generator
            with open(prokka_gff) as gff_fh:
                for line in gff_fh:
                    if line.startswith("##FASTA"):
                        break
                    if line.startswith("#"):
                        continue
                    toks = line.strip().split("\t")
                    if not toks[2] == "CDS":
                        continue
                    try:
                        locus_tag = locus_tag_re.findall(toks[-1])[0]
                    except IndexError:
                        locus_tag = ""
                    if not locus_tag:
                        logger.critical(
                            "Unable to locate a locus tag in [%s]" % toks[-1]
                        )
                        sys.exit(1)
                    try:
                        gene = gene_re.findall(toks[-1])[0]
                    except IndexError:
                        gene = ""
                    try:
                        ec_number = ec_re.findall(toks[-1])[0].replace("%2", ",")
                    except IndexError:
                        ec_number = ""
                    try:
                        product = product_re.findall(toks[-1])[0].replace("%2", ",")
                    except IndexError:
                        product = ""
                    prokka_annotation[toks[0] + "-" + toks[3] + "-" + toks[4]] = {
                        "contig_id": toks[0],
                        "gene": gene,
                        "EC_number": ec_number,
                        "product": product,
                    }

            with open(gff) as gff_fh, open(protein_out, "w") as output:
                # print the header into the output file
                print(
                    "contig_id",
                    "locus_tag",
                    "ftype",
                    "start",
                    "stop",
                    "strand",
                    "prokka_gene",
                    "prokka_EC_number",
                    "prokka_product",
                    "swissprot_gene",
                    "swissprot_EC_number",
                    "swissprot_product",
                    "swissprot_eggNOG",
                    "swissprot_KO",
                    "swissprot_Pfam",
                    "swissprot_CAZy",
                    "swissprot_TIGRFAMs",
                    sep="\t",
                    file=output,
                )

                for line in gff_fh:
                    if line.startswith("##FASTA"):
                        break
                    if line.startswith("#"):
                        continue
                    toks = line.strip().split("\t")
                    if not toks[2] == "CDS":
                        continue
                    try:
                        locus_tag = locus_tag_re.findall(toks[-1])[0]
                    except IndexError:
                        locus_tag = ""
                    if not locus_tag:
                        logger.critical(
                            "Unable to locate a locus tag in [%s]" % toks[-1]
                        )
                        sys.exit(1)
                    try:
                        gene = gene_re.findall(toks[-1])[0]
                    except IndexError:
                        gene = ""
                    try:
                        ec_number = ec_re.findall(toks[-1])[0].replace("%2", ",")
                    except IndexError:
                        ec_number = ""
                    try:
                        product = product_re.findall(toks[-1])[0]
                    except IndexError:
                        product = ""

                    product = product.replace("%2", ",")
                    additional_annotation = dict()
                    if "^^" in product:
                        for tokens in product.split("^^"):
                            items = tokens.split("::")
                            additional_annotation[items[0]] = items[1]
                    else:
                        additional_annotation = {
                            "product": product,
                            "eggNOG": "",
                            "KO": "",
                            "Pfam": "",
                            "CAZy": "",
                            "TIGRFAMs": "",
                        }

                    try:
                        prokka_entry = prokka_annotation[
                            toks[0] + "-" + toks[3] + "-" + toks[4]
                        ]
                    except KeyError:
                        # lines from the prokka annotation will be missing
                        logger.warning(
                            "Prokka annotation missing for %s-%s-%s"
                            % (toks[0], toks[3], toks[4])
                        )
                        prokka_entry = {"gene": "", "EC_number": "", "product": ""}

                    print(
                        toks[0],
                        locus_tag,
                        toks[2],
                        toks[3],
                        toks[4],
                        toks[6],
                        prokka_entry["gene"],
                        prokka_entry["EC_number"],
                        prokka_entry["product"],
                        gene,
                        ec_number,
                        additional_annotation["product"],
                        additional_annotation["eggNOG"],
                        additional_annotation["KO"],
                        additional_annotation["Pfam"],
                        additional_annotation["CAZy"],
                        additional_annotation["TIGRFAMs"],
                        sep="\t",
                        file=output,
                    )

            # delete all of the other files
            for f in prot_files:
                os.remove(f)
        except:
            logger.warning("Annotation with Prokka+Proteins of %s failed" % prefix)
            pass

    return out_files


def run_interproscan(fasta, out_file, tmp_dir=None, cores=1):
    if file_exists(out_file):
        return out_file

    if not tmp_dir:
        tmp_dir = tempfile.gettempdir()

    with file_transaction(out_file) as tx:
        cmd = (
            "interproscan.sh --tempdir {tmp_dir} "
            "--input {fasta} --formats tsv "
            "--pathways --iprlookup --goterms "
            "--cpu {cores} --outfile {out_file}"
        ).format(tmp_dir=tmp_dir, fasta=fasta, cores=cores, out_file=tx)
        try:
            run(cmd, description="Running InterProScan")
            if file_exists(tx):
                header = [
                    "Protein Accession",
                    "Sequence MD5 digest",
                    "Sequence Length",
                    "Analysis",
                    "Signature Accession",
                    "Signature Description",
                    "Start",
                    "Stop",
                    "Score",
                    "Status",
                    "Date",
                    "InterPro accession",
                    "InterPro description",
                    "GO annotations",
                    "Pathways annotations",
                ]
                for line in fileinput.input([tx], inplace=True):
                    if fileinput.isfirstline():
                        print(*header, sep="\t")
                    print(line.strip())
        except:
            logger.warning("Annotation with InterProScan on %s failed" % fasta)
            return False

    return out_file


def parse_prokka_output(path):
    data = dict(count="NA", hypothetical_fraction="NA", average_length="NA")
    if os.path.exists(path):
        with open(path) as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            total = 0.0
            hypothetical = 0.0
            lengths = []
            for row in reader:
                total += 1
                if (
                    row["prokka_product"] == "hypothetical protein"
                    and row["swissprot_product"] == "hypothetical protein"
                ):
                    hypothetical += 1
                lengths.append(int(row["stop"]) - int(row["start"]))
            data["count"] = total
            data["hypothetical_fraction"] = hypothetical / total
            data["average_length"] = sum(lengths) / float(len(lengths))
    return data


def run_bbmerge(pe_fq, out_file, k=40, extend2=60, iterations=5, loose="t", qtrim2="t"):

    if file_exists(out_file):
        return out_file
    if not out_file.endswith(".gz"):
        out_file = out_file + ".gz"
        if file_exists(out_file):
            return out_file

    with file_transaction(out_file) as tx:
        cmd = (
            "bbmerge.sh -Xmx40G k={k} extend2={extend2} "
            "iterations={iterations} loose={loose} qtrim2={qtrim2} "
            "in={pe_fq} out={tx}"
        ).format(
            k=k,
            extend2=extend2,
            iterations=iterations,
            loose=loose,
            qtrim2=qtrim2,
            pe_fq=pe_fq,
            tx=tx,
        )
        run(cmd, description="Joining PE reads with bbmerge")
    return out_file
