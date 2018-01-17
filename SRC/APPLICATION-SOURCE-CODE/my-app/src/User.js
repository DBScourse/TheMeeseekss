import React, { Component } from "react";
import Navbar from "./Navbar.js";
import Tops from "./Tops.js";
import Lyrics from "./Lyrics.js";
import Playlist from "./Playlist.js";
import Recommendations from "./Recommendations.js";
import CreatePlaylistModal from "./CreatePlaylistModal.js"
import SearchResults from "./SearchResults.js"
import { Grid, Col, Row, Container, Modal} from "react-bootstrap";

import "./User.css";

// sleep time expects milliseconds
function sleep(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}



export default class User extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
          playlists: null,
          tops: null,
          userRecommendation: null,
          playlistRecommendation: null,
          currentPlaylist: null,
          currentLyrics: null,
          playlistPreferences: null,
          showCreatePlaylistModal: false,
          freeSearch:null,
          currentResults: null
        };
    }
    
    /*onChangePlaylist(playlist) {
        console.log(playlist);
        fetch('/api/get_playlist?playlist_id=' + playlist.id)
            .then(res => res.json())
            .then(res => this.setState({currentPlaylist: res}));
        
        fetch('/api/get_playlist_recommendation?playlist_id=' playlist.id)
            .then(res => res.json())
            .then(res => this.setState({playlistRecommendation: res}));
            
        fetch('/api/get_user_recommendation')
            .then(res => res.json())
            .then(res => this.setState({userRecommendation: res}));
    }*/
    
    onChangePlaylist(playlist) {
        console.log('onChangePlaylist');
        sleep(2000)
            .then(res => ({
                id: 3,
                name: 'Friends',
                tracks: [{name: 'hilulim', id: 15, artist: {name: 'The G', id: 78}},
                         {name: 'namaste', id: 15, artist: {name: 'static', id: 77}},
                         {name: 'gold', id: 15, artist: {name: 'benel', id: 68}},
                         {name: 'silsulim', id: 15, artist: {name: 'static', id: 77}}]
            }))
            .then(res => this.setState({currentPlaylist: res}));

        sleep(2000)
            .then(res => ({name: 'its all for the best', id: 15, artist: {name: 'stat boy', id: 78}}))
            .then(res => this.setState({playlistRecommendation: res}));
            
        sleep(3000)
            .then(res => ({name: 'benel', id: 16, artist: {name: 'stat', id: 77}}))
            .then(res => this.setState({userRecommendation: res}));
        
        sleep(2000)
            .then(res => ({name: 'song name', id: 33, artist: {name: 'artist', id: 4}, lyrics: 'here is the lyrics\n lalalala'}))
            .then(res => this.setState({currentLyrics: res}));
    }
    
    /*changeLyrics(track){
        fetch('/api/get_lyrics?lyrics_id=' + res.tracks[0].id)
            .then(res => res.json())
            .then(res => this.setState({currentLyrics: res}));       
    }*/
    
    changeLyrics(track){
        console.log('changeLyrics');
        this.setState({currentResults: null})
        sleep(2000)
            .then(res => ({name: 'hallelujah', id: 33, artist: {name: 'leonard cohen', id: 4}, lyrics: 'Ive heard there was a secret chord\nThat David played and it pleased the lord\nBut you don\'t really care for music do you\nIt goes like this \nThe fourth the fifth \nThe minor fall the major lift\nThe baffled king composing Hallelujah'}))
            .then(res => this.setState({currentLyrics: res}));
            
    }
    
    
    /*addToPlaylist(track){
        fetch('/api/add_track', {
            method: 'POST',
            body: JSON.stringify({
                track_id: track.id,
                playlist_id: this.state.currentPlaylist.id
            })
        })
    }*/

    openCreatePlaylistModal() {
        console.log('openCreatePlaylistModal');
        this.setState({showCreatePlaylistModal: true});
    }
    
    hideCreatePlaylistModal(){
        console.log('hideCreatePlaylistModal');
        this.setState({showCreatePlaylistModal: false});
    }
    
    componentDidMount() {
        console.log('componentDidMount');
        var playlists_promise = sleep(3000)
            .then(res => [{name: 'Love', id: 1}, {name: 'Happy', id: 2}, {name: 'Friends', id: 3}]);

        playlists_promise
            .then(res => this.setState({playlists: res}));

        playlists_promise
            .then(res => sleep(3000))
            .then(res => (
                        {id: 1, 
                        name: 'Love', 
                        tracks: [{name: 'hi jude', id: 15, artist: {name: 'The Beatles', id: 78}}, 
                          {name: 'No woman no cry', id: 18, artist: {name: 'Bob Marely', id: 77}},
                          {name: 'Black Bird', id: 65, artist: {name: 'The Beatles', id: 68}},
                          {name: 'Stand by me', id: 15, artist: {name: 'Ben E King', id: 78}},
                          {name: 'Dont stop Me Now', id: 15, artist: {name: 'queen', id: 78}}]}))
            .then(res => this.setState({currentPlaylist: res}));
        
        playlists_promise
            .then(res => sleep(3000))
            .then(res => ({name: 'hi jude', id: 15, artist: {name: 'The Beatles', id: 78}}))
            .then(res => this.setState({playlistRecommendation: res}));
        
        sleep(2000)
            .then(res => ({name: 'hi jude', id: 33, artist: {name: 'The Beatles', id: 4}, lyrics: 'hi jude skjghsfjkjg\n lalala\nladbdffb'}))
            .then(res => this.setState({currentLyrics: res}));
        
        sleep(3000)
            .then(res => ({track: {name: 'I love you baby', id: 55, artist: {name: 'Gili', id:24}}, artist: {name: 'bery saharof', id: 27}}))
            .then(res => this.setState({tops: res}));
            
        sleep(3000)
            .then(res => ({name: 'hi Alice', id: 16, artist: {name: 'The Bugs', id: 77}}))
            .then(res => this.setState({userRecommendation: res}));

        /*var playlists_promise = fetch('/api/get_playlists')
            .then(res => res.json());

        playlists_promise
            .then(res => this.setState({playlists: res}));

        playlists_promise
            .then(res => fetch('/api/get_playlist?playlist_id=' + res[0].id))
            .then(res => res.json())
            .then(res => this.setState({currentPlaylist: res}));
        
        fetch('/api/get_lyrics?lyrics_id=' + res.tracks[0].id)
            .then(res => res.json())
            .then(res => this.setState({currentLyrics: res}))
        
        playlists_promise
            .then(res => fetch('/api/get_playlist_recommendation?playlist_recommendation=' + res[0].id))
            .then(res => res.json())
            .then(res => this.setState({playlistRecommendation: res}));
        
        fetch('/api/get_tops')
            .then(res => res.json())
            .then(res => this.setState({tops: res}));
            
        fetch('/api/get_user_recommendation')
            .then(res => res.json())
            .then(res => this.setState({userRecommendation: res}));*/
        
    }
    
    
    
    changeData(){
        this.setState({showCreatePlaylistModal: false});
        
        var playlists_promise = sleep(3000)
            .then(res => [{name:'hate',id:4}, {name: 'Love', id: 1}, {name: 'Happy', id: 2}, {name: 'Friends', id: 3}]);

        playlists_promise
            .then(res => this.setState({playlists: res}));
        
        playlists_promise
            .then(res => sleep(3000))
            .then(res => ({name: 'afterfinidplaylisttrackname', id: 15, artist: {name: 'artisy', id: 78}}))
            .then(res => this.setState({playlistRecommendation: res}));
        
        sleep(2000)
            .then(res => ({name: 'llllll', id: 33, artist: {name: 'The Beatles', id: 4}, lyrics: 'gggg ggggg\n lalala\nffffff'}))
            .then(res => this.setState({currentLyrics: res}));
        
        sleep(3000)
            .then(res => ({track: {name: 'rrrrrrrr', id: 55, artist: {name: 'Gili', id:24}}, artist: {name: 'yyyyyyyy', id: 27}}))
            .then(res => this.setState({tops: res}));
            
        sleep(3000)
            .then(res => ({name: 'sssss', id: 16, artist: {name: 'The Bugs', id: 77}}))
            .then(res => this.setState({userRecommendation: res}));

    }
    
    /*changeData(){
        this.setState({showCreatePlaylistModal: false});
        
        var playlists_promise = fetch('/api/get_playlists')
            .then(res => res.json());

        playlists_promise
            .then(res => this.setState({playlists: res}));
        
        fetch('/api/get_lyrics?lyrics_id=' + res.tracks[0].id)
            .then(res => res.json())
            .then(res => this.setState({currentLyrics: res}))
        
        playlists_promise
            .then(res => fetch('/api/get_playlist_recommendation=' + res[0].id))
            .then(res => res.json())
            .then(res => this.setState({playlistRecommendation: res}));
        
        fetch('/api/get_tops')
            .then(res => res.json())
            .then(res => this.setState({tops: res}));
            
        fetch('/api/get_user_recommendation')
            .then(res => res.json())
            .then(res => this.setState({userRecommendation: res}));

    }*/
    
    
    onAddPlaylist(playlistPreferences){
        console.log('onAddPlaylist');
        sleep(3000).then(() => ({id: 1, name: 'Love', tracks: [{name: 'hi jude', id: 15, artist: {name: 'The Beatles', id: 78}}, 
                                                            {name: 'No woman no cry', id: 18, artist: {name: 'Bob Marely', id: 77}},
                                                            {name: 'Black Bird', id: 65, artist: {name: 'The Beatles', id: 68}},
                                                            {name: 'Stand by me', id: 15, artist: {name: 'Ben E King', id: 78}},
                                                            {name: 'Dont stop Me Now', id: 15, artist: {name: 'queen', id: 78}}]
                                }
                            )
                        )
        .then(res => this.setState({currentPlaylist: res}));
        this.changeData();
    }
    
    /*onAddPlaylist(playlistPreferences){
        fetch('/api/create_new_playlist', {
            method: 'POST',
            body: JSON.stringify({
                playlist_name: this.state.playlistPreferences.name,
                danceabilityValue: this.state.playlistPreferences.danceabilityValue,
                energyValue: this.state.playlistPreferences.energyValue,
                freeSearchType: this.state.playlistPreferences.freeSearchType,
                freeSearchData: this.state.playlistPreferences.freeSearchData,
                tags: this.state.playlistPreferences.tags
            })
        })
        .then(res => res.json())
        .then(res => this.setState({currentPlaylist: res.currentPlaylist}));
        changeData();
        
    }*/

    search(userInput){
        console.log(userInput);
        console.log(this.state);
        /*fetch('/api/create_new_playlist', {
                method: 'POST',
                body: JSON.stringify({
                type: this.state.freeSearch.type,
                data: this.state.freeSearch.data})
            }).then(res => res.json()).then(res=>{type: userInput.type, data: res.data})
        
        */
        
        sleep(3000).then(() => {
            if (userInput.type == 'track') {
                return {type: userInput.type, data:[{name: 'hi billllll', id: 15, artist: {name: 'The Beatles', id: 78}}, 
                                                    {name: 'No woman no cry', id: 18, artist: {name: 'Bob Marely', id: 77}},
                                                    {name: 'Black Bird', id: 65, artist: {name: 'The Beatles', id: 68}},
                                                    {name: 'Stand by me', id: 15, artist: {name: 'Ben E King', id: 78}},
                                                    {name: 'Dont stop Me Now', id: 15, artist: {name: 'queen', id: 78}}]}
            } else {
                return {type: userInput.type, data:[{name:'eyal golan', id: 67},
                                                     {name:'rami fortis', id: 80},
                                                     {name:'sarit hadad', id: 30}]}
            }})
        .then(res => this.setState({currentResults: res}));            
    }
    
    getArtistSongs(artistId) {
        /*fetch('/api/get_artist_song?id=' + artistId)
        .then(res => res.json()).then(res=>{type: userInput.type, data: res.data})
        
        */
        sleep(3000).then(() => {
                return {type: 'track', data:[{name: 'yafa sheli', id: 15, artist: {name: 'The Beatles', id: 78}}, 
                                                    {name: 'buy you daimond', id: 18, artist: {name: 'Bob Marely', id: 77}},
                                                    {name: 'sick on soccer', id: 65, artist: {name: 'The Beatles', id: 68}}]}
        }).then(res => this.setState({currentResults: res})); 
    }
    
    render() {
        console.log(this.state);
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
                        search={(userInput) => this.search(userInput)}
                        user={this.props.user} 
                        onLoggedOut={()=> this.props.onLoggedOut()} />
                <Grid>
                    <Row className="show-grid">
                        <Col xs={6} md={4}>
                            {(this.state.tops == null) ? "Loading..." : <Tops topArtist={this.state.tops.artist.name} topSong={this.state.tops.track.name} /> }
                        </Col>
                        <Col xs={6} md={4}>
                            {mainComponent}
                        </Col>
                        <Col xs={6} md={4}>
                            { (this.state.userRecommendation==null || this.state.playlistRecommendation==null) ? "Loading..." : <Recommendations playlistRec={this.state.playlistRecommendation.name} usersRec={this.state.userRecommendation.name} addToPlaylist={(track) => this.addToPlaylist(track)}/> }
                        </Col>
                        <Col xs={6} md={4}>
                            { (this.state.currentPlaylist==null) ? "Loading..." : <Playlist name={this.state.currentPlaylist.name} tracks={this.state.currentPlaylist.tracks} changeLyrics={(track) => this.changeLyrics(track)}/> }
                        </Col>
                    </Row>
                </Grid>
                <CreatePlaylistModal findNewPlaylist={(preferences) => this.onAddPlaylist(preferences)} show={this.state.showCreatePlaylistModal} onHide={() => this.hideCreatePlaylistModal()} />
            </div>
        );
    }
}
