from data_impute import impute


def run(df):
    try:
        impute.missing_values_handling(df)
        print("After handling")
        missing_values_percentage = (df.isnull().sum() / len(df)) * 100
        print(missing_values_percentage)
    except Exception as e:
        print(e)