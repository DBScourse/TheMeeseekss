export default class Server {
    constructor(username) {
        this.username = username;
        // this.server = (process.env.NODE_ENV == 'production') ? '' : 'http://localhost:8000';
    }

    getPlaylist(id, playlistName) {
        console.log()
        return fetch('/api/get_playlist?playlist_id=' + id +'&username=' + this.username.username)
            .then(res => res.json())
            .then(res => {
                console.log(res)
                if (res.status_message == 'Playlist updated successfully') {
                    return {playlistId: id, playlistName:playlistName, tracks: res.data}
                } else if (res.status_message == 'Empty result set') {
                    return {}
                } else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }


    getTagsRecommendations(playlistId) {
        return fetch('/api/get_tags_recommendation?username=' + this.username.username)
            .then(res => res.json())
            .then(res => {
                if (res.status_message == 'Playlist updated successfully') {
                    return res.data
                } else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }
    
    getArtistRecommendation(playlistId) {
        return fetch('/api/get_artist_recommendation?username=' + this.username.username)
            .then(res => res.json())
            .then(res => {
                if (res.status_message == 'Playlist updated successfully') {
                    return res.data
                } else if (res.status_message == 'Empty result set') {
                    return []
                } else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }
    
    getLyrics(trackId) {
        return fetch('/api/get_lyrics?lyrics_id=' + trackId)
            .then(res => res.json())
            .then(res => {
                if (res.status_message == 'Playlist updated successfully') {
                    return res.data
                } else if (res.status_message == 'Empty result set') {
                    return []
                }else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }
    
    addToPlaylist(trackId) {
        console.log(trackId)
        return fetch('/api/add_song_to_playlist', {
            method: 'POST',
            body: JSON.stringify({
                song_id: trackId,
                username: this.username.username
            })
        }).then(res => res.json())
        .then(res => {
            if (res.status_message == 'Playlist updated successfully') {
                return
            } else {
                return Promise.reject(new Error(res.status_message))
            }
        })
    }
    
    getPlaylists() {
        return fetch('/api/get_playlists?username='+this.username.username)
            .then(res => res.json())
            .then(res => 
                {if (res.status_message == 'Data pulled successfully') {
                    console.log(res.data)
                    return res.data
                } else if (res.status_message == 'Empty result set') {
                    return []
                } else {
                    return Promise.reject(new Error(res.status_message))
                }
                });
    }
    
    getTops() {
        return fetch('/api/get_tops')
            .then(res => res.json())
            .then(res =>
                {if (res.status_message == 'Playlist updated successfully') {
                    console.log(res)
                    return res.data
                } else {
                    return Promise.reject(new Error(res.status_message))
                }});
    }
    
    createNewPlaylist(name, danceability, energy, tags) {
        console.log(this.username.username, name, danceability, energy, tags)
        return fetch('/api/create_new_playlist', {
            method: 'POST',
            body: JSON.stringify({
                username: this.username.username,
                playlist_name: name,
                danceability: danceability,
                energy: energy,
                tags: tags
            })
        }).then((res) => res.json())
        .then(res => {
            console.log(res)
            if (res.status_message != 'Playlist generated successfully') {
                return Promise.reject(new Error(res.status_message))
            } else {
                return res.data
            }
        })
    }
    search(artistName) {
        console.log(artistName)
        return fetch('/api/free_search?search_query=' + artistName)
            .then(res => res.json())
            .then(res => {
                if (res.status_message == 'Data pulled successfully') {
                    return res.data
                } else if (res.status_message == 'Empty result set') {
                    return []
                }else {
                    return Promise.reject(new Error(res.status_message))
                }
            })
    }
    
    getArtistSongs(artistId) {
        return fetch('/api/get_artist_song?id=' + artistId)
            .then(res => res.json())
            .then (res => {
                if (res.status_message == 'Playlist updated successfully') {
                    return res.data
                } else if (res.status_message == 'Empty result set'){
                    return []
                } else {
                   return Promise.reject(new Error(res.status_message)) 
                }
            })
            
            
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
