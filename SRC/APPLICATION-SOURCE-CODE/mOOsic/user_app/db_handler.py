import django.core.exceptions
import django.db
import mysql.connector


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
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT password_hash FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (username,))
        results = [password_hash for password_hash in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results[0][0]
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_user_data(username):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT playlist_id, playlist_name FROM Playlists_tbl AS pt JOIN Users_tbl AS ut ON pt.user_id = ut.user_id WHERE user_name = %s")
        cursor.execute(q, (username,))
        results = [{'name': item[1], 'id': item[0]} for item in cursor]
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_tracks_by_playlist_id(username, playlist_id):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT Tracks_tbl.track_id, track_name, album_name, artist_name FROM Tracks_tbl JOIN Artists_tbl ON Tracks_tbl.artist_id = Artists_tbl.artist_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id JOIN Playlists_tbl ON PlaylistToTracks_tbl.playlist_id = Playlists_tbl.playlist_id AND Playlists_tbl.playlist_id = %s")
        cursor.execute(q, (playlist_id,))
        results = [
            {'track_id': track_id, 'track_name': track_name, 'album_name': album_name, 'artist_name': artist_name} for
            track_id, track_name, album_name, artist_name in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def is_user(username):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT user_id FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (username,))
        results = [user_id for user_id in cursor]
        if not results:
            return False
        return True
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def add_user(username, password):
    cnx, cursor = open_db_connection()
    try:
        q = ("INSERT INTO Users_tbl(user_name, password_hash) VALUES (%s, %s)")
        cursor.execute(q, (username, password))
        cnx.commit()
        return
    except mysql.connector.Error as err:
        print err
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def create_playlist(username, danceability, energy, playlist_name, tag):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "INSERT INTO Playlists_tbl(user_id, playlist_name) SELECT user_id, %s FROM Users_tbl WHERE user_name = %s")
        cursor.execute(q, (playlist_name, username))
        cnx.commit()
        q = ("SELECT last_insert_id()")
        cursor.execute(q)
        plid = [item for item in cursor]
        plid = plid[0][0]
        if not tag == '':
            q = (
                "SELECT tb.track_id, track_name, album_name, tb.artist_id, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id JOIN Moods_tbl AS mt ON tb.mood_id = mt.mood_id JOIN TracksToTags_tbl AS ttt ON tb.track_id = ttt.track_id JOIN Tags_tbl ON ttt.tag_id = Tags_tbl.tag_id WHERE ABS(danceability - %s) < 0.1 AND ABS(energy - %s) < 0.1 AND tag_name = %s GROUP BY track_name ORDER BY ABS(danceability - %s) + ABS(energy - %s) ASC LIMIT 20")
            cursor.execute(q, (danceability, energy, tag, danceability, energy))
        else:
            q = (
                "SELECT tb.track_id, track_name, album_name, tb.artist_id, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl ON tb.artist_id = Artists_tbl.artist_id JOIN Moods_tbl AS mt ON tb.mood_id = mt.mood_id WHERE ABS(danceability - %s) < 0.1 AND ABS(energy - %s) < 0.1 GROUP BY track_name ORDER BY ABS(danceability - %s) + ABS(energy - %s) ASC LIMIT 20")
            cursor.execute(q, (danceability, energy, danceability, energy))

        results = [item for item in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        q = ("INSERT INTO PlaylistToTracks_tbl VALUES (%s, %s)")
        args = (plid, results[0][0])
        for i in range(1, len(results)):
            q = q + ", (%s, %s)"
            args = args + (plid, results[i][0])
        cursor.execute(q, args)
        cnx.commit()
        tracks = [{'id': item[0], 'name': item[1], 'artist': {'name': item[4], 'id': item[3]}} for item in results]
        return {'id': plid, 'name': playlist_name, 'tracks': tracks}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def search(sq):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT artist_id, artist_name FROM ArtistsAsText_tbl WHERE MATCH(artist_name) AGAINST(%s IN NATURAL LANGUAGE MODE) LIMIT 20")
        cursor.execute(q, (sq,))
        results = [{'id': artist_id, 'name': artist_name} for artist_id, artist_name in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return results
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def update_playlist(username, track_id):
    cnx, cursor = open_db_connection()
    try:
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
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT lyrics FROM Tracks_tbl WHERE track_id = %s")
        cursor.execute(q, (track_id,))
        lyr = [lyrics for lyrics in cursor]
        if not lyr:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        q = (
            "SELECT track_id, track_name, Tracks_tbl.artist_id, artist_name FROM Tracks_tbl, Artists_tbl WHERE track_id = %s AND Tracks_tbl.artist_id = Artists_tbl.artist_id")
        cursor.execute(q, (track_id,))
        tr = [item for item in cursor]
        if not tr:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        lyr = lyr[0]
        tr = tr[0]
        return {'name': tr[1], 'id': tr[0], 'lyrics': lyr[0], 'artist': {'name': tr[3], 'id': tr[2]}}
    except mysql.connector.Error as err:
        print err
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_top_artist_top_track():
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT Tracks_tbl.track_id, track_name, album_name, Tracks_tbl.artist_id, artist_name FROM Tracks_tbl JOIN Artists_tbl ON Tracks_tbl.artist_id = Artists_tbl.artist_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY track_id HAVING COUNT(PlaylistToTracks_tbl.track_id) >= ALL (SELECT COUNT(PlaylistToTracks_tbl.track_id) FROM PlaylistToTracks_tbl GROUP BY track_id) LIMIT 1")
        cursor.execute(q)
        track = [[item[0], item[1], item[2], item[3], item[4]] for item in cursor]
        q = (
            "SELECT Artists_tbl.artist_id, artist_name FROM Artists_tbl JOIN Tracks_tbl ON Artists_tbl.artist_id = Tracks_tbl.artist_id JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY Artists_tbl.artist_id HAVING COUNT(Artists_tbl.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl JOIN PlaylistToTracks_tbl ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id GROUP BY artist_id) LIMIT 1")
        cursor.execute(q)
        artist = [[item[0], item[1]] for item in cursor]
        artist = artist[0]
        track = track[0]
        return {'track': {'name': track[1], 'id': track[0], 'album': track[2],
                          'artist': {'name': track[4], 'id': track[3]}}, 'artist': {'name': artist[1], 'id': artist[0]}}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_artist_recommendation_from_last_playlist(username):
    cnx, cursor = open_db_connection()
    try:
        q = (
        "SELECT art.artist_id, artist_name FROM Artists_tbl AS art JOIN Tracks_tbl AS tt ON art.artist_id = tt.artist_id JOIN (SELECT DISTINCT mood_id FROM Tracks_tbl JOIN (SELECT ptt2.track_id FROM PlaylistToTracks_tbl AS ptt2 JOIN Playlists_tbl AS pt2 ON ptt2.playlist_id = pt2.playlist_id JOIN Users_tbl AS ut2 ON pt2.user_id = ut2.user_id WHERE user_name = %s AND pt2.playlist_timestamp = (SELECT MAX(playlist_timestamp) FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s)) AS tracks_in_playlist ON Tracks_tbl.track_id = tracks_in_playlist.track_id WHERE mood_id IS NOT NULL) AS moods_in_pl ON tt.mood_id = moods_in_pl.mood_id GROUP BY art.artist_id HAVING COUNT(art.artist_id) >= ALL (SELECT COUNT(artist_id) FROM Tracks_tbl AS tt3 JOIN (SELECT DISTINCT mood_id FROM Tracks_tbl JOIN (SELECT ptt4.track_id FROM PlaylistToTracks_tbl AS ptt4 JOIN Playlists_tbl AS pt4 ON ptt4.playlist_id = pt4.playlist_id JOIN Users_tbl AS ut4 ON pt4.user_id = ut4.user_id WHERE user_name = %s AND pt4.playlist_timestamp = (SELECT MAX(playlist_timestamp) FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s)) AS tracks_in_playlist ON Tracks_tbl.track_id = tracks_in_playlist.track_id WHERE mood_id IS NOT NULL) AS moods_in_pl2 ON tt3.mood_id = moods_in_pl2.mood_id GROUP BY artist_id) LIMIT 1")
        cursor.execute(q, (username, username, username, username))
        results = [item for item in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return {'name': results[0][1], 'id': results[0][0]}
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_tag_recommendations(username):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT ttt.tag_id, tag_name FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s) AS ptu ON ptt.playlist_id = ptu.playlist_id JOIN Tags_tbl AS tt ON tt.tag_id = ttt.tag_id GROUP BY ttt.tag_id HAVING COUNT(ttt.tag_id) >= ALL (SELECT COUNT(tag_id) FROM TracksToTags_tbl AS ttt JOIN PlaylistToTracks_tbl AS ptt ON ttt.track_id = ptt.track_id JOIN (SELECT playlist_id FROM Playlists_tbl JOIN Users_tbl ON Playlists_tbl.user_id = Users_tbl.user_id WHERE user_name = %s) AS ptu ON ptt.playlist_id = ptu.playlist_id GROUP BY tag_id) LIMIT 5")
        cursor.execute(q, (username, username))
        results = [item for item in cursor]
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return [item[1] for item in results]
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)


def get_tracks_by_artist(artist_id):
    cnx, cursor = open_db_connection()
    try:
        q = (
            "SELECT tb.track_id, track_name, album_name, tb.artist_id, artist_name FROM Tracks_tbl AS tb JOIN Artists_tbl AS art ON tb.artist_id = art.artist_id WHERE tb.artist_id = %s LIMIT 20")
        cursor.execute(q, (int(artist_id),))
        results = [item for item in cursor]
        # close_db_connection(cnx, cursor)
        if not results:
            raise django.core.exceptions.EmptyResultSet('Empty result set')
        return [{'name': item[1], 'id': item[0], 'album': item[2], 'artist': {'name': item[4], 'id': item[3]}} for item
                in results]
    except mysql.connector.Error as err:
        raise django.db.Error('DB error occurred: {}'.format(err))
    finally:
        close_db_connection(cnx, cursor)
