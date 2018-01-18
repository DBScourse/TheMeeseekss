SELECT tb.track_id,
    track_name,
    album_name,
    artist_name 
FROM Tracks_tbl AS tb
JOIN 
(
	SELECT track_id
	FROM TracksToTags_tbl 
	WHERE tag_id =
	(
		SELECT tag_id
		FROM Tags_tbl
		WHERE tag_name = %s
	)
) AS ttb
ON tb.track_id = ttb.track_id
JOIN Artists_tbl
ON tb.artist_id = Artists_tbl.artist_id
WHERE mood_id = 
(
	SELECT mood_id
    FROM Moods_tbl
    WHERE ABS(danceability - %d) < 0.0001 AND ABS(energy - %d) < 0.0001
)
LIMIT 20