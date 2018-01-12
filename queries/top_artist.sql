SELECT artist_name 
FROM Artists_tbl
WHERE artist_id = 
(
	SELECT artist_id, COUNT(artist_id) AS c
    FROM Tracks_tbl 
    JOIN PlaylistToTracks_tbl 
    ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
    WHERE c >= ALL
    (
		SELECT artist_id, COUNT(artist_id) AS c
		FROM Tracks_tbl 
		JOIN PlaylistToTracks_tbl 
		ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
        GROUP BY artist_id
    )
    GROUP BY artist_id
    LIMIT 1
)
