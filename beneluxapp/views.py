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

def fienanciering(request):
     return render(request, 'beneluxapp/fienanciering.html')

def werkwijze(request):
     return render(request, 'beneluxapp/werkwijze.html')

def begrippen(request):
     return render(request, 'beneluxapp/begrippen.html')
def faq(request):
     return render(request, 'beneluxapp/faq.html')
def dakkapelPrijzen(request):
     return render(request, 'beneluxapp/dakkapel-prijzen.html')
def dakkapelVergunning(request):
     return render(request, 'beneluxapp/dakkapel-vergunning.html')
def dakkapelVergunningsvrij(request):
     return render(request, 'beneluxapp/dakkapel-vergunningsvrij.html')
def garanties(request):
     return render(request, 'beneluxapp/garanties.html')
def kenmerken(request):
     return render(request, 'beneluxapp/kenmerken.html')
def kostenDakkapel(request):
     return render(request, 'beneluxapp/kosten-dakkapel.html')
def prefabDakkapel(request):
     return render(request, 'beneluxapp/prefab-dakkapel.html')
def prijslijstVergunning(request):
     return render(request, 'beneluxapp/prijslijst-vergunning.html')
def rolluiken(request):
     return render(request, 'beneluxapp/rolluiken-in-het-overstek.html')
def scree(request):
     return render(request, 'beneluxapp/screens-in-het-overstek.html')
def van(request):
     return render(request, 'beneluxapp/van-offerte-tot-montage.html')

 
