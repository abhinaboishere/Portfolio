from django.urls import path
from . import views


urlpatterns =[
    path("",views.home) #it call the home function from views.py
    
]