import React, { Component } from "react";
import "./Lyrics.css";

export default class Lyrics extends Component {
  
  
  render() {
    if (this.props.track.length == 0) {
        return (<div>no results</div>);
    }
    return (
        <div>
            song: {this.props.track.name}, artist: {this.props.track.artist.name}<br/>
            {this.props.track.lyrics.split('\n').map((line) => <div>{line}</div>)}
        </div>
    );
  }    
}
