from datetime import time
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# import time as timecounter

from .columns import targets, time_columns, label_encoders, error_codes, groups, exclude, predictors, group_starts_with
from .important_features import get_important_features


def encode(df, output_df, label_encoders):
    for column in label_encoders:  # for each column where label encoding is necessary

        for i, label in enumerate(label_encoders[column]):  # for each label in column
            df.loc[df[column]==label, column] = i
        x = df[column]
        x = x.fillna(i+1)
        output_df[column] = x
    return


def process_error_codes(df, output_df, code_columns):
    for column in code_columns:
        output_df[column] = df[column].fillna(0)
    return


def reduce_dim(df, columns, dim, pca):
    X = df[columns]
    X = X.fillna(0)

    group_key = ','.join(columns)
    if group_key not in pca:
        # print('not in pca: ', group_key)
        pca[group_key] = PCA(n_components=dim)
        pca[group_key].fit(X)

    X = pca[group_key].transform(X)
    return X


def load_columns(df, output_df, groups, kvr_duo_delta_columns, dim, pca):
    group_id = 0
    for columns in groups:
        if isinstance(columns, list): # convolve
            columns_in_df = list(set(columns) & set(kvr_duo_delta_columns))
            if not columns_in_df:
                continue
            columns_in_df.sort()
            output_df[f'Group_{columns[0]}'] = reduce_dim(df, columns_in_df, dim, pca)
            group_id+=1
        else:
            output_df[columns] = df[columns]
    return


def load_targets(df, Y, targets):
    for y in targets:
        Y[y] = df[targets[y]].mean(axis=1)
    return


# TO DO: to change when Filters_date is added
def time2num(df, columns):
    for column in columns:
        df[column] = df[column].astype(str)
        df[column] = df[column].apply(lambda x: np.dot(np.array(x.split(':'), dtype=float), np.array([1.0, 1.0/60, 1.0])))
    return


def flatten(t):
    flat_list = []
    for sublist in t:
        if isinstance(sublist, list):
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    return flat_list


def get_pca_key_for_features(columns):
    keys = []
    for col in columns:
        if isinstance(col, list):
            key = ','.join(col)
            keys.append(key)
    return keys


class Data_Preprocessor:

    def __init__(self, features, targets, pca={}):
        self.pca = pca
        self.features = features
        self.targets = targets

        if features:
            self.is_features_invoked = True
        else:
            # default
            self.is_features_invoked = False

        self.mode = 'predict' if pca else 'train'

    def get_pca(self):
        return self.pca

    def get_important_features(self):
        return self.features

    def preprocess(self, df):
        reduced_group_dim = 1

        # 1. drop
        if self.mode == 'train':
            filtered = set(df[df['NOMP'].str.contains('П')].index) | set(df[df['NOMP'].str.contains('У')].index) | set(df[df['NOMP'].str.startswith('9')].index)
            df.drop(index=list(filtered), inplace=True)

        not_startswith = ['ДУО_ПРОХ', 'ДУО_ХОЛОСТ', 'ДУО_Т_3_ПР', 'ДУО_Т_ПОСЛ',
                          'КВР_Т_ПЛАН', 'КВР_Т_1_ПР', 'КВР_Т_ПОСЛ', 'КВР_ПРОХ',
                          'КВР_ХОЛОСТ', 'ДУО_ВРЕМЯ', 'ДУО_КВР', 'КВР_ВРЕМЯ']

        data = pd.DataFrame()
        Y = pd.DataFrame()

        # this way there is no need in rewriting whole preproccessing
        # for case when df is pd.Series, not pd.DataFrame
        # it will be used ONLY when self.predict is invoked
        # because no fitting with 1 test rows is possible
        if isinstance(df, pd.Series):
            df = pd.DataFrame(columns=df.keys(), data=[df, df], index=[0, 1])

        time2num(df, time_columns)
        encode(df, data, label_encoders)
        process_error_codes(df, data, error_codes)

        # an array with КВР, ДУО и DELTA columns for correct PCA compression
        # print("features: ", self.features)
        kvr_duo_delta_columns = []
        if self.is_features_invoked:
            kvr_duo_delta_columns = [col for col in self.features
                                    if ((col.startswith('КВР') or col.startswith('ДУО') or col.startswith('DELTA'))
                                    and not (col in not_startswith))]
        else:
            kvr_duo_delta_columns = df.columns
        # print("kvr_duo_delta_columns: ", kvr_duo_delta_columns)
        load_columns(df, data, groups, kvr_duo_delta_columns, reduced_group_dim, self.pca)

        if data.shape[0] == 0:
            raise ValueError('0 rows in dataset after filtering')

        print(data)

        if self.mode == 'predict':
            data.fillna(np.nan, inplace=True)
            return data

        elif self.mode == 'train':
            load_targets(df, Y, {target:targets[target] for target in self.targets})
            print(Y)

            # getting important features
            if not self.is_features_invoked:
                temp = set()
                for target in self.targets:
                    fts = data.drop(exclude[target], axis=1, errors='ignore')

                    # start_time = timecounter.time()
                    important_columns = get_important_features(fts, Y[target])
                    # print("--- Getting important features for %s: %s seconds ---" % (target, (timecounter.time() - start_time)))

                    if len(important_columns)==0:
                        raise ValueError('0 allowed predictors chosen')
                    print(target, '             ', important_columns)
                    temp.update(important_columns)

                # print('     ', temp)
                temp = [
                        col if col in predictors
                        else group_starts_with[col]
                        for col in list(temp)
                ]
                # print("----->", temp)
                self.features = list(flatten(temp))
                # print(self.features)

                # leave in self.pca only important pca transformers
                important_pca_keys = get_pca_key_for_features(temp)
                self.pca = {key: self.pca[key] for key in important_pca_keys}

            print('Before fitting self.features: ', self.features)
            print(data.columns, Y.columns)
            return pd.concat([data, Y], axis=1)
