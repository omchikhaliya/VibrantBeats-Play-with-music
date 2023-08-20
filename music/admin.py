from django.contrib import admin
from music.models import audio
# Register your models here.

class audioAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'upload_date', 'language', 'duration', 'thumbnail', 'audio_file', 'description', 'type', 'artist')

admin.site.register(audio,audioAdmin)