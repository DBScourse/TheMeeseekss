SELECT * 
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
LIMIT 20
