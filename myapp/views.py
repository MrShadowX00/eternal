from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"app/index.html")
def index_ru(request):
    return render(request,"appru/index.html")
def index_en(request):
    return render(request,"appen/index.html")
