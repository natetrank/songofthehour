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
                                 fields='items.track')

    print(response.get('items'))

    #while True:
        #response = sp.playlist_items(everything_uri,
        #                             offset=offset,
        #                             fields='items.track.id,total',
        #                             additional_types=['track'])

        #if len(response['items']) == 0:
        #    break

        #print(response['items'])
        #offset = offset + len(response['items'])
        #print(offset, "/", response['total'])


def get_playlist_size(sp, uri):
    everything = sp.playlist(uri)

    playlist_size = everything.get('tracks').get('total')
    print("\nplaylist size: ", playlist_size)

    return playlist_size


def get_track_index(playlist_size):
    track_num = random.randrange(playlist_size)
    print("\ntrack num: ", track_num)
    set_index = track_num // 100
    print("\nset index: ", set_index)
    track_index = track_num % 100
    print("\ntrack index: ", track_index)

    return set_index, track_index


if __name__ == "__main__":
    main()