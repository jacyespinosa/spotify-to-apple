from datetime import datetime, timedelta
from urllib.parse import urlencode
import base64
import requests

'''Client ID and Client Secret can be retrieved from the user's Spotify account.'''
client_id = "ENTER CLIENT ID"
client_secret = "ENTER CLIENT SECRET"


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        client_id = self.client_id
        client_secret = self.client_secret

        if client_secret == None or client_id == None:
            raise Exception("Set client_id and client_secret")

        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_header()
        r = requests.post(token_url, data=token_data, headers=token_header)

        if r.status_code in range(200, 299):
            data = r.json()
            now = datetime.now()
            access_token = data['access_token']
            expires_in = data['expires_in']
            expires = now + timedelta(seconds=expires_in)
            self.access_token = access_token
            self.access_token_expires = expires
            self.access_token_did_expire = expires < now
            return True


    def get_spotify_tracks(self):
        spotify = SpotifyAPI(client_id, client_secret)
        spotify.perform_auth()

        access_token = spotify.access_token

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        finished = False
        OFFSET = 0
        playlist = []

        while not finished:
            playlist_id = "ENTER PLAYLIST ID"
            endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            data = urlencode({"offset": OFFSET, "limit": 100})
            look_up_url = f"{endpoint}?{data}"
            r = requests.get(look_up_url, headers=headers)
            r.raise_for_status()

            playlist_info = r.json()

            total_tracks = playlist_info['total']
            if total_tracks == len(playlist):
                finished = True

            else:
                for track_info in playlist_info['items']:
                    artist = track_info['track']['artists'][0]['name']
                    song = track_info['track']['name']
                    track = {f"{artist}": f"{song}"}
                    playlist.append(track)

            OFFSET += 100

        return playlist

s = SpotifyAPI.get_spotify_tracks(SpotifyAPI)