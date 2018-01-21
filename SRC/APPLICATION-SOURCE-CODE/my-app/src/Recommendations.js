import React, { Component } from "react";
import { Button, Panel } from "react-bootstrap";
import "./Recommendations.css";

export default class Recommendations extends Component {
  renderTagsRecommendation() {
      if (this.props.recommendations.tags == null) {
          return <div>Loading...</div>
      } else {
          return <div><b>You may also like songs with those tags:</b> {this.props.recommendations.tags}</div>
      }
  }

  renderArtistRecommendation() {
      if (this.props.recommendations.artist == null) {
          return <div>Loading...</div>
      } else {
          return <div><b>You may also like songs of:</b> {this.props.recommendations.artist.name}</div>
      }
  }
  
/*  renderTrackRecommendation() {
      if (this.props.recommendations.track == null) {
          return <div>Loading...</div>
      } else {
          return <div>you may also like the song: {this.props.recommendations.track.name}</div>
      }
  }*/
  
  render() {
    return (
        <div>
            <h4>{this.renderTagsRecommendation()}</h4>
            <h4>{this.renderArtistRecommendation()}</h4>
        </div>
       );
  }    
}
