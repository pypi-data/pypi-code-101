from __future__ import print_function
import bisect
import functools
import logging
import os
import re
import six
from Bio import Phylo
from collections import defaultdict, deque, OrderedDict
from itertools import groupby

from six.moves import zip_longest

from .fastx import format_fasta_record, read_fasta
from .utils import file_exists, file_transaction, run

RANKS = {8: "s", 7: "g", 6: "f", 5: "o", 4: "c", 3: "p", 2: "k"}
BLAST6 = [
    "qseqid",
    "sseqid",
    "pident",
    "length",
    "mismatch",
    "gapopen",
    "qstart",
    "qend",
    "sstart",
    "send",
    "evalue",
    "bitscore",
]


class BlastHits(object):
    def __init__(self, names=None, max_hits=10, top_fraction=None):
        """Class that represents BLAST hits for a single target sequence. Hits are added to queues
        for bitscore and ID and ordered by increasing bitscore.

        Args:
            names (Optional[list]): when initiated with a name list; :func:`best_hit` and
                :func:`add` will no longer operate as intended
            max_hits (int): maximum number of hits to consider for this :class:`BlastHits` group
            top_fraction (float): fraction cutoff from best bitscore, e.g. 0.3 will filter out 699 when best bitscore is 1000

        Notes:
            max_hits and top_fraction work in conjunction of one another
        """
        if names is None:
            # increasing bitscore sorted
            self.names = deque()
            self.percent_ids = deque()
            self.bitscores = deque()
        else:
            self.names = names
        self.max_hits = max_hits
        self.top_fraction = top_fraction

    def __repr__(self):
        return "{cls}[{tax}]".format(cls=self.__class__.__name__, tax=self.names)

    def __len__(self):
        return len(self.names)

    def add(self, name, percent_id, bitscore):
        """Add entry to this :class:`BlastHits` group.

        Args:
            name (str): hit identifier
            bitscore (str): bitscore for hit

        """
        bitscore = float(bitscore)
        if self.top_fraction and self.bitscores:
            # the filter
            if bitscore < (self.bitscores[-1] * self.top_fraction):
                bitscore = None
            # new best
            elif bitscore > self.bitscores[-1]:
                score = self.bitscores[0]
                while score < bitscore * self.top_fraction:
                    self.names.popleft()
                    self.percent_ids.popleft()
                    self.bitscores.popleft()
                    score = self.bitscores[0]
        if bitscore:
            # insert into sorted list
            idx = bisect.bisect_left(self.bitscores, bitscore)
            if six.PY3:
                self.bitscores.insert(idx, bitscore)
                self.percent_ids.insert(idx, percent_id)
                self.names.insert(idx, name)
            # this is awful
            if six.PY2:
                b = list(self.bitscores)
                b.insert(idx, bitscore)
                self.bitscores = deque(b)
                p = list(self.percent_ids)
                p.insert(idx, percent_id)
                self.percent_ids = deque(p)
                n = list(self.names)
                n.insert(idx, name)
                self.names = deque(n)
            if len(self.names) > self.max_hits:
                # remove lowest bitscore
                self.names.popleft()
                self.percent_ids.popleft()
                self.bitscores.popleft()

    def best_hit(self):
        """Returns the hit ID of the best scoring alignment."""
        return self.names[-1]

    def majority(self):
        """Returns the hit ID of the best scoring hit ID that is repeated or the best hit when
        no items are repeated.
        """
        # no repeated names
        if len(self.names) == len(set(self.names)):
            return self.best_hit()

        else:
            # count each taxonomy, grab top taxonomy
            most_common = Counter(self.names).most_common(1)[0][0]
            # need to flip to grab best bitscore
            names_reversed = self.names.copy()
            names_reversed.reverse()
            # left most index match
            idx = names_reversed.index(most_common)
            return names_reversed[idx]


