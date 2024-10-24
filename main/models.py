from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10,unique=True, blank=True, null=True, validators=[RegexValidator(regex=r"^\d{10}", message="Phone number must be 10 digits only.")])
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.CharField(max_length=2, default=3)
    otp_max_out = models.DateTimeField(blank=True, null=True)
class Prompt(models.Model):
    prompt = models.CharField(max_length=256)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)