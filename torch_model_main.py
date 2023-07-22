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

count_image = 101
image_dir = 'Dataset_1'
img_size_x = 400
img_size_y = 400
img_count_chanel = 3

oldpwd = os.getcwd()

os.chdir(image_dir)

files = os.listdir()

data_x = []

for index in range(count_image):
    image = io.imread(files[index])
    arr = np.array(image)
    data_x.append(arr.tolist())

os.chdir(oldpwd)

# numpy.random.seed(42)
data_y = numpy.random.random(count_image)
print(len(data_x))
print(len(data_y))

data_x = torch.tensor(data_x, dtype=torch.float32)
data_x = torch.transpose(data_x, 1, 3)
print(data_x.shape)
data_y = torch.tensor(data_y, dtype=torch.float32)
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

    loss_list.append((loss_ar/count_image).detach().numpy())

net.eval()

preds = []

plt.plot(loss_list)
plt.savefig('Image/loss_train.jpg')

for i in range(len(X_test)):
    preds.append(net(X_test[i]))

print(F.l1_loss(torch.tensor(preds),y_test))

torch.save(net, 'model/model.pytorch')
