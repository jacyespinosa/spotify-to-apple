import json

from spotify import SpotifyAPI
from apple import AppleMusic
import requests


'''SPOTIFY'''
CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER SECRET ID"

'''APPLE'''
APPLE_KEY = "ENTER APPLE KEY"
TEAM_ID = "ENTER APPLE TEAM ID"
SECRET_KEY = '''-----BEGIN PRIVATE KEY-----
ENTER SECRET KEY HERE
-----END PRIVATE KEY-----'''

apple = AppleMusic(APPLE_KEY, TEAM_ID, SECRET_KEY)
ACCESS_TOKEN = apple.get_authorization()


spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
get_tracks = apple.get_songs_from_spotify(spotify.get_spotify_tracks())

'''CREATE APPLE MUSIC LIBRARY'''
LIBRARY_URL = "https://api.music.apple.com/v1/me/library/playlists"
header = ACCESS_TOKEN
LIBRARY_PAYLOAD = {"attributes":
                       {"name": "ENTER PLAYLIST NAME"}
                   }

playlist_response = requests.post(LIBRARY_URL, data=json.dumps(LIBRARY_PAYLOAD), headers=header)
playlist_response_json = playlist_response.json()



