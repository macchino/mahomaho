from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_form/', views.contact_form, name='contact_form'),  
    path('complete/', views.complete, name='complete'), 
]