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


'''ADD TRACKS TO PLAYLIST'''
PLAYLIST_ID = playlist_response_json['data'][0]['id']
print(PLAYLIST_ID)
PLAYLIST_URL = f'https://api.music.apple.com/v1/me/library/playlists/{PLAYLIST_ID}/tracks'

spotify_playlist_length = len(apple.list_of_track_id)
i = 0

while i < spotify_playlist_length:
    song_id = get_tracks[i]
    params = {
        "data": [
            {
                "id": f"{song_id}",
                "type": "songs"
            },
        ]
    }

    add_tracks = requests.post(PLAYLIST_URL, headers=header, data=json.dumps(params))
    results = add_tracks.status_code

    i += 1
