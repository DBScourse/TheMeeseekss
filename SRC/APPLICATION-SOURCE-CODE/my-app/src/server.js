export default class Server {
    constructor(username) {
        this.username = username;
        this.server = (process.env.NODE_ENV == 'production') ? '' : 'http://localhost:8000';
    }

    getPlaylist(id, playlistname) {
        return fetch(this.server + '/api/get_playlist?playlistId=' + id +'&username=' + this.state.username)
            .then(res => res.json())
            .then(res => res.playlist)
            .then(res => ({
                id: id, name: playlistname, tracks: [res.map((track) => ({id: track.track_id, name: track.track_name, artist: {name: track.artist_name}}))]}));
    }

    getTrackRecommendation(playlistId) {
        return fetch(this.server + 'get_playlist_recommendation?playlist_id=' + playlistId)
            .then(res => res.json());
    }

    getTagsRecommendations(playlistId) {
        return fetch(this.server + '/api/get_tags_recommendation?id=' + playlistId)
            .then(res => res.json());
    }
    
    getArtistRecommendation(playlistId) {
        return fetch(this.server + '/api/get_artist_recommendation?id=' + playlistId)
            .then(res => res.json());
    }
    
    getLyrics(trackId) {
        return fetch(this.server + '/api/get_lyrics?lyrics_id=' + trackId)
            .then(res => res.json());
    }
    
    addToPlaylist(trackId, playlistId) {
        return fetch(this.server + '/api/add_track', {
            method: 'POST',
            body: JSON.stringify({
                track_id: trackId,
                playlist_id: playlistId
            })
        }).then(res => res.json());
    }
    
    getPlaylists() {
        return fetch(this.server + '/api/get_playlists')
            .then(res => res.json());
    }
    
    getTops() {
        return fetch(this.server + '/api/get_tops')
            .then(res => res.json());
    }
    
    createNewPlaylist(this.state.username, name, danceability, energy, tags) {
        return fetch(this.server + '/api/create_new_playlist', {
            method: 'POST',
            body: JSON.stringify({
                username: this.username,
                playlist_name: name,
                danceability: danceability,
                energy: energy,
                tags: tags
            })
        }).then(res => res.json())
        .then(res => {
            if (res.status != 200) {
                return Promise.reject(new Error(res.response.status_message))
        }).then (res => ({
                id: id, name: playlistname, tracks: [res.map((track) => ({id: track.track_id, name: track.track_name, artist: {name: track.artist_name}}))]}))
    }
    track_id, track_name, album_name, artist_name
    
    
    search(artistName) {
        return fetch(this.server + '/api/free_search?search_query=' + artistName)
            .then(res => res.json())
            .then(res => {
                if (res.status == 200) {
                    return res.search_result
                } else {
                    return Promise.reject(new Error(res.response.status_message))
                }
            })
    }
    
    getArtistSongs(artistId) {
        return fetch(this.server + '/api/get_artist_song?id=' + artistId)
            .then(res => res.json())
            
    }
    
    login(name, password) {
        return fetch(this.server + '/api/login', {
            method: 'POST',
            body: JSON.stringify({
                username: name,
                password: password
            })
        }).then(res => res.json())
        .then(res => {
                if (res.status == 200) {
                    return
                } else {
                    return Promise.reject(new Error(res.response.status_message))
                }
        })
    }
    
    register(name, password) {
        return fetch(this.server + '/api/register', {
            method: 'POST',
            body: JSON.stringify({
                username: name,
                password: password
            })
        }).then(res => res.json())
          .then(res => {
            if (res.status == 200){
                return
            } else {
                return Promise.reject(new Error(res.response.status_message))
            }
        })
    }
    
}
