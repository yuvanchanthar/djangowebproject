from django.db import models
from django.forms import ModelForm, Textarea

class Web(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
class Meta:
    db_table="web"



# Create your models here.
