from django.db import models

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=250)
    body = models.TextField()