import numpy as np


def make_log_refl(*labels):
    labels = labels_to_df(labels)
    return np.log10(generator.simulate_reflectivity(labels[prediction.columns], progress_bar=False)[0])


def labels_to_df(labels):
    columns = ['Film_thickness', 'Film_roughness', 'Film_sld', 'SiOx_thickness']
    labels = pd.DataFrame(data=np.atleast_2d(labels), columns=columns)
    for column in prediction.columns:
        if column not in columns:
            labels[column] = float(prediction[column])
    return labels[prediction.columns]


def log_likelihood(labels, measured_intensity, stdev, function):
    model = function(*labels)
    variance = stdev ** 2
    return -0.5 * np.sum((measured_intensity - model) ** 2 / variance + np.log(2 * np.pi * variance))


def negative_log_likelihood(labels, measured_intensity, stdev, function):
    return -log_likelihood(labels, measured_intensity, stdev, function)


def log_prior(labels, limits):
    if all([within(labels[i], limits[i]) for i in range(len(limits))]):
        return 0.0
    return -np.inf


def within(a, limits):
    return limits[0] < a < limits[1]


def log_probability(labels, limits, y, stdev, function):
    return log_likelihood(labels, y, stdev, function) + log_prior(labels, limits)
