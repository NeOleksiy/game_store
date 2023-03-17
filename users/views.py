from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from users.models import Users


# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('games:index'))

    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        reg_form = UserRegistrationForm(data=request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        reg_form = UserRegistrationForm()
    context = {
        'reg_form': reg_form,
    }
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == "POST":
        prof_form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(prof_form.errors)
    else:
        prof_form = UserProfileForm(instance=request.user)

    context = {
        'prof_form': prof_form,
    }
    return render(request, 'users/profile.html', context)


def email_ver(request):
    return render(request, 'users/email_verification.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
