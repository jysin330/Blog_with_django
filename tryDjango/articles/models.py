from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)