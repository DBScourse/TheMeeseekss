SELECT artist_name
FROM Artists_tbl AS art
JOIN Tracks_tbl AS tt
ON art.artist_id = tt.artist_id
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
		WHERE user_name = 'aaa'
		AND pt2.playlist_timestamp = 
		(
			SELECT MAX(playlist_timestamp)
			FROM Playlists_tbl
			JOIN Users_tbl
			ON Playlists_tbl.user_id = Users_tbl.user_id
			WHERE user_name = 'aaa'
		)
	) AS tracks_in_playlist
    ON Tracks_tbl.track_id = tracks_in_playlist.track_id
	WHERE mood_id IS NOT NULL
) AS moods_in_pl
ON tt.mood_id = moods_in_pl.mood_id
GROUP BY art.artist_id
HAVING COUNT(art.artist_id) >= ALL
(
	SELECT COUNT(artist_id)
	FROM Tracks_tbl AS tt3
	JOIN
	(
		-- moods in last playlist
		SELECT DISTINCT mood_id
		FROM Tracks_tbl
		JOIN
		(
			SELECT ptt4.track_id
			FROM PlaylistToTracks_tbl AS ptt4
			JOIN Playlists_tbl AS pt4
			ON ptt4.playlist_id = pt4.playlist_id
			JOIN Users_tbl AS ut4
			ON pt4.user_id = ut4.user_id
			WHERE user_name = 'aaa'
			AND pt4.playlist_timestamp = 
			(
				SELECT MAX(playlist_timestamp)
				FROM Playlists_tbl
				JOIN Users_tbl
				ON Playlists_tbl.user_id = Users_tbl.user_id
				WHERE user_name = 'aaa'
			)
		) AS tracks_in_playlist
		ON Tracks_tbl.track_id = tracks_in_playlist.track_id
		WHERE mood_id IS NOT NULL
	) AS moods_in_pl2
    ON tt3.mood_id = moods_in_pl2.mood_id
    GROUP BY artist_id
)
LIMIT 1