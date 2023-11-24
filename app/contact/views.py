from django.shortcuts import redirect, render 
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import AppealingForm
from .models import ContactInfo

def contact(request):
    contact_info = ContactInfo.objects.first()
    form = AppealingForm()
    if request.method == 'POST':
        form = AppealingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' Мы приняли ваш запрос, постараемся ответить как можно быстрее)')
            
            return redirect(reverse_lazy('contact'))

    context  = {
        "contact_info" : contact_info,
        'form' : form
    }
    
    return render(request, 'contact/index.html ', context)

 