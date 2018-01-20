INSERT INTO Playlists_tbl(user_id, playlist_name) 
SELECT user_id, %s
FROM Users_tbl 
WHERE user_name = {username}