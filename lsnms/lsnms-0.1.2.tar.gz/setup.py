# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lsnms']

package_data = \
{'': ['*']}

install_requires = \
['numba==0.54.1', 'numpy==1.19.5']

setup_kwargs = {
    'name': 'lsnms',
    'version': '0.1.2',
    'description': 'Large Scale Non Maximum Suppression',
    'long_description': '# LSNMS\nSpeeding up Non Maximum Suppresion ran on very large images by a several folds factor, using a sparse implementation of NMS.  \nThis project becomes useful in the case of very high dimensional images data, when the amount of predicted instances to prune becomes considerable (> 10,000 objects).\n\n<p float="center">\n  <center><img src="https://raw.githubusercontent.com/remydubois/lsnms/main/assets/images/timings_medium_image.png?token=AEJMSVNEIBF2PMWIVASMKATAMIKHS" width="700" />\n  <figcaption>Run times (on a virtual image of 10kx10k pixels)</figcaption></center>\n</p>\n\n\n## Installation\nThis project is fully installable with pip:\n```\npip install lsnms\n```\nor by cloning this repo\n```\ngit clone https://github.com/remydubois/lsnms\ncd lsnms/\npip install -e .\n```\nOnly dependencies are numpy and numba.\n\n## Example usage:\n```python\nimport numpy as np\nfrom lsnms import nms, wbc\n\n# Create boxes: approx 30 pixels wide / high\nimage_size = 10_000\nn_predictions = 10_000\ntopleft = np.random.uniform(0.0, high=image_size, size=(n_predictions, 2))\nwh = np.random.uniform(15, 45, size=topleft.shape)\nboxes = np.concatenate([topleft, topleft + wh], axis=1).astype(np.float64)\n# Create scores\nscores = np.random.uniform(0., 1., size=(len(boxes), ))\n\n# Apply NMS\n# During the process, only boxes distant from one another of less than 64 will be compared\nkeep = nms(boxes, scores, iou_threshold=0.5, score_threshold=0.1, cutoff_distance=64)\nboxes = boxes[keep]\nscores = scores[keep]\n\n# Apply WBC\npooled_boxes, pooled_scores, cluster_indices = wbc(boxes, scores, iou_threshold=0.5, score_threshold=0.1, cutoff_distance=64)\n```\n# Description\n## Non Maximum Suppression\n<!-- Non maximum suppression is an essential step of object detection tasks, aiming at pruning away multiple predictions actually predicting the same instance. This algorithm works greedily by sorting in decreasing order predicted boxes, and step by step, pruning away boxes having an high intersection over union with any other box with higher confidence score (it deletes all the non maximally-scored overlapping boxes). Picture below depicts the overall process: in the left image, several bounding boxes actuually predict the same instance (the model\'s face). In the right image, NMS was applied to prune away redundant boxes and keep only the highest scoring box.  \nNote: confidence score are not represented on this image.\n<p float="center">\n  <center><img src="./assets/images/nms_fast_03.jpeg" width="700" />\n  <figcaption>NMS example (source https://www.pyimagesearch.com/2015/02/16/faster-non-maximum-suppression-python/)</figcaption></center>\n</p> -->\nA nice introduction of the non maximum suppression algorithm can be found here: https://www.coursera.org/lecture/convolutional-neural-networks/non-max-suppression-dvrjH.  \nBasically, NMS discards redundant boxes in a set of predicted instances. It is an essential step of object detection pipelines.\n\n\n## Scaling up the Non Maximum Suppression process\n### Complexity\n* In the best case scenario, NMS is a **linear-complex** process (`O(n)`): if all boxes are perfectly overlapping, then one pass of the algorithm discards all the boxes except the highest scoring one.\n* In worst case scenario, NMS is a **quadratic-complex** operation (one needs to perform `n * (n - 1) / 2 ` iou comparisons): if all boxes are perfectly disconnected, each NMS step will discard only one box (the highest scoring one, by decreasing order of score).  Hence, one needs to perform `(n-1) + (n-2) + ... + 1 = n * (n - 1) / 2 ` iou computations.  \n### Working with huge images\nWhen working with high-dimensional images (such as satellital or histology images), one often runs object detection inference by patching (with overlap) the input image and applying NMS to independant patches. Because patches do overlap, a final NMS needs to be re-applied afterward.  \nIn that final case, one is close to be in the worst case scenario since each NMS step will discard only a very low amount of candidate instances (actually, pretty much the amount of overlapping passes over each instance, usually <= 10). Hence, depending on the size of the input image, computation time can reach several minutes on CPU.  \nA more natural way to speed up NMS could be through parallelization, like it is done for GPU-based implementations, but:\n1. Efficiently parallelizing NMS is not a straightforward process\n2. If too many instances are predicted, GPU VRAM will often not be sufficient, retaining one from using GPU accelerators\n3. The process remains quadratic, and does not scale well.\n### LSNMS\nThis project offers a way to overcome the aforementioned issues elegantly:\n1. Before the NMS process, a binary 2-dimensional tree is built on bounding boxes centroids (in a `O(n*log(n))` time)\n2. At each NMS step, boxes distant from less than a fixed radius of the considered box are queried in the tree (in a `O(log(n))` complexity time), and only those neighbors are considered in the pruning process: IoU computation + pruning if necessary. Hence, the overall NMS process is turned from a `O(n**2)` into a `O(n * log(n))` process. See a comparison of run times on the graph below (results obtained on sets of instances whose coordinates vary between 0 and 100,000 (x and y)). Note that the choice of the radius neighborhood is essential: the bigger the radius, the closer one is from the naive NMS process. On the other hand, if this radius is too small, one risks to produce wrong results. A safe rule of thumb is to choose a radius approximately equalling the size of the biggest bounding box of the dataset.\n\nNote that the timing reported below are all inclusive: it notably includes the tree building process, otherwise comparison would not be fair.\n\n<p float="center">\n  <center><img src="https://github.com/remydubois/lsnms/blob/main/assets/images/timingsxkcd.png" width="700" />\n  <figcaption>Run times (on a virtual image of 100kx100k pixels)</figcaption></center>\n</p>\n\n\nFor the sake of speed, this repo is entirely (including the binary tree) built using Numba\'s just-in-time compilation.\n\n>Concrete example:  \n>Some tests were ran considering ~ 40k x 40k pixels images, and detection inference ran on 512 x 512 overlapping patches (256-strided). Aproximately 300,000 bounding boxes (post patchwise NMS) resulted. Naive NMS ran in approximately 5 minutes on modern CPU, while this implementation ran in 5 seconds, hence offering a close to 60 folds speed up.\n\n### Going further: weighted box clustering\nFor the sake of completeness, this repo also implements a variant of the Weighted Box Clustering algorithm (from https://arxiv.org/pdf/1811.08661.pdf). Since NMS can artificially push up confidence scores (by selecting only the highest scoring box per instance), WBC overcomes this by averaging box coordinates and scores of all the overlapping boxes (instead of discarding all the non-maximally scored overlaping boxes).\n\n## Disclaimer: \n1. The binary tree implementation could probably be further optimized, see implementation notes below.\n2. Much simpler implementation could rely on existing KD-Tree implementations (such as sklearn\'s), query the tree before NMS, and tweak the NMS process to accept tree query\'s result. This repo implements it from scratch in full numba for the sake of completeness and elegance.\n3. The main parameter deciding the speed up brought by this method is (along with the amount of instances) the **density** of boxes over the image: in other words, the amount of overlapping boxes trimmed at each step of the NMS process. The lower the density of boxes, the higher the speed up factor.\n4. Due to numba\'s compiling process, the first call to each jitted function might lag a bit, second and further function calls (per python session) should not suffer this overhead.\n\n-> Will I benefit from this sparse NMS implementation ?\nAs said above, the main parameter guiding speed up from naive NMS is instance (or boxes) **density** (rather than image size or amount of instances):\n- If a million boxes overlap perfectly on a 100k x 100k pixels image, no speed up will be obersved (even a slow down, related to tree building time)\n- If 1,000 boxes are far appart from each other on a small image, the optimal speed up will be observed (with a good choice of neighborhood radius query)\n\n---\n# Implementations notes\nDue to Numba compiler\'s limitations, tree implementations has some specificities:  \nBecause jit-class methods can not be recursive, the tree building process (node splitting + children instanciation) can not be entirely done inside the `Node.__init__` method:\n* Otherwise, the `__init__` method would be recursive (children instanciation)\n* However, methods can call recursive (instance-external) functions: a `build` function is dedicated to this\n* Hence the tree building process must be as follows:\n```python\n# instanciate root\nroot = Node(data, leaf_size=16)\n# recursively split and attach children if necessary\nroot.build()  # This calls build(root) under the hood\n```\n* For convenience: a wrapper class `BallTree` was implemented, encapsulating the above steps in `__init__`:\n```python\ntree = BallTree(data, leaf_size=16)\n```\n\n* For the sake of exhaustivity, a `KDTree` class was also implemented, but turned out to be equally fast as the `BallTree` when used in the NMS:\n<p float="center">\n  <center><img src="https://github.com/remydubois/lsnms/blob/main/assets/images/timings_kd_versus_bt.png" width="700" />\n  <figcaption>Tree building times comparison</figcaption></center>\n</p>\n\n\n## Performances\nThe BallTree implemented in this repo was timed against scikit-learn\'s `neighbors` one. Note that runtimes are not fair to compare since sklearn implementation allows for node to contain\nbetween `leaf_size` and `2 * leaf_size` datapoints. To account for this, I timed my implementation against sklearn tree with `int(0.67 * leaf_size)`  as `leaf_size`.\n### Tree building time\n<p float="center">\n  <center><img src="https://github.com/remydubois/lsnms/blob/main/assets/images/building_timings.png" width="700" />\n  <figcaption>Trees building times comparison</figcaption></center>\n</p>\n\n\n### Tree query time\n<p float="center">\n  <center><img src="https://github.com/remydubois/lsnms/blob/main/assets/images/query_timings.png" width="700" />\n  <figcaption>Trees query times comparison (single query, radius=100) in a 1000x1000 space</figcaption></center>\n</p>\n\nQuery time are somehow identical.\n',
    'author': 'Rémy Dubois',
    'author_email': 'remydubois14@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/remydubois/lsnms',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
