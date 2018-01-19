SELECT Tracks_tbl.track_id,
	track_name,
	album_name,
	artist_name 
FROM Tracks_tbl
JOIN Artists_tbl
ON Tracks_tbl.artist_id = Artists_tbl.artist_id
JOIN PlaylistToTracks_tbl
ON Tracks_tbl.track_id = PlaylistToTracks_tbl.track_id
JOIN Playlists_tbl
ON PlaylistToTracks_tbl.playlist_id = Playlists_tbl.playlist_id
JOIN Users_tbl
ON Playlists_tbl.user_id = Users_tbl.user_id
WHERE user_name = {ausername}
AND playlist_name = {playlist_name}