class Tree(object):
    ROOT = 0
    META = 1
    DOMAIN = 2
    SUPERKINGDOM = 3
    KINGDOM = 4
    PHYLUM = 5
    CLASS = 6
    ORDER = 7
    FAMILY = 8
    GENUS = 9
    SPECIES = 10
    SUBSPECIES = 11
    depths = {
        ROOT: "root",
        META: "meta",
        DOMAIN: "domain",
        SUPERKINGDOM: "superkingdom",
        KINGDOM: "kingdom",
        PHYLUM: "phylum",
        CLASS: "class",
        ORDER: "order",
        FAMILY: "family",
        GENUS: "genus",
        SPECIES: "species",
        SUBSPECIES: "strain",
    }

    def __init__(self, mapfile, trefile):
        self.tree = Phylo.read(
            trefile, "newick", values_are_confidence=True, rooted=True
        )
        self.root = self.tree.root
        self.names = {}
        self.node_names = {}
        self.node_ids = {}
        self.assignment_min = {}
        self.parents = {}
        self.no_hits = self.add_node("No hits", self.root)
        for child in self.get_all_children(self.root):
            self.node_ids[child.name] = child
        # why not just remove these from the map?
        accession_re = [
            re.compile("\D\D\d\d\d\d\d\d\Z"),
            re.compile("\D\d\d\d\d\d\Z"),
            re.compile("\D\D\D\D\d\d\d\d\d\d\d\d\d\Z"),
            re.compile("\D\D\D\D\d\d\d\d\d\d\d\d\Z"),
        ]
        # Read nodes from .map file (id\t name\t cutoff)
        with open(mapfile) as fh:
            for line in fh:
                toks = line.strip().split("\t")
                node_id = toks[0]
                name = toks[1]
                similarity_cutoff = float(toks[3])
                # Find node and map name or accession to it
                n = self.node_ids.get(node_id)
                if n:
                    self.node_names[name] = n
                    # Unless this is just an accession, update node name and assignment min.
                    if similarity_cutoff >= 0 and not (
                        accession_re[0].match(name)
                        or accession_re[1].match(name)
                        or accession_re[2].match(name)
                        or accession_re[3].match(name)
                    ):
                        self.assignment_min[name] = similarity_cutoff
                        n.name = name
                else:
                    logging.error(
                        "Error: Node %s (%s) not found in tree" % (node_id, name)
                    )

    def verify_node(self, node):
        if isinstance(node, Phylo.BaseTree.Clade):
            return node

        elif isinstance(node, str):
            nn = node
            node = self.node_names.get(nn)
            if not node:
                logging.error("Verification Error: Node '%s' not found" % nn)
                return

            else:
                return node

        else:
            logging.error("Verification Error: Node %s is a strange instance" % node)
            return

    def add_node(self, nodename, parent, assignment_min=0):
        # insert instead of append?
        if nodename in self.node_names:
            logging.error("Node name '%s' is not unique - not added" % nodename)
            return None

        node = Phylo.Newick.Clade(name=nodename)
        parent = self.verify_node(parent)
        if not parent:
            return None

        parent.clades.append(node)
        self.node_names[nodename] = node
        self.assignment_min[node.name] = assignment_min
        self.parents[node] = parent
        return node

    def get_immediate_children(self, node):
        node = self.verify_node(node)
        children = []
        for c in node.clades:
            children.append(c)
        return children

    def get_parent(self, node):
        node = self.verify_node(node)
        if not node:
            return None

        if node in self.parents:
            return self.parents[node]

        else:
            p = self.tree.get_path(node)
            if p and len(p) > 1:
                parent = p[-2]
                self.parents[node] = parent
                return parent

            else:
                return self.tree.root

    def get_rank(self, node):
        depth = self.get_depth(node)
        if depth > Tree.SUBSPECIES:
            depth = Tree.SUBSPECIES
        return Tree.depths[depth]

    def get_depth(self, node):
        node = self.verify_node(node)
        pth = self.get_path(node)
        if len(pth) == 1 and pth[0] is self.tree.root:
            return 0

        else:
            return len(pth)

    def get_path(self, node):
        plist = [node]
        if node is self.tree.root:
            return plist

        parent = self.get_parent(node)
        while parent and parent is not self.tree.root:
            plist = [parent] + plist
            parent = self.get_parent(parent)
        if not parent:
            logging.error("Cannot find parent beyond %s" % plist)
        else:
            return plist

    def get_common_ancestor(self, node_names):
        """
        Accepts a list of accessions (corresponding to tre file) incl.
        duplicates and returns LCA
        """
        nodes = list(set([self.node_names.get(n) for n in node_names]))
        if len(nodes) == 1:
            return nodes[0]

        paths = sorted([self.get_path(n) for n in nodes], key=len)
        lca_path = paths[0]
        for path in paths[1:]:
            while not lca_path[-1] in path:
                if len(lca_path) == 1:
                    return self.tree.root

                else:
                    lca_path.pop()
        return lca_path[-1]

    def get_all_children(self, node, children=None, parent=None):
        if children is None:
            children = []
        for c in node.clades:
            self.get_all_children(c, children, parent=node)
        children.append(node)
        self.parents[node] = parent
        return children

    def get_taxonomy(self, node):
        taxonomy = OrderedDict()
        for i in "kpcofgs":
            taxonomy[i] = "?"
        if node is not None:
            for clade in self.get_path(node):
                depth = self.get_depth(clade)
                if (
                    depth > Tree.META
                    and depth < Tree.SUBSPECIES
                    and not depth == Tree.SUPERKINGDOM
                    and not depth == Tree.KINGDOM
                ):
                    if Tree.depths[depth][0] == "d":
                        abb = "k"
                    else:
                        abb = Tree.depths[depth][0]
                    taxonomy[abb] = clade.name.replace(" ", "_")
        return taxonomy


