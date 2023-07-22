from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.
def home(request):
    if (request.method == 'POST'):
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            # img_object = form.instance
            return redirect('RatingLogos-results')
    else: 
        form = DataForm()
    context = {
        'form': form,
        # 'img_obj': img_object
    }
    return render(request, 'RatingLogos/home.html', context)

def results(request):
    rated_logo = Data.objects.all().first()
    context={
        'rated_logo': rated_logo
    }
    return render(request, 'RatingLogos/results.html', context)
    # return render(request, 'RatingLogos/results.html')