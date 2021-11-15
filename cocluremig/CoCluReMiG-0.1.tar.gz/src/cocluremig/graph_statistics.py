"""
Graph Statisic Getters
"""
import math
import statistics
from numbers import Real
from typing import List, NamedTuple

from cocluremig.analyzer import graph_analyzer


class GraphMetrics(NamedTuple):
    """
    Graph Metrics Container
    """
    edge_count: int
    """Number of edges"""

    node_count: int
    """Number of Nodes/Vertices"""

    backwards_edge_count: int = 0
    """Number of direct backwards count"""


def get_graph_metrics(graph: graph_analyzer.Graph) -> GraphMetrics:
    """
    calculates basic metrics for given graph

    @param graph: the graph to analyze
    @return: metrics
    """
    if isinstance(graph, graph_analyzer.AdjencyMatrix):
        graph = [(x[0], x[1]) for x in graph_analyzer.adjency_matrix_to_edge_list(graph)]
    edge_count = len(graph)
    node_count = len({node for edge in graph for node in edge})
    backwards_edge_count = int(len({(n1, n2) for (n1, n2) in graph if (n2, n1) in graph}) / 2)
    return GraphMetrics(edge_count, node_count, backwards_edge_count)


class NodeTypeCount(NamedTuple):
    """
    Numbers of nodes per type
    """
    head_count: int
    """Number of heads (commits without children)"""
    root_count: int
    """Number of roots (commits without parents)"""
    branching_count: int
    """Number of branchings (commits with at least two children)"""
    merge_count: int
    """Number of merges (commits with at least two parents)"""
    sequential_count: int
    """Number of sequential commits (exactly one parent and one child)"""


def get_node_types_count(graph: graph_analyzer.Graph) -> NodeTypeCount:
    """
    Calaculates node counts per type

    @param graph: the graph to analyze
    @return: metrics
    """
    if isinstance(graph, graph_analyzer.AdjencyMatrix):
        graph = [(x[0], x[1]) for x in graph_analyzer.adjency_matrix_to_edge_list(graph)]
    db_con = graph_analyzer.edge_list_to_memory_db(graph)
    head_count = len(graph_analyzer.get_merge_or_branch_nodes(db_con, True, True, True, False))
    root_count = len(graph_analyzer.get_merge_or_branch_nodes(db_con, True, True, False, True))
    branching_count = len(graph_analyzer.get_merge_or_branch_nodes(db_con, True, False, True, True))
    merge_count = len(graph_analyzer.get_merge_or_branch_nodes(db_con, False, True, True, True))
    sequential_count = len(graph_analyzer.get_sequential_commits(db_con))
    return NodeTypeCount(head_count, root_count, branching_count, merge_count, sequential_count)


class ClusterStats(NamedTuple):
    """
    A simple Container for basic cluster analysis
    """
    cluster_cnt: int
    """Number of clusters"""

    clustered_nodes_total: int
    """Number of nodes in clusters"""

    cluster_max_size: int
    """Size of biggest cluster"""

    cluster_min_size: int
    """Size of smallest cluster"""

    cluster_median_size: Real
    """Median size of clusters"""

    cluster_avg_size: float
    """Average (mean) size of clusters"""

    cluster_size_variance: float
    """Variance of cluster size"""


def calculate_cluster_stats(clusters: List[List[str]]) -> ClusterStats:
    """
    Calculates some basic statistics about given clusters

    @param clusters: a list of clusters (as list of elements)
    @return: the statistics
    """
    cluster_sizes: List[int] = list(map(len, clusters))
    total_clustered_nodes = sum(cluster_sizes)
    no = len(cluster_sizes)
    maxs = max(cluster_sizes)
    mins = min(cluster_sizes)
    medians = statistics.median(cluster_sizes)
    avg_s = statistics.fmean(cluster_sizes)
    variance = math.nan if no < 2 else statistics.variance(cluster_sizes, avg_s)
    return ClusterStats(no, total_clustered_nodes, maxs, mins, medians, avg_s, variance)
