from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from users.models import Users, EmailVerification
from games.models import Basket, purchase
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

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        baskets = Basket.objects.filter(user=self.object)
        quantity_product = lambda product_id, purchase_method_id: Basket.objects.filter(user=self.object,
                                                                                        product=product_id,
                                                                                        purchaseMethod=purchase_method_id).first().quantity
        decimal = lambda product_id, purchase_id: purchase.objects.get(name=product_id,
                                                                       purchaseMethod=purchase_id).price * quantity_product(
            product_id, purchase_id)
        context['total_sum'] = sum(decimal(basket.product, basket.purchaseMethod) for basket in baskets)
        context['total_quantity'] = sum(basket.quantity for basket in baskets)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


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
