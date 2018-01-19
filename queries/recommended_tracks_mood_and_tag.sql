SELECT tb.track_id,
    track_name,
    album_name,
    artist_name 
FROM Tracks_tbl AS tb
JOIN TracksToTags_tbl AS ttb
ON tb.track_id = ttb.track_id
JOIN Artists_tbl
ON tb.artist_id = Artists_tbl.artist_id
WHERE tag_id =
(
	SELECT tag_id
	FROM Tags_tbl
	WHERE tag_name = {tag_name}
)
AND mood_id = 
(
	SELECT mood_id
	FROM Moods_tbl
	WHERE ABS(danceability - {danceability}) < 0.0001 AND ABS(energy - {energy}) < 0.0001
	LIMIT 1
)
LIMIT 20