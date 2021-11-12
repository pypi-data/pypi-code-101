import pandas as pd
from module_placeholder.workflows import superhuman_calibration, common

if __name__ == "__main__":
    df = pd.read_csv("../data/animal_shelter_train.csv")
    _, df_calibrate, df_test = common.create_train_calibrate_and_test_datasets(df)
    superhuman_calibration.superhuman_calibration(df_calibrate, df_test)