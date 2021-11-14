from __future__ import print_function
import logging
import multiprocessing
import operator
import os
import sys
from itertools import groupby
from pysam import FastxFile
from toolshed import nopen

try:
    from itertools import izip as zip
except ImportError:
    pass

from .utils import file_exists, file_transaction, multiprocess, cp, grouper, run, pigz_file


logger = logging.getLogger(__name__)


def readfx(fastx):
    if not file_exists(fastx):
        logger.critical("File Not Found: %s" % fastx)
        raise IOError(2, "No such file:", fastx)

    fx = ""
    try:
        fx = FastxFile(fastx)
        for f in fx:
            yield f.name, f.sequence, f.quality
    finally:
        if fx:
            fx.close()


def read_fasta(fh):
    """FASTA iterator where name isn't split by space."""
    for header, group in groupby(fh, lambda line: line[0] == '>'):
        if header:
            line = next(group)
            name = line[1:].strip()
        else:
            seq = ''.join(line.strip() for line in group)
            yield name, seq


def complexity_filter_sequence(seq, threshold=0.05, alphabet='ACGT'):
    """
    filter sequence based on a given expectation of bases above an observed
    threshold.

    parameters
        seq : sequence string
        threshold : minimal observed composition for each character in alphabet
        alphabet : verified sequence characters above threshold

    returns
        boolean
    """
    count_threshold = len(seq) * threshold
    for elem in alphabet:
        if seq.count(elem) < count_threshold:
            return False
    return True


def complexity_filter_pe_record(complextuple, threshold, alphabet):
    """
    mapped function to filter 2 records at once.

    parameters
        n1, s1, q1 : tuple of first record's name, sequence, and quality values
        n2, s2, q2 : tuple of second record
        threshold : minimal observed fraction for each character in alphabet
        alphabet : verified sequence characters above threshold

    returns
        full records string on success. empty string on fail.
    """
    ((n1, s1, q1), (n2, s2, q2)) = complextuple
    try:
        assert n1 == n2
    except AssertionError:
        assert n1[:-2] == n2[:-2], "Pairing failed due to sync: %s %s" % (n1, n2)

    pass1 = complexity_filter_sequence(s1, threshold, alphabet)
    pass2 = complexity_filter_sequence(s2, threshold, alphabet)

    if pass1 and pass2:
        if not n1.endswith('/1'): n1 += '/1'
        if not n2.endswith('/2'): n2 += '/2'
        records = "@%s\n%s\n+\n%s\n@%s\n%s\n+\n%s" % (n1, s1, q1, n2, s2, q2)
        return records
    return ""


def complexity_filter(r1, r2, out_file, threshold=0.05, cores=1):
    """
    filters fastq based on read composition above threshold.

    parameters
        r1 : R1 fastq
        r2 : R2 fastq
        out_file : interleaved fastq file path
        threshold : fraction of required bases (ACTG) per read sequence
        cores : number of cores

    returns
        a tuple (out_file: string, surviving read pairs: int)
    """
    if file_exists(out_file):
        return out_file, read_count(out_file) / 2

    gzip = False
    if out_file.endswith(".gz"):
        gzip = True
        out_file = out_file.rpartition('.gz')[0]

    count_file = out_file + '.count'
    total_pairs = 0
    filtered_pairs = 0
    p = multiprocessing.Pool(cores)

    logger.info("Complexity filtering. Threshold is %0.02f" % threshold)

    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            for results in multiprocess(complexity_filter_pe_record,
                    zip(readfx(r1), readfx(r2)), threshold, 'ACGT', pool=p):
                for record in results:
                    total_pairs += 1
                    if not record:
                        filtered_pairs += 1
                        continue
                    print(record, file=out_handle)
    surviving_pairs = total_pairs - filtered_pairs
    if gzip:
        # returns with .gz added to out_file
        out_file = pigz_file(out_file, cores)

    logger.info("Filtering complete. Observed pairs: %d. Total surviving: %d" % (total_pairs, surviving_pairs))
    with open(count_file, 'w') as out_handle:
        print(surviving_pairs * 2, file=out_handle)

    return out_file, surviving_pairs


def read_count(fname):
    """Count the number of reads and write metadata .count file.

    Args:
        fname (str): fastq or fasta file path

    Returns:
        int
    """
    if not file_exists(fname):
        return 0
    total = 0
    fq = True
    for name, seq, qual in readfx(fname):
        if not qual:
            fq = False
        break

    if fname.endswith("gz"):
        count_file = fname.rsplit(".gz", 1)[0] + ".count"
        cat = "gzip -d -c"
    else:
        count_file = fname + ".count"
        cat = "cat"

    if file_exists(count_file):
        with open(count_file) as fh:
            for line in fh:
                total = int(line.strip())
                return total

    if not fq:
        cmd = '%s %s | grep -c "^>"' % (cat, fname)
    else:
        cmd = '%s %s | wc -l' % (cat, fname)

    for line in run(cmd, description="Counting reads", iterable=True):
        total = int(line.rstrip())
        if fq:
            assert total % 4 == 0, "Multi-line or invalid FASTQ"
            total = int(total / 4)

    with open(count_file, 'w') as fh:
        print(total, file=fh)

    return total


