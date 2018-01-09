import React, { Component } from "react";
import { Navbar, Nav, NavItem, MenuItem, NavDropdown, Grid, Col, Row, Container} from "react-bootstrap";
import "./Navbar.css";

export default class MoosicsNavbar extends Component {
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
                        {this.props.playlists == null? "Loading..." : this.props.playlists.map((playlist) => <MenuItem eventKey={2.1}>{playlist.name}</MenuItem>)}
                    </NavDropdown>
                    <NavItem eventKey={3} href="#">
                        create new playlist
                    </NavItem>
                </Nav>
                <Nav pullRight>
                    <NavItem eventKey={4} href="#">
                        Hi {this.props.username}
                    </NavItem>
                </Nav>
                <Nav pullRight>
                    <NavItem eventKey={4} href="#">
                        Logout
                    </NavItem>
                </Nav>
            </Navbar>
        </div>
    );
  }    
}
