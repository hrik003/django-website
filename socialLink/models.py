from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class SocialLink(models.Model):
    sl_name = models.CharField(max_length=255)
    sl_url = models.CharField(max_length=255)
    sl_icon = models.FileField(upload_to="social/",max_length=255,null=True,default=None)
    sl_slug = AutoSlugField(populate_from='sl_name',unique=True,null=True,default=None)