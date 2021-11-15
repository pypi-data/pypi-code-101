import numpy as np


def pre_processing(table_arr, working_mode, target_feature):
    table_arr = np.delete(table_arr, [0, 1], axis=1)  # remove the first two columns, which are irrelevant
    bound_low = target_feature[0] - 3
    bound_up = target_feature[1] - 3

    res = table_arr[:, bound_low:(bound_up+1)]

    res = res.astype(np.float32)

    # the 8th and 10th columns are negative, should be corrected to positive
    if working_mode < 2:
        res[:, 8] = -res[:, 8] + 10  # maximum value is 10
        res[:, 10] += 10
    res += 1
    processed = np.log(res)
    return processed


def re_ranging(prediction, target_range, current_range):
    # target_range: [min, max]
    # current_range: [min, max]
    prediction -= current_range[0]
    prediction /= (current_range[1] - current_range[0])

    prediction += target_range[0]
    prediction *= (target_range[1] - target_range[0])
    return prediction


def post_processing(prediction, score_min, score_max):
    for i in range(len(prediction)):
        if prediction[i] < score_min:
            prediction[i] = score_min
        if prediction[i] > score_max:
            prediction[i] = score_max

    return prediction
