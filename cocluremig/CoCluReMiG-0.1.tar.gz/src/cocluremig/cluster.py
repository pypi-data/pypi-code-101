"""
clustering algorithm
"""
import logging
import math
from builtins import isinstance
from collections import OrderedDict
from numbers import Real
from typing import Callable, Dict, Iterable, List, Optional, Set, Tuple, Union

import git
import pandas as pd

from cocluremig.analyzer import graph_analyzer
from cocluremig.analyzer.graph_analyzer import AdjencyMatrix, Edge, Graph, Node


def create_meta_graph_from_matrix(graph: Graph) -> AdjencyMatrix:
    """
    Converts the given graph into a Meta_graph
    ( https://doi.org/10.1109/ICSME.2014.48 )

    @param graph: The input graph
    @return: the meat-graph as adjency matrix
    """
    # https://doi.org/10.1109/ICSME.2014.48
    adjency_matrix: AdjencyMatrix
    if not isinstance(graph, AdjencyMatrix):
        # transform to adjency_matrix
        adjency_matrix = graph_analyzer.edge_list_to_directed_adjency_matrix(graph)
    else:
        adjency_matrix = graph
    logging.info("Creating meta graph")
    m_nodes = graph_analyzer.get_merge_or_branch_nodes(adjency_matrix)
    for vertex in adjency_matrix.index.tolist():
        logging.debug("Processing %s", vertex)
        if vertex in m_nodes:
            continue
        # with only one incoming and one outgoing edge per node,
        # it can be replaces by a new edge incoming -> outgoing
        # index row != 0 -> index column != 0
        ins = adjency_matrix.loc[vertex, :]
        outs = adjency_matrix.loc[:, vertex]
        in_index = ins[ins != 0].index.tolist()
        out_index = outs[outs != 0].index.tolist()
        if len(out_index) != 1 or len(in_index) != 1:
            # continue
            raise ValueError(vertex, in_index, out_index, graph)
        out_index = out_index[0]
        in_index = in_index[0]
        adjency_matrix.at[out_index, in_index] = adjency_matrix.at[out_index, in_index] + \
                                                 ins[in_index] + outs[out_index]
        if adjency_matrix.at[out_index, in_index] < 1:
            raise ValueError(vertex, in_index, out_index, graph)
        adjency_matrix = adjency_matrix.drop(vertex, axis='columns')
        adjency_matrix = adjency_matrix.drop(vertex, axis='rows')
    return adjency_matrix


def create_meta_graph(edge_list: List[str]) -> Iterable[Tuple[str, str, Optional[List[str]]]]:
    """
     Converts the given edge-list of a graph graph into a Meta_graph
    ( https://doi.org/10.1109/ICSME.2014.48 )
    Each meta-edge is given the list sequential commits
    composing that edge as metadata
    @param edge_list: an list of edges
    @return: the Meta-Graph as Edge list with metadata
    """
    # https://doi.org/10.1109/ICSME.2014.48
    db_con = graph_analyzer.edge_list_to_memory_db(edge_list)
    sequentials = graph_analyzer.get_sequential_commits(db_con)
    seq_paths = graph_analyzer.get_sequential_paths(db_con)
    edges = []
    for (v1, v2) in edge_list:
        if not (v1 in sequentials or v2 in sequentials):
            edges.append((v1, v2, []))
    for path in seq_paths:
        edges.append((path[0], path[-1], path[1:-1]))
    return edges


def create_quasi_meta_graph(edges: List[Edge]) \
        -> Tuple[Iterable[Edge], Dict[int, List[str]]]:
    """
    Creates a Quasi-Meta-Graph from given edge-list.
    this is a derivation of the meta-graph ( https://doi.org/10.1109/ICSME.2014.48 ) ,
    where every crossroad node is connected to up to one itermediate node and
    merging is done on nodes not edges
    @param edges: an edge-list of a graph
    @return: A tuple of
        the edge-list of the meta-graph and
        a dictionary mapping clusters to their contained nodes
    """
    db_con = graph_analyzer.edge_list_to_memory_db(edges)
    crossroads = graph_analyzer.get_merge_or_branch_nodes(db_con)
    weight_fuction = lambda x, y, repo: 0 if (x in crossroads or y in crossroads) else 1
    (quasi_meta, values) = cluster(edges, None, weight_fuction, 0, 1)
    values = [[v1, v2, res] for (v1, v2), res in values.items()]
    (graph, clusters, replacement_table) = make_visuable_clustered_graph_step(quasi_meta)
    return (graph, clusters)


DataSource = Union[git.Repo, pd.DataFrame]


