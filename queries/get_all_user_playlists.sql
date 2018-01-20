SELECT playlist_id, playlist_name
FROM Playlists_tbl AS pt 
JOIN Users_tbl AS ut 
ON pt.user_id = ut.user_id
WHERE user_name = {username}