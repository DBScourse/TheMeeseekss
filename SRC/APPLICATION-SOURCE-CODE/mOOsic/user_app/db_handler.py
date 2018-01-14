from queries import *
from django.db import connection
import uuid


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
    # TODO
    return {}


def is_user(username):
    # TODO
    return False


def add_user(username, password):
    # TODO
    return None


def update_user_history(username, danceability, energy, tags):
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