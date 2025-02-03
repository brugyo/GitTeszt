import random
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


def get_random_album(artist_name):
    spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.search(q=f"artist:{artist_name}", type="artist", limit=1)

    if results["artists"]["items"]:
        artist_id = results["artists"]["items"][0]["id"]
        albums = spotify.artist_albums(artist_id, album_type="album")["items"]

        if albums:
            return random.choice(albums)["name"]
        else:
            return None
    else:
        return None


def hide_longest_word(title):
    words = title.split()
    longest = max(words, key=len)
    return title.replace(longest, "_" * len(longest)), longest


def main():
    artist_name = input("Add meg a kedvenc előadód nevét: ")

    album_title = get_random_album(artist_name)

    if album_title:
        hidden_title, hidden_word = hide_longest_word(album_title)

        print(f"Találd ki a hiányzó szót! Az album címe: {hidden_title}")
        guess = input("Mi a hiányzó szó? ")

        if guess.lower() == hidden_word.lower():
            print("Helyes! Ügyes vagy!")
        else:
            print(f"Helytelen! A helyes válasz: {hidden_word}")
    else:
        print(f"Nem található előadó, vagy nincs albuma: {artist_name}")


main()
