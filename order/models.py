from django.db import models
from users.models import Users


class Order(models.Model):
    CREATED = 0
    PAID = 1
    STATUS = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUS)
    initiator = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    want_scamed = models.BooleanField(default=False)


