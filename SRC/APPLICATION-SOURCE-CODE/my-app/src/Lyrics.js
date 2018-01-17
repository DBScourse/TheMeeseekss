import React, { Component } from "react";
import "./Lyrics.css";

export default class Lyrics extends Component {
  
  
  render() {
    return (
        <div>
            song: {this.props.track.name}, artist: {this.props.track.artist.name}<br/>
            {this.props.track.lyrics.split('\n').map((line) => <div>{line}</div>)}
        </div>
    );
  }    
}
