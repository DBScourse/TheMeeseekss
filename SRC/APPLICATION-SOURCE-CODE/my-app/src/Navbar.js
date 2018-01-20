import React, { Component } from "react";
import { Navbar, Nav, NavItem, MenuItem, NavDropdown, Grid, Col, Row, Container, FormGroup, InputGroup, Button, FormControl} from "react-bootstrap";
import "./Navbar.css";

export default class MoosicsNavbar extends Component {
    constructor (props, context) {
        super(props, context)
        this.state = {
          freeSearchType: 'artist',
          freeSearchData: '',
        }
    }
    freeSearchHandleChange(value) {
        this.setState({freeSearchData: value})
    }
    searchArtist(){
        this.setState({freeSearchType: "artist"})
    }
    searchTrack(){
        this.setState({freeSearchType: "track"})
    }
    search(){
        this.props.search({type:this.state.freeSearchType, data:this.state.freeSearchData})
        this.setState({freeSearchData: ""});
    }
    render() {
        return (
            <div>
                <Navbar>
                    <Navbar.Header>
                        <Navbar.Brand>
                            <a href="#home">mOOsic</a>
                        </Navbar.Brand>
                    </Navbar.Header>
                    <Nav>
                        <NavDropdown eventKey={2} title="your playlists" id="basic-nav-dropdown">
                            {this.props.playlists == null? "Loading..." : this.props.playlists.map((playlist) =>
                                <MenuItem onSelect={() => this.props.onChangePlaylist(playlist)}>{playlist.name}</MenuItem>)}
                        </NavDropdown>
                    </Nav>
                    <Nav pullLeft>
                        <NavItem eventKey={3} onClick={() => this.props.createPlaylistModal()}>
                            create new playlist
                        </NavItem>
                    </Nav>
                    <Navbar.Form pullLeft>
                        <FormGroup>
                            <InputGroup>
                                <InputGroup.Button>
                                    <Button>artist</Button>
                      
                                </InputGroup.Button>
                                <FormControl type="text" onChange={(e) => this.freeSearchHandleChange(e.target.value)} value={this.state.freeSearchData}/>
                                <InputGroup.Button>
                                    <Button onClick={() => this.search()}>Search!</Button>
                                </InputGroup.Button>
                            </InputGroup>
                        </FormGroup>
                    </Navbar.Form>
                    <Nav pullRight>
                        <NavItem eventKey={4} href="#">
                            Hi {this.props.user.username}
                        </NavItem>
                        <NavItem eventKey={4} onClick={() => this.props.onLoggedOut()}>
                            Logout
                        </NavItem>
                    </Nav>
                </Navbar>
            </div>
        );
    }    
}
