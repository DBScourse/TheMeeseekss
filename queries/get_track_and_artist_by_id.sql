SELECT track_id, track_name, artist_id, artist_name 
FROM Tracks_tbl, Artist_tbl 
WHERE track_id = %s AND Tracks_tbl.artist_id = Artist_tbl.artist_id