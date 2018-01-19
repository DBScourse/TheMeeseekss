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

var userMock = true;



export default class User extends Component {
    constructor(props) {
        super(props);
        
        if (userMock) {
            this.server = new ServerMock(this.props.user);
        } else {
            this.server = new Server(this.props.user);
        }

        this.state = {
          playlists: null,
          tops: null,
          tagsRecommendation: null,
          playlistRecommendation: null,
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
            .then(res => this.onChangePlaylist(res[0]));
    }

    onChangePlaylist(playlist) {
        this.server.getPlaylist(playlist.id)
            .then(res => this.showPlaylist(res));
    }

    showPlaylist(playlist) {
        this.setState({currentPlaylist: playlist});

        this.changeLyrics(playlist.tracks[0]);

        this.server.getTrackRecommendation(playlist.id)
            .then(res => this.setState({playlistRecommendation: res}));

        this.server.getTagsRecommendations(playlist.id)
            .then(res => this.setState({tagsRecommendation: res}));

        this.server.getArtistRecommendation(playlist.id)
            .then(res => this.setState({artistRecommendation: res}));

        this.server.getTops()
            .then(res => this.setState({tops: res}));
    }
    
    
    changeLyrics(track) {
        this.setState({currentResults: null});
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
        this.server.createNewPlaylist(playlistPreferences.name, playlistPreferences.danceability, 
                                      playlistPreferences.energy, playlistPreferences.tags)
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

    render() {
        var mainComponent = "Loading..."
        if (this.state.currentResults != null) {
            mainComponent = <SearchResults type={this.state.currentResults.type} 
                             data={this.state.currentResults.data}
                             addToPlaylist={(track) => this.addToPlaylist(track)} 
                             changeLyrics={(track) => this.changeLyrics(track)}
                             getArtistSongs={(artistId) => this.getArtistSongs(artistId)}/>
        } else if (this.state.currentLyrics != null) {
            mainComponent = <Lyrics track={this.state.currentLyrics} />
        }

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
                            {(this.state.tops == null) ? "Loading..." : <Tops topArtist={this.state.tops.artist.name} topSong={this.state.tops.track.name} /> }
                            { (this.state.tagsRecommendation==null || this.state.playlistRecommendation==null) ? "Loading..." : <Recommendations playlistRec={this.state.playlistRecommendation.name} tagsRec={this.state.tagsRecommendation.name} /> }
                        </Col>
                        <Col xs={6} md={4}>
                            {mainComponent}
                        </Col>

                        <Col xs={6} md={4}>
                            { (this.state.currentPlaylist==null) ? "Loading..." : <Playlist name={this.state.currentPlaylist.name} tracks={this.state.currentPlaylist.tracks} changeLyrics={(track) => this.changeLyrics(track)}/> }
                        </Col>
                    </Row>
                </Grid>
                <CreatePlaylistModal findNewPlaylist={(preferences) => this.createNewPlaylist(preferences)} show={this.state.showCreatePlaylistModal} onHide={() => this.hideCreatePlaylistModal()} />
            </div>
        );
    }
}
