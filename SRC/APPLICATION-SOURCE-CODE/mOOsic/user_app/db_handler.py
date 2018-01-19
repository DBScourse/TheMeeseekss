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
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    # INSERT INTO Users_tbl(user_name, password_hash) VALUES ({username}, {password_hash})
    return None


def update_user_history(username, danceability, energy, tag, playlist_name):
    try:
        cnx, cursor = open_db_connection()
        file_create_new_playlist = open('static/queries/create_new_playlist.sql', 'r')
        q = file_create_new_playlist.read()
        file_create_new_playlist.close()
        cursor.execute(q, (playlist_name, username))
        file_create_new_playlist.close()

        if tag is not None:
            file_recommended_tracks_mood_and_tag = open('static/queries/recommended_tracks_mood_and_tag.sql', 'r')
            q = file_recommended_tracks_mood_and_tag.read()
            file_recommended_tracks_mood_and_tag.close()
            cursor.execute(q, (tag, danceability, energy))
        else:
            file_recommended_tracks_mood = open('static/queries/recommended_tracks_mood.sql', 'r')
            q = file_recommended_tracks_mood.read()
            file_recommended_tracks_mood.close()
            cursor.execute(q, (danceability, energy))

        results = ((track_id, track_name, album_name, artist_name) for track_id, track_name, album_name, artist_name in
                   cursor)
        if not results:
            close_db_connection(cnx, cursor)
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        file_insert_tracks_to_playlist = open('static/queries/insert_tracks_to_playlist.sql', 'r')
        q = file_insert_tracks_to_playlist.read()
        file_insert_tracks_to_playlist.close()
        args = ()
        for i in range(len(results)-1):
            q = q + ', (last_insert_id(), %s)'
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


def update_playlist(username, song_id, playlist_id):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return None


def get_lyrics_by_track_id(track_id):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return None



def get_top_artist_top_track():
    try:
        cnx, cursor = open_db_connection()
        file_top_track = open('static/queries/top_track.sql', 'r')
        q = file_top_track.read()
        file_top_track.close()
        cursor.execute(q)
        results = ((track_id, track_name, album_name, artist_name) for track_id, track_name, album_name, artist_name in cursor)
        file_top_artist = open('static/queries/top_artist.sql', 'r')
        q = file_top_artist.read()
        file_top_artist.close()
        cursor.execute(q)
        results = results + (artist_name for artist_name in cursor)
        close_db_connection(cnx, cursor)
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))


def get_user_recommendations(username):
    cnx, cursor = open_db_connection()
    # TODO

    close_db_connection(cnx, cursor)
    return None


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