class OTU(object):
    def __init__(self, name, sequence, classification=None):
        self.name = name
        self.sequence = sequence
        self.classification = classification


def parse_blasthits(blasthits, otus, tre, min_score=155, top_fraction=0.98):
    hsps = defaultdict(lambda: BlastHits(top_fraction=top_fraction))
    with open(blasthits) as blast_hits_fh:
        # TODO iterator as some may not be able to process very large files
        for hsp in blast_hits_fh:
            toks = dict(zip(BLAST6, hsp.strip().split("\t")))
            if float(toks["bitscore"]) < min_score:
                continue

            hsps[toks["qseqid"]].add(
                toks["sseqid"], float(toks["pident"]) / 100, toks["bitscore"]
            )
    for otu_name, hits in hsps.items():
        otu = otus[otu_name]
        lca_node = tre.get_common_ancestor(hits.names)
        if not lca_node:
            logging.debug("No LCA -- assigning to No Hits: %s" % hits.names)
            otu.classification = tre.no_hits
            continue

        while (
            lca_node.name in tre.assignment_min
            and hits.percent_ids[-1] < tre.assignment_min[lca_node.name]
            and lca_node is not tre.root
        ):
            lca_node = tre.get_parent(lca_node)
        otu.classification = lca_node
    return otus


def run_crest_classifier(
    fasta,
    blasthits,
    mapfile,
    trefile,
    outfasta,
    outtab,
    min_score=155,
    top_fraction=0.98,
    min_length=250,
):
    otus = OrderedDict()
    logging.info("Reading the input fasta (%s)" % fasta)
    with open(fasta) as fh:
        for name, seq in read_fasta(fh):
            otus[name] = OTU(name, seq)
    logging.info("Parsing the map and tree inputs")
    tre = Tree(mapfile, trefile)
    logging.info("Classifying BLAST hits")
    otus = parse_blasthits(blasthits, otus, tre, min_score, top_fraction)
    with open(outfasta, "w") as fasta_out, open(outtab, "w") as tsv_out:
        for otu_id, otu in otus.items():
            if len(otu.sequence) < min_length:
                continue

            taxonomy = tre.get_taxonomy(otu.classification)
            full_name = "{name} {taxonomy}".format(
                name=otu.name,
                taxonomy=";".join(
                    ["%s__%s" % (abb, tax) for abb, tax in taxonomy.items()]
                ),
            )
            print(format_fasta_record(full_name, otu.sequence), file=fasta_out)
            print(
                otu_id,
                ";".join(["%s__%s" % (abb, tax) for abb, tax in taxonomy.items()]),
                sep="\t",
                file=tsv_out,
            )


