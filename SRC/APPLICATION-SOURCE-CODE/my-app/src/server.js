export default class Server {
    constructor(username) {
        this.username = username;
        // this.server = (process.env.NODE_ENV == 'production') ? '' : 'http://localhost:8000';
    }

    getPlaylist(id, playlistname) {
        return fetch('/api/get_playlist?playlistId=' + id +'&username=' + this.state.username)
            .then(res => res.json())
            .then(res => res.playlist)
            .then(res => ({
                id: id, name: playlistname, tracks: res.map((track) => ({id: track.track_id, name: track.track_name, artist: {name: track.artist_name}}))}));
    }


    getTagsRecommendations(playlistId) {
        return fetch('/api/get_tags_recommendation?id=' + playlistId)
            .then(res => res.json());
    }
    
    getArtistRecommendation(playlistId) {
        return fetch('/api/get_artist_recommendation?id=' + playlistId)
            .then(res => res.json());
    }
    
    getLyrics(trackId) {
        return fetch('/api/get_lyrics?lyrics_id=' + trackId)
            .then(res => res.json());
    }
    
    addToPlaylist(trackId, playlistId) {
        return fetch('/api/add_song_to_playlist', {
            method: 'POST',
            body: JSON.stringify({
                track_id: trackId,
                playlist_id: playlistId
            })
        }).then(res => res.json());
    }
    
    getPlaylists() {
        return fetch('/api/get_playlists')
            .then(res => res.json())
            .then(res => 
                {if (res.status_message == 'Data pulled successfully') {
                    return 
                }
                });
    }
    
    getTops() {
        return fetch('/api/get_tops')
            .then(res => res.json())
            .then(res =>
                {if (res.status_message == 'Playlist updated successfully') {
                    console.log(res)
                    return res.tops
                } else {
                    return Promise.reject(new Error(res.response.status_message))
                }});
    }
    
    createNewPlaylist(name, danceability, energy, tags) {
        return fetch('/api/create_new_playlist', {
            method: 'POST',
            body: JSON.stringify({
                username: this.username,
                playlist_name: name,
                danceability: danceability,
                energy: energy,
                tags: tags
            })
        }).then((res) => res.json())
        .then(res => {
            if (res.status_message != 'Playlist generated successfully') {
                return Promise.reject(new Error(res.response.status_message))
            } else {
                return res
            }
        })
    }
    search(artistName) {
        return fetch('/api/free_search?search_query=' + artistName)
            .then(res => res.json())
            .then(res => {
                if (res.status_message == 'Data pulled successfully') {
                    return res
                } else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }
    
    getArtistSongs(artistId) {
        return fetch('/api/get_artist_song?id=' + artistId)
            .then(res => res.json())
            
            
    }
    
    login(name, password) {
        return fetch('/api/login', {
            method: 'POST',
            body: JSON.stringify({
                username: name,
                password: password
            })
        }).then(res => res.json())
        .then(res => {
            if (res.status_message == 'Logged in successfully') {
                return
            } else {
                return Promise.reject(new Error(res.status_message))
            }
        })
    }
    
    register(name, password) {
        return fetch('/api/register', {
            method: 'POST',
            body: JSON.stringify({
                username: name,
                password: password
            })
        }).then(res => res.json())
          .then(res => {
            if (res.status_message == 'Registered successfully'){
                return
            } else {
                return Promise.reject(new Error(res.status_message))
            }
        })
    }
    
}
