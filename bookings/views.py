from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import SubmitForm
from .models import Appointment


# Create your views here.

# msg_html = render_to_string('email_template.html')

plaintext_message = get_template('email_template.txt')
html_message = get_template('email_template.html')


def returnHome(request):
    return render(request, 'home.html')


def submit_page(request):

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid:
            instance = form.save()
            instance.user = request.user
            instance.save()
            email = request.POST.get('email', '')
            subject, from_email, recipient_list = 'Your Submission', settings.EMAIL_HOST_USER, [email, ]
            text_content = plaintext_message.render()
            html_content = html_message.render()
            msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('submit')

    form = SubmitForm()
    return render(request, 'booking.html', {'form': form})


def returnAboutPage(request):
    return render(request, 'about.html')


def return_appointments(request):
    return render(request, 'appointments.html', {
        'appointments': Appointment.objects.all(),
        })
