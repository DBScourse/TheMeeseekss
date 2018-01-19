SELECT artist_name
FROM Artists_tbl AS art
JOIN Tracks_tbl AS tt
ON art.artist_id = tt.artist_id
JOIN TracksToTags_tbl as ttt
ON tt.track_id = ttt.track_id
JOIN Moods_tbl mt
ON tt.mood_id = mt.mood_id
JOIN Tags_tbl AS tg
ON tg.tag_id = ttt.tag_id 
WHERE abs(danceability - {danceability}) < 0.0001 AND abs(energy - {energy}) < 0.0001
AND tag_name = {tag_name}
GROUP BY art.artist_id
HAVING COUNT(art.artist_id) >= ALL
(
	SELECT COUNT(artist_id)
	FROM Tracks_tbl AS tt2
	JOIN TracksToTags_tbl AS ttt2
	ON tt2.track_id = ttt2.track_id
	JOIN Moods_tbl mt2
	ON tt2.mood_id = mt2.mood_id
	JOIN Tags_tbl AS tg2
	ON tg2.tag_id = ttt2.tag_id 
	WHERE abs(danceability - {danceability}) < 0.0001 AND abs(energy - {energy}) < 0.0001
	AND tag_name = {tag_name}
	GROUP BY artist_id
)
LIMIT 5