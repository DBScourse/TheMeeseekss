SELECT *
FROM Tracks_tbl 
WHERE mood_id = 
(
	SELECT mood_id
    FROM Moods_tbl
    WHERE danceability = {danceability} AND energy = {energy}
)
LIMIT 20