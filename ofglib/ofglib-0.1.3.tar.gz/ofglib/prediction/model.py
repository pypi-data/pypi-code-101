import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
from pyod.models.abod import ABOD
# from sklearn.manifold import TSNE
# from sklearn.cluster import DBSCAN
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.model_selection import train_test_split

import time

from .columns import targets, time_columns, label_encoders, error_codes, groups, exclude, predictors, group_starts_with
from .preprocessing import time2num, encode, process_error_codes, load_columns, load_targets
from .important_features import get_important_features

sns.set()


class MechModel:
    def __init__(self, targets, features, pca):
        self.targets = targets
        self.features = features
        self.pca = pca

        self.performance = {key: {} for key in self.targets}
        self.models = {}
        self.tsne_images = {}

    # a function to replace string elements in list
    def _list_replace(self, lst: list[str], to_replace: str, value: str):
        for i, element in enumerate(lst):
            if element == to_replace:
                lst[i] = value[:-2]+'01'
        return lst

    def _colapse_features_list(self):
        prefixes_to_replace = [
            'ДУО_ОБЖ', 'ДУО_УСС', 'ДУО_УСП', 'ДУО_СКР',
            'КВР_ОБЖ', 'КВР_УСС', 'КВР_УСП', 'КВР_СКР',
            'DELTA'
        ]

        features_temp = self.features.copy()
        for prefix in prefixes_to_replace:
            columns_with_prefix = [col for col in features_temp
                                   if col.startswith(prefix)]
            for column in columns_with_prefix:
                features_temp = self._list_replace(features_temp, column,
                                                   f'Group_{columns_with_prefix[0]}')
            features_temp = list(set(features_temp))
        return features_temp

    def to_features(self, data, target=''):

        # ex: ['ДУО_СКР_01', 'ДУО_СКР_02] -> Group_ДУО_СКР_01
        features_temp = self._colapse_features_list()

        # below: were used when 'Group_' was
        # be able to be named with not only _01
        # features_temp = list(set(features_temp)&set(predictors))

        set_exclude = set(exclude[self.targets[0]])
        for tar in self.targets:
            if tar != self.targets[0]:
                set_exclude &= set(exclude[tar])

        # features_temp = list(set(features_temp)-set(exclude[target]))
        features_temp = list(set(features_temp)-set_exclude)

        # return data.drop(exclude[target], axis=1, errors='ignore')
        return data[features_temp]

    def fit(self, df):  # mode=1

        data, Y = df[df.columns.difference(self.targets)], df[self.targets]
        # print(data, Y)
        print('Before fitting: ', self.features)

        # TO DO: change with multioutput model

        # 5. fit multioutput model
        X = self.to_features(data)
        print('Fitting ', self.targets, ',\n    predictors: ', X.columns)
        start_time = time.time()
        self.fit_multioutput_model(X, Y)
        print("--- Fitting multioutput model: %s seconds ---" % (time.time() - start_time))

        # deprecated: fit models for each target
        # for target in self.targets:
        #     X = self.to_features(data, target)
        #     print('Fitting ', target, ', predictors: ', X.columns)
        #     self.fit_model(X, Y[target], target)  # mode

        return 0

    def fit_multioutput_model(self, X, Y):
        X, Y = X.values, Y.values

        # 1. drop nan
        sl = ~np.logical_or(np.isnan(X).any(axis=1), np.isnan(Y).any(axis=1))
        X, Y = X[sl], Y[sl]

        if X.shape[0]==0:
            raise ValueError('0 samples without NaN for fitting')

        # 2. filter out
        outlier_detector = ABOD(contamination=0.1, n_neighbors=5, method='fast')
        XY = np.hstack((X, Y))

        # normalization
        XY_scaled = (XY - XY.min(axis=0)) / (XY.max(axis=0) - XY.min(axis=0))

        outlier_detector.fit(XY_scaled)
        outliers = outlier_detector.predict(XY_scaled)
        normal = outliers!=1
        X, Y = X[normal], Y[normal]

        if X.shape[0]==0:
            raise ValueError('0 samples after outliers filtering')
        print(X.shape[0])

        # 3. Set up model
        model = RandomForestRegressor(n_estimators=60)
        # 4. Calc performance
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

        if len(self.targets)==1:
            Y = Y.ravel()
            y_train = y_train.ravel()
            y_test = y_test.ravel()

        model.fit(X_train, y_train)
        y_pred_train = model.predict(X_train).T
        y_pred_test = model.predict(X_test).T
        y_train = y_train.T
        y_test = y_test.T

        # 5. Train model
        model.fit(X, Y)

        self.models = model

        y_pred = model.predict(X).T
        Y = Y.T

        if len(self.targets)==1:
            target = self.targets[0]
            self.performance[target]['Samples'] = X.shape[0]
            self.performance[target]['MAE'] = np.round(mae(Y, y_pred), 2)
            self.performance[target]['P95'] = np.round(np.percentile(np.abs(Y-y_pred), 95), 2)
            self.performance[target]['MAE train'] = np.round(mae(y_train, y_pred_train), 2)
            self.performance[target]['MAE test'] = np.round(mae(y_test, y_pred_test), 2)
        else:
            for i, target in enumerate(self.targets):
                self.performance[target]['Samples'] = X.shape[0]
                self.performance[target]['MAE'] = np.round(mae(Y[i], y_pred[i]), 2)
                self.performance[target]['P95'] = np.round(np.percentile(np.abs(Y[i]-y_pred[i]), 95), 2)
                self.performance[target]['MAE train'] = np.round(mae(y_train[i], y_pred_train[i]), 2)
                self.performance[target]['MAE test'] = np.round(mae(y_test[i], y_pred_test[i]), 2)

        return 0

    def fit_model(self, X, y, target):  # mode
        print('fitting ', target)
        X, y = X.values, y.values

        # 1. drop nan
        sl = ~np.logical_or(np.isnan(X).any(axis=1), np.isnan(y))
        X, y = X[sl], y[sl]

        if X.shape[0]==0:
            raise ValueError('0 samples without NaN for fitting')
        # 2. filter out

        # if mode==2:
        outlier_detector = ABOD(contamination=0.1, n_neighbors=5, method='fast')
        XY = np.hstack((X, y.reshape(-1, 1)))

        # normalization
        XY_scaled = (XY - XY.min(axis=0)) / (XY.max(axis=0) - XY.min(axis=0))

        outlier_detector.fit(XY_scaled)
        outliers = outlier_detector.predict(XY_scaled)
        normal = outliers!=1
        X, y = X[normal], y[normal]

        # elif mode==3:
        #     X_embedded = TSNE(
        #         n_components=2, learning_rate=200, init='random'
        #         ).fit_transform(X)
        #     # save image
        #     self.save_image(X_embedded, y, target)
        #     clustering = DBSCAN(eps=10, min_samples=5).fit(np.hstack((X_embedded, y.reshape(-1,1))))
        #     normal = clustering.labels_ != -1
        #     X, y = X[normal], y[normal]

        if X.shape[0]==0:
            raise ValueError('0 samples after outliers filtering')
        self.performance[target]['Samples'] = X.shape[0]
        print(X.shape[0])

        # 3. Set up model
        model = RandomForestRegressor(n_estimators=60)
        # 4. Calc performance
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        model.fit(X_train, y_train)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        # 5. Train model
        model.fit(X, y)
        self.models[target] = model

        y_pred = model.predict(X)
        self.performance[target]['MAE'] = np.round(mae(y, y_pred), 2)
        self.performance[target]['P95'] = np.round(np.percentile(np.abs(y-y_pred), 95), 2)
        self.performance[target]['MAE train'] = np.round(mae(y_train, y_pred_train), 2)
        self.performance[target]['MAE test'] = np.round(mae(y_test, y_pred_test), 2)

        return 0

    def save_image(self, X, y, target):
        si = np.argsort(y)
        fig, ax = plt.subplots(1, figsize=(10,10))
        sns.scatterplot(x=X[si, 0], y=X[si, 1], hue=y[si],
                        legend=True,
                        s=50, alpha=0.8,
                        palette='icefire', linewidth=0.3, edgecolor='k')
        #sns.set(rc={'figure.figsize':(30,30)})

        plt.title(target, weight='bold').set_fontsize('14')
        plt.xlabel('Component 1', weight='bold').set_fontsize('14')
        plt.ylabel('Component 2', weight='bold').set_fontsize('14')

        # plt.show()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        self.tsne_images[target] = buf
        return

    def predict(self, data):
        # print(data.shape)

        Y = ()
        X = data[self._colapse_features_list()].values

        if X.shape[0]==1:
            sl = np.isnan(X)
            if np.any(sl):
                raise Exception('''Prediction from this data is impossible:
                                not enough data in the features.\n''')
            X = np.nan_to_num(X).reshape(1, -1)
            Y = self.models.predict(X)
        else:
            sl = np.isnan(X).any(axis=1)
            X = np.nan_to_num(X)
            Y = self.models.predict(X)
            Y[sl] = np.nan

        # print(Y)
        return pd.DataFrame(data=Y, columns=self.targets, index=data.index)
        # return pd.DataFrame(index=df.index, columns=self.targets, data=Y) #.fillna(0)

    def __predict(self, data): # old predict
        print(data.shape)

        Y = ()
        for target in self.targets:
            X = data[self._colapse_features_list()].values
            print(target, X)
            if X.shape[0]==1:
                sl = np.isnan(X)
                if np.any(sl):
                    raise Exception('''Prediction from this data is impossible:
                                     not enough data in the features.\n''')
                X = np.nan_to_num(X).reshape(1, -1)
                y = self.models[target].predict(X)
            else:
                sl = np.isnan(X).any(axis=1)
                X = np.nan_to_num(X)
                y = self.models[target].predict(X)
                y[sl] = np.nan
            Y += (y,)

        Y = np.vstack(Y).T
        # print(Y)
        return pd.DataFrame(data=Y, columns=self.targets, index=data.index)
        # return pd.DataFrame(index=df.index, columns=self.targets, data=Y) #.fillna(0)



if __name__ == "__main__":
    model = MechModel(['FPT', 'FVS'])
    df = pd.read_csv('D:/work/17Г1С-У.csv')

    print(df.head(5))
    print(model.features)

    model.fit(df, None)
    print(model.features)
    print(model.performance)
