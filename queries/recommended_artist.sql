SELECT artist_name
FROM Artists_tbl AS art
JOIN Tracks_tbl AS tt
ON art.artist_id = tt.artist_id
JOIN
(
	SELECT track_id
	FROM TracksToTags_tbl 
	WHERE tag_id =
	(
		SELECT tag_id
		FROM Tags_tbl
		WHERE tag_name = {tag_name}
	)
) AS ttn
ON tt.track_id = ttn.track_id
JOIN Moods_tbl mt
ON tt.mood_id = mt.mood_id
WHERE abs(danceability - {danceability)) < 0.0001 AND abs(energy - {energy}) < 0.0001
GROUP BY art.artist_id
HAVING COUNT(art.artist_id) >= ALL
(
	SELECT COUNT(artist_id)
	FROM Tracks_tbl AS tt
	JOIN
	(
		SELECT track_id
		FROM TracksToTags_tbl 
		WHERE tag_id =
		(
			SELECT tag_id
			FROM Tags_tbl
			WHERE tag_name = 'black metal'
		)
	) AS ttn
	ON tt.track_id = ttn.track_id
	JOIN Moods_tbl mt
	ON tt.mood_id = mt.mood_id
	WHERE abs(danceability - {danceability)) < 0.0001 AND abs(energy - {energy}) < 0.0001
	GROUP BY artist_id
)
