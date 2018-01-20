SELECT tb.track_id,
    track_name,
    album_name,
    tb.artist_id,
    artist_name 
FROM Tracks_tbl AS tb
JOIN Artists_tbl
ON tb.artist_id = Artists_tbl.artist_id
WHERE mood_id = 
(
    SELECT mood_id
    FROM Moods_tbl
    WHERE ABS(danceability - {danceability}) < 0.0001 AND ABS(energy - {energy}) < 0.0001
    LIMIT 1
)
LIMIT 20