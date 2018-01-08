import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def spotify_trackid(query):
    client_credentials_manager = SpotifyClientCredentials(client_id="a30fb9dcef504d679a32798ee598de58",
                                                          client_secret="58723610684241ecaffe055cd9a72f0a")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(q=query, type='track', limit=1)
    return result['tracks']['items']['id']


def spotify_track_mood(track_ids):
    client_credentials_manager = SpotifyClientCredentials(client_id="a30fb9dcef504d679a32798ee598de58",
                                                          client_secret="58723610684241ecaffe055cd9a72f0a")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.audio_features(track_ids)
    return result


ids = []
f = open('C:\Users\yotro\Desktop\lyrics_list.json') # TODO
d = json.load(f)
for i in range(len(d)):
    s = d[i]['track'] + ' ' + d[i]['artist']
    track_id = spotify_trackid(s)
    d[i]['id'] = track_id
    ids.append(track_id)

track_dict = {}
for track in d:
    track_dict[track['id']] = track

subseq50 = [ids[i:i + 50] for i in range(0, len(ids), 50)]
for seq in subseq50:
    moods50 = spotify_track_mood(seq)
    for feats in moods50:
        track_dict[feats['id']]['danceability'] = feats['danceability']
        track_dict[feats['id']]['energy'] = feats['energy']

target = open('spotifyData.json', 'a') # TODO
target.write(json.dumps(track_dict))
