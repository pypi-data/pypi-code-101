"""
Graph Properties analyzer
"""
import sqlite3 as sql
from typing import Dict, Iterable, List, NamedTuple, Optional, Tuple, Union

import git
import pandas as pd

import cocluremig.utils.gitutils as gitutils

Node = Union[str, git.Commit]
"""Graph Node"""


class Edge(NamedTuple):
    """
    Graph Edge
    """
    child: Node
    parent: Node


AdjencyMatrix = pd.DataFrame
"""Adjency matrix of graph"""
Graph = Union[List[Edge], AdjencyMatrix]
"""Graph representation"""


def edge_list_to_directed_adjency_matrix(edge_list: List[Edge], nodes: Optional[Iterable[str]] = None) -> AdjencyMatrix:
    """
    converts the given edge list to an adjency matrix

    @param edge_list: list of edges
    @param nodes: the list of nodes in the graph
    @return: the adjency matrix
    """
    shas: List[str]
    if not nodes:
        shas = set({x for e in edge_list for x in e})
    else:
        shas = set(nodes)
    shas = sorted(shas)
    res = pd.DataFrame(0, index=shas, columns=shas)
    for (child, parent) in edge_list:
        res.at[child, parent] = 1
    return AdjencyMatrix(res)


def edge_list_to_memory_db(edge_list: List[Edge]) -> sql.Connection:
    """
    Puts the edge list into an in-memory database

    @param edge_list: a graph edge list
    @return: a connection to the in-memory database
    """
    db_con = sql.connect(":memory:")
    cursor = db_con.cursor()
    cursor.execute("CREATE TABLE Edges(child TEXT,parent TEXT,annotation JSON DEFAULT NULL)")
    db_con.commit()
    for (e1, e2) in edge_list:
        cursor.execute("""INSERT INTO Edges('child', 'parent') VALUES (?,?)""", (e1, e2))
    db_con.commit()
    cursor.close()
    return db_con


def get_head_nodes(db_con: sql.Connection) -> Iterable[str]:
    """
    Gets all head nodes (no children) from given commit graph
    @param db_con: the database connection
    @return: a collection of nodes
    """
    return get_merge_or_branch_nodes(db_con, True, True, True, False)


def get_merge_nodes(db_con: sql.Connection) -> Iterable[str]:
    """
    Gets all merge nodes (at least two parents) from given commit graph
    @param db_con: the database connection
    @return: a collection of nodes
    """
    return get_merge_or_branch_nodes(db_con, False, True, True, True)


def get_branching_nodes(db_con: sql.Connection) -> Iterable[str]:
    """
    Gets all branching nodes (at least two children) from given commit graph
    @param db_con: the database connection
    @return: a collection of nodes 
    """
    return get_merge_or_branch_nodes(db_con, True, False, True, True)


def get_root_nodes(db_con: sql.Connection) -> Iterable[str]:
    """
    Gets all root nodes (no parents) from given commit graph
    @param db_con: the database connection
    @return: a collection of nodes 
    """
    get_merge_or_branch_nodes(db_con, True, True, False, True)


def get_merge_or_branch_nodes(db_con: sql.Connection,
                              ignore_merges=False,
                              ignore_branching=False,
                              ignore_root=False,
                              ignore_head=False) \
        -> Iterable[str]:
    """
    gets structural special nodes from an in-memory database containing a graph

    @param db_con: the database connection
    @param ignore_merges: ignore merge nodes (=>2 parent nodes)
    @param ignore_branching: ignore branching nodes (=>2 child nodes)
    @param ignore_root: ignore root nodes (no parent nodes)
    @param ignore_head: ignore head/leaf nodes (no child nodes)
    @return: a list of the special nodes from the graph
    """
    cursor = db_con.cursor()
    merges = []
    if not ignore_merges:
        cursor.execute("SELECT child, COUNT(parent) as no FROM Edges GROUP BY child HAVING no > 1")
        for row in cursor.fetchall():
            merges.append(row[0])
    branchings = []
    if not ignore_branching:
        cursor.execute("SELECT parent, COUNT(child) as no FROM Edges GROUP BY parent HAVING no > 1")
        for row in cursor.fetchall():
            merges.append(row[0])
    roots = []
    if not ignore_root:
        cursor.execute("SELECT parent p FROM Edges WHERE p NOT IN (SELECT child FROM Edges)")
        for row in cursor.fetchall():
            roots.append(row[0])
    heads = []
    if not ignore_head:
        cursor.execute("SELECT child p FROM Edges WHERE p NOT IN (SELECT parent FROM Edges)")
        for row in cursor.fetchall():
            heads.append(row[0])
    cursor.close()
    return set(merges + branchings + roots + heads)


def get_sequential_commits(db_con: sql.Connection) -> Iterable[str]:
    """
    gets all sequential nodes from an in-memory database containing a graph
    Sequential are all nodes with exactly one parent and exactly one child
    @param db_con: the database connection
    @return: a collection of nodes
    """
    cursor = db_con.cursor()
    cursor.execute(
        """SELECT e1.parent p FROM Edges e1 JOIN Edges e2
        ON e1.parent == e2.child GROUP BY p HAVING COUNT(*) == 1""")
    res = map(lambda x: x[0], cursor.fetchall())
    return list(res)


