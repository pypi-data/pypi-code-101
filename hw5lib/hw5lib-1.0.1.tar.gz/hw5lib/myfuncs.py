import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
ohe = OneHotEncoder(sparse=False,handle_unknown='error',drop='first')
import matplotlib.pyplot as plt

def read_data(x): # WORKING
    try:
        df = pd.read_csv(x)
    except FileNotFoundError:
        print('File does not exist')
    return df



def subset(x,y): # WORKING
    return x[y]



def splitter(df): # WORKING
    train, test = train_test_split(df, test_size=0.3)
    return train, test


def nan_dropper(x,y): # WORKING
    for item in y:
        x = x.dropna(subset=[item])
    return x




def nan_filler(x,y):
    for item in y:
        x[item] = x[item].transform(lambda x: x.fillna(x.mean()))




def cat_dummies(x,y): # WORKING
    cat_features_df = pd.DataFrame(ohe.fit_transform(x[y]), columns=ohe.get_feature_names()) # GENERATE DATAFRAME
                                                                     # WITH DUMMIES OF THE FEATURE
    x = x.join(cat_features_df)  # JOIN THE DATAFRAME WITH THE CATEGORICAL FEATURES AS DUMMIES
    for item in y:
        x = x.drop([item],axis=1) # REMOVE THE ORIGINAL CATEGORICAL VARIABLE FROM THE DATAFRAME
    return x



def log_regr(F,y,x_test):
    lregr = LogisticRegression(penalty='l2', C=100.0, fit_intercept=True, intercept_scaling=1, solver='liblinear',max_iter=500)
    lregr.fit(F, y)
    in_sample_preds = lregr.predict_proba(F)
    isp_df = pd.DataFrame(in_sample_preds[:,1],columns=['predictions'])
    test_sample_preds = lregr.predict_proba(x_test)
    tsp_df = pd.DataFrame(test_sample_preds[:,1],columns=['predictions'])
    return isp_df,tsp_df



def roc_curve(df,df_preds,target,preds):
    fpr, tpr, thresholds = metrics.roc_curve(df['target'], df_preds['preds'])
    roc_auc = metrics.auc(fpr, tpr)
    display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='example estimator')
    return display.plot()

def roc_curve(df,df_preds): # WORKING
    fpr, tpr, thresholds = metrics.roc_curve(df, df_preds)
    roc_auc = metrics.auc(fpr, tpr)
    display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='example estimator')
    return display.plot()



def total(x,y):
    return x+y

