import pandas as pd
from pandas.api.types import is_integer_dtype, is_numeric_dtype, is_object_dtype  # noqa


__all__ = [
    'is_target_dtype_valid',
    'are_classes_balanced',
    'has_no_missing_values',
    'are_features_numeric'
]


def is_target_dtype_valid(problem: str, target: pd.Series):
    if problem == 'classification':
        assert is_integer_dtype(target) or is_object_dtype(target), \
            "Target column dtype must be either integer or object (string)."
    elif problem == 'regression':
        assert is_numeric_dtype(target), "Target column dtype must be numeric."


def are_classes_balanced(target: pd.Series, threshold: float = 0.1):
    class_count = target.groupby(target).count()
    return (class_count / class_count.max()).min() >= threshold


def has_no_missing_values(data: pd.DataFrame):
    assert not data.isnull().any(None), "Data should not contain NaN values."  # noqa


def are_features_numeric(df_feat: pd.DataFrame):
    assert all(map(lambda col: is_numeric_dtype(df_feat[col]), df_feat)), "All features must be numeric."
