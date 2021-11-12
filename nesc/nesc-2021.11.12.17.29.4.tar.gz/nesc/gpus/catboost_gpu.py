# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 12:24:21 2018
@author: Administrator
"""
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import catboost as cb
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X, y = cancer.data, cancer.target
train_x, test_x, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

cat_features_index = [0, 1, 2, 3, 4, 5, 6]


def auc(m, train, test):
    return (metrics.roc_auc_score(y_train, m.predict_proba(train)[:, 1]),
            metrics.roc_auc_score(y_test, m.predict_proba(test)[:, 1]))


params = {'depth': [4, 7, 10],
          'learning_rate': [0.03, 0.1, 0.15],
          'l2_leaf_reg': [1, 4, 9],
          'iterations': [300]}
cb = cb.CatBoostClassifier(task_type="GPU",
                           learning_rate=0.01,
                           iterations=1000, verbose=1000)
# cb_model = GridSearchCV(cb, params, scoring="roc_auc", cv = 5)
cb.fit(train_x, y_train)

print("accuracy on the training subset:{:.3f}".format(cb.score(train_x, y_train)))
print("accuracy on the test subset:{:.3f}".format(cb.score(test_x, y_test)))
'''
accuracy on the training subset:1.000
accuracy on the test subset:0.982
'''