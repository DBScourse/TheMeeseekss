To search and add to playist use:
1. create_new_playlist.sql - takes username and playlist name, returns nothing.
2. recommended_tracks_mood_and_tag.sql OR recommended_tracks_mood.sql - takes danceability, energy and tag (if using the first one) and returns a list of up to 20 tracks, including: track_id, track_name, album_name, artist_name.
3. insert_tracks_to_playlist.sql - adds tracks to last playlist by track_id. Note that you need to repeat the last row for each track_id.
NOTE: all of the above must happen in the same connection, because of one of the functions used!

To search for artist name containing a string:
1. search_artist_full_text.sql - take a substring, returns at most 20 artists whos names contain that substring.

To display general recommendations:
1. top_track.sql - takes nothing, returns artist name.
2. top_artist.sql - takes nothing, returns track_id, track_name, album_name, artist_name.

To display user-specific recommendations:
1. recommended_tags.sql - takes username, returns up to 5 tags that are most compatible with the songs the user has in his playlist.
2. recommended_artist.sql / recommended_artist_mood_only.sql - takes tag (if using the first one), danceability and energy, and returns the artist with most songs compatible to that mood.
3. get_tracks_by_artist.sql - takes artist name, returns at most 20 tracks of that artist, including: track_id, track_name, album_name, artist_name.

To insert another song into the user's last playlist:
1. add_to_last_playlist.sql - takes username and track_id and inserts the track into the most recent playlist of this user.


*** There will be no fulltext search on track names!

