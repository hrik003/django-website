from django.db import models

# Create your models here.
class Enquiry(models.Model):
    en_name = models.CharField(max_length=255)
    en_email = models.EmailField(max_length=255)
    en_phone = models.BigIntegerField()
    en_message = models.TextField()