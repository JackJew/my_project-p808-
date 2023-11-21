from django.shortcuts import render
from .models import ContactInfo, Appealing

def contact(request):
    contac_info = ContactInfo.objects.first()
    context  = {
        "contact_info" : contact_info
    }
    return render(request, 'contact/index.html ')