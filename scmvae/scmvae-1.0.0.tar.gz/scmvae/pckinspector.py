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
from sklearn.decomposition import PCA
from scipy.stats.mstats import gmean
from sklearn.preprocessing import MinMaxScaler
import phenograph
from umap import UMAP
import umap.plot
from bokeh.plotting import show, save, output_notebook, output_file
import scanpy as sc
import tensorflow as tf
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Lambda, Input, Dense, Layer, Concatenate
from keras.losses import mean_squared_logarithmic_error, mean_squared_error
from keras.models import Model
from keras import regularizers
from keras import initializers
from keras import optimizers