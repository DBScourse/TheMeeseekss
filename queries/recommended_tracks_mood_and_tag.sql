SELECT tb.track_id, 
	tb.mood_id,
    track_name,
    album_name,
    tb.artist_id,
    artist_name
FROM Tracks_tbl AS tb
JOIN Artists_tbl
ON tb.artist_id = Artists_tbl.artist_id
JOIN Moods_tbl AS mt
ON tb.mood_id = mt.mood_id
JOIN TracksToTags_tbl AS ttt
ON tb.track_id = ttt.track_id
JOIN Tags_tbl
ON ttt.tag_id = Tags_tbl.tag_id
WHERE ABS(danceability - {danceability}) < 0.1 AND ABS(energy - {energy}) < 0.1
AND tag_name = {tag}
GROUP BY track_name
ORDER BY ABS(danceability - {danceability}) + ABS(energy - {energy}) ASC
LIMIT 20