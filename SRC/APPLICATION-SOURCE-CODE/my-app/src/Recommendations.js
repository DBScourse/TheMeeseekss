import React, { Component } from "react";
import { Button, Panel } from "react-bootstrap";
import "./Recommendations.css";

export default class Recomendations extends Component {
  
  
  render() {
    return (
        <div>
            you may also like songs with thos tags: {this.props.tagsRec}
            <br/>
            <br/>
            you may also like songs of: {this.props.playlistRec}
        </div>
       );
  }    
}
