SELECT Tracks_tbl.track_id,
	track_name,
	album_name,
	Tracks_tbl.artist_id,
	artist_name 
FROM Tracks_tbl
JOIN Artists_tbl
ON Tracks_tbl.artist_id = Artists_tbl.artist_id 
JOIN PlaylistToTracks_tbl
ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
GROUP BY track_id
HAVING COUNT(PlaylistToTracks_tbl.track_id) >= ALL
(
	SELECT COUNT(PlaylistToTracks_tbl.track_id)
	FROM PlaylistToTracks_tbl
	GROUP BY track_id
)
LIMIT 1