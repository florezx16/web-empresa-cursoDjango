from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import contactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    active_page = 'contact_us'
    contact_form = contactForm()

    if request.method == 'POST':
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            content = contact_form.cleaned_data["content"]

            email = EmailMessage(
                'Nuevo mensaje de contacto',
                'de {}<{}>\n\nEscribio:\nHoliwis'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ['florezx15@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                print('error')
                return redirect(reverse('contact_us')+'?fail')
            finally:
                return redirect(reverse('contact_us')+'?ok')

    return render(request,'contact/contact.html',{'active_page':active_page,'contact_form':contact_form})