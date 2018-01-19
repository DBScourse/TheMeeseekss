INSERT INTO PlaylistToTracks_tbl(playlist_id, track_id)
SELECT playlist_id, {track_id}
FROM Playlists_tbl AS pt
JOIN Users_tbl AS ut
ON pt.user_id = ut.user_id
WHERE user_name = {username}
AND playlist_timestamp = 
(
	SELECT MAX(playlist_timestamp)
	FROM Playlists_tbl AS pt2
	JOIN Users_tbl AS ut2
	ON pt2.user_id = ut2.user_id
	WHERE user_name = {username}
)