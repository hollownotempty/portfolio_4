from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import BookingForm


# Create your views here.

# msg_html = render_to_string('email_template.html')

plaintext_message = get_template('email_template.txt')
html_message = get_template('email_template.html')


def returnHome(request):
    return render(request, 'home.html')


def returnBookingPage(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid:
            email = request.POST.get('email', '')
            form.save()
            subject, from_email, recipient_list = 'Your Booking', settings.EMAIL_HOST_USER, [email, ]
            text_content = plaintext_message.render()
            html_content = html_message.render()
            msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('booking')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def returnAboutPage(request):
    return render(request, 'about.html')
