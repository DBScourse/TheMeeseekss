import React, { Component } from "react";
import Navbar from "./Navbar.js";
import Tops from "./Tops.js";
import Lyrics from "./Lyrics.js";
import Playlist from "./Playlist.js";
import Recommendations from "./Recommendations.js";
import { Grid, Col, Row, Container} from "react-bootstrap";

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
          currentPlaylist: null
          
        /*this.state = {
          playlists: [{name: 'Loading', id: 1}],
          tops: {track: {name: 'Loading', id: 55, artist: {name: 'Loading', id:24}}, artist: {name: 'Loading', id: 27}},
          userRecommendation: {name: 'Loading', id: 16, artist: {name: 'Loading', id: 77}},
          playlistRecommendation: {name: 'Loading', id: 16, artist: {name: 'Loading', id: 77}},
          currentPlaylist: [{name: 'Loading', id: 15, artist: {name: 'Loading', id: 78}}]*/
        };
    }
    
    componentDidMount() {
        var playlists_promise = sleep(3000)
            .then(res => [{name: 'Love', id: 1}, {name: 'Happy', id: 2}, {name: 'Friends', id: 3}]);

        playlists_promise
            .then(res => this.setState({playlists: res}));

        playlists_promise
            .then(res => sleep(3000))
            .then(res => [{name: 'hi jude', id: 15, artist: {name: 'The Beatles', id: 78}}, 
                          {name: 'No woman no cry', id: 18, artist: {name: 'Bob Marely', id: 77}},
                          {name: 'Black Bird', id: 65, artist: {name: 'The Beatles', id: 68}},
                          {name: 'Stand by me', id: 15, artist: {name: 'Ben E King', id: 78}},
                          {name: 'Dont stop Me Now', id: 15, artist: {name: 'queen', id: 78}}])
            .then(res => this.setState({currentPlaylist: res}));
        
        playlists_promise
            .then(res => sleep(3000))
            .then(res => ({name: 'hi jude', id: 15, artist: {name: 'The Beatles', id: 78}}))
            .then(res => this.setState({playlistRecommendation: res}));
        
        sleep(3000)
            .then(res => ({track: {name: 'I love you baby', id: 55, artist: {name: 'Gili', id:24}}, artist: {name: 'Roi Cohen', id: 27}}))
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
        
        playlists_promise
            .then(res => fetch('/api/get_playlist_recommendation=' + res[0].id))
            .then(res => res.json())
            .then(res => this.setState({playlistRecommendation: res}));
        
        fetch('/api/get_tops')
            .then(res => res.json())
            .then(res => this.setState({tops: res}));
            
        fetch('/api/get_user_recommendation')
            .then(res => res.json())
            .then(res => this.setState({userRecommendation: res}));*/
        
    }

    render() {
        return (
            <div>
                <Navbar playlists={this.state.playlists} username={"Gili"} />
                <Grid>
                    <Row className="show-grid">
                        <Col xs={6} md={4}>
                            {(this.state.tops == null) ? "Loading..." : <Tops topArtist={this.state.tops.artist.name} topSong={this.state.tops.track.name} /> }
                        </Col>
                        <Col xs={6} md={4}>
                            <Lyrics songName="hi jude" artist="The Beatles" lyrics={"Hey Jude, don't make it bad\nTake a sad song and make it better\nRemember to let her into your heart\nThen you can start to make it better\nHey Jude, don't be afraid\nYou were made to go out and get her\nThe minute you let her under your skin\nThen you begin to make it better\nAnd anytime you feel the pain, hey Jude, refrain\nDon't carry the world upon your shoulders\nFor well you know that it's a fool who plays it cool\nBy making his world a little colder\nNah nah nah nah nah nah nah nah nah\nHey Jude, don't let me down\nYou have found her, now go and get her\nRemember to let her into your heart\nThen you can start to make it better\nSo let it out and let it in, hey Jude, begin\nYou're waiting for someone to perform with\nAnd don't…\n"} />  
                        </Col>
                        <Col xs={6} md={4}>
                            { (this.state.userRecommendation==null || this.state.playlistRecommendation==null) ? "Loading..." : <Recommendations playlistRec={this.state.playlistRecommendation.name} usersRec={this.state.userRecommendation.name} /> }
                        </Col>
                        <Col xs={6} md={4}>
                            { (this.state.currentPlaylist==null) ? "Loading..." : <Playlist name={this.state.playlists[0].name} tracks={this.state.currentPlaylist} /> }
                        </Col>
                    </Row>
                </Grid>
            </div>
        );
    }
}
