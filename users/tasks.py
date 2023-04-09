from celery import shared_task
from users.models import Users, EmailVerification
import uuid
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_email_verification(user_id):
    user = Users.objects.get(user_id=user_id)
    explore_time = timezone.now() + timedelta(hours=24)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user,
                                              exploration=explore_time)
    record.send_verification_email()