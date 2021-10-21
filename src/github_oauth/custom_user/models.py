from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(
        max_length=128, blank=True
    )  # limited to a single field for simplicity
    prev_address = models.CharField(max_length=128, blank=True)
