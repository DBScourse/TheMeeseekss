import urllib2
import json
import time


def get_top_albums_for_artists():
    key = "76f83b22ef5966ee279a753a377fb3ba"

    artists = open('artists_by_top_tags.txt', 'r')
    albums_by_artist = open('albums_by_artist.txt', 'a')

    i = 1
    for l in artists.readlines():
        d = {}
        print "getting albums for tag number: {i}".format(**locals())
        for artist in json.loads(l):
            d[artist] = []

            print "\tgetting album for artist: {}".format(artist)
            try:
                url_artist = urllib2.quote(artist)
                url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={url_artist}&api_key={key}&format=json".format(**locals())
                albums_str = urllib2.urlopen(url, timeout=5).read()
            except Exception as e:
                print "failed getting albums for artist {artist}: {e}".format(**locals())
                continue

            albums = json.loads(albums_str)
            d[artist] = [a["name"] for a in albums["topalbums"]["album"]]

        albums_by_artist.write(json.dumps(d))
        time.sleep(10)


if __name__ == '__main__':
    get_top_albums_for_artists()