def cluster(topology: List[Edge], data: DataSource,
            heuristic: Callable[
                [Node, Node, DataSource], Real],
            steps: Union[Real, List[Real]] = 0,
            threshold: Real = 0) \
        -> Tuple[Iterable[Iterable[Edge]], Dict[Edge, Real]]:
    """
    Performs topology-aware-clustering on the given topology
    @param topology: an edge-list
    @param data: an additional data-source for our heurisitc
    @param heuristic: a function which gives all edges a weight
    @param steps: Either a List of predifined values of values, which determine the clustering steps
                    or a value to define merge step size,
                    when left empty every value of the heuristic is its own step
    @param threshold: a value, which when reached stops merging
    @return: A tuple of
        1. A List of Lists where every sublist represtens the edges merged in on step
        2. the mapping of edges to their heuristic
    """
    values: OrderedDict[Edge, Real] = \
        OrderedDict(sorted(
            [((e1, e2), heuristic(e1, e2, data))
             for (e1, e2) in topology],
            key=lambda x: x[1], reverse=True))
    curr_val: Real = next(iter(values.items()))[1]
    if steps:
        if isinstance(steps, Real):
            step_size = steps
            back_iter = iter(reversed(values.items()))
            fore_iter = iter(values.items())
            max_val = next(fore_iter)[1]
            min_val = next(back_iter)[1]
            while math.isinf(min_val):
                min_val = next(back_iter)[1]
            while math.isinf(max_val):
                max_val = next(fore_iter)[1]
            max_val = math.ceil(max_val / step_size)
            min_val = math.ceil(min_val / step_size)
            step_no = max(abs(max_val), abs(min_val))
            max_val *= step_size
            min_val *= step_size
            steps = [c * step_size for c in range(0, step_no)]
            if not steps:
                steps = [step_size, step_size / 2]
        if isinstance(steps, list):
            if curr_val <= 0 and steps[1] >= 0:
                steps = list(map(lambda x: -x, steps))
            steps = list(sorted(steps, reverse=True))
    steps: List[Real]
    merged_this_step: List[Edge] = []
    unmerged: Set[Edge] = set(topology)
    out: Iterable[Iterable[Edge]] = []
    curr_step = 1
    for (edge, value) in values.items():
        if steps and value <= steps[curr_step]:
            curr_step += 1
            if merged_this_step:
                out.append(list(merged_this_step))
                merged_this_step = []
            if curr_step == len(steps):
                break
        elif not steps and value < curr_val:
            if merged_this_step:
                out.append(list(merged_this_step))
                merged_this_step = []
            curr_val = value
        if threshold and value < threshold:
            break

        # merge vertices
        merged_this_step.append(edge)
        unmerged.remove(edge)
    # only add if non-empty
    if merged_this_step:
        out.append(merged_this_step)
    if unmerged:
        out.append(list(unmerged))
    return (out, values)


def make_visuable_clustered_graph_step(
        merge_steps: Iterable[Iterable[Edge]],
        step: int = 0,
        replacement_table: Optional[Dict[str, Set[str]]] = None) \
        -> Tuple[Iterable[Edge],
                 Dict[int, List[str]],
                 Dict[str, Set[str]]]:
    """
    Converts the given output of our topology-aware-clustering into a usable edge-list
    @param merge_steps:  A List of Lists where every sublist represtens the edges merged in on step
    @param step: which step to currently merge
    @param replacement_table: A mapping of nodes to their merged clusters (default: empty)
    @return: A tuple of
            1. an edge list of the output graph
            2. a dictionary mapping the cluster-no to the contained shas
            3. a mapping of nodes to their clusters (to insert into the following merge-step)
    """
    if replacement_table is None:
        replacement_table = {}
    merged_edges: Set[Tuple[Edge]] = set()
    # populate replacement table
    for (vertex_1, vertex_2) in merge_steps[step]:
        c_list_1 = replacement_table.get(vertex_1, {vertex_1})
        c_list_2 = replacement_table.get(vertex_2, {vertex_2})
        c_list_1 = c_list_1.union(c_list_2)
        for vertex in c_list_1:
            replacement_table[vertex] = c_list_1
    # name clusters
    clusters: Dict[int, List[str]] = {}
    for vertex in replacement_table.values():
        clusters[id(vertex)] = list(vertex)
    for unmerged in merge_steps[(step + 1):]:
        for (vertex_1, vertex_2) in unmerged:
            new_vertex_1 = replacement_table.get(vertex_1)
            if new_vertex_1:
                new_vertex_1 = "c_" + str(id(new_vertex_1))
            else:
                new_vertex_1 = vertex_1
            new_vertex_2 = replacement_table.get(vertex_2)
            if new_vertex_2:
                new_vertex_2 = "c_" + str(id(new_vertex_2))
            else:
                new_vertex_2 = vertex_2
            # remove self-referencing edges
            if new_vertex_1 != new_vertex_2:
                merged_edges.add((new_vertex_1, new_vertex_2))
    return (merged_edges, clusters, replacement_table)


def visuable_cluster_blind(edges: Iterable[Edge], replacement_table: Dict[str, Set[str]]) \
        -> Iterable[Edge]:
    """
    Creates a new graph based on given repalcement information
    @param edges:  an edge list
    @param replacement_table: a mapping from a vertex to a cluster/set of vertices
    @return: the edge list of the output-graph
    """
    new_edges, clusters, replacement_out = \
        make_visuable_clustered_graph_step(
            [[], list(edges)], 0, replacement_table)
    return new_edges
