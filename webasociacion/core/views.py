from django.shortcuts import render, HttpResponse
from benefits.models import Benefits
from blog.models import Blog, Post
from services.models import Services
from about.models import About
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.shortcuts import render
# Create your views here.
"""
Inicio
Acerca de 
Contacto
Beneficios
Blog
Servicios

"""
class HomePageView(TemplateView):

    template_name ="core/home.html"
    posts = Post.objects.all().order_by('-created')[:5]
    benefits= get_object_or_404(Benefits, order=0)
    service_intro= Services.objects.get(title = "Introduccion")
    about = get_object_or_404(About, order=0)


    def get(self, request, **kwargs):    
        
        return render(request, self.template_name,{'posts':self.posts , 
                                             'benefits':self.benefits,
                                             'service_intro':self.service_intro,
                                             'about':self.about})






def contact(request):
    return render(request, "core/contact.html")

