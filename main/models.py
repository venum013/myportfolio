from django.db import models

# Create your models here.
class CV(models.Model):
    cv = models.FileField(upload_to=None, max_length=100)