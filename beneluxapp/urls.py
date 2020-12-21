from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('diensten/', views.diensten, name='diensten'),
    path('project/', views.project, name='project'),
    path('prijscalculator/', views.prijscalculator, name='prijscalculator'),
    path('contact/', views.contact, name='contact'),
    path('fienanciering/', views.fienanciering, name='fienanciering'),
    path('werkwijze/', views.werkwijze, name='werkwijze'),
    path('begrippen/', views.begrippen, name='begrippen'),
    path('faq/', views.faq, name='faq'),
    path('dakkapel-prijzen/', views.dakkapelPrijzen, name='dakkapel-prijzen'),
    path('dakkapel-vergunning/', views.dakkapelVergunning, name='dakkapel-vergunning'),
    path('dakkapel-vergunningsvrij/', views.dakkapelVergunningsvrij, name='dakkapel-vergunningsvrij'),
    path('garanties/', views.garanties, name='garanties'),
    path('kenmerken/', views.kenmerken, name='kenmerken'),
    path('kosten-dakkapel/', views.kostenDakkapel, name='kosten-dakkapel'),
    path('prefab-dakkapel/', views.prefabDakkapel, name='prefab-dakkapel'),
    path('prijslijst-vergunning/', views.prijslijstVergunning, name='prijslijst-vergunning'),
    path('rolluiken-in-het-overstek/', views.rolluiken, name='rolluiken-in-het-overstek'),
    path('screens-in-het-overstek/', views.scree, name='screens-in-het-overstek'),
    path('van-offerte-tot-montage/', views.van, name='van-offerte-tot-montage'),
    path('sendMessage/', views.sendMessageToClient, name='sendMessage'),
    path('_calc_form_submit/', views._calc_msgsend, name='_calc_form_submit'),
    path('reqQuote/', views.reqQuote, name='reqQuote'),
    path('over/', views.over, name='over'),
    
]