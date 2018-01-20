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
AND Playlists_tbl.playlist_id = {playlist_id}