def get_sequential_paths(db_con: sql.Connection) -> Iterable[List[str]]:
    """
    Creates all sequential paths  from an in-memory database containing a graph

    @param db_con: the database connection
    @return: a List of paths (list of nodes)
    """
    cursor = db_con.cursor()
    # get all parts of sequential paths
    starts = []
    cursor.execute(
        """SELECT child, parent FROM Edges WHERE
        parent in
        (SELECT e1.parent p FROM Edges e1 JOIN Edges e2
        ON e1.parent == e2.child GROUP BY p HAVING COUNT(*)== 1)
        """)
    for row in cursor.fetchall():
        starts.append((row[0], row[1]))
    ends = []
    cursor.execute(
        """SELECT child, parent FROM Edges WHERE
        child in
        (SELECT e1.parent p FROM Edges e1 JOIN Edges e2
        ON e1.parent == e2.child GROUP BY p HAVING COUNT(*)== 1)""")
    for row in cursor.fetchall():
        ends.append((row[0], row[1]))
    inter = []
    cursor.execute(
        """SELECT child, parent FROM Edges WHERE
        child in
        (SELECT e1.parent p FROM Edges e1 JOIN Edges e2
        ON e1.parent == e2.child GROUP BY p HAVING COUNT(*)== 1)
        AND parent in
        (SELECT e1.parent p FROM Edges e1 JOIN Edges e2
        ON e1.parent == e2.child GROUP BY p HAVING COUNT(*)== 1)""")
    for row in cursor.fetchall():
        inter.append((row[0], row[1]))
    starts = [x for x in starts if x not in inter]
    start_finder = {r[1]: r[0] for r in starts}
    ends = [x for x in ends if x not in inter]
    end_finder = dict(ends)
    inter_starts = {x[0] for x in inter if x[0] not in map(lambda x: x[1], inter)}
    connections = dict(inter)
    # multilple sequential paths may start from the same v1
    paths = []
    for node in inter_starts:
        curr_path = [node]
        next_node = connections.get(node)
        while next_node:
            curr_path.append(next_node)
            node = next_node
            next_node = connections.get(node)
        paths.append(
            [start_finder[curr_path[0]]]
            + curr_path
            + [end_finder[curr_path[-1]]]
        )
    for sp in set(start_finder.keys()).intersection(end_finder.keys()):
        paths.append([start_finder[sp], sp, end_finder[sp]])
    # paths = set([tuple(x) for x in paths])
    return paths


def get_merge_or_branch_nodes_from_adjency_matrix(graph: Graph,
                                                  ignore_merges=False, ignore_branching=False,
                                                  ignore_root=False, ignore_head=False) \
        -> Iterable[str]:
    """
    gets structural special nodes from given graph

    @param graph: an edge-list of adjency-matrix
    @param ignore_merges: ignore merge nodes (=>2 parent nodes)
    @param ignore_branching: ignore branching nodes (=>2 child nodes)
    @param ignore_root: ignore root nodes (no parent nodes)
    @param ignore_head: ignore head/leaf nodes (no child nodes)
    @return: a list of the special nodes from the graph
    """
    adjency_matrix: AdjencyMatrix
    if not isinstance(graph, AdjencyMatrix):
        # transform to adjency_matrix
        adjency_matrix = edge_list_to_directed_adjency_matrix(graph)
    else:
        adjency_matrix = graph
    (m_nodes_in, m_nodes_root, m_nodes_out, m_nodes_head) = ([], [], [], [])
    # get number of in/out-going edges
    (edge_count_out, edge_count_in) = (None, None)
    if not (ignore_merges and ignore_root):
        edge_count_out = adjency_matrix.sum()
    if not ignore_merges:
        m_nodes_out = edge_count_out.index[edge_count_out > 1].tolist()
    if not ignore_root:
        m_nodes_root = edge_count_out.index[edge_count_out == 0].tolist()
    if not (ignore_branching and ignore_head):
        edge_count_in = adjency_matrix.sum(1)
    if not ignore_branching:
        m_nodes_in = edge_count_in.index[edge_count_in > 1].tolist()
    if not ignore_head:
        m_nodes_head = edge_count_in.index[edge_count_in == 0].tolist()
    return set(m_nodes_in + m_nodes_root + m_nodes_out + m_nodes_head)


def get_head_refs(repo: git.Repo, db_con: Optional[sql.Connection] = None) -> Dict[str, str]:
    """
    Gets the names of graph's head nodes

    @param repo: a git repo
    @param db_con: the edge list db (generated if not set)
    @return: a dict of sha to name
    """
    if not db_con:
        db_con = edge_list_to_memory_db(gitutils.get_edge_list(repo))
    return {k: v
            for k, v in gitutils.get_ref_names(repo).values()
            if k in
            get_merge_or_branch_nodes
            (db_con, True, True, True, False)}


def adjency_matrix_to_edge_list(adjency_matrix: AdjencyMatrix) -> Tuple[str, str, int]:
    """
    Converts the adjency- matrix to an edge list with weight

    @param adjency_matrix: the matrix to convert
    @return: an edge list with weight
    """
    # https://stackoverflow.com/questions/48218455/how-to-create-an-edge-list-dataframe-from-a-adjacency-matrix-in-python
    adjency_matrix = adjency_matrix.rename_axis('Child') \
        .reset_index() \
        .melt('Child', value_name='Weight', var_name='Parent') \
        .query('Child != Parent') \
        .reset_index(drop=True)
    adjency_matrix = adjency_matrix[adjency_matrix['Weight'] != 0]
    return adjency_matrix.values.tolist()
