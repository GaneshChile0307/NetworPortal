from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=10)
    mac_address = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)