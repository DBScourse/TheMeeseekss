import json
import spotipy
import time
from requests import ConnectionError
from spotipy.oauth2 import SpotifyClientCredentials


def spotify_trackid(query):
    client_credentials_manager = SpotifyClientCredentials(client_id="a30fb9dcef504d679a32798ee598de58",
                                                          client_secret="58723610684241ecaffe055cd9a72f0a")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    try:
        result = sp.search(q=query, type='track', limit=1)
        return result['tracks']['items'][0]['id']
    except IndexError:
        print('Song not found in search:' + query)
        return None
    except spotipy.client.SpotifyException as err:
        print(err)
        print('Spotify exception occurred. going to sleep and trying again.')
        time.sleep(10)
        return spotify_trackid(query)
    except ConnectionError as err:
        print(err)
        print('Connection Error occurred. going to sleep and trying again.')
        time.sleep(10)
        return spotify_trackid(query)
    except:
        print('An error has occurred. ignoring song')
        return None


def spotify_track_mood(query):
    client_credentials_manager = SpotifyClientCredentials(client_id="a30fb9dcef504d679a32798ee598de58",
                                                          client_secret="58723610684241ecaffe055cd9a72f0a")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    try:
        result = sp.audio_features(query)
        return result
    except spotipy.client.SpotifyException as err:
        print(err)
        print('Spotify exception occurred. going to sleep and trying again.')
        time.sleep(10)
        return spotify_track_mood(query)
    except ConnectionError as err:
        print(err)
        print('Connection Error occurred. going to sleep and trying again.')
        time.sleep(10)
        return spotify_track_mood(query)
    except ValueError as err:
        print(err)
        print('Value Error occurred. going to sleep and trying again.')
        time.sleep(10)
        return spotify_track_mood(query)
    except:
        print('An error has occurred. ignoring song')
        time.sleep(10)
        return spotify_track_mood(query)


with open('lyrics_list.json') as source:
    target = open('spotifyData.json', 'a')
    target.write('[')
    data = json.load(source)
    track_dict = {}
    for i in range(len(data)):
        q = data[i]['track'] + ' ' + data[i]['artist']
        try:
            q = str(q)
        except UnicodeEncodeError:
            print('contains special chars. trying without conversion')
        track_id = spotify_trackid(q)
        if track_id is not None and track_id not in track_dict:
            res = spotify_track_mood(str(track_id))
            if res is not None:
                data[i]['danceability'] = res[0]['danceability']
                data[i]['energy'] = res[0]['energy']
                data[i]['id'] = track_id
                track_dict[track_id] = data[i]
                print('#################' + q + '#################')
                target.write(json.dumps(data[i]))
                target.write(',\n')
    target.write(']')
