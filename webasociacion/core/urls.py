from django.urls import path
from . import views 

urlpatterns = [

    #paths de core
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
]
