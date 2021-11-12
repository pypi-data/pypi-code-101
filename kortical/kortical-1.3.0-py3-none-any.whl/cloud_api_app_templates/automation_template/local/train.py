import pandas as pd
from module_placeholder.workflows import train, common

if __name__ == "__main__":
    df = pd.read_csv("../data/animal_shelter_train.csv")
    df_train, df_calibrate, df_test = common.create_train_calibrate_and_test_datasets(df)
    train.train(df_train, df_calibrate, df_test)
