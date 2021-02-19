from django.urls import path
from . import views 

app_name = 'TemplateApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
]