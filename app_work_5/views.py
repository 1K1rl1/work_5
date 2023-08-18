from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement_2
def index(request):
    advertisements = Advertisement_2.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)
    
def top_sellers(request):
    return render(request, 'top-sellers.html')