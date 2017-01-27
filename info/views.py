from django.shortcuts import render, HttpResponse
#from django.conf import settings
#from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
    send = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
#            send_mail('Subject here', 'Here is the message.', 'from@example.com',['ftaeml@gmail.com'], fail_silently=False)

            form.save()
            send = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'info/contact.html', {'form': form, 'send': send,})

def about(request):
    return render(request,"info/about.html")

