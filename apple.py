'''SPOTIFY'''
CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER CLIENT SECRET"

'''APPLE'''
APPLE_KEY = "ENTER APPLE KEY"
TEAM_ID = "ENTER APPLE TEAM ID"


class AppleMusic:

    def __init__(self, apple_key, team_id, secret_key):
        self.apple_key = apple_key
        self.team_id = team_id
        self.secret_key = secret_key