def print_fasta_record(name, seq, out_handle=sys.stdout, wrap=80):
    """
    print fasta record and wraps the sequence line.

    parameters
        name : name or header for fasta entry
        seq : sequence
        out_handle : open file handle in which to write or stdout
        wrap : line width of fasta sequence
    """
    print('>', name, sep='', file=out_handle)
    if wrap:
        for i in range(0, len(seq), wrap):
            print(seq[i:i + wrap], file=out_handle)
    else:
        print(seq, file=out_handle)


def format_fasta_record(name, seq, wrap=100):
    """Fasta __str__ method.

    Convert fasta name and sequence into wrapped fasta format.

    Args:
        name (str): name of the record
        seq (str): sequence of the record
        wrap (int): length of sequence per line

    Yields:
        tuple: name, sequence

    >>> format_fasta_record("seq1", "ACTG")
    ">seq1\nACTG"
    """
    record = ">" + name + "\n"
    if wrap:
        for i in range(0, len(seq), wrap):
            record += seq[i:i+wrap] + "\n"
    else:
        record += seq + "\n"
    return record.strip()


def munge_header(fastx, out_file, text, intent='prepend', sep='_'):
    """
    Prepend or append text to name field of fastx using sep.

    parameters
        fastx : fasta or fastq
        out_file : result file
        text : string to append to name field
        intent : 'prepend' or 'append' action
        sep : separator to use between text and existing name

    returns
        output file name : string
    """
    if file_exists(out_file):
        return out_file

    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            for name, seq, qual in readfx(fastx):
                if intent == 'prepend':
                    name = "%s%s%s" % (text, sep, name)
                elif intent == 'prepend-and-split':
                    # update the fasta headers from
                    # AG-325-P19_NODE_1_length_12099_cov_58.823
                    # to
                    # AG-325-P19_NODE_1
                    name = name.partition('_length')[0]
                    name = "%s%s%s" % (text, sep, name)
                else:
                    name = "%s%s%s" % (name, sep, text)

                # fastq
                if qual:
                    print("@" + name, seq, "+", qual, sep="\n", file=out_handle)
                # fasta
                else:
                    print_fasta_record(name, seq, out_handle)
    return out_file


def length_filter(fasta, pass_file, fail_file, operation='gt', length=2000, wrap=60):
    """
    filter fasta sequences by length. pass_file meets criteria of operation.

    parameters
        fasta : fasta sequence file
        pass_file : sequences that pass criteria
        fail_file : sequences that do not pass criteria
        operation : 'gt' or 'lt'; keep sequences of length greater than or
            less than respectively
        length : length threshold
        wrap : line width of fasta sequence

    returns
        pass_file and fail_file : tuple
    """
    if file_exists([pass_file, fail_file]):
        return pass_file, fail_file

    logger.info('Filtering %s by length %d' % (fasta, length))

    op_func = operator.gt if operation == 'gt' else operator.lt
    with file_transaction([pass_file, fail_file]) as tx_out_files:
        with open(tx_out_files[0], 'w') as passfh, open(tx_out_files[1], 'w') as failfh:
            for name, seq, qual in readfx(fasta):
                if op_func(len(seq), length):
                    print_fasta_record(name, seq, passfh, wrap)
                else:
                    print_fasta_record(name, seq, failfh, wrap)
    return pass_file, fail_file


def bedtools_genome(fasta, out_file):
    with open(out_file, 'w') as fh:
        for name, seq, qual in readfx(fasta):
            print(name, len(seq), sep="\t", file=fh)


def fasta_stats(fasta):
    """
    calculate basic stats from a fasta file.

    parameters
        fasta : fasta file path

    returns
        total bases, max contig size, contig count, gc percent : tuple
    """
    logger.info('Calculating stats for %s' % fasta)

    if read_count(fasta) == 0:
        return 0, 0, 0, 0

    total_contigs = 0
    contig_sizes = []
    gc_total = 0

    for i, (name, seq, qual) in enumerate(readfx(fasta), start=1):
        contig_sizes.append(len(seq))
        gc_total += seq.count('G') + seq.count('C')
        total_contigs = i

    if total_contigs > 0:
        contig_sizes.sort(reverse=True)
        max_contig_size = contig_sizes[0]
        total_bases = sum(contig_sizes)
        gc_percent = float(gc_total) / total_bases * 100

    else:
        total_bases = 0
        max_contig_size = 0
        gc_percent = 0

    return total_bases, max_contig_size, total_contigs, gc_percent


