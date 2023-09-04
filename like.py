import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-modify"))

playlist_url = input("Enter the playlist URL: ")

playlist_id = playlist_url.split("/")[-1]

liked_count = 0
offset = 0

while True:
    tracks = sp.playlist_tracks(playlist_id, offset=offset)
    
    if not tracks['items']:
        break
    
    for track in tracks['items']:
        track_uri = track['track']['uri']
        sp.current_user_saved_tracks_add(tracks=[track_uri])
        liked_count += 1
    
    print(f"Liked {liked_count} songs in the playlist.")
    
    offset += len(tracks['items'])

print(f"Liked all {liked_count} songs in the playlist!")
