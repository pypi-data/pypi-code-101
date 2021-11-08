from . import utils
from .dataset import Dataset
import seaborn as sns
sns.set_style('darkgrid') 

def загрузить_базу(база = ''):
    global ds
    ds = Dataset(база)
    ds.load_dataset()    

def показать_примеры():
    global ds
    ds.show_samples()
    
def создать_выборки():
    global ds
    ds.create_sampling()
    
def создать_сеть(слои):
    ds.create_model(слои)    
   
def обучить_модель(количество_эпох, количество_запусков=0):
    ds.train_model(количество_эпох, количество_запусков)
    
def тестировать_модель(data = None):
    ds.test_model(data)