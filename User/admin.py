from django.contrib import admin
from User.models import Peoples

# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'profile_pic')

admin.site.register(Peoples,userAdmin)