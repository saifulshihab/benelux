from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from beneluxapp.models import projects

def home(request):
     return render(request, 'beneluxapp/home.html')
     
def index(request):
     return render(request, 'beneluxapp/index.html')

def about(request):
     return render(request, 'beneluxapp/about.html')
     
def contact(request):
     return render(request, 'beneluxapp/contact.html')

def project(request):
     project_list = projects.objects.all()
     context = {'project_list': project_list}
     print(project_list)
     return render(request, 'beneluxapp/project.html', context)

def prijscalculator(request):    
     return render(request, 'beneluxapp/prijsberekening.html')

def diensten(request):
     return render(request, 'beneluxapp/diensten.html')

 
