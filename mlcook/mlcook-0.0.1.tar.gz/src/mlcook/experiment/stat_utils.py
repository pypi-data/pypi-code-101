import pandas as pd
import numpy as np
import logging
from scipy.stats import chi2_contingency


def chi2_test(a: np.array, b: np.array):
    contingency_table = pd.crosstab(a, b)
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)
    return {'chi2_stat': chi2_stat,
            'p_value': p_value,
            'dof': dof,
            'contingency_table': contingency_table}


def get_stat_by_group(feature_values: np.array, by_values: np.array, feature_labels: list = None):
    """only for categorical features"""
    assert len(by_values) == len(feature_values)
    na_mask = pd.isnull(by_values) & pd.isnull(feature_values)
    if np.sum(na_mask) > 0:
        logging.info('warning: presence of missing values in either by_values or feature_values. Pairs with one value'
                     'missing are deleted')
        by_values = by_values[~na_mask]
        feature_values = feature_values[~na_mask]

    distribution_by = {}
    for value in pd.Series(by_values).unique():
        distribution = pd.Series(feature_values[by_values == value]).value_counts(normalize=True)
        if feature_labels is not None:
            distribution = distribution.reindex(feature_labels).fillna(0)
        distribution_by[value] = distribution
    return {'distribution_by': distribution_by, 'chi2_test': chi2_test(by_values, feature_values)}
