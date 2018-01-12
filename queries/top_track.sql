SELECT * 
FROM Tracks_tbl
WHERE track_id = 
(
	SELECT track_id, COUNT(track_id) AS c
	FROM PlaylistToTracks_tbl
    WHERE c >= ALL
    (
		SELECT COUNT(track_id) AS c
		FROM PlaylistToTracks_tbl
        GROUP BY track_id
    )
    GROUP BY track_id
    LIMIT 1
)