def length_sort(fasta, out_file):
    """
    sort a fasta file by sequence length.

    parameters
        fasta : fasta file path
        out_file : output file path

    returns
        output file path : string
    """
    if file_exists(out_file):
        return out_file

    logger.info('Sorting %s sequences by length' % fasta)

    records = [(name, seq) for name, seq, qual in readfx(fasta)]
    records.sort(key=lambda x: len(x[1]), reverse=True)

    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            for name, seq in records:
                print_fasta_record(name, seq, out_handle)
    return out_file


def remove_seq_wraps(fasta, out_file):
    """
    Remove line wraps in the sequence string of a fasta.

    parameters
        fasta : fasta file path
        out_file : output file

    returns
         output file path : string
    """
    if file_exists(out_file):
        return out_file

    logger.info("Removing line wraps in %s" % fasta)

    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            for name, seq, qual in readfx(fasta):
                print(">%s\n%s" % (name, seq), file=out_handle)

    return out_file


def calc_skew_and_content(seq, window_size=500):
    """
    sliding window implementation of gc_skew and gc_content.

    parameters
        seq : sequence string to analyze
        window_size : length of string to analyze at a time

    returns
        mid point location of window, skew, gc content : tuple

    """
    half_window = window_size / 2
    seq = seq.upper()
    seq_len = len(seq)
    if not seq_len >= window_size:
        logger.warn("Sequence too short: %s" % seq)
        yield None, None, None

    # could likely be improved by using numpy.chararray
    for start in range(0, seq_len - window_size + 1):
        stop = start + window_size
        mid = stop - half_window
        s = seq[start:stop]

        g = s.count('G')
        c = s.count('C')
        gc = g + c

        content = float(gc) / window_size
        skew = 0 if gc == 0 else (g - c) / float(g + c)
        yield mid, skew, content


def gc_skew_and_content(fasta, out_file, window_size=500):
    """
    Calculate GC content and skew for a fasta file over a sliding window of
    each sequence.

    parameters
        fasta : fasta file path
        out_file : output file path
        window_size : sliding window size on which to analyze sequence

    returns
        output file path : string
    """
    if file_exists(out_file):
        return out_file

    header = ["SEQUENCE_NAME", "POSITION", "SKEW", "CONTENT"]
    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            print(*header, sep="\t", file=out_handle)
            for name, seq, qual in readfx(fasta):
                for point, skew, content in calc_skew_and_content(seq, window_size):
                    if not point:
                        continue
                    print(name, point, skew, content, sep="\t", file=out_handle)

    return out_file


def trim(s, left, right):
    """
    trim('AAAACCCCCAAAA', 4, 4)
    'CCCCC'
    trim('AAAACCCCCAAAA', 4, 0)
    'CCCCCAAAA'
    trim('AAAACCCCCAAAA', 0, 4)
    'AAAACCCCC'
    """
    return s[left:][:-right] if right > 0 else s[left:]


def trim_fastx(fastx_file, out_file, left=0, right=0):
    """
    Trim sequence (and qual) based on left and right options.

    fastx_file : fasta or fastq sequence file path
    out_file : output file path
    left : number of bases to trim from 5' end
    right : number of bases to trim from 3' end

    returns out_file path : string
    """
    assert left >= 0 and right >= 0

    if file_exists(out_file):
        return out_file

    if left == 0 and right == 0:
        cp(fastx_file, out_file)
        return out_file

    logger.info("Trimming the contigs of %s" % fastx_file)

    with file_transaction(out_file) as tx_out_file:
        with open(tx_out_file, 'w') as out_handle:
            for name, seq, qual in readfx(fastx_file):
                seq = trim(seq, left, right)
                if not seq: continue
                if qual:
                    qual = trim(qual, left, right)
                    print('@' + name, seq, '+', qual, sep='\n', file=out_handle)
                else:
                    print_fasta_record(name, seq, out_handle)

    return out_file


def check_sync(name1, name2):
    try:
        assert name1 == name2
    except AssertionError:
        assert name1[:-2] == name2[:-2], \
            "Run failed due to read sync: %s %s" % (name1, name2)


def tmp_split_reads(reads, tmp="/tmp"):
    """
    split interleaved fastq into R1 and R2 in the context of not having to save
    the two fastqs for later use.
    """
    r1 = os.path.join(tmp, "r1.fastq")
    r2 = os.path.join(tmp, "r2.fastq")
    with open(r1, 'w') as fh1, open(r2, 'w') as fh2:
        for (n1, s1, q1), (n2, s2, q2) in grouper(2, readfx(reads)):
            check_sync(n1, n2)
            print('@' + n1, s1, '+', q1, sep='\n', file=fh1)
            print('@' + n2, s2, '+', q2, sep='\n', file=fh2)
    return r1, r2
