from django.shortcuts import render
from .models import About


def about(request):
    about = About.objects.first()
    context = {
        'about' : about
    }
    return render(request, 'about/index.html',context)    