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
            <h4><b>Playlist: {this.props.playlist.name}</b></h4>
            {console.log(this.props)}
            <ListGroup>{
                this.props.playlist.tracks.map((track) =>
                        <ListGroupItem onClick={() => this.props.changeLyrics(track)}>{(track.name) + " - " + (track.artist.name)}</ListGroupItem>)
            }</ListGroup>
        </div>
    );
  }    
}
