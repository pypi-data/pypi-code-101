import numpy as np
import pickle

def save_obj(data, fillepath):
  with open(fillepath, 'wb') as f:
    pickle.dump(data, f)
  
  return 1

def load_obj(filepath):
  tempobj = None
  with open(filepath, 'rb') as f:
    tempobj = pickle.load(f)

  return tempobj

def get_omic_exp(omic_andata, omic_name):
  omic_names = omic_andata.index
  return omic_andata.iloc[np.where(omic_name==omic_names)].values[0]

def manual_cell_annotation (clustering_label, celltype_dict):
  clustering_label_copy = np.array(clustering_label.copy()).astype("str")
  for key in celltype_dict:
    clustering_label_copy[np.where(clustering_label_copy==key)] = celltype_dict[key]
  
  return clustering_label_copy