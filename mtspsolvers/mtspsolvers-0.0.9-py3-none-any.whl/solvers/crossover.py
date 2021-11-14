"""
Crossover method to solve mTSP;
Disclaimer: This method is not optimized at all ! / I didn't conduct code coverage test also.
Original code writter: Minjun Kim

"""

from copy import deepcopy
from time import perf_counter

import elkai
import numpy as np
from scipy.spatial import distance_matrix

from mTSPsolvers.solvers.twophase import solve_twophase


def get_distance(route, dis):
    j = 0
    for i in range(len(route) - 1):
        j += dis[route[i], route[i + 1]]
    return j


def elk(v_lst, dis):
    lst = deepcopy(v_lst)
    le = lst.pop()
    ls = len(lst)
    dis2 = np.zeros([ls, ls])
    for i in range(ls):
        for j in range(ls):
            dis2[i, j] = dis[lst[i], lst[j]]
    s = elkai.solve_int_matrix(dis2 * 1000)
    r = []
    for i in range(ls):
        r.append(lst[s[i]])
    r.append(le)

    return r


def CROSS2(tour1, tour2, dis):
    a1 = get_distance(tour1, dis)
    a2 = get_distance(tour2, dis)
    init_v = max(a1, a2)
    best_tour1 = deepcopy(tour1)
    best_tour2 = deepcopy(tour2)
    best_imp = max(a1, a2)

    is_change = 0
    b1 = get_distance(best_tour1, dis)
    b2 = get_distance(best_tour2, dis)

    for i in range(1, len(tour1)):
        for k in range(i, len(tour1)):
            for j in range(1, len(tour2)):
                for l in range(j, len(tour2)):
                    new_tour1 = tour1[:i] + tour2[j:l] + tour1[k:]
                    new_tour2 = tour2[:j] + tour1[i:k] + tour2[l:]
                    v1 = get_distance(new_tour1, dis)
                    v2 = get_distance(new_tour2, dis)
                    CROSS_cost = max(v1, v2)

                    if CROSS_cost < best_imp:
                        is_change = 1
                        best_imp = CROSS_cost
                        best_tour1 = deepcopy(new_tour1)
                        best_tour2 = deepcopy(new_tour2)
                        b1 = get_distance(best_tour1, dis)
                        b2 = get_distance(best_tour2, dis)
    v = max(b1, b2)
    value = init_v - v

    return best_tour1, best_tour2, b1, b2, is_change, value


def cross_over(tour, tour_value, dis, timeout: float = None):
    lt = len(tour_value)
    v_lst = deepcopy(tour)
    value = deepcopy(tour_value)

    uc = 0
    start_time = perf_counter()

    while True:
        ch = 0
        value = np.array(value)
        id = np.argmax(value)
        id_lst = np.argsort(-value)
        valuechange = np.zeros(lt)
        for i in range(lt):
            if i != id:
                valuechange[i] = CROSS2(v_lst[id], v_lst[i], dis)[5]
        for i in range(lt - 1):
            if max(valuechange) == 0:
                ch = ch + 1
                id = id_lst[ch]
                for i in range(lt):
                    if i != id:
                        valuechange[i] = CROSS2(v_lst[id], v_lst[i], dis)[5]

        if max(valuechange) == 0:  # If local improvement converges
            break

        cid = np.argmax(valuechange)
        a1, a2, _, _, _, _ = CROSS2(v_lst[id], v_lst[cid], dis)
        h1 = get_distance(v_lst[id], dis)
        h2 = get_distance(v_lst[cid], dis)
        uc = uc + 1
        x1 = elk(a1, dis)
        x2 = elk(a2, dis)
        z1 = get_distance(a1, dis)
        z2 = get_distance(a2, dis)
        y1 = get_distance(x1, dis)
        y2 = get_distance(x2, dis)

        if max(h1, h2) < max(y1, y2) - 0.001:
            break

        v_lst[id] = x1
        v_lst[cid] = x2
        value[id] = y1
        value[cid] = y2
        h1 = max(value)

        if timeout is not None:
            if perf_counter() - start_time >= timeout:
                print("hit timeout")
                break

    return v_lst, value, uc


def solve_crossover(m: int,
                    n: int = None,  # Number of cities including the depot
                    coords: np.ndarray = None,  # Depot and cities positions [ n x 2]
                    init_solution_heuristics: str = 'NI',
                    timeout: float = None,
                    seed: int = None):  # random seed for generating city positions

    if seed is not None:
        np.random.seed(seed)

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        coords = np.random.uniform(size=(n, 2))

    start_time = perf_counter()
    init_result = solve_twophase(m=m, coords=coords, tsp_heuristics=init_solution_heuristics)

    tours = [tour for tour in init_result['tours'].values()]
    tour_lengths = [tour_length for tour_length in init_result['tour_length'].values()]
    dis = distance_matrix(init_result['coords'], init_result['coords'])

    updated_tours, updated_tour_lengths, num_improvements = cross_over(tours, tour_lengths, dis, timeout=timeout)
    end_time = perf_counter()

    result_updated = deepcopy(init_result)
    result_updated['solution_method'] = result_updated['solution_method'] + ' + Cross-over'
    result_updated['tours'] = {i: v for i, v in enumerate(updated_tours)}
    result_updated['tour_length'] = {i: v for i, v in enumerate(updated_tour_lengths)}
    result_updated['obj_val'] = max(updated_tour_lengths)
    result_updated['total_length'] = sum(updated_tour_lengths)
    result_updated['amplitude'] = max(updated_tour_lengths) - min(updated_tour_lengths)
    result_updated['n_inactive'] = int((updated_tour_lengths == 0.0).sum())
    result_updated['utilization'] = 1.0 - (updated_tour_lengths == 0.0).sum() / result_updated['m']
    result_updated['n_improvements'] = num_improvements
    result_updated['run_time'] = end_time - start_time
    return result_updated
