from django.urls import path
from . import views

urlpatterns = [
    path('', views.usage, name='usage'),
    path('hello', views.hello, name='hello'),    
]