from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import login, registration, profile, email_ver, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('email_verification/', email_ver, name='email_ver'),
    path('logout/', logout, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)