from datetime import datetime, timedelta


client_id = "ENTER CLIENT ID FROM SPOTIFY ACCOUNT"
client_secret = "ENTER SECRET ID FROM SPOTIFY ACCOUNT"


class SpotifyAPI(object):
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"