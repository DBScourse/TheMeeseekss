from queries import *
from django.db import connection
import uuid
import django.core.exceptions
import django.db
import mysql.connector


def sample_sql_query():
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM numerico.track limit 1;")
    #     rows = cursor.fetchall()
    # return rows
    return 'we are here'


def open_db_connection():
    # TODO add connection parameters
    cnx = mysql.connector.connect(user='scott', password='password',
                                  host='127.0.0.1',
                                  database='employees')
    cursor = cnx.cursor()
    return cnx, cursor


def close_db_connection(cnx, cursor):
    cursor.close()
    cnx.close()
    return


def get_password(username):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return


def get_user_data(username):
    # TODO playlist form: [{name: 'Love', id: 1}, {name: 'Happy', id: 2}, {name: 'Friends', id: 3}]
    # TODO ordered by descending time stamp
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return {}


def is_user(username):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return False


def add_user(username, password):
    try:
        cnx, cursor = open_db_connection()
        q = ("INSERT INTO Users_tbl(user_name, password_hash) VALUES (%s, %s)")
        cursor.execute(q, (username, password))
        close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def update_user_history(username, danceability, energy, playlist_name, tag=None):
    try:
        cnx, cursor = open_db_connection()
        q = (
            "INSERT INTO Playlists_tbl(user_id, playlist_name) SELECT user_id as cur_user_id, %s FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (playlist_name, username))

        if tag is not None:
            q = (
                "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN (SELECT track_id FROM TracksToTags_tbl WHERE tag_id =(SELECT tag_id FROM Tags_tbl WHERE tag_name = %s)) AS ttb ON tb.track_id = ttb.track_id JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE mood_id = (SELECT mood_id FROM Moods_tbl WHERE ABS(danceability - %d) < 0.0001 AND ABS(energy - %d) < 0.0001) LIMIT 20")
            cursor.execute(q, (tag, danceability, energy))
        else:
            q = (
                "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE mood_id = (SELECT mood_id FROM Moods_tbl WHERE ABS(danceability - %d}) < 0.0001 AND ABS(energy - %d) < 0.0001) LIMIT 20")
            cursor.execute(q, (danceability, energy))

        results = ((track_id, track_name, album_name, artist_name) for track_id, track_name, album_name, artist_name in
                   cursor)
        if not results:
            close_db_connection(cnx, cursor)
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        q = ("INSERT INTO PlaylistToTracks_tbl VALUES (last_insert_id(), %s)")
        args = ()
        for i in range(len(results) - 1):
            q = q + ", (last_insert_id(), %s)"
            args = args + (results[i][0])
        cursor.execute(q, args)
        close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def search(query):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return None


def update_playlist(username, track_id):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "INSERT INTO PlaylistToTracks_tbl(playlist_id, track_id) SELECT playlist_id, %s FROM Playlists_tbl AS pt JOIN Users_tbl AS ut ON pt.user_id = ut.user_id WHERE user_name = %s AND playlist_timestamp >= ALL (SELECT playlist_timestamp FROM Playlists_tbl AS pt2 WHERE pt.user_id = pt2.user_id)")
        cursor.execute(q, (track_id, username))
        close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def get_lyrics_by_track_id(track_id):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return None


def get_top_artist_top_track():
    try:
        cnx, cursor = open_db_connection()
        q = (
            "SELECT track_id, track_name, album_name, artist_name FROM Tracks_tbl JOIN Artists_tbl ON Tracks_tbl.artist_id = Artists_tbl.artist_id WHERE track_id = (SELECT track_id FROM PlaylistToTracks_tbl	GROUP BY track_id HAVING COUNT(track_id) >= ALL (SELECT COUNT(track_id)	FROM PlaylistToTracks_tbl GROUP BY track_id) LIMIT 1)")
        cursor.execute(q)
        track = ((track_id, track_name, album_name, artist_name) for track_id, track_name, album_name, artist_name in
                 cursor)
        q = (
            "SELECT artist_name FROM Artists_tbl WHERE artist_id = (SELECT artist_id FROM Tracks_tbl JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY artist_id HAVING COUNT(artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl JOIN PlaylistToTracks_tbl	ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY artist_id) LIMIT 1)")
        cursor.execute(q)
        artist = (artist_name for artist_name in cursor)
        results = {'top_track': track[0], 'top_artist': artist[0]}
        close_db_connection(cnx, cursor)
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def get_artist_recommendation(danceability, energy, tag=None):
    try:
        cnx, cursor = open_db_connection()
        if tag is not None:
            q = (
            "SELECT artist_name FROM Artists_tbl AS art JOIN Tracks_tbl AS tt ON art.artist_id = tt.artist_id JOIN (SELECT track_id FROM TracksToTags_tbl WHERE tag_id = (SELECT tag_id FROM Tags_tbl WHERE tag_name = %s)) AS ttn ON tt.track_id = ttn.track_id JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY art.artist_id HAVING COUNT(art.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl AS tt JOIN (SELECT track_id FROM TracksToTags_tbl WHERE tag_id = (SELECT tag_id FROM Tags_tbl WHERE tag_name = 'black metal')) AS ttn ON tt.track_id = ttn.track_id JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY artist_id)")
            cursor.execute(q, (tag, danceability, energy, danceability, energy))
        else:
            q = (
            "SELECT artist_name FROM Artists_tbl AS art JOIN Tracks_tbl AS tt ON art.artist_id = tt.artist_id JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY art.artist_id HAVING COUNT(art.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl AS tt JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY artist_id)")
            cursor.execute(q, (danceability, energy, danceability, energy))
        results = [artist_name for artist_name in cursor]
        close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return {results[0]}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def get_tag_recommendations(username):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT tag_name FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = 'aa') AS ptu ON ptt.playlist_id = ptu.playlist_id JOIN Tags_tbl AS tt ON tt.tag_id = ttt.tag_id GROUP BY ttt.tag_id HAVING COUNT(ttt.tag_id) >= ALL (SELECT COUNT(tag_id) FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s) AS ptu ON ptt.playlist_id = ptu.playlist_id GROUP BY tag_id) LIMIT 5")
        cursor.execute(q, (username,))
        results = [tag_name for tag_name in cursor]
        close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def get_tracks_by_artist(name):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE artist_name = %s LIMIT 20")
        cursor.execute(q, (name,))
        results = [artist_name for artist_name in cursor]
        close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))

# def get_playlist(username, danceability, energy):
#     cnx, cursor = open_db_connection()
#
#     close_db_connection(cnx, cursor)
#     return []


# def get_recommendation_by_playlist(playlist_id):
#     cnx, cursor = open_db_connection()
#
#     close_db_connection(cnx, cursor)
#     return None


# def get_playlist_by_id(username, playlist_id):
#     cnx, cursor = open_db_connection()
#
#     close_db_connection(cnx, cursor)
#     return None
