from django.db import models

# Create your models here.
class Peoples(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=13)
    profile_pic = models.ImageField(upload_to="images/")

    class Meta:
        db_table = 'peoples'