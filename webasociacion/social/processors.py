from .models import Link

def context_dictionary(request):
    context = {'test':'hola'}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context