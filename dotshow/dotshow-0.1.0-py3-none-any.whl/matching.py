import numpy as np
from PIL import Image
from sys import stdout
from .under import under_sampling
from .weight import weight_match

def dotshow(arr, gray=True, size=7):
    d_arr, real = under_sampling(arr, size=size)
    print("__"*real[0])
    for line in d_arr:
        print("|", end="")
        for var in line:
            val = weight_match(var, gray)
            print(val, end=" ")
        print("|")
    print("__"*real[0])

def __stdshow__(arr, gray=True, size=7):
    d_arr, real = under_sampling(arr, size=size)
    stdout.write("__"*real[0]+"\n")
    for line in d_arr:
        stdout.write("|")
        for var in line:
            val = weight_match(var, gray)
            stdout.write(val+" ")
        stdout.write("|"+"\n")
    stdout.write("__"*real[0]+"\n")

def loadshow(path, gray=True, size=7):
    img = np.array(Image.open(path))
    dotshow(img, gray, size)