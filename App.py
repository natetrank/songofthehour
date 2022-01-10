import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials


def main():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    everything_uri = 'spotify:playlist:7422MBQ8Hy1vJMoKCS7j2W'

    playlist_size = get_playlist_size(sp, everything_uri)

    track_num = random.randrange(playlist_size)

    offset = track_num

    response = sp.playlist_items(everything_uri,
                                 offset=track_num,
                                 limit=1,
                                 fields='items.track.artists,items.track.name')

    artists = (response.get('items')[0]).get('track').get('artists')

    print('artists: ')
    for artist in artists:
        print(artist['name'])

    track = (response.get('items')[0]).get('track').get('name')

    print('\ntrack:\n', track)


def get_playlist_size(sp, uri):
    everything = sp.playlist(uri)

    playlist_size = everything.get('tracks').get('total')
    print("\nplaylist size: ", playlist_size)

    return playlist_size


if __name__ == "__main__":
    main()
