import logging
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from .utils import file_exists, run


logger = logging.getLogger(__name__)
sns.set_context('paper')
sns.set_style('whitegrid')


def out_file_format(out_file):
    _, ext = os.path.splitext(out_file)
    if not ext == '.pdf' or ext == '.png':
        raise IOError('Format must be either pdf of png, not "%s"' % ext)
    return ext[1:]


# TODO: move this to stats.py
def Lc(v):
    """
    Replicate the functionality of R's Lc().

    In R:
    > library(ineq)
    > t <- c(7,13,16)
    > lc <- Lc(t)
    > lc$p
    [1] 0.0000000 0.3333333 0.6666667 1.0000000
    > lc$L
    [1] 0.0000000 0.1944444 0.5555556 1.0000000
    > ineq(t, type="Gini")
    [1] 0.1666667

    :type v: list
    :param v: list of numbers

    :rtype: tuple
    :return: x values, y values, Gini coefficient

    >>> t = [7,13,16]
    >>> Lc(t)
    ((0.0, 0.33..., 0.66..., 1.0), (0.0, 0.19..., 0.55..., 1.0), 0.16...)
    """
    v_len = len(v)
    assert v_len > 0

    a = np.array([0.] + v)
    a.sort()
    x = np.arange(0., v_len + 1) / v_len
    y = a.cumsum() / a.sum()
    G = 1 + (1 - 2 * y.sum()) / v_len
    return x, y, G


# TODO: this should be generic; wrap function to get vector under something else
def lorenz_curve(bam, out_file):
    """
    Calculate Gini coefficient and plot Lorenze curve.

    :type bam: string
    :param bam: aligned reads in bam format

    :type out_file: string
    :param out_file: output file path with extension

    :rtype: float
    :return: Gini coefficient
    """
    file_format = out_file_format(out_file)
    coverages = []
    cmd = '| bedtools genomecov -5 -d -ibam %s' % bam
    header = ['name', 'start', 'coverage']
    for toks in reader(cmd, header=header):
        coverages.append(int(toks['coverage']))
    x, y, G = Lc(coverages)
    logger.info('Gini coefficient:', G, file=sys.stderr)

    plt.plot(x, y)
    plt.plot([0, 1], [0, 1])
    plt.xlabel('Fraction of Genome')
    plt.ylabel('Fraction of Reads')
    plt.savefig(out_file, bbox_inches='tight', format=file_format)
    return G


def get_coverage(bam):
    bedgraph = ""
    filename, _ = path.splitext(bam)
    bedgraph = filename + ".bedgraph.gz"
    if not file_exists(bedgraph):
        cmd = ("bedtools genomecov -bga -ibam {bam} "
            "| bedtools sort -i - "
            "| gzip > {bedgraph}").format(bam=bam, bedgraph=bedgraph)
        run(cmd)
    return bedgraph


def genome_coverage(bam, out_file):
    file_format = out_file_format(out_file)
    fig = plt.figure(figsize=(12, 3))
    bg = get_coverage(bam)
    h = ['chrom', 'start', 'stop', 'count']
    x, y = list(zip(*[(int(t['start']), int(t['count'])) for t in reader(bg, header=h)]))
    plt.plot(x, y)
    plt.xlabel('Genomic Position')
    plt.ylabel('Read Count')
    plt.savefig(out_file, bbox_inches='tight', format=file_format)
