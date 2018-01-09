import React, { Component } from "react";
import "./Playlist.css";

export default class Playlist extends Component {
  
  
  render() {
    return (
        <div>
            playlist: {this.props.name}
            <ul>{
                this.props.tracks.map((track) => <li>{"track: " + (track.name) + " artist: " + (track.artist.name)}</li>)
            }
            </ul>
        </div>
    );
  }    
}
