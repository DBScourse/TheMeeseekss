import urllib2
import json


def get_artists_by_top_tags():
    key = "76f83b22ef5966ee279a753a377fb3ba"

    top_tags_f = open('top_tags.txt', 'r')
    artists_f = open('artists_by_top_tags.txt', 'a')

    top_tags = json.loads(top_tags_f.read())
    top_tags_names = [tag["name"] for tag in top_tags["toptags"]["tag"]]
    artists_strs = []

    for tag_name in top_tags_names:
        print "getting {tag_name}".format(**locals())
        try:
            url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag={tag_name}&api_key={key}&format=json".format(**locals())
            artists_strs.append(urllib2.urlopen(url).read())
        except Exception as e:
            print "failed to retrieve artists for {tag_name}: {e}".format(**locals())

    artists = [json.loads(artist_s) for artist_s in artists_strs]

    i = 0
    for top_artists in artists:
        artist_names = [a["name"] for a in top_artists["topartists"]["artist"]]
        i += 1
        artists_f.write(json.dumps(artist_names))


if __name__ == '__main__':
    get_artists_by_top_tags()
