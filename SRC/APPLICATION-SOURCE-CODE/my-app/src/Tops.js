import React, { Component } from "react";
import "./Tops.css";

export default class Tops extends Component {
  

  render() {
    return (
        <div>
            top artist is: {this.props.topArtist}<br/>
            <br/>
            top song: {this.props.topSong}
        </div>
    );
  }    
}
