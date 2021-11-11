import pkg_resources
import pandas as pd

def load_jobs():
    """
    A dataset containing 50 random job descriptions, titles,
    and IDs.

    Contains the following fields:
        index        50 non-null int
        job_id       50 non-null str
        title        50 non-null str
        description  50 non-null str
    """
    stream = pkg_resources.resource_stream(__name__, 'data/job_desc.csv')
    return pd.read_csv(stream)