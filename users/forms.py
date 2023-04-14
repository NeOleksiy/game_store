from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import Users
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите логин"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"
    }))

    class Meta:
        model = Users
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите Имя"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите фамилию"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите логин"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите адрес эл. почты"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    img = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "custom-file-input"
    }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4", 'readonly': True}))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'img', 'username', 'email')
