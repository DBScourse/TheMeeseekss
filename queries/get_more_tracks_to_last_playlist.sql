SELECT tt.track_id,
    tt.track_name,
    tt.album_name,
    tt.artist_id,
    artist_name
FROM Tracks_tbl AS tt
JOIN Artists_tbl AS art
ON tt.artist_id = art.artist_id
LEFT JOIN
(
	-- tracks in last playlist
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
JOIN 
(
	-- moods in last playlist
	SELECT DISTINCT mood_id
	FROM Tracks_tbl
	JOIN
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
	) AS tracks_in_playlist
    ON Tracks_tbl.track_id = tracks_in_playlist.track_id
	WHERE mood_id IS NOT NULL
) AS moods_in_playlist 
ON tt.mood_id = moods_in_playlist.mood_id
WHERE last_playlist_tracks.track_id IS NULL
LIMIT 20