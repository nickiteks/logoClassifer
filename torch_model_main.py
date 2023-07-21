import numpy as np
import numpy.random
from PIL import Image
from numpy import asarray
import os
from skimage import io
import skimage
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


count_image = 100

image = io.imread('Logos/bat-logo-preview-400x400.png')

# plotting the original image
i, (im1, im2, im3, im4) = plt.subplots(1, 4, sharey=True)
i.set_figwidth(20)

im1.imshow(image)  # Original image
im2.imshow(image[:, :, 0])  # Red
im3.imshow(image[:, :, 1])  # Green
im4.imshow(image[:, :, 2])  # Blue
i.suptitle('Original & RGB image channels')

oldpwd = os.getcwd()

os.chdir('Logos')

files = os.listdir()

data_x = []

for index in range(count_image):
    image = io.imread(files[index])

    arr = np.array(image)

    data_x.append(arr.tolist())
    # data_x.append(np.reshape(arr, (1, 400 * 400 * 4))[0].tolist())

os.chdir(oldpwd)

numpy.random.seed(42)
data_y = numpy.random.random(count_image)
print(len(data_x))
print(len(data_y))

import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(4, 6, 5)
        self.pool = nn.MaxPool2d(3, 3)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(28224, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 1)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 0)  # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()

loss_fn = nn.L1Loss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

data_x = torch.tensor(data_x, dtype=torch.float32)
data_x = torch.transpose(data_x, 1, 3)
print(data_x.shape)
data_y = torch.tensor(data_y, dtype=torch.float32)
print(data_y.shape)

for epoch in range(10):
    loss_ar = 0
    for i in range(count_image):
        optimizer.zero_grad()

        pred = net(data_x[i])

        loss = loss_fn(pred, data_y[i])
        loss.backward()
        loss_ar += loss
        optimizer.step()

    print(loss_ar/count_image)

image = io.imread('Logos/nike-golf-vector-logo-400x400.png')

arr = np.array(image)
print(arr.shape)
test = torch.tensor(arr, dtype=torch.float32)
print(test.shape)
test = torch.transpose(test, 0,2)
print(test.shape)
print('-'*100)
net.eval()
print(net(test))
print(data_y)
