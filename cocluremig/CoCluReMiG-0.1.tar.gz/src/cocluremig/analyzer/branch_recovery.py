"""
    Branch recovery method
    from Michaud, Guarnera, Collard & Maletic's method
    https://doi.org/10.1109/ICSME.2016.39
"""

import logging
import sqlite3
from collections import Counter
from typing import *

import git

# https://doi.org/10.1109/ICSME.2016.39
from cocluremig.analyzer.graph_analyzer import Edge, edge_list_to_memory_db, get_merge_or_branch_nodes
from cocluremig.utils.gitutils import get_edge_list, get_ref_names


def recover_branches(repo: git.Repo) -> Tuple[Dict[str, str], Iterable[Edge]]:
    """
    Associates commits with their branch of origin
    according to Michaud, Guarnera, Collard & Maletic's method
    https://doi.org/10.1109/ICSME.2016.39

    @param repo: a Git repository
    @return: a Tuple of
        a dictionary mapping commits to their branches
        and
        the edge list of the commit graph
    """
    (edges, _) = get_edge_list(repo)
    db: sqlite3.Connection = edge_list_to_memory_db(edges)
    refs: Dict[str, List[str]] = get_ref_names(repo, True, True)
    merges = get_merge_or_branch_nodes(db, False, True, True, True)
    branchings = get_merge_or_branch_nodes(db, True, False, True, False)
    del db
    unnamed_pairs = {}
    # head rule
    processed_commits = {sha: ref[0] for sha, ref in refs.items()}
    logging.info("marked heads with branch names")
    # parents of merges
    for merge_commit in merges:
        try:
            branch_names, merge_type = \
                get_parents_names(repo.commit(merge_commit), None)
            if not merge_type:
                logging.warning("No merge for %s with message %s",
                                merge_commit, repo.commit(merge_commit).message)
            if merge_type and "branch" not in str(merge_type):
                unnamed_pairs[merge_commit] = repo.commit(merge_commit).parents[0].hexsha
            else:
                for commit, name in branch_names:
                    if name:
                        processed_commits[commit.hexsha] = name
                    else:
                        # workaround for not named pairs of same branch
                        unnamed_pairs[merge_commit] = commit.hexsha
        except NoStdMergeMessageError as e:
            logging.info((merge_commit, e))
        except MessageParsingError as e:
            logging.error((merge_commit, e))
    logging.info("marked parents of merge")
    # ancestral rule
    while True:
        pre_process_copy = processed_commits.copy()
        for commit, label in pre_process_copy.items():
            commit = repo.commit(commit)
            if not commit.parents:
                continue
            commit = commit.parents[0]
            while commit.hexsha not in branchings and not processed_commits.get(commit.hexsha):
                processed_commits[commit.hexsha] = label
                if unnamed_pairs.get(commit.hexsha):
                    processed_commits[unnamed_pairs[commit.hexsha]] = label
                    del unnamed_pairs[commit.hexsha]
                commit = commit.parents[0]
        if len(processed_commits) == len(pre_process_copy):
            break
    logging.info("applied ancenstral rule")
    # majority rule
    for commit in branchings:
        commit = repo.commit(commit)
        if processed_commits.get(commit.hexsha):
            continue
        name_cntr = Counter()
        parent: git.Commit = commit
        unlabeled_commits = []
        if len(commit.parents) == 1:
            parent = commit.parents[0]
        while parent.hexsha not in merges and parent.hexsha not in branchings:
            branch = processed_commits.get(parent.hexsha)
            if branch:
                name_cntr[branch] += 1
            else:
                unlabeled_commits.append(parent.hexsha)
            if len(parent.parents) >= 1:
                parent = parent.parents[0]
            else:
                break
        if parent.hexsha in branchings:
            branch = processed_commits.get(parent.hexsha)
            if branch:
                name_cntr[branch] += 1
        if len(name_cntr) > 0:
            majority_branch = name_cntr.most_common(1)[0][0]
            processed_commits[commit.hexsha] = majority_branch
            for c in unlabeled_commits:
                processed_commits[c] = majority_branch
    return (processed_commits, edges)


