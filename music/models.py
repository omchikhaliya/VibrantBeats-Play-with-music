from django.db import models

# Create your models here.
class audio(models.Model):
    name = models.CharField(max_length=50)
    size = models.FloatField()
    upload_date = models.DateField()
    language = models.CharField(max_length=50)
    duration = models.DurationField()
    thumbnail = models.ImageField(upload_to="images/")
    audio_file = models.FileField(upload_to="audio/")
    description = models.TextField(max_length=100)
    type = models.CharField(max_length=20)
    artist = models.TextField(max_length=50)