import React, { Component } from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import "./Playlist.css";

export default class Playlist extends Component {
  
  
  render() {
    console.log(this.props);
    return (
        <div>
            playlist: {this.props.name}
            <ListGroup>{
                this.props.tracks.map((track) =>
                        <ListGroupItem onClick={() => this.props.changeLyrics(track)}>{"track: " + (track.name) + " artist: " + (track.artist.name)}</ListGroupItem>)
            }</ListGroup>
        </div>
    );
  }    
}
