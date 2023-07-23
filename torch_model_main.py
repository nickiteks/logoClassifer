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

image_dir = 'Dataset_1'
img_size_x = 400
img_size_y = 400
img_count_chanel = 3

dataset = pd.read_csv('data/preprocess_data.csv')
images = []

for label in dataset['label']:
    images.append(io.imread(f'Dataset_1/{label}'))
# numpy.random.seed(42)

print(len(images))
print(len(dataset))
print(dataset)

data_x = torch.tensor(images, dtype=torch.float32)
data_x = torch.transpose(data_x, 1, 3)
print(data_x.shape)
data_y = torch.tensor(dataset[dataset.columns[1:]].values, dtype=torch.float32)
print(data_y.shape)

X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25)

net = Net()
loss_fn = nn.L1Loss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

loss_list = []

for epoch in range(10):
    loss_ar = 0
    for i in range(len(X_train)):
        optimizer.zero_grad()

        pred = net(X_train[i])

        loss = loss_fn(pred, y_train[i])
        loss.backward()
        loss_ar += loss
        optimizer.step()

    loss_list.append((loss_ar/len(X_train)).detach().numpy())

net.eval()

preds = []

plt.plot(loss_list)
plt.savefig('Image/loss_train.jpg')

for i in range(len(X_test)):
    preds.append(net(X_test[i]).detach().numpy())
print('0'*100)
print(y_test.shape)

preds = torch.tensor(np.array(preds))
print(preds.shape)

print(F.l1_loss(torch.tensor(preds),y_test))

torch.save(net.state_dict(), 'model/model.pytorch')
