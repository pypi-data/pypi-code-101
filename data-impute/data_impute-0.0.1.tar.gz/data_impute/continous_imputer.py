class cont_impute:
# Continuous Missing Values Handling Types

# Mean Imputation
    def meanImputation(df, feature):
        mean = df[feature].mean()
        df[feature] = df[feature].fillna(mean)
    # Mean Imputation

    # Median Imputation
    def medianImputation(df, feature):
        median = df[feature].median()
        df[feature] = df[feature].fillna(median)
    # Median Imputation

    # Random Sample Imputation
    def randomSampleImputation(df, feature):
        df[feature] = df[feature]
        random_sample = df[feature].dropna().sample(df[feature].isnull().sum(), random_state=0)
        random_sample.index = df[df[feature].isnull()].index
        df.loc[df[feature].isnull(), feature] = random_sample
    # Random Sample Imputation

    # End of Distribution Imputation
    def endOfDistributionImputation(df, feature):
        extreme = df[feature].mean() + 3 * df[feature].std()
        df[feature] = df[feature].fillna(extreme)
    # End of Distribution Imputation

    # Continuous Missing Values Handling Types
