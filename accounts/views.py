from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Successfully logged in!')
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, try again..."))
            return redirect('login.html')

    else:
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out!"))
    return redirect('home')


plaintext_message = get_template('signup_email.txt')
html_message = get_template('signup_email.html')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            login(request, user)
            subject, from_email, recipient_list = 'Thank you for signing up!', settings.EMAIL_HOST_USER, [email, ]
            text_content = plaintext_message.render()
            html_content = html_message.render()
            msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, ("Registration successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register_user.html', {
        'form': form,
    })


def view_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)
