// sleep time expects milliseconds
function sleep(time) {
  if (time === undefined) {
      time = 200 + 2800 * Math.random();
  }
  return new Promise((resolve) => setTimeout(resolve, time));
}

export default class Server {
    constructor(username) {
        this.username = username;
        this.server = (process.env.NODE_ENV == 'production') ? '' : 'http://localhost:8000';
    }

    getPlaylist(id) {
        return sleep().then(() => ({
            id: 3,
            name: 'Friends ' + id,
            tracks: [{
                name: 'hilulim',
                id: 15,
                artist: {
                    name: 'The G',
                    id: 78
                }
            }, {
                name: 'namaste',
                id: 16,
                artist: {
                    name: 'static',
                    id: 77
                }
            }, {
                name: 'gold',
                id: 17,
                artist: {
                    name: 'benel',
                    id: 68
                }
            }]
        }));
    }

    getTrackRecommendation(playlistId) {
        return sleep().then(() => ({
            name: 'its all for the best',
            id: 15,
            artist: {
                name: 'stat boy',
                id: 78
            }
        }));
    }

    getTagsRecommendations(playlistId) {
        return sleep().then(() => ['Love', 'Happy', 'Popular', 'Pop', 'Friends']);
    }
    
    
    getArtistRecommendation(playlistId) {
        return sleep().then(() => ({
            name: 'benel',
            id: 16,
            artist: {
                name: 'stat',
                id: 77
            }
        }));
    }
    
    getLyrics(trackId) {
        return sleep().then(() => ({
            name: 'Perfect ' + trackId,
            id: 33,
            artist: {
                name: 'Ed shearan',
                id: 4
            }, 
            lyrics: 'I found a love for me\nOh darling, just dive right in and follow my lead\nWell, I found a girl, beautiful and sweet\nOh, I never knew you were the someone waiting for me\nCause we were just kids when we fell in love\nNot knowing what it was'
        }));
    }
    
    addToPlaylist(trackId, playlistId) {
        return sleep();
    }
    
    getPlaylists() {
        return sleep().then(() => [{
            name: 'Love',
            id: 1
        }, {
            name: 'Happy',
            id: 2
        }, {
            name: 'Friends',
            id: 3
        }])
    }

    getTops() {
        return sleep().then(() => ({
            track: {
                name: 'I love you baby',
                id: 55,
                artist: {
                    name: 'Gili',
                    id:24
                }
            },
            artist: {
                name: 'bery saharof',
                id: 27
            }
        }));
    }
    
    createNewPlaylist(name, danceability, energy, tags) {
        return sleep().then(() => ({
            id: 1,
            name: name,
            tracks: [{
                name: 'hi jude',
                id: 15,
                artist: {
                    name: 'The Beatles',
                    id: 78
                }
            }, {
                name: 'No woman no cry',
                id: 18,
                artist: {
                    name: 'Bob Marely',
                    id: 77
                }
            }, {
                name: 'Black Bird',
                id: 65,
                artist: {
                    name: 'The Beatles',
                    id: 68
                }
            }, {
                name: 'Stand by me',
                id: 15,
                artist: {
                    name: 'Ben E King',
                    id: 78
                }
            }, {
                name: 'Dont stop Me Now',
                id: 15,
                artist: {
                    name: 'queen',
                    id: 78
                }
            }]
        }));
    }
    
    
    search(artistName) {
        return sleep().then(() => [{
            name:'eyal golan',
            id: 67
        }, {
            name:'eyal fortis',
            id: 80
        }, {
            name:'eyal hadad',
            id: 30
        }]);
    }
    
    getArtistSongs(artistId) {
        return sleep().then(() => [{
                name: 'pasta',
                id: 44,
                artist: {
                    name: 'The Beatles',
                    id: 78
                }
            }, {
                name: 'basta',
                id: 18,
                artist: {
                    name: 'Bob Marely',
                    id: 77
                }
            }, {
                name: 'Black Bird',
                id: 65,
                artist: {
                    name: 'The Beatles',
                    id: 68
                }
            }, {
                name: 'Stand by me',
                id: 15,
                artist: {
                    name: 'Ben E King',
                    id: 78
                }
            }, {
                name: 'Dont stop Me Now',
                id: 15,
                artist: {
                    name: 'queen',
                    id: 78
                }
            }])
    }
    
    login(name, password) {
        if (password == '123') {
            return sleep()
        } else {
            return sleep().then(() => Promise.reject(new Error('Wrong username/passowrd')))
        }
    }
    
    register(name, password) {
        if (name == 'gili') {
            return sleep().then(() => Promise.reject(new Error('this username is taken, choose different username')))
        } else {
            return sleep()
        }
    }
}
