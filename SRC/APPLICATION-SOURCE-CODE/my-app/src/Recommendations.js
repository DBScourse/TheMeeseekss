import React, { Component } from "react";
import { Button, Panel } from "react-bootstrap";
import "./Recommendations.css";

export default class Recommendations extends Component {
  renderTagsRecommendation() {
      if (this.props.recommendations.tags == null) {
          return <div>Loading...</div>
      } else {
          return <div>you may also like songs with those tags: {this.props.recommendations.tags}</div>
      }
  }

  renderArtistRecommendation() {
      if (this.props.recommendations.artist == null) {
          return <div>Loading...</div>
      } else {
          return <div>you may also like songs of: {this.props.recommendations.artist.name}</div>
      }
  }
  
  render() {
    return (
        <div>
            {this.renderTagsRecommendation()}
            {this.renderArtistRecommendation()}
        </div>
       );
  }    
}
