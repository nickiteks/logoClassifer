from django.shortcuts import render
from .forms import DataForm
from skimage import io
import torch
import torch.nn as nn
import torch.nn.functional as F


# Create your views here.
def home(request):
    form = DataForm()
    context = {'form': form, }
    return render(request, 'RatingLogos/home.html', context)


def results(request):
    y_pred = 0
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            class Net(nn.Module):
                def __init__(self):
                    super().__init__()
                    self.conv1 = nn.Conv2d(3, 6, 5)
                    self.pool = nn.MaxPool2d(3, 3)
                    self.conv2 = nn.Conv2d(6, 16, 5)
                    self.fc1 = nn.Linear(28224, 120)
                    self.fc2 = nn.Linear(120, 84)
                    self.fc3 = nn.Linear(84, 3)

                def forward(self, x):
                    x = self.pool(F.relu(self.conv1(x)))
                    x = self.pool(F.relu(self.conv2(x)))
                    x = torch.flatten(x, 0)  # flatten all dimensions except batch
                    x = F.relu(self.fc1(x))
                    x = F.relu(self.fc2(x))
                    x = self.fc3(x)
                    return x

            net = Net()

            net.load_state_dict(torch.load("/Users/nikita/PycharmProjects/logoClassifer/ML_Model/model.pytorch"))
            net.eval()

            arr = io.imread(f'media/media/{form.cleaned_data["file"]}')
            X = torch.tensor(arr, dtype=torch.float32)
            X = torch.transpose(X, 0, 2)

            y_pred = [int(i) for i in net(X).detach().numpy()]

            # image = io.imread(f'media/media/{form.cleaned_data["file"]}')
            #
            # arr = np.array(image)
            #
            # bst = XGBClassifier(n_estimators=50, max_depth=10, learning_rate=0.01, objective='multi:softprob')
            # bst.load_model("ML_model/xgBoostModel.json")
            #
            # data_x = [np.reshape(arr, (1, 400 * 400 * 3))[0]]
            #
            # y_pred = bst.predict(data_x)

    context = {"Predict": y_pred}
    return render(request, 'RatingLogos/results.html', context)