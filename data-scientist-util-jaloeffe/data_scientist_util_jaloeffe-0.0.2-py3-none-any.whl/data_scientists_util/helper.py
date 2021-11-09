import pandas as pd
from datetime import datetime
import csv
import joblib
from datetime import datetime

def write_output(predicted_outcome, input_dir='../input', submission_dir='../submission'):
    t = pd.read_csv('{}/train.csv'.format(input_dir))
    dump = [int(element) for index, element in enumerate(predicted_outcome, start=len(t))]
    now = datetime.now()
    filename = '{}/submission-{}-{}-{}_{}-{}-{}.csv'.format(submission_dir, now.year, now.month, now.day, now.hour,
                                                            now.minute, now.second)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('id', 'sales'))
        writer.writerows((index, element) for index, element in enumerate(dump, start=len(t)))

    return filename


def read_pre_processed_data(pre_processed_dir='../pre_processed_input'):
    X_train = pd.read_csv('{}/train.csv'.format(pre_processed_dir))
    Y_train = pd.read_csv('{}/train_target.csv'.format(pre_processed_dir))
    X_valid = pd.read_csv('{}/validation.csv'.format(pre_processed_dir))
    Y_valid = pd.read_csv('{}/validation_target.csv'.format(pre_processed_dir))
    X_test = pd.read_csv('{}/test.csv'.format(pre_processed_dir))

    return X_train, Y_train, X_valid, Y_valid, X_test


def is_in_num_columns(name, columns_to_check):
    for column in columns_to_check:
        if name == column:
            return True
    return False


# This function takes the column names of a pandas dataframe and the processed columns of a sklearn pipeline. It then generates
# the original order of columns of the dataframe.
def get_ordered_columns(original_features, processed_columns):
    ordered_columns = []
    # We can not use sets because sets are not ordered
    for feature in original_features:
        is_present = is_in_num_columns(feature, processed_columns)
        if not is_present:
            ordered_columns.append(feature)

    processed_columns_cp = processed_columns.copy()
    processed_columns_cp.extend(ordered_columns)
    return processed_columns_cp


def dump_model(grid_search, type='best_estimator', path='../best_models'):
    now = datetime.now()
    date_time = now.strftime("%m_%d_%Y-%H%M%S")

    model_name = str(round(grid_search.best_score_, 5)).replace('.', ',')
    joblib.dump(grid_search.best_estimator_, "%s/%s-%s-%s.pkl" % (path, model_name, type, date_time))


def load_model(name, path='../models'):
    model = joblib.load("{}/{}.pkl".format(path, name))
    if model is not None:
        return model

    raise FileNotFoundError
