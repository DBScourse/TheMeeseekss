import requests
import json




def getAllSongs(key,track_file, lyrics_file,not_found,start):

    f = open(track_file,'r')
    lyrics_f = open(lyrics_file, 'a')
    tracks_list = f.readlines()
    num = 0

    if start+1000 < (len(tracks_list)):
        end = start+1000
    else:
        end = len(tracks_list)

    for i in range(start, end):
        num += 1
        if i%100 == 0:
            print 'i = '+str(i)
        json_line = json.loads(tracks_list[i])
        artist = json_line['artist']
        track = json_line['track']
        r = requests.get('http://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track='+track+'&q_artist='+artist+'&apikey='+key)
        if (r.json()['message']['header']['status_code'] == 200):
            lyrics = r.json()['message']['body']['lyrics']['lyrics_body']
            json_line['lyrics'] = lyrics
            lyrics_f.write(json.dumps(json_line)+'\n')
        else:
            nf = open(not_found, 'a')
            nf.write(tracks_list[i])
            nf.close()
    f.close()
    lyrics_f.close()






def main():
    #key = '4ea5a1ebfdde51815bf431e133fac3d2'
    key = '53425e1c0000c141d5536f892b38b83c'
    #key = 'de88efc47c1d2f113533299386530789'
    tracks_path = 'C:/Users/gilikatabi/Desktop/missing_tracks.txt'
    lyrics_path = 'C:/Users/gilikatabi/Desktop/lyrics_list.txt'
    not_found_path = 'C:/Users/gilikatabi/Desktop/not_found_tracks'
    for i in range(30697,40000,1000):
        #was 0, 1000, 2000, 3000 - 10000, 10000 - 20000, 20000 - 30000 - 40000
        getAllSongs(key,tracks_path,lyrics_path,not_found_path,i)
if __name__ == "__main__":
    main()
