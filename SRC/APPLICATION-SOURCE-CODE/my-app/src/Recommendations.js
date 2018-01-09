import React, { Component } from "react";
import { Button } from "react-bootstrap";
import "./Recommendations.css";

export default class Recomendations extends Component {
  
  
  render() {
    return (
        <div>            
            <div>Recommended song: {this.props.playlistRec}
            <Button bsStyle="primary">Add this song to your last playlist</Button>
            </div>

            <div>
                Other people also like: {this.props.usersRec}
                <Button bsStyle="primary">Add this song to your last playlist</Button>
            </div>
        </div>
    );
  }    
}
