import datetime
from dateutil.relativedelta import *

from urllib.parse import urlencode

import jwt
import requests


'''SPOTIFY'''
CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER CLIENT SECRET"

'''APPLE'''
APPLE_KEY = "ENTER APPLE KEY"
TEAM_ID = "ENTER APPLE TEAM ID"
SECRET_KEY = '''-----BEGIN PRIVATE KEY-----
ENTER SECRET KEY HERE
-----END PRIVATE KEY-----'''

class AppleMusic:

    def __init__(self, apple_key, team_id, secret_key):
        self.apple_key = apple_key
        self.team_id = team_id
        self.secret_key = secret_key
        self.token = None

    def get_authorization(self):
        """
        Get header for API request
        :return: header in dictionary format
        """
        if self.token:
            return {
                'Authorization': f'Bearer {self.token}',
                'Music-User-Token': f'{self.token}'
            }

        else:
            return {}

    def get_token(self):
        # Return existing token if present
        if self.token is not None:
            return self.token

        headers = {
            'alg': 'ES256',
            'kid': self.apple_key,
        }
        time_now = datetime.datetime.now()
        time_expired = datetime.datetime.now() + relativedelta(months=+6)

        payload = {
            "iss": self.team_id,
            "exp": int(time_expired.strftime("%s")),
            "iat": int(time_now.strftime("%s"))
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='ES256', headers=headers)
        self.token = token if type(token) is not bytes else token.decode()

        return self.token


    def get_songs_from_spotify(self, playlist):
        for song in playlist:
            artist = list(song)[0]

            track_name = list(song.values())[0]
            track_name = track_name.replace(' ', '+')

            song_name = f'{track_name}'

            params = {
                'term': f'{song_name}',
                'limit': 5,
                'types': 'songs',
                'with': 'topResults',
                }
            apple_data = urlencode(params)

            url = f"https://api.music.apple.com/v1/catalog/us/search?{apple_data}"
            r = requests.get(url, headers=self.get_authorization())
            r.raise_for_status()
            results = r.json()
