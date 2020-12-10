from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from beneluxapp.models import projects
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
     return render(request, 'beneluxapp/home.html')
     
def index(request):
     return render(request, 'beneluxapp/index.html')
     
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

def over(request):
     return render(request, 'beneluxapp/over.html')

def sendMessageToClient(request):
     if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          topic = request.POST['topic']
          message = request.POST['message']
          if(name == '' or email == '' or topic == '' or message == '' ):
               context = {"error": "true", 'msg': "Please fill all input box correctly!"}
          else:
               template = render_to_string('beneluxapp/success.html', {'name': name, 'email': email, 'topic': topic, 'message': message})
               email = EmailMessage(
                    'New message from customer',
                    template,
                    settings.EMAIL_HOST_USER,
                    ['a.shakib.abubaker@gmail.com']
               )
               email.fail_silently=False
               email.send()
               context = {"error": "false", 'msg': "Thank you! You message has been received."}                              
          return render(request, 'beneluxapp/contact.html', context)     
     else:
          return render(request, 'beneluxapp/contact.html')     

def reqQuote(request):
     if request.method == "POST":
          f_name = request.POST['f_name']
          l_name = request.POST['l_name']
          phone = request.POST['phone']
          shift = request.POST['shift']
          message = request.POST['message']
          if(f_name == '' or l_name == '' or phone == '' or shift == '' or message == '' ):
               context = {"error": "true", 'msg': "Please fill all input box correctly!"}
          else:
               template = render_to_string('beneluxapp/successQuote.html', {'f_name': f_name, 'l_name': l_name, 'phone': phone, 'shift': shift, 'message': message})
               email = EmailMessage(
                    'New quotes from customer!',
                    template,
                    settings.EMAIL_HOST_USER,
                    ['a.shakib.abubaker@gmail.com']
               )
               email.fail_silently=False
               email.send()
               context = {"error": "false", 'msg': "Thank you! You message has been received."}                              
          return render(request, 'beneluxapp/index.html', context)     
     else:
          return render(request, 'beneluxapp/index.html')     
