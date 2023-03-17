from django.urls import path


from users.views import login, registration, profile, email_ver, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('email_verification/', email_ver, name='email_ver'),
    path('logout/', logout, name='logout')
]