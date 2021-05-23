from django.db import models
from django.db.models.fields.related import ForeignKey

class Dojo (models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Ninja (models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    Dojo_id=models.ForeignKey( Dojo,related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)