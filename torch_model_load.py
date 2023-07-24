import torch
from skimage import io
from model.model3 import Net

collumns = ['Style', 'Noice', 'Place']
models = []

for col in collumns:
    model = Net()
    model.load_state_dict(torch.load(f'model/model{col}.pytorch'))
    model.eval()
    models.append(model)

print('123')
im = io.imread('Dataset_1/16.jpg')
im = torch.tensor(im, dtype=torch.float32)
im.transpose_(0,2)
im = torch.unsqueeze(im, 0)
for ml in models:
    print(ml(im))

#
# net = Net()
# net.load_state_dict(torch.load('model/model.pytorch'))
# net.eval()
#
# arr = io.imread('Dataset_1/16.jpg')
# X = torch.tensor(arr, dtype=torch.float32)
# X = torch.transpose(X,0,2)
#
# print(net(X))


