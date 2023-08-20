from django.http  import HttpResponse
from django.shortcuts import render
from music.models import audio
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import webbrowser
import urllib.parse
import json
from requests import *
from django.http import JsonResponse


def homepage(request):
    return render(request,"index.html")

def profile(request):
    return render(request,"profile.html")

def fetch_song(request):
    username = 'om chikhaliya'
    clientID = '54a2cfa981f84349a4ec90f647e935f6'
    clientSecret = 'f15e303a720f43798b003c3ec3ae7594'
    redirect_uri = 'http://google.com/callback/'
    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    # if request.method == 'POST':
    # search_song = input('enter song name: ')
    search_song = request.POST['song-query']
    results = spotifyObject.search(search_song, 1, 0, "track")

    track_uri = results['tracks']['items'][0]['uri']
    track = spotifyObject.track(track_uri)
    track_name = track['name']
    track_artists = [artist['name'] for artist in track['artists']]
    track_album = track['album']['name']
    track_preview_url = track['preview_url']

    # Get track metadata
    api_url = "https://api.spotify.com/v1"
    track_id = results["tracks"]["items"][0]["id"]
    track_url = f"{api_url}/tracks/{track_id}"
    track_response = requests.get(track_url, headers={"Authorization": f"Bearer {token}"})
    track_data = track_response.json()
    album_id = track_data["album"]["id"]
    album_url = f"{api_url}/albums/{album_id}"  
    album_response = requests.get(album_url, headers={"Authorization": f"Bearer {token}"})
    album_data = album_response.json()
    thumbnail_url = album_data["images"][0]["url"]
    context = {
        'track_name': track_name,
        'track_artists': track_artists,
        'track_album': track_album,
        'track_preview_url': track_preview_url,
        'track_thumbnail': thumbnail_url,
    }

    return render(request, 'mp_template2.html', context)
