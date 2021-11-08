#from GBT_RFI_Webpage.python_django_dev.aaron_gui.data_reader import *
from data_reader import *
import os

def search(rcvr):
    path = r"C:\Users\nukac\OneDrive\Documents\RFI"  #Insert path to rfi files
    file = os.listdir(path)
    for i in file:
        if i.endswith("{}.csv".format(rcvr)):
            return i



