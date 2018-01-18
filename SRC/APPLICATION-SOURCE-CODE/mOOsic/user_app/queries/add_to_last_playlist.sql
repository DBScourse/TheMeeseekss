INSERT INTO PlaylistToTracks_tbl(playlist_id, track_id)
SELECT playlist_id, {track_id}
FROM Playlists_tbl AS pt
JOIN Users_tbl AS ut
ON pt.user_id = ut.user_id
WHERE user_name = {username}
AND playlist_timestamp >= ALL
(
	SELECT playlist_timestamp
    FROM Playlists_tbl AS pt2
    WHERE pt.user_id = pt2.user_id
)