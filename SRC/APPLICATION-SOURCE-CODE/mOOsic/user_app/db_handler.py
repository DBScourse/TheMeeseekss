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


def get_password(username):
    # TODO
    password = 'sheker'
    return password


def get_user_data(username):
    # TODO playlist form: [{name: 'Love', id: 1}, {name: 'Happy', id: 2}, {name: 'Friends', id: 3}]
    # TODO ordered by descending time stamp
    return {}


def is_user(username):
    # TODO
    return False


def add_user(username, password):
    # TODO
    return None


def update_user_history(username, danceability, energy, tags, playlist_name):
    # TODO
    return


def get_playlist(username, danceability, energy):
    # TODO
    return []


def search(query):
    # TODO
    return None


def update_playlist(username, song_id, playlist_id):
    # TODO
    return None


def get_playlist_by_id(username, playlist_id):
    # TODO
    return None


def get_lyrics_by_track_id(track_id):
    # TODO
    return None


def get_recommendation_by_playlist(playlist_id):
    # TODO
    return None


def get_top_artist_top_track(artist_id, track_id):
    # TODO
    return None


def get_recommendation_by_other_user(playlist_id):
    # TODO
    return None