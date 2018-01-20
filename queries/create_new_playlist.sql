INSERT INTO Playlists_tbl(user_id, playlist_name) 
SELECT user_id, {playlist_name}
FROM Users_tbl 
WHERE user_name = {username}