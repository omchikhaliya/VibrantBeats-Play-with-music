from django.urls import path
from .views import fetch_playlist

urlpatterns = [
    path('', fetch_playlist, name='fetch_playlist'),
]
