from django.shortcuts import render, HttpResponse
from benefits.models import Benefits
from blog.models import Blog, Post
from services.models import Services
from about.models import About
from django.shortcuts import get_object_or_404
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
    posts = Post.objects.all().order_by('id')[:5]
    benefits= get_object_or_404(Benefits, order=0)
    service_intro= Services.objects.get(title = "Introduccion")
    
    about = get_object_or_404(About, order=0)
    return render(request, "core/home.html",{'posts':posts , 
                                             'benefits':benefits,
                                             'service_intro':service_intro,
                                             'about':about})


def contact(request):
    return render(request, "core/contact.html")

