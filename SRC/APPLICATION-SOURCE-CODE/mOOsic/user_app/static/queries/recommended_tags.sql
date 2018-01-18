SELECT tag_name
FROM TracksToTags_tbl AS ttt
JOIN PlaylistToTracks_tbl AS ptt
ON ttt.track_id = ptt.track_id
JOIN
(
	SELECT playlist_id
	FROM Playlists_tbl
	JOIN Users_tbl
	ON Playlists_tbl.user_id = Users_tbl.user_id
	WHERE user_name = 'aa'
) AS ptu
ON ptt.playlist_id = ptu.playlist_id
JOIN Tags_tbl AS tt
ON tt.tag_id = ttt.tag_id
GROUP BY ttt.tag_id
HAVING COUNT(ttt.tag_id) >= ALL
(
	SELECT COUNT(tag_id)
	FROM TracksToTags_tbl AS ttt
	JOIN PlaylistToTracks_tbl AS ptt
	ON ttt.track_id = ptt.track_id
	JOIN
	(
		SELECT playlist_id
		FROM Playlists_tbl
		JOIN Users_tbl
		ON Playlists_tbl.user_id = Users_tbl.user_id
		WHERE user_name = {username}
	) AS ptu
	ON ptt.playlist_id = ptu.playlist_id
    GROUP BY tag_id
)
LIMIT 5