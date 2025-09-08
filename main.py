import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

header = os.getenv("header")

date = input("Which year would you want to travel to? Plaese enter in YYYY-MM-DD format: ")

client_id = os.getenv("client_id")

client_secret = os.getenv("client_secret")

URL = "https://www.billboard.com/charts/hot-100/"+date

response = requests.get(url=URL,headers=header)


soup = BeautifulSoup(response.text,"html.parser")
song_names =  soup.select(selector="li ul li h3")

names = [nam.get_text().strip() for nam in song_names]

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth
#                      (scope="playlist-modify-private",
#                       client_id=client_id,
#                       client_secret=client_secret,
#                       redirect_uri="http://example.com",
#                       show_dialog=True,
#                       cache_path="token.txt",
#                       username=YOUR SPOTIFY DISPLAY NAME
#                                                ))

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://127.0.0.1:9090"))


results = sp.current_user()
id = results["id"]
# print(results["id"])

song_uri = []
year = date.strip("-")[0]

for song in names:
    result_of_song_search = sp.search(q=f"track:{song} year{year}", type="track",limit=10) 
    # print(result_of_song_search)
    try:
        uri = result_of_song_search["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        continue

# print(song_uri)


    
hopefully_playlist_id = sp.user_playlist_create(user=id,name=f"Top songs during {date} date :)",public=False)
print(hopefully_playlist_id["id"])

if song_uri == None or hopefully_playlist_id == None:
    print("the params are none")
else:
    maybe_playlist_id = sp.playlist_add_items(playlist_id=hopefully_playlist_id["id"],items=song_uri)
    print(f"this is the id {maybe_playlist_id}")