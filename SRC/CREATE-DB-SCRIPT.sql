-- create users table
CREATE TABLE Users_tbl
(
  user_id int NOT NULL AUTO_INCREMENT,
  user_name varchar(20) NOT NULL,
  password_hash char(32) NOT NULL,
  PRIMARY KEY (user_id),
  UNIQUE (user_name)
);

-- make sure hashed password is exactly 32 chars long
DELIMITER //
CREATE TRIGGER pass_hash_len BEFORE INSERT ON Users_tbl
  FOR EACH ROW
    IF (LENGTH(NEW.password_hash) <> 32) THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'password hash not 32 chars long!';
    END IF;//
DELIMITER ;

-- create playlist table
CREATE TABLE Playlists_tbl
(
  playlist_id int NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  playlist_name varchar(20) NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  PRIMARY KEY (playlist_id),
  FOREIGN KEY (user_id) REFERENCES Users_tbl(user_id)
);

-- create moods table
CREATE TABLE Moods_tbl
(
  mood_id int NOT NULL AUTO_INCREMENT,
  danceability int NOT NULL,
  energy int NOT NULL,
  genre varchar(20) NOT NULL,
  PRIMARY KEY (mood_id),
  UNIQUE (danceability, energy, genre)
);

-- create tags table
CREATE TABLE Tags_tbl
(
  tag_id int NOT NULL AUTO_INCREMENT,
  tag_name varchar(20) NOT NULL,
  UNIQUE (tag_name),
  PRIMARY KEY (tag_id)
);

-- create moods table
CREATE TABLE Artists_tbl
(
  artist_id int NOT NULL AUTO_INCREMENT,
  artist_name varchar(20) NOT NULL,
  PRIMARY KEY (artist_id)
);

-- create tracks table
CREATE TABLE Tracks_tbl
(
  track_id int NOT NULL AUTO_INCREMENT,
  track_name varchar(20) NOT NULL,
  album_name varchar(20),
  release_year YEAR,
  lyrics_url varchar (128),
  artist_id int NOT NULL,
  mood_id int NOT NULL,
  PRIMARY KEY (track_id),
  FOREIGN KEY (artist_id) REFERENCES Artists_tbl(artist_id),
  FOREIGN KEY (mood_id) REFERENCES Moods_tbl(mood_id)
);

-- create PlaylistToTracks table
CREATE TABLE PlaylistToTracks_tbl
(
  playlist_id int NOT NULL,
  track_id int NOT NULL,
  UNIQUE (playlist_id, track_id),
  FOREIGN KEY (playlist_id) REFERENCES Playlists_tbl(playlist_id),
  FOREIGN KEY (track_id) REFERENCES Tracks_tbl(track_id)
);

-- create TracksToTags table
CREATE TABLE TracksToTags_tbl
(
  track_id int NOT NULL,
  tag_id int NOT NULL,
  FOREIGN KEY (track_id) REFERENCES Tracks_tbl(track_id),
  FOREIGN KEY (tag_id) REFERENCES Tags_tbl(tag_id)
);