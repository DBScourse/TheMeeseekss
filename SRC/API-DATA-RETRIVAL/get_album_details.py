import urllib2
import json


def get_album_details():
    key = "76f83b22ef5966ee279a753a377fb3ba"
    albums_f = open("albums_by_artist.txt", 'r')
    out_f = open("albums_details.txt", 'a')

    for s in albums_f.readlines():
        d = json.loads(s)
        artist = d.keys()[0]
        albums = d[artist]
        for album in albums:
            try:
                print "getting album {album}".format(**locals())
                url_artist = urllib2.quote(artist)
                url_album = urllib2.quote(album)
                ad = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={key}&artist={url_artist}&album={url_album}&format=json".format(**locals()), timeout=5).read()
                out_f.write(ad)
                out_f.write('\n')
            except Exception as e:
                print "failed to get album:{a} with exception: {e}".format(**locals())
        break



if __name__ == '__main__':
    get_album_details()

# key = "76f83b22ef5966ee279a753a377fb3ba"
# in_f = open("d:\\Adi\\Dropbox\\University\\DB\\Project\\albums_by_artist.txt", 'r')
# out_f = open("d:\\Adi\\Dropbox\\University\\DB\\Project\\albums_details.txt", 'a')
#
# for s in in_f.readlines():
#     d = json.loads(s)
#     artists_to_albums = d[d.keys()[0]]
#     for atoa in artists_to_albums:
#         for album in atoa:
#             try:
#                 print "getting album {album}".format(**locals())
#                 ad = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={key}&artist={artist}&album={album}&format=json".format(**locals()), timeout=5).read()
#                 out_f.write(ad)
#                 out_f.write('\n')
#             except:
#                 print u"failed to get album:{a}".format(**locals())
#
#
