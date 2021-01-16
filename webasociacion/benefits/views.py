from django.shortcuts import render
from .models import Benefits

# Create your views here.
def benefits(request):
    benefits = Benefits.objects.all()
    return render(request, "benefits/benefits.html",{'benefits':benefits})

