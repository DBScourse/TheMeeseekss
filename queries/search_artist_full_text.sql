SELECT artist_id, artist_name
FROM ArtistsAsText_tbl
WHERE MATCH(artist_name)
AGAINST({substr} IN NATURAL LANGUAGE MODE)
LIMIT 20