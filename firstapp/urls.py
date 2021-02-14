from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('Hello', views.index, name='index'),
]