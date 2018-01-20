import React, { Component } from "react";
import { ListGroup, ListGroupItem, Button } from "react-bootstrap";
import "./SearchResults.css";

class ArtistSearchResults extends Component {
    render() {
        console.log(this.props)
        if (this.props.data.length == 0) {
            return <div>no results</div>
        }
        return (
            <ListGroup>
                {this.props.data.map((artist) =>
                            <ListGroupItem>
                                {"artist: " + (artist.name)}
                                <Button bsStyle="primary" bsSize="xsmall" onClick={() => this.props.getArtistSongs(artist.id)}>
                                    + 
                                </Button>
                            </ListGroupItem>)
                }
            </ListGroup>
        );
    }
}

class TrackSearchResults extends Component {
    render() {
        if (this.props.data.length == 0) {
            return <div>no results</div>
        }
        return (
            <ListGroup>
                {this.props.data.map((track) =>
                            <ListGroupItem>
                                {"track: " + (track.name) + " artist: " + (track.artist.name)}
                                {(this.props.playlists.length != 0)? (
                                <Button bsStyle="primary" bsSize="xsmall" onClick={() => this.props.addToPlaylist(track)}>
                                  + 
                                    </Button>):null}
                                <Button bsStyle="info" bsSize="xsmall" onClick={() => this.props.changeLyrics(track)}>
                                    lyrics
                                </Button>
                            </ListGroupItem>)
                }
            </ListGroup>
        );
    }
}

export default class SearchResults extends Component {
    render() {
        if (this.props.type == 'track') {
            return <TrackSearchResults data={this.props.data} addToPlaylist={this.props.addToPlaylist} changeLyrics={this.props.changeLyrics} playlists={this.props.playlists}/>
        } else if (this.props.type == 'artist') {
            return <ArtistSearchResults data={this.props.data} getArtistSongs={this.props.getArtistSongs}/>
        }
    }
}
