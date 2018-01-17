SELECT track_id,
	track_name,
	album_name,
	artist_name 
FROM Tracks_tbl
JOIN Artists_tbl
ON Tracks_tbl.artist_id = Artists_tbl.artist_id 
WHERE track_id = 
(
	SELECT track_id
	FROM PlaylistToTracks_tbl
	GROUP BY track_id
    HAVING COUNT(track_id) >= ALL
    (
		SELECT COUNT(track_id)
		FROM PlaylistToTracks_tbl
		GROUP BY track_id
    )
	LIMIT 1
)