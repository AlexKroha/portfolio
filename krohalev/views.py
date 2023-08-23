from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    template = 'base.html'
    sent = False
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # Form was submitted
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            from_email = cd['from_email']
            subject = cd['subject']
            message = cd['message']
            send_mail(f'{subject} от {from_email}', message, 'sash20052@gmail.com',
                      ['sash20052@gmail.com'])
            sent = True
    else:
        form = ContactForm()
    return render(request, template, {'form': form,
                                      'sent': sent})





