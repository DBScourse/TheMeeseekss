SELECT track_id,
    track_name,
    album_name,
    artist_id,
    mood_id,
    artist_name    
FROM Tracks_tbl JOIN Artists_tbl
ON Tracks_tbl.artist_id = Artists_tbl.artist_id
WHERE track_id IN
(
	SELECT track_id
	FROM TracksToTags_tbl 
	WHERE tag_id =
	(
		SELECT tag_id
		FROM Tags_tbl
		WHERE tag_name = 'rock'
	)
)
AND mood_id = 
(
	SELECT mood_id
    FROM Moods_tbl
    WHERE ABS(danceability - 0.288) < 0.0001 AND ABS(energy - 0.864) < 0.0001
)

LIMIT 20

