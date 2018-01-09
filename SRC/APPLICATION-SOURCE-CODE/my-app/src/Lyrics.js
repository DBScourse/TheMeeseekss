import React, { Component } from "react";
import "./Lyrics.css";

export default class Lyrics extends Component {
  
  
  render() {
    return (
        <div>
            song: {this.props.songName}, artist: {this.props.artist}<br/>
            {this.props.lyrics.split('\n').map((line) => <div>{line}</div>)}
        </div>
    );
  }    
}
