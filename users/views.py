from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from users.models import Users
from games.models import Basket, purchase
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('products'))
#
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)


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


@login_required
def email_ver(request):
    return render(request, 'users/email_verification.html')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse(''))
