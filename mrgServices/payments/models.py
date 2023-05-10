from django.conf import settings
from django.db import models
from django.utils import timezone


class Payments(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title