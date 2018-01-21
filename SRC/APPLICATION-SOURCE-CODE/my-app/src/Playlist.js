import React, { Component } from "react";
import { ListGroup, ListGroupItem } from "react-bootstrap";
import "./Playlist.css";

export default class Playlist extends Component {
  render() {
    if (this.props.playlist == null) {
        return <div>Loading...</div>
    }

    return (
        <div>
            playlist: {this.props.playlist.name}
            {console.log(this.props)}
            <ListGroup>{
                this.props.playlist.tracks.map((track) =>
                        <ListGroupItem onClick={() => this.props.changeLyrics(track)}>{"track: " + (track.name) + " artist: " + (track.artist.name)}</ListGroupItem>)
            }</ListGroup>
        </div>
    );
  }    
}
