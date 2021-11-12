from sklearn.cluster import KMeans
import numpy as np

def get_optimal_cluster(
    points=None,
    max_k=20
):
    inertia_list = []
    for n_clusters in range(1, max_k+1):
        if len(points) >= n_clusters:
            model = KMeans(
                n_clusters=n_clusters,
                init="k-means++",
                max_iter=100,
                n_init=10,
                random_state=0
            ).fit(points)

            inertia_list.append(model.inertia_)

    k = [i*100 for i in np.diff(inertia_list, 2)].index(
        min(
            [i*100 for i in np.diff(inertia_list, 2)]
        )
    )

    return k
