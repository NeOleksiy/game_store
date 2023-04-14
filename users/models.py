from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings


class Users(AbstractUser):
    img = models.ImageField(upload_to='media/users_img', null=True, blank=True)
    verificationStatus = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    exploration = models.DateTimeField()

    def __str__(self):
        return f'Email Verification: {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_ver', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подверждение учетной записи для {self.user.username}'
        message = 'для подтверждения учётной записи {} перейдите по ссылке{}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def explore(self):
        return True if timezone.now() >= self.exploration else False
