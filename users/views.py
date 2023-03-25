from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.models import Users
from games.models import Basket


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
                return HttpResponseRedirect(reverse('index'))

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


@login_required
def profile(request):
    if request.method == "POST":
        prof_form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if prof_form.is_valid():
            prof_form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(prof_form.errors)
    else:
        prof_form = UserProfileForm(instance=request.user)

    context = {
        'null': 0,
        'prof_form': prof_form,
        'users': Users,
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context)


@login_required
def email_ver(request):
    return render(request, 'users/email_verification.html')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
