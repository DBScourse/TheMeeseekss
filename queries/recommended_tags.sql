SELECT tag_name 
FROM Tags_tbl
WHERE tag_id IN
(
	SELECT tag_id, COUNT(tag_id) AS c
	FROM TracksToTags_tbl
	WHERE track_id IN
	(
		SELECT DISTINCT track_id
		FROM PlaylistToTracks_tbl
		WHERE playlist_id IN
		(
			SELECT playlist_id
			FROM Playlists_tbl
			WHERE user_id = 0000000
		)
	) 
	AND c >= ALL
	(
		SELECT COUNT(tag_id)
		FROM TracksToTags_tbl
		WHERE track_id IN
		(
			SELECT DISTINCT track_id
			FROM PlaylistToTracks_tbl
			WHERE playlist_id IN
			(
				SELECT playlist_id
				FROM Playlists_tbl
				WHERE user_id = 0000000
			)
		)
	)
	GROUP BY tag_id
)