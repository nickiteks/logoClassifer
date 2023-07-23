from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
import numpy as np
from skimage import io


# Create your views here.
def home(request):
    form = DataForm()
    context = {'form': form, }
    return render(request, 'RatingLogos/home.html', context)


def results(request):
    if request.method == 'POST':
        form = DataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            image = io.imread(f'media/media/{form.cleaned_data["file"]}')

            arr = np.array(image)



    context = {}
    return render(request, 'RatingLogos/results.html', context)
