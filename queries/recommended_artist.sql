SELECT artist_id, COUNT(artist_id) AS count
FROM Tracks_tbl 
WHERE track_id IN
(
	SELECT track_id
	FROM TracksToTags_tbl 
	WHERE tag_id =
	(
		SELECT tag_id
		FROM Tags_tbl
		WHERE tag_name = {tag_name}
	)
)
AND mood_id = 
(
	SELECT mood_id
    FROM Moods_tbl
    WHERE danceability = {danceability} AND energy = {energy}
)
GROUP BY artist_id 
WHERE count >= ALL
(
	SELECT COUNT(artist_id)
	FROM Tracks_tbl 
	WHERE track_id IN
	(
		SELECT track_id
		FROM TracksToTags_tbl 
		WHERE tag_id =
		(
			SELECT tag_id
			FROM Tags_tbl
			WHERE tag_name = {tag_name}
		)
	)
	AND mood_id = 
	(
		SELECT mood_id
		FROM Moods_tbl
		WHERE danceability = {danceability} AND energy = {energy}
	)
	GROUP BY artist_id
)