from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from beneluxapp.models import projects
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import over_para, diensten_para

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
     diensten_data = diensten_para.objects.all()
     context = {'diensten_para': diensten_data}
     return render(request, 'beneluxapp/diensten.html', context)

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
     over_data = over_para.objects.all()
     context = {'over_para': over_data}
     return render(request, 'beneluxapp/over.html', context)

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
                    'Nieuwe bericht van een bezoeker',
                    template,
                    settings.EMAIL_HOST_USER,
                    ['info@beneluxdakkapellen.nl']
               )
               email.fail_silently=False
               email.send()
               context = {"error": "false", 'msg': "Bedankt, uw bericht is in goede orde ontvangen."}                              
          return render(request, 'beneluxapp/contact.html', context)     
     else:
          return render(request, 'beneluxapp/contact.html')     

def reqQuote(request):
     if request.method == "POST":
          f_name = request.POST['f_name']
          l_name = request.POST['l_name']
          email = request.POST['email']
          phone = request.POST['phone']
          shift = request.POST['shift']
          message = request.POST['message']
          if(f_name == '' or l_name == '' or email == '' or phone == '' or shift == '' or message == '' ):
               context = {"error": "true", 'msg': "Vul aub alle velden correct in!"}
          else:
               template = render_to_string('beneluxapp/successQuote.html', {'f_name': f_name, 'l_name': l_name, 'email': email, 'phone': phone, 'shift': shift, 'message': message})
               email = EmailMessage(
                    'Nieuwe offerte van bezoeker!',
                    template,
                    settings.EMAIL_HOST_USER,
                    ['info@beneluxdakkapellen.nl']
               )
               email.fail_silently=False
               email.send()
               context = {"error": "false", 'msg': "Bedankt! Uw bericht is in goede staat ontvangen."}
          return render(request, 'beneluxapp/index.html', context)     
     else:
          return render(request, 'beneluxapp/index.html')

def _calc_msgsend(request):
     if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          tel = request.POST['tel']
          street = request.POST['street']
          postcode = request.POST['postcode']
          msg = request.POST['msg']

          if(name == '' or email == '' or tel == '' or street == '' or postcode == '' or msg == '' ):
               context = {"error": "true", 'msg': "Vul aub alle velden correct in!"}
          else:
               template = render_to_string('beneluxapp/cal_msg_quote.html', {'name': name, 'email': email, 'tel': tel, 'street': street, 'postcode': postcode, 'msg': msg})
               email = EmailMessage(
                    'Nieuwe offerte van bezoeker!',
                    template,
                    settings.EMAIL_HOST_USER,
                    ['info@beneluxdakkapellen.nl']
               )
               email.fail_silently=False
               email.send()
               context = {"error": "false", 'msg': "Bedankt! Uw bericht is in goede staat ontvangen."}
          return render(request, 'beneluxapp/prijsberekening.html', context)          
