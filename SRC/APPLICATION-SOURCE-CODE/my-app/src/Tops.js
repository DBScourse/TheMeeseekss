import React, { Component } from "react";
import "./Tops.css";

export default class Tops extends Component {
  

  render() {
    if (this.props.tops == null) {
        return <div>Loading...</div>
    }

    return (
        <div>
            <div>top artist is: {this.props.tops.artist.name}</div>
            <div>top song: {this.props.tops.track.name}</div>
        </div>
    );
  }    
}
