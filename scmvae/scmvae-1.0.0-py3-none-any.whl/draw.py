import warnings
warnings.filterwarnings('ignore')
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
import seaborn as sns
import phenograph
from umap import UMAP
import umap.plot
from bokeh.plotting import show, save, output_notebook, output_file

def draw_loss(ae, title='Model Loss'):
  plt.plot(ae.history['loss'])
  plt.plot(ae.history['val_loss'])
  plt.title(title)
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(['Train','Validation'], loc = 'upper right')
  plt.show()
  plt.close("all")

high_contrast_colors = ['#649EFC', '#1FBFC3', 'blueviolet', '#CC6A6F', 'gold', 'brown', 'forestgreen', 'magenta', 'crimson', 'mediumpurple', 'orangered', 'skyblue', 'pink', '#F37726', 'yellowgreen', "#6D7176", "#2883B3", "#b8e986", "#BCC9E2", "#29705C", "#EA9D9E", "#d0021b", "#f5a623", "#f8e71c", "#8b572a", "#7ed321", "#417505", "#9013fe", "#50e3c2"]
cdict = high_contrast_colors
cmap_high_contrast_colors = LinearSegmentedColormap.from_list('high_contrast_colors', cdict)
cm.register_cmap(cmap=cmap_high_contrast_colors)

sns_high_contrast_colors = sns.color_palette("high_contrast_colors", 64)
camp_sns_high_contrast_colors = ListedColormap(sns_high_contrast_colors.as_hex())

def draw_umap(x, y, cell_type=None, hue="cell_type", **kwargs):
  if cell_type is None:
    tempdata = pd.DataFrame({
    "UMAP_1":x,
    "UMAP_2":y
    })
  else:
    tempdata = pd.DataFrame({
      "UMAP_1":x,
      "UMAP_2":y,
      "cell_type":cell_type
    })
  return sns.relplot(x="UMAP_1", y="UMAP_2", data=tempdata, hue=hue, **kwargs)

def draw_marker_umap(x, y, exp_value=None, hue="exp_value", **kwargs):
  tempdata = pd.DataFrame({
    "UMAP_1":x,
    "UMAP_2":y,
    "exp_value":exp_value
  })
  return sns.relplot(x="UMAP_1", y="UMAP_2", data=tempdata, hue=hue, **kwargs)

def bulid_umap(data, **kwargs):
  model_umap = UMAP(**kwargs)
  return model_umap.fit(data)

def build_interactive_umap(data, width=4.8, height=3.2, dpi=300, point_size=2, n_neighbors=30, min_dist=0.0, alpha=1):
    plt.figure(figsize=(width, height), dpi=dpi)
    model_umap = UMAP(n_neighbors=n_neighbors, min_dist=min_dist, n_components=2, verbose=0, random_state=123)    
    umap = model_umap.fit(data)
    
    return umap