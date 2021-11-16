import numpy as np
class cat_impute:
# Categorical Missing Values Handling Types

# Frequent Category Imputation
    def frequentCategoryImputation(df,feature):
        most_frequent_category=df[feature].value_counts().index[0]
        df[feature].fillna(most_frequent_category,inplace=True)
    # Frequent Category Imputation

    # Capturing NaN with a new feature Imputation
    def captureNaNwithFeatureImputation(df, feature):
        df[feature+"_new"] = np.where(df[feature].isnull(), 1, 0)
    # Capturing NaN with a new feature Imputation

    # Capturing NaN with a new category Imputation
    def captureNaNwithCategoryImputation(df, feature):
        df[feature+"_new"]=np.where(df[feature].isnull(),"Missing",df[feature])
    # Capturing NaN with a new category Imputation

    # Categorical Missing Values Handling Types
