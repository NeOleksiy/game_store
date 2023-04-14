from django.shortcuts import HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from users.models import Users, EmailVerification
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class RegistrationView(SuccessMessageMixin, CreateView):
    model = Users
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    SuccessMessageMixin = 'Вы успешно зарегестрированы'


class ProfileView(UpdateView):
    model = Users
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Users.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(code=code, user=user)
        if email_verification.exists() and not email_verification.first().explore():
            user.verificationStatus = True
            user.save()
            return super(EmailVerificationView, self).get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('products'))