def classify_by_ssu(
    fasta,
    blast_db,
    blast_db_map,
    blast_db_tre,
    out_hits,
    out_fasta,
    out_annotation_tsv,
    min_score=155,
    top_fraction=0.98,
    min_length=250,
    threads=1,
):
    """Runs an LCA classification across contigs and returns taxonomy and
    contig length per annotation.

    Returns:
        list: [name, length, annotation] for each SSU
    """
    unannotated = out_fasta + ".ssu.TEMP.fasta"
    if not file_exists(out_fasta):
        # index the incoming fasta file so we can pull regions from it later
        run("samtools faidx {fa}".format(fa=fasta))
        # align SSU hits to reference
        with file_transaction(out_hits) as tx:
            cmd = (
                "blastn -task megablast -query {query} -db {db} "
                "-num_alignments 10 -outfmt 6 -num_threads {threads} "
                "-out {tsv}"
            ).format(query=fasta, db=blast_db, threads=threads, tsv=tx)
            run(cmd, "Aligning SSU hits to reference")
        if not file_exists(out_hits):
            return "no SSU regions found"

        # pull out SSU segments from fasta using blast hit coordinates
        with file_transaction(unannotated) as tx:
            with open(out_hits) as fh, open(tx, "w") as fo:
                for query, qgroup in groupby(fh, key=lambda x: x.partition("\t")[0]):
                    # assuming sorted input; just going to take best hit here
                    for hsp in qgroup:
                        toks = dict(zip(BLAST6, hsp.strip().split("\t")))
                        break

                    # append this entry onto temp output
                    cmd = "samtools faidx {fa} {name}:{start}-{stop}".format(
                        fa=fasta,
                        name=toks["qseqid"],
                        start=toks["qstart"],
                        stop=toks["qend"],
                    )
                    for line in run(cmd, iterable=True):
                        line = line.strip()
                        if line.startswith(">"):
                            # trim the coordinates from the fasta names
                            line = line.rpartition(":")[0]
                        print(line, file=fo)
        if not file_exists(unannotated):
            # this is most likely due to an error if we've made it here
            return "no SSU regions found"

        run_crest_classifier(
            unannotated,
            out_hits,
            blast_db_map,
            blast_db_tre,
            out_fasta,
            out_annotation_tsv,
            min_score,
            top_fraction,
            min_length,
        )
    if file_exists(unannotated):
        os.remove(unannotated)
    # parse the out_fasta to create the return string
    ssus = []
    if file_exists(out_fasta):
        with open(out_fasta) as fh:
            for name, seq in read_fasta(fh):
                if len(seq) < min_length:
                    continue

                contig_name, _, annotation = name.partition(" ")
                # no hits case == k__?,p__?,c__?,o__?,f__?,g__?,s__?
                if len(annotation) > 34:
                    ssus.append([contig_name, len(seq), annotation])
    if len(ssus) == 0:
        return "no SSUs were classified"

    ssus.sort(key=lambda x: x[1], reverse=True)
    return ssus


def parse_functional_assignment(db_hits, start, stop):
    if not db_hits:
        return None

    largest_overlap = 0
    index_of_largest = 0
    for i, hit in enumerate(db_hits):
        if start < hit[3]:
            this_start = hit[3]
        else:
            this_start = start
        if stop > hit[4]:
            this_stop = hit[4]
        else:
            this_stop = stop
        overlap = this_stop - this_start
        if overlap > largest_overlap:
            index_of_largest = i
            largest_overlap = overlap
    return db_hits[index_of_largest]


def get_pident(length, toks):
    ed = 0
    # toks is like ["NM:i:8", "AM:i:29"]
    for idx in toks:
        if idx.startswith("NM"):
            ed = int(idx.rpartition(":")[-1])
    return 100 - (ed / length)


def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


