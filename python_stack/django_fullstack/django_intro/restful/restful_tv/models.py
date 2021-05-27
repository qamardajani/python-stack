from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
class Shows (models.Model):
    title = models.CharField(max_length=255)
    network= models.TextField(null=True)
    releasedate= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

