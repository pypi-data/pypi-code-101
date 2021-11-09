import numpy as np
import pandas as pd
from numpy import ndarray as NDArray
import skimage
import statistics
import sklearn
from tqdm import tqdm

__all__ = ['AverageMeter', 'compute_pro_score', 'estimate_thred_with_fpr']

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def compute_pro_score(amaps: NDArray, masks: NDArray) -> float:
    # from skimage import measure
    # from statistics import mean

    df = pd.DataFrame([], columns=["pro", "fpr", "threshold"])
    binary_amaps = np.zeros_like(amaps, dtype=np.bool)

    max_step = 200
    min_th = amaps.min()
    max_th = amaps.max()
    delta = (max_th - min_th) / max_step

    for th in tqdm(np.arange(min_th, max_th, delta), desc="compute pro"):
        binary_amaps[amaps <= th] = 0
        binary_amaps[amaps > th] = 1

        pros = []
        for binary_amap, mask in zip(binary_amaps, masks):
            for region in skimage.measure.regionprops(skimage.measure.label(mask)):
                axes0_ids = region.coords[:, 0]
                axes1_ids = region.coords[:, 1]
                TP_pixels = binary_amap[axes0_ids, axes1_ids].sum()
                pros.append(TP_pixels / region.area)

        inverse_masks = 1 - masks
        FP_pixels = np.logical_and(inverse_masks, binary_amaps).sum()
        fpr = FP_pixels / inverse_masks.sum()

        df = df.append({"pro": statistics.mean(pros), "fpr": fpr, "threshold": th}, ignore_index=True)

    return sklearn.metrics.auc(df["fpr"], df["pro"])

def estimate_thred_with_fpr(scores, max_step=1000, expect_fpr=0.05):
        """
        Use training or validation set to estimate the threshold.
        """
        threshold = 0
        min_th = scores.min()
        max_th = scores.max()
        delta = (max_th - min_th) / max_step
        for step in range(max_step):
            threshold = max_th - step * delta
            # segmentation
            binary_score_maps = np.zeros_like(scores)
            binary_score_maps[scores <= threshold] = 0
            binary_score_maps[scores > threshold] = 1

            # estimate the optimal threshold base on user defined min_area
            fpr = binary_score_maps.sum() / binary_score_maps.size

            if fpr >= expect_fpr:  # find the optimal threshold
                break
        return threshold