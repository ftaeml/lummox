from django.shortcuts import render
#from django.conf import settings
#from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
#            send_mail('Subject here', 'Here is the message.', 'from@example.com',['ftaeml@gmail.com'], fail_silently=False)

            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'info/contact.html', {'form': form})

def about(request):
    return render(request,"info/about.html")

