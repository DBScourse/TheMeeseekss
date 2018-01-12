import urllib2
import json


def get_top_tags():
    key = "76f83b22ef5966ee279a753a377fb3ba"
    tags = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key={key}&format=json".format(**locals()), timeout=7).read()
    f = open("top_tags.txt", 'w')
    f.write(tags)


if __name__ == '__main__':
    get_top_tags()