# https://doi.org/10.1109/ICSME.2016.39
def get_parents_names(commit: git.Commit, current_branch_name: Optional[str] = "main(implicit)") \
        -> Tuple[List[Tuple[git.Commit, str]], Optional[str]]:
    """
    retrieves given commit's parent name from commit message

    @param commit: a commit
    @param current_branch_name: the name of the branch the commit is on
    @return: a tuple of list of (commit, branch) tuples and the merge type
    @raise MessageParsingError: the parsing ran into an error
    @raise NoStdMergeMessageError: the message does not conform to expected schema
    """
    logging.log(logging.DEBUG - 5, "Processing %s", commit.hexsha)
    parents = commit.parents
    res = []
    # ancestral rule
    if len(parents) == 1:
        return ([(parents[0], current_branch_name)], None)
    # parse commit message for branch names
    # \n split due to bad multiline Pull-Requests
    message_parts: List[str] = commit.message.lower().split("\n")[0].split()
    logging.log(1, "Decomposing %s", message_parts)
    parent_names = []
    curr_token: int = 0
    if not message_parts[curr_token] == "merge" or len(message_parts) < 2:
        raise NoStdMergeMessageError("No merge message detected: %s", commit.message)
    curr_token += 1
    merge_type = message_parts[curr_token]
    if merge_type == "pull" or merge_type.startswith("remote"):
        merge_type = message_parts[curr_token] + " " + message_parts[curr_token + 1]
        curr_token += 2
    elif merge_type in ["branch", "tag", "commit", "branches", "tags", "commits"]:
        curr_token += 1
    else:
        logging.warning("No Merge type detected: %s", commit.message)
        merge_type = "Unknown"
    octopi_merge = False
    if "and" in message_parts[curr_token:] and \
            merge_type in \
            ["tags", "commits", "branches", "remote braches", "remote-tracking branches"]:
        octopi_merge = True
    if merge_type == "pull request":
        pull_request_no = message_parts[curr_token]
        curr_token += 1
        if curr_token >= len(message_parts) or not message_parts[curr_token] == "from":
            raise MessageParsingError("pull request lacks origin description: %s", commit.message)
        curr_token += 1
    if not octopi_merge:
        parent_names = [message_parts[curr_token]]
        curr_token += 1
    else:
        while not message_parts[curr_token] == "into" or curr_token == len(message_parts):
            if not message_parts[curr_token] == "and":
                parent_names.append(message_parts[curr_token].rstrip(","))
            curr_token += 1
    if not curr_token == len(message_parts):
        # edit of original algorithm
        if message_parts[curr_token] == "from" or message_parts[curr_token] == "of":
            curr_token += 1
            branch_repo = message_parts[curr_token]
            curr_token += 1
        # end
    if not curr_token == len(message_parts):
        if message_parts[curr_token] == "into":
            curr_token += 1
            current_branch_name = message_parts[curr_token]
        else:
            logging.warning("Abitrary message postfix detected: %s", commit.message)
    del curr_token
    del message_parts
    if not len(parents) - 1 == len(parent_names):
        raise MessageParsingError(
            "NLP-detected no of parent commits does not match actual parent no."
            " Is %i should be %i",
            len(parent_names) + 1, len(parents))
    res.append((parents[0], current_branch_name))
    for i, name in enumerate(parent_names):
        if name:
            res.append((parents[i + 1], name.strip("\"").strip("\'").strip("\\")))
        else:
            logging.warning("No name for %s (parent %i) by Message",
                            parents[i + 1].hexsha, i, commit.message)
    return (res, merge_type)


class MessageParsingError(Exception):
    """
    The parsing of commit message ran into an error
    """
    pass


class NoStdMergeMessageError(MessageParsingError):
    """
    The commit message does not conform to given schema
    """
    pass
