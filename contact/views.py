from django.contrib import messages
from django.shortcuts import render

from contact.forms import ContactForm


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your message has been sent. We will get back to you soon.')
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
