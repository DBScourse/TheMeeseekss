import React, { Component } from "react";
import "./Tops.css";

export default class Tops extends Component {
  

  render() {
    if (this.props.tops == null) {
        return <div>Loading...</div>
    }

    return (
        <div>
            <div><h4><b>Top artist is:</b> {this.props.tops.artist.name}</h4></div>
            <div><h4><b>Top song: </b>{this.props.tops.track.name}</h4></div>
        </div>
    );
  }    
}
