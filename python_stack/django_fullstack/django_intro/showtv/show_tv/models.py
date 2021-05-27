from django.db import models
from django.db.models.fields import CharField,DateTimeField
class Shows (models.Model):
    title = models.CharField(max_length=255)
    network= models.TextField(null=True)
    releasedate= models.DateField(max_length=255)
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

