import requests
from django.http import HttpResponse
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import webbrowser
import urllib.parse
import json
from requests import *
from django.http import JsonResponse
from spotipy.oauth2 import SpotifyOAuth

def fetch_playlist(request):
    clientId = '63b5dc4558c142f0b67dff00a0b8237c'
    clientSecret = 'fec1cfe64c8d46ddb58069e1bf9f5c19'
    # Step 1 - Authorization 
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')


    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)
    token = r.json()['access_token']


    oauth_object = spotipy.SpotifyOAuth(clientId, clientSecret, url)
    spotifyObject = spotipy.Spotify(auth=token)
    name = request.POST['playlist-query']
    results = spotifyObject.search(q=name, type='playlist')
    playlist = results['playlists']['items'][0]
    playlistId = playlist['id']
    playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
    headers = {
        "Authorization": "Bearer " + token
    }
    res = requests.get(url=playlistUrl, headers=headers)
    playlist_data = json.loads(res.content)
    tracks = playlist_data['tracks']['items']

    track_urls = []
    for track in tracks:
        track_urls.append(track['track']['preview_url'])

    track_name = []
    for track in tracks:
        track_name.append(track['track']['name'])
    

    track_thumbnail = []
    for track in tracks:
        if len(track['track']['album']['images']) > 0:
            track_thumbnail.append(track['track']['album']['images'][0]['url'])
    
    zipped_list = zip(track_urls,track_name,track_thumbnail)
    context = {
        'name': playlist_data['name'],
        'description': playlist_data['description'],
        'tracks': [track['track']['name'] for track in playlist_data['tracks']['items']],
        'track_urls' : track_urls,
        'track_name' : track_name,
        'zlist' : zipped_list,
        # 'track_thumbnail' : track_thumbnail,
    }
    return render(request,"index2.html",context)

