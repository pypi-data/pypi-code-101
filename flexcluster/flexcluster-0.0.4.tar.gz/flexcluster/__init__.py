import numpy as np
from flexcluster.impl.cluster_impl import _clustering

def kmedoids(data, k, stop_criteria=0.1, initial_centroids=None, max_tries=5):
    dissimilarity_fn = lambda item1, item2: np.abs(item2 - item1)
    centroid_calc_fn = lambda arr: np.median(arr)
    return _clustering(data, k, dissimilarity_fn, centroid_calc_fn, stop_criteria, initial_centroids, max_tries)


def kmeans(data, k, stop_criteria=0.1, initial_centroids=None, max_tries=5):
    dissimilarity_fn = lambda item1, item2: np.abs(item2 - item1)
    centroid_calc_fn = lambda arr: np.mean(arr)
    return _clustering(data, k, dissimilarity_fn, centroid_calc_fn, stop_criteria, initial_centroids, max_tries)


def clustering(data, k, dissimilarity_fn, centroid_calc_fn, stop_criteria=0.1, initial_centroids=None, max_tries=5):
    return _clustering(data, k, dissimilarity_fn, centroid_calc_fn, stop_criteria, initial_centroids, max_tries)
