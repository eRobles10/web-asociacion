from django.shortcuts import render, HttpResponse

# Create your views here.
"""
Inicio
Acerca de 
Contacto
Beneficios
Blog
Servicios

"""

def home(request):
    return render(request, "core/home.html")


def contact(request):
    return render(request, "core/contact.html")


def benefits(request):
   return render(request, "core/benefits.html")


def services(request):
   return render(request, "core/services.html")


