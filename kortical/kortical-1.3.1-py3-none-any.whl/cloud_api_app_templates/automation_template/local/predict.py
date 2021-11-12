import pandas as pd
from module_placeholder.workflows import common, predict

if __name__ == "__main__":
    df = pd.read_csv("../data/animal_shelter_train.csv")
    _, _, df_test = common.create_train_calibrate_and_test_datasets(df)
    predict.predict(df_test)