import pandas as pd

def json_write_dataframe_list(dataframe_list):
    json_dataframe_list = []
    for dataframe in dataframe_list:
        json_dataframe_list.append(json_write_dataframe(dataframe))
    return json_dataframe_list

def json_read_dataframe_list(json_dataframe_list):
    dataframe_list = []
    for json_dataframe in json_dataframe_list:
        dataframe_list.append(json_read_dataframe(json_dataframe))
    return dataframe_list

def json_write_dataframe(dataframe):
    return dataframe.to_json(orient='table')

def json_read_dataframe(json_dataframe):
    return pd.read_json(json_dataframe, orient='table')