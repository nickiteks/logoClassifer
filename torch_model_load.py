import torch
from skimage import io

net = torch.load('model/model.pytorch')
net.eval()

arr = io.imread('Dataset_1/18.jpg')

print(int(net(torch.transpose(torch.tensor(arr, dtype=torch.float32),0,2))*10))


