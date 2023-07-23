from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
import numpy as np
from skimage import io
from xgboost import XGBClassifier


# Create your views here.
def home(request):
    form = DataForm()
    context = {'form': form, }
    return render(request, 'RatingLogos/home.html', context)


def results(request):
    y_pred = 0
    if request.method == 'POST':
        print('yes!!')
        # form = DataForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form.save()
        #
        #     image = io.imread(f'media/media/{form.cleaned_data["file"]}')
        #
        #     arr = np.array(image)
        #
        #     bst = XGBClassifier(n_estimators=50, max_depth=10, learning_rate=0.01, objective='multi:softprob')
        #     bst.load_model("ML_model/xgBoostModel.json")
        #
        #     data_x = [np.reshape(arr, (1, 400 * 400 * 3))[0]]
        #
        #     y_pred = bst.predict(data_x)

    context = {"Predict":y_pred}
    return render(request, 'RatingLogos/results.html', context)
