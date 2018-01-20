SELECT Artists_tbl.artist_id, artist_name
FROM Artists_tbl
JOIN Tracks_tbl 
ON Artists_tbl.artist_id = Tracks_tbl.artist_id
JOIN PlaylistToTracks_tbl 
ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
GROUP BY Artists_tbl.artist_id
HAVING COUNT(Artists_tbl.artist_id) >= ALL
(
	SELECT COUNT(artist_id)
	FROM Tracks_tbl 
	JOIN PlaylistToTracks_tbl 
	ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
	GROUP BY artist_id
)
LIMIT 1
