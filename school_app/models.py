from django.db import models

# Create your models here.

class Message(models.Model):
    name=models.CharField(max_length=30, null=False)
    mail=models.EmailField()
    msg=models.TextField(max_length=100)
