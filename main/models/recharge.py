# models.py

from accounts.models import User
from django.db import models
from datetime import timedelta

class Recharge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recharge_time = models.DateTimeField(auto_now_add=True)
    validity_days = models.PositiveIntegerField(default=30)

    @property
    def valid_till(self):
        return self.recharge_time + timedelta(days=self.validity_days)

    def __str__(self):
        return f"{self.user.username} - {self.recharge_time}"
