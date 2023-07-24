import numpy as np
import numpy.random
import os
from skimage import io
import matplotlib.pyplot as plt
import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from model.model import Net
import pandas as pd

images = []

names = os.listdir('Logos')

size = 200

for im in names[:size]:
    images.append(io.imread(f'Logos/{im}'))

marks = np(size)

print(marks)
