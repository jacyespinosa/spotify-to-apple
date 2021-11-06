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
