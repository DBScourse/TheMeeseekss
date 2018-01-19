SELECT tt.track_id,
    tt.track_name,
    tt.album_name,
    artist_name
FROM Tracks_tbl AS tt
JOIN Artists_tbl AS art
ON tt.artist_id = art.artist_id
LEFT JOIN
(
	SELECT track_id
	FROM PlaylistToTracks_tbl AS ptt
	JOIN Playlists_tbl AS pt
	ON ptt.playlist_id = pt.playlist_id
	JOIN Users_tbl AS ut
	ON pt.user_id = ut.user_id
	AND user_name = {username}
	AND pt.playlist_timestamp = 
	(
		SELECT MAX(playlist_timestamp)
		FROM Playlists_tbl
		JOIN Users_tbl
		ON Playlists_tbl.user_id = Users_tbl.user_id
		WHERE user_name = {username}
	)
) AS last_playlist_tracks
ON tt.track_id = last_playlist_tracks.track_id
WHERE mood_id = 
(
	SELECT mood_id
	FROM Tracks_tbl
	WHERE Tracks_tbl.track_id = 
	(
		SELECT ptt2.track_id
		FROM PlaylistToTracks_tbl AS ptt2
		JOIN Playlists_tbl AS pt2
		ON ptt2.playlist_id = pt2.playlist_id
		JOIN Users_tbl AS ut2
		ON pt2.user_id = ut2.user_id
		WHERE user_name = {username}
		AND pt2.playlist_timestamp = 
		(
			SELECT MAX(playlist_timestamp)
			FROM Playlists_tbl
			JOIN Users_tbl
			ON Playlists_tbl.user_id = Users_tbl.user_id
			WHERE user_name = {username}
		)
		LIMIT 1
	)
)
AND last_playlist_tracks.track_id IS NULL
LIMIT 20