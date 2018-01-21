import React, { Component } from "react";
import "./Lyrics.css";

export default class Lyrics extends Component {
  
  
  render() {
    if (this.props.track.length == 0) {
        return (<div>no results</div>);
    }
    return (
        <div>
            <h3><b>{this.props.track.name}</b></h3>
            <h4>{this.props.track.artist.name}</h4>
            <br/>
            {this.props.track.lyrics.split('\n').map((line) => <div>{line}</div>)}
        </div>
    );
  }    
}
