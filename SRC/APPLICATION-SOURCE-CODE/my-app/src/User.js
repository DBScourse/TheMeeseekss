import React, { Component } from "react";
import Navbar from "./Navbar.js";
import Tops from "./Tops.js";
import Lyrics from "./Lyrics.js";
import Playlist from "./Playlist.js";
import Recommendations from "./Recommendations.js";
import CreatePlaylistModal from "./CreatePlaylistModal.js"
import SearchResults from "./SearchResults.js"
import { Grid, Col, Row, Container, Modal} from "react-bootstrap";
import Server from "./server.js";
import ServerMock from "./serverMock.js";

import "./User.css";

var useMock = true;



export default class User extends Component {
    constructor(props) {
        super(props);
        
        if (useMock) {
            this.server = new ServerMock(this.props.user);
        } else {
            this.server = new Server(this.props.user);
        }

        this.state = {
          playlists: null,
          tops: null,
          recommendations: {
              track: null,
              artist: null,
              tags: null
          },
          artistRecommendation: null,
          currentPlaylist: null,
          currentLyrics: null,
          playlistPreferences: null,
          showCreatePlaylistModal: false,
          freeSearch:null,
          currentResults: null
        };
    }
    
    componentDidMount() {
        var playlists_promise = this.server.getPlaylists();

        playlists_promise
            .then(res => this.setState({playlists: res}));
        playlists_promise
            .then(res => {
                if (res.length != 0) {
                    this.onChangePlaylist(res[0])
                }
            });

        this.server.getTops()
            .then(res => this.setState({tops: res}));
    }

    onChangePlaylist(playlist) {
        this.server.getPlaylist(playlist.id, playlist.name)
            .then(res => this.showPlaylist(res));
    }

    showPlaylist(playlist) {
        this.setState({
            currentPlaylist: playlist,
        });

        this.changeLyrics(playlist.tracks[0]);

        this.server.getTrackRecommendation(playlist.id)
            .then(res => this.setState({
                recommendations: {
                    ...this.state.recommendations,
                    track: res
                }
            }));

        this.server.getTagsRecommendations(playlist.id)
            .then(res => this.setState({
                recommendations: {
                    ...this.state.recommendations,
                    tags: res
                }
            }));

        this.server.getArtistRecommendation(playlist.id)
            .then(res => this.setState({
                recommendations: {
                    ...this.state.recommendations,
                    artist: res
                }
            }));
    }
    
    changeLyrics(track) {
        this.setState({
            currentResults: null
        });
        this.server.getLyrics(track.id)
            .then(res => this.setState({currentLyrics: res}));
    }

    addToPlaylist(track) {
        var playlistId = this.state.currentPlaylist.id;
        this.server.addToPlaylist(track.id, playlistId)
            .then(() => {
                if (this.state.currentPlaylist.id != playlistId) {
                    return;
                }
                this.setState({
                    currentPlaylist: {
                        ...this.state.currentPlaylist,
                        tracks: [...this.state.currentPlaylist.tracks, track]
                    }
                });
            });
    }

    showCreatedPlaylist(playlist) {
        this.setState({
            showCreatePlaylistModal: false,
            playlists: [...this.state.playlists, {
                id: playlist.id,
                name: playlist.name
            }]
        })

        this.showPlaylist(playlist);
    }

    
    openCreatePlaylistModal() {
        this.setState({showCreatePlaylistModal: true});
    }
    
    hideCreatePlaylistModal(){
        this.setState({showCreatePlaylistModal: false});
    }
    
    
    createNewPlaylist(playlistPreferences) {
        this.server.createNewPlaylist(playlistPreferences.name, playlistPreferences.danceability/1000.0, 
                                      playlistPreferences.energy/1000.0, playlistPreferences.tags)
            .then(res => this.showCreatedPlaylist(res));
    }
    
    search(userInput) {
        this.server.search(userInput.data)
            .then(res => this.setState({
                currentResults: {
                    type: 'artist',
                    data: res
                }
            }));
    }

    getArtistSongs(artistId) {
        this.server.getArtistSongs(artistId)
            .then(res => this.setState({currentResults: {type: 'track', data: res}}))
    }

    renderMain() {
        if (this.state.currentResults != null) {
            return <SearchResults
                        type={this.state.currentResults.type}
                        data={this.state.currentResults.data}
                        addToPlaylist={(track) => this.addToPlaylist(track)} 
                        changeLyrics={(track) => this.changeLyrics(track)}
                        getArtistSongs={(artistId) => this.getArtistSongs(artistId)} />
        } else if (this.state.currentLyrics != null) {
            return <Lyrics track={this.state.currentLyrics} />
        } else if (this.state.playlists == null) {
            return <div>Waiting for playlists...</div>
        } else if (this.state.playlists.length == 0) {
            return <div>Welcome, newbie!!!</div>
        } else {
            return <div>Loading...</div>
        }
    }

    renderRecommendations() {
        if (this.state.playlists != null) {
            if (this.state.playlists.length == 0) {
                return <div>No Playlist</div>
            } else {
                return <Recommendations recommendations={this.state.recommendations} />
            }
        } else {
            return <div>Waiting for playlists...</div>
        }
    }

    renderPlaylist() {
        if (this.state.playlists != null) {
            if (this.state.playlists.length == 0) {
                return <div>No Playlist</div>
            } else {
                return <Playlist playlist={this.state.currentPlaylist}
                                 changeLyrics={(track) => this.changeLyrics(track)}/>
            }
        } else {
            return <div>Waiting for playlists...</div>
        }
    }

    render() {
        return (
            <div>
                <Navbar playlists={this.state.playlists} 
                        onChangePlaylist={(playlist) => this.onChangePlaylist(playlist)} 
                        createPlaylistModal={() => this.openCreatePlaylistModal()}
                        search={(userInput) => this.search(userInput.data)}
                        user={this.props.user} 
                        onLoggedOut={()=> this.props.onLoggedOut()} />
                <Grid>
                    <Row className="show-grid">
                        <Col xs={6} md={4}>
                            <Tops tops={this.state.tops} />
                            {this.renderRecommendations()}
                        </Col>
                        <Col xs={6} md={4}>
                            {this.renderMain()}
                        </Col>
                        <Col xs={6} md={4}>
                            {this.renderPlaylist()}
                        </Col>
                    </Row>
                </Grid>
                <CreatePlaylistModal
                    findNewPlaylist={(preferences) => this.createNewPlaylist(preferences)}
                    show={this.state.showCreatePlaylistModal}
                    onHide={() => this.hideCreatePlaylistModal()} />
            </div>
        );
    }
}
