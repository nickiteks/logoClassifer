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
from model.model3 import Net
import pandas as pd
from tqdm import tqdm


is_dataset = True
images = []
epoches = 20
chanels = 3
collumns = ['Style', 'Noice', 'Place']

if (is_dataset):
    dataset = pd.read_csv('data/preprocess_data.csv')
    for label in dataset['label']:
        images.append(np.array(io.imread(f'Dataset_1/{label}')))
else:
    count_image = 500
    names = os.listdir('Logos')
    for im in names[:count_image]:
        images.append(np.array(io.imread(f'Logos/{im}')))
images = np.array(images)

x_tensor = torch.tensor(images, dtype=torch.float32)
x_tensor = torch.transpose(x_tensor, 1, 3)
if is_dataset:
    y_tensor = torch.tensor(dataset[dataset.columns[1:]].values-1)
else:
    marks = np.random.randint(1, 10, (count_image,3))
    y_tensor = torch.tensor(marks)
print(x_tensor.shape)
print(y_tensor.shape)
models = []
index = 0
for index in range(0,3):
    x_train, x_test, y_train, y_test = train_test_split(x_tensor, y_tensor[:,index], test_size=0.25)
    print(x_train.shape, y_train.shape)


    model = Net(chanels)
    optimizer = optim.SGD(model.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()

    losses = []
    for epoch in tqdm(range(epoches)):
        optimizer.zero_grad()
        preds = model(x_train)
        loss = loss_fn(preds,y_train)
        loss.backward()
        optimizer.step()

        losses.append(loss.item())
    print(collumns[index])
    print(f"{losses[-1]}")
    print(f'{F.cross_entropy(model(x_test), y_test)}')
    # print(f'{F.cross_entropy(model(torch.cat([x_test,x_train])), torch.cat(y_test,y_train))}')
    print('-'*20)
    torch.save(model.state_dict(), f'model/model{collumns[index]}.pytorch')