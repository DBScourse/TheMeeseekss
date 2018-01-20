SELECT tb.track_id,
    track_name,
    album_name,
    tb.artist_id,
    artist_name 
FROM Tracks_tbl AS tb
JOIN Artists_tbl AS art
ON tb.artist_id = art.artist_id
WHERE tb.artist_id = {artist_id}
LIMIT 20