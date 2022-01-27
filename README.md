Switching from Spotify to Apple Music? Do you have hundreds of playlists that you created with your own blood, sweat and tears?

Worry no more! This script will help you transfer your Spotify playlists to Apple Music.

!IMPORTANT: You must sign up for an Apple Developer account in order to get an Apple Key, Team ID and Secret Key. These are very important in order to get authorized to access Apple Music API.

Another important keys to get are the Spotify Client ID and Client Secret that you can retrieve from Spotify Developer Dashboard (you must have a Spotify account).

SPOTIFY API:
Step 1: <br>
  -Get authorized to use Spotify API. https://developer.spotify.com/documentation/general/guides/authorization/
  -Requires Client ID and Client Secret Key (retrieved from Spotify Developer Dashboard).
  -The Client ID and Client Secret Key must be b64 encoded.
  <br>
  <img width="500" alt="image" src="https://miro.medium.com/max/1400/1*m7aF6hjbMBFv_fWqIbDSsQ.png">
  <br>
Step 2:<br>
  -After encodeing the Client ID and Client Secret Key, we can now add them into our API endpoint request.
  <br>
  <img width="500" alt="image" src="https://cdn-images-1.medium.com/max/800/1*VQoupHw_33xhOw5I2bQ3wA.png">
<br>
Step 3: <br>
  -Access the specific playlist that you want to be transferred to Apple Music.
  -In order to access your playlist ID, just click on the specific playlist, click on the '...', click share and 'Copy link to playlist.'
  -After retrieving the Playlist ID, pass that Playist ID in the endpoint. 
  <br>
  <img width="500" alt="image" src="https://cdn-images-1.medium.com/max/800/1*iF3cvkytmuEO9cxDG_djfQ.png">
<br>  
Step 4: <br>
  -The last step on the Spotify end is to create a list of the songs that is in the playlist. The list will then be used later on when we are working with the Apple Music API.
  <br><img width="500" alt="image" src="https://cdn-images-1.medium.com/max/800/1*Ivz8G2uU_-h6e5pIsNxp4A.png">
<br>
<br>
APPPLE MUSIC API:
