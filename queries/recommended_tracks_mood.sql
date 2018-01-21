SELECT tb.track_id, mood_id,
    track_name,
    album_name,
    tb.artist_id,
    artist_name 
FROM Tracks_tbl AS tb
JOIN Artists_tbl
ON tb.artist_id = Artists_tbl.artist_id
WHERE mood_id IN
(
    SELECT mood_id
    FROM Moods_tbl
    WHERE ABS(danceability - 0.118) < 0.1 AND ABS(energy - 0.221) < 0.1
    order by ABS(danceability - 0.118) + ABS(energy - 0.221) ASC
)
LIMIT 20