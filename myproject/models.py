from django.db import models

class search(models.Model):
    name = models.CharField(max_length=200)