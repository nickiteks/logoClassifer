import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class Simple(nn.Module):
    def __init__(self):
        super(Simple, self).__init__()
        self.sq = nn.Sequential(
            nn.Flatten(1),
            nn.Linear(480000,3)
        )

    def forward(self, x):
        # print(x.shape)
        x = self.sq(x)
        return x