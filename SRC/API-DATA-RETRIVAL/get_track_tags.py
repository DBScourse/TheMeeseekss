import urllib2
import json


def get_track_tags():
    key = "76f83b22ef5966ee279a753a377fb3ba"
    in_f = open("albums_details.txt", 'r')
    out_f = open("track_tags.txt", 'a')

    for s in in_f.readlines():
        try:
            tracks = json.loads(s)['album']['tracks']['track']
            album = json.loads(s)['album']['name']
            artist = urllib2.quote(json.loads(s)['album']['artist'])
            i, j = 0, 0
            for track in tracks:
                j += 1
                try:
                    name = urllib2.quote(track['name'])
                    tags = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist={artist}&track={name}&api_key={key}&format=json".format(**locals()), timeout=7).read()
                    out_f.write(tags)
                    out_f.write('\n')
                    i += 1
                except Exception as e:
                    print "failed to get {artist}: {name} with exception: {e}".format(**locals())
            print "got {i} / {j} tracks for {artist}: {album}".format(**locals())
        except Exception as e:
            print "failed miserably in operation on:\n{s}\nException:{e}".format(**locals())


if __name__ == '__main__':
    get_track_tags()
