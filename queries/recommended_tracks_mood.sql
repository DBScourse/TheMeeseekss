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
WHERE ABS(danceability - 0.118) < 0.1 AND ABS(energy - 0.221) < 0.1
GROUP BY track_name
ORDER BY ABS(danceability - 0.118) + ABS(energy - 0.221) ASC
LIMIT 20