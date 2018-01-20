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
    cnx = mysql.connector.connect(user='DbMysql19', password='DbMysql19',
                                  host='127.0.0.1', port='3305',
                                  database='DbMysql19')
    cursor = cnx.cursor()
    return cnx, cursor


def close_db_connection(cnx, cursor):
    cursor.close()
    cnx.close()
    return


def get_password(username):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT password_hash FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (username,))
        results = [password_hash for password_hash in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return {'password': results[0]}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_user_data(username):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT playlist_name, playlist_id FROM Playlists_tbl AS pt JOIN Users_tbl AS ut ON pt.user_id = ut.user_id WHERE user_name = %s ORDER BY playlist_timestamp")
        cursor.execute(q, (username,))
        results = [{'name': playlist_name, 'id': playlist_id} for playlist_name, playlist_id in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_tracks_by_playlist_id(username, playlist_id):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT Tracks_tbl.track_id, track_name, album_name, artist_name FROM Tracks_tbl JOIN Artists_tbl ON Tracks_tbl.artist_id = Artists_tbl.artist_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id JOIN Playlists_tbl ON PlaylistToTracks_tbl.playlist_id = Playlists_tbl.playlist_id JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s AND playlist_id = %s")
        cursor.execute(q, (username, playlist_id))
        results = [{'track_id': track_id, 'track_name': track_name, 'album_name': album_name, 'artist_name': artist_name} for track_id, track_name, album_name, artist_name in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def is_user(username):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT user_id FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (username,))
        results = [user_id for user_id in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            return False
        return True
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def add_user(username, password):
    try:
        cnx, cursor = open_db_connection()
        q = ("INSERT INTO Users_tbl(user_name, password_hash) VALUES (%s, %s)")
        cursor.execute(q, (username, password))
        cnx.commit()
        # close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        print(err)
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def update_user_history(username, danceability, energy, playlist_name, tag=None):
    try:
        cnx, cursor = open_db_connection()
        q = (
            "INSERT INTO Playlists_tbl(user_id, playlist_name) SELECT user_id as cur_user_id, %s FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (playlist_name, username))
        cnx.commit()

        if tag is not None:
            q = (
                "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN TracksToTags_tbl AS ttb ON tb.track_id = ttb.track_id JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE tag_id = (SELECT tag_id FROM Tags_tbl WHERE tag_name = {tag_name}) AND mood_id = (SELECT mood_id FROM Moods_tbl WHERE ABS(danceability - {danceability}) < 0.0001 AND ABS(energy - {energy}) < 0.0001 LIMIT 1) LIMIT 20")
            cursor.execute(q, (tag, danceability, energy))
        else:
            q = (
                "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE mood_id = (SELECT mood_id FROM Moods_tbl WHERE ABS(danceability - %d}) < 0.0001 AND ABS(energy - %d) < 0.0001 LIMIT 1) LIMIT 20")
            cursor.execute(q, (danceability, energy))

        results = ((track_id, track_name, album_name, artist_name) for track_id, track_name, album_name, artist_name in
                   cursor)
        if not results:
            # close_db_connection(cnx, cursor)
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        q = ("INSERT INTO PlaylistToTracks_tbl VALUES (last_insert_id(), %s)")
        args = ()
        for i in range(len(results) - 1):
            q = q + ", (last_insert_id(), %s)"
            args = args + (results[i][0])
        cursor.execute(q, args)
        cnx.commit()
        # close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def search(sq):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT * FROM ArtistsAsText_tbl WHERE MATCH(artist_name) AGAINST(%s IN NATURAL LANGUAGE MODE) LIMIT 20")
        cursor.execute(q, (sq,))
        results = [{'id': artist_id, 'name': artist_name} for artist_id, artist_name in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def update_playlist(username, track_id):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "INSERT INTO PlaylistToTracks_tbl(playlist_id, track_id) SELECT playlist_id, %s FROM Playlists_tbl AS pt JOIN Users_tbl AS ut ON pt.user_id = ut.user_id WHERE user_name = %s AND playlist_timestamp = (SELECT MAX(playlist_timestamp) FROM Playlists_tbl AS pt2 JOIN Users_tbl AS ut2 ON pt2.user_id = ut2.user_id WHERE user_name = %s)")
        cursor.execute(q, (track_id, username, username))
        cnx.commit()
        # close_db_connection(cnx, cursor)
        return
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_lyrics_by_track_id(track_id):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT lyrics FROM Tracks_tbl WHERE track_id = %s")
        cursor.execute(q, (track_id,))
        results = [lyrics for lyrics in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return {track_id: results[0]}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_top_artist_top_track():
    try:
        cnx, cursor = open_db_connection()
        q = (
            "SELECT Tracks_tbl.track_id, track_name, album_name, artist_name FROM Tracks_tbl JOIN Artists_tbl ON Tracks_tbl.artist_id = Artists_tbl.artist_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY track_id HAVING COUNT(PlaylistToTracks_tbl.track_id) >= ALL (SELECT COUNT(PlaylistToTracks_tbl.track_id) FROM PlaylistToTracks_tbl GROUP BY track_id) LIMIT 1")
        cursor.execute(q)
        track = [[track_id, track_name, album_name, artist_name] for track_id, track_name, album_name, artist_name in
                 cursor]
        q = (
            "SELECT artist_name FROM Artists_tbl JOIN Tracks_tbl ON Artists_tbl.track_id = Tracks_tbl.track_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY artist_id HAVING COUNT(artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY artist_id) LIMIT 1")
        cursor.execute(q)
        artist = [artist_name for artist_name in cursor]
        results = {'top_track': track[0], 'top_artist': artist[0]}
        # close_db_connection(cnx, cursor)
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)

###########################TODO#################################
def get_artist_recommendation_from_last_playlist(username):
    return
    # try:
    #     cnx, cursor = open_db_connection()
    #     if tag is not None:
    #         q = (
    #         "SELECT artist_name FROM Artists_tbl AS art JOIN Tracks_tbl AS tt ON art.artist_id = tt.artist_id JOIN TracksToTags_tbl as ttt ON tt.track_id = ttt.track_id JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id JOIN Tags_tbl AS tg ON tg.tag_id = ttt.tag_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 AND tag_name = %s GROUP BY art.artist_id HAVING COUNT(art.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl AS tt2 JOIN TracksToTags_tbl AS ttt2 ON tt2.track_id = ttt2.track_id JOIN Moods_tbl mt2 ON tt2.mood_id = mt2.mood_id JOIN Tags_tbl AS tg2 ON tg2.tag_id = ttt2.tag_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 AND tag_name = %s GROUP BY artist_id) LIMIT 5")
    #         cursor.execute(q, (danceability, energy, tag, danceability, energy, tag))
    #     else:
    #         q = (
    #         "SELECT artist_name FROM Artists_tbl AS art JOIN Tracks_tbl AS tt ON art.artist_id = tt.artist_id JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY art.artist_id HAVING COUNT(art.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl AS tt JOIN Moods_tbl mt ON tt.mood_id = mt.mood_id WHERE abs(danceability - %d) < 0.0001 AND abs(energy - %d) < 0.0001 GROUP BY artist_id)")
    #         cursor.execute(q, (danceability, energy, danceability, energy))
    #     results = [artist_name for artist_name in cursor]
    #     if not results:
    #         raise django.core.exceptions.EmptyResultSet('Empty result set')
    #     return {'artist_name': results[0]}
    # except mysql.connector.Error as err:
    #     raise django.db.Error('DB error occurred: {}'.format(err))
    # finally:
    #     close_db_connection(cnx, cursor)


def get_tag_recommendations(username):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT tag_name FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s) AS ptu ON ptt.playlist_id = ptu.playlist_id JOIN Tags_tbl AS tt ON tt.tag_id = ttt.tag_id GROUP BY ttt.tag_id HAVING COUNT(ttt.tag_id) >= ALL (SELECT COUNT(tag_id) FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s) AS ptu ON ptt.playlist_id = ptu.playlist_id GROUP BY tag_id) LIMIT 5")
        cursor.execute(q, (username, username))
        results = [tag_name for tag_name in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_tracks_by_artist(name):
    try:
        cnx, cursor = open_db_connection()
        q = (
        "SELECT tb.track_id, track_name, album_name, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id WHERE artist_name = %s LIMIT 20")
        cursor.execute(q, (name,))
        results = [artist_name for artist_name in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)

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
