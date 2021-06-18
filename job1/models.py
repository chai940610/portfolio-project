from django.db import models

class Job1(models.Model):
    image=models.ImageField(upload_to='happy/')
    summary=models.CharField(max_length=500)

# Create your models here.
