from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import StandardScaler,OneHotEncoder

from customer_churn_model.config.core import config


scale=StandardScaler()
ohe=OneHotEncoder()
logreg=LogisticRegression()


ct=make_column_transformer(
    (ohe,categ_features),
    (scale,num_features),
    remainder='passthrough')

feature_selection=SelectKBest(k=6)

pipe_lg=make_pipeline(ct,feature_selection,logreg)
