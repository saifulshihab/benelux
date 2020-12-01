from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
     return render(request, 'beneluxapp/home.html')
     
def index(request):
     return render(request, 'beneluxapp/index.html')