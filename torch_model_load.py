import torch
from skimage import io
from model.model import Net

net = Net()
net.load_state_dict(torch.load('model/model.pytorch'))
net.eval()

arr = io.imread('Dataset_1/16.jpg')
X = torch.tensor(arr, dtype=torch.float32)
X = torch.transpose(X,0,2)

print(net(X))


