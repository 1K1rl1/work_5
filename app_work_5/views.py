from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement_2
from .forms import AdvForms
from django.urls import reverse
def index(request):
    advertisements = Advertisement_2.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)
    
def top_sellers(request):
    return render(request, 'top-sellers.html')
def adv_post(request):
    #form = AdvForms()
    #context = {'form':form  }
    #return render(request, 'advertisement-post.html', context)
    if request.method == 'POST':
        form = AdvForms(request.POST, request.FILES)
        if form.is_valid():
            advs = Advertisement_2(**form.cleaned_data)
            advs.user = request.user
            advs.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvForms()
        context = {'form':form}
    return render(request, 'advertisement-post.html', context)