class SimpleTree(object):
    """Parses nodes.dmp and provides LCA method."""
    def __init__(self, nodes, root="1"):
        self.tree = self.parse_nodes(nodes)
        self.root = root

    def parse_nodes(self, nodes):
        n = dict()
        with open(nodes) as fh:
            for line in fh:
                toks = [i.strip() for i in line.split("|", 2)]
                n[toks[0]] = toks[1]
        return n

    @memoize
    def get_lineage(self, taxid):
        """
        Separate lineage retrieval methods due to memoization.

        '1655516' -> ['131567', '2', '1224', '28211', '54526', '1655514', '1655516']
        """
        if taxid == self.root:
            return taxid

        lineage = [taxid]
        parent = self.tree[taxid]
        while not parent == self.root:
            # prepend onto list
            lineage.insert(0, parent)
            # get next taxonomic level
            parent = self.tree[parent]
        return lineage

    def get_lca(self, ids):
        num_ids = len(ids)
        lineages = list()
        for i in ids:
            lineages.append(self.get_lineage(i))
        if num_ids == 1:
            return lineages[0][-1]
        # transpose the lineages to compare per level
        # [[2, 4, 5], [2, 4]] -> [[2, 2], [4, 4], [5, None]]
        lineages = [list(i) for i in zip_longest(*lineages)]
        lca = self.root
        for group in lineages:
            if len(set(group)) == num_ids:
                break
            lca = group[0]
        return lca


from tqdm import tqdm

def classify_reads(
    fastx,
    db,
    crest_nodes,
    ncbi_nodes,
    out_hits,
    out_tsv,
    min_pid=90,
    min_length=100,
    top_fraction=0.90,
    threads=1,
):
    """Runs an LCA classification across reads (FASTA) and returns taxonomy
    and length per annotation.

    Returns:
        tuple: (out_hits, out_annotation_tsv)
    """
    if not out_hits.endswith(".sam"):
        out_hits = os.path.splitext(out_hits)[0] + ".sam"
    logger = logging.getLogger(__name__)
    if file_exists([out_hits, out_tsv]):
        return (out_hits, out_tsv)

    # align reads to reference
    if not file_exists(out_hits):
        with file_transaction(out_hits) as tx:
            cmd = (
                "bbmap.sh local=t threads={threads} path={path} ref={db} "
                "in={fastx} out={hits} ordered=t noheader=t secondary=t "
                "sssr={top} maxsites=12 mappedonly=t minid={minid}"
            ).format(
                threads=threads,
                db=db,
                fastx=fastx,
                hits=tx,
                top=top_fraction,
                minid=min_pid,
                path=os.path.dirname(os.path.realpath(db)),
            )
            run(cmd, "Aligning reads to reference")
        if not file_exists(out_hits):
            return "no reads were aligned to reference db: {db}".format(db=blast_db)
    else:
        logger.info("Found existing hits [%s]; not re-aligning" % out_hits)

    # represents highest-scoring pair
    header = ["query", "contig", "sag", "start", "stop", "pid", "len", "ncbi", "crest"]
    ncbi_tre = SimpleTree(ncbi_nodes)
    crest_tre = SimpleTree(crest_nodes)

    with tqdm() as pbar:
        # parse the hits into minimal tsv
        with open(out_hits) as sam, open(out_tsv, "w") as tsv:
            # header of annotation file
            print(*header, sep="\t", file=tsv)
            for qseqid, alignments in groupby(sam, key=lambda x: x.partition("\t")[0]):
                crest_ids = set()
                ncbi_ids = set()
                best = list()
                for hsp in alignments:
                    toks = hsp.strip().split("\t")
                    contig, ncbi_id, crest_id = toks[2].split(";")
                    sag = contig.partition("_")[0]
                    aln = len(toks[9])
                    pid = get_pident(aln, toks[10:])
                    # truncate to 3 decimal places
                    pid = "%.3f" % pid
                    stop = aln + int(toks[3])
                    if not best:
                        best = [toks[0], toks[2], sag, toks[3], str(stop), pid, str(aln)]
                    ncbi_ids.add(ncbi_id)
                    crest_ids.add(crest_id)
                # ncbi_id = get_lca(ncbi_ids, ncbi_tre)
                ncbi_id = ncbi_tre.get_lca(ncbi_ids)
                crest_id = crest_tre.get_lca(crest_ids)
                pbar.update()
                print("\t".join(best), ncbi_id, crest_id, sep="\t", file=tsv)
    return (out_hits, out_tsv)
