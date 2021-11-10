from time import perf_counter

import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans


def insertion(coord, method='nearest'):
    assert method in ['nearest', 'farthest']
    dist_mat = cdist(coord, coord)
    large_num = dist_mat.max() + 0.1

    # assuming depot is the first city
    selecting_op = np.argmin if method == 'nearest' else np.argmax
    mask_val = large_num if method == 'nearest' else -1.0 * large_num

    tour = [0, selecting_op(dist_mat[0, 1:]) + 1, 0]

    while len(tour) <= coord.shape[0]:
        sub_dist_mat = dist_mat[tour, :]
        sub_dist_mat[:, tour] = mask_val
        next_idx = np.unravel_index(selecting_op(sub_dist_mat),
                                    sub_dist_mat.shape)[-1]
        src, dst = tour[:-1], tour[1:]
        dist_incr = dist_mat[src, next_idx] + dist_mat[next_idx, dst] - dist_mat[src, dst]
        tour.insert(dist_incr.argmin() + 1, next_idx)

    tour_length = np.sum(dist_mat[tour[:-1], tour[1:]])
    return tour, tour_length


def nearest_neighbor(coord):
    dist_mat = cdist(coord, coord)
    large_num = dist_mat.max() + 0.1

    tour = [0, np.argmin(dist_mat[0, 1:]) + 1]
    while len(tour) <= coord.shape[0]:
        cur_city_idx = tour[-1]
        sub_dist_mat = dist_mat[cur_city_idx, :]
        sub_dist_mat[tour] = large_num
        tour.append(np.unravel_index(np.argmin(sub_dist_mat), sub_dist_mat.shape)[-1])

    tour_length = np.sum(dist_mat[tour[:-1], tour[1:]])
    return tour, tour_length


def solve_tsp(sub_coord, tsp_heuristics):
    if tsp_heuristics == 'NN':
        tour, tour_length = nearest_neighbor(sub_coord)
    elif tsp_heuristics == 'NI':
        tour, tour_length = insertion(sub_coord, method='nearest')
    elif tsp_heuristics == 'FI':
        tour, tour_length = insertion(sub_coord, method='farthest')
    else:
        raise NotImplementedError
    return tour, tour_length


def solve_twophase(m: int,  # Number of salesmen
                   n: int = None,  # Number of cities including the depot
                   coords: np.ndarray = None,  # Depot and cities positions [ n x 2]
                   tsp_heuristics: str = 'NI',
                   seed: int = 0):  # random seed

    if seed is not None:
        np.random.seed(seed)

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        coords = np.random.uniform(size=(n, 2))
        depot_coord = coords[0:1, :]
        city_coord = coords[1:, :]
    if coords is not None:
        n = coords.shape[0]
        depot_coord = coords[0:1, :]
        city_coord = coords[1:, :]

    start_time = perf_counter()
    kmeans = KMeans(n_clusters=m, random_state=seed).fit(city_coord)

    assigned_cities = {_m: np.arange(1, n)[kmeans.labels_ == _m] for _m in range(m)}
    tours = dict()
    tour_length = dict()
    for _m in range(m):
        if len(assigned_cities[_m]) == 0:  # Not assigned to any city
            tours[_m] = []
            tour_length[_m] = 0.0
        elif len(assigned_cities[_m]) == 1:  # Assigned to a single city
            city_i = int(assigned_cities[_m][0])
            tours[_m] = [city_i]
            # the depot returning cost
            tour_length[_m] = float(2 * cdist(depot_coord, city_coord[city_i - 1:city_i, :], metric='euclidean'))
        else:
            assigned_city_idx = assigned_cities[_m]
            sub_coords = np.vstack([depot_coord, city_coord[assigned_city_idx - 1, :]])
            tour, tl = solve_tsp(sub_coords, tsp_heuristics)

            # adjust city index
            # https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list?rq=1
            replacer = {i + 1: city_i for i, city_i in enumerate(assigned_city_idx)}.get
            tour = [int(replacer(n, n)) for n in tour]

            tours[_m] = tour
            tour_length[_m] = float(tl)

    end_time = perf_counter()

    info = dict()

    # meta info
    info['solution_method'] = '2phase-{}'.format(tsp_heuristics)
    info['n'] = int(n)
    info['m'] = int(m)
    info['coords'] = coords

    # solution and solver conditions
    info['solve'] = True
    info['obj_val'] = float(max(tour_length.values()))
    info['run_time'] = end_time - start_time
    info['tours'] = tours

    # additional performance metrics
    info['amplitude'] = float(max(tour_length.values()) - min(tour_length.values()))
    info['total_length'] = float(sum(tour_length.values()))
    info['tour_length'] = tour_length

    n_inactive = 0
    for tl in info['tour_length'].values():
        if tl <= 0.0:
            n_inactive += 1
    info['n_inactive'] = n_inactive
    info['utilization'] = (m - n_inactive) / m

    return info

if __name__ == '__main__':
    from mTSPsolvers.utils import summary_solution
    info = solve_twophase(m=10, n=50, tsp_heuristics='NI')
    print(info['tours'].values())
    summary_solution(info)
