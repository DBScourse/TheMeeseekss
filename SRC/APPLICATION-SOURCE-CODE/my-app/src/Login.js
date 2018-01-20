import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel, Nav, Navbar, NavItem, Modal, HelpBlock} from "react-bootstrap";
import RegistrationModal from "./RegistrationModal"
import Server from "./server.js";
import ServerMock from "./serverMock.js";

import "./Login.css";


var useMock = false;


export default class Login extends Component {
    constructor(props) {
        super(props);

        if (useMock) {
            this.server = new ServerMock(this.props.user);
        } else {
            this.server = new Server(this.props.user);
        }

        this.state = {
            username: "",
            password: "",
            showModal: false,
            error: null,
        };
    }

    validateForm() {
        return this.state.username.length > 0 && this.state.password.length > 0;
    }

    handleChange = event => {
        this.setState({[event.target.id]: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault()
        // this.props.onLoggedIn({username: this.state.username});
        this.server.login(this.state.username, this.state.password)
            .then(() =>
                this.props.onLoggedIn({
                    username: this.state.username
                })
            ).catch((err) =>
                this.setState({
                    error: err.message,
                }));
    }

    showRegistrationModal() {
        this.setState({ showModal: true });
    }
  
    hideRegistrationModal() {
		this.setState({ showModal: false });
    }
    
    handleRegistration(user){
        this.server.register(user.username, user.password)
            .then(() =>
                this.props.onLoggedIn({
                    username: user.username})
            ).catch((err) =>
                this.setState({
                    error: err.message
                }));
    }
    
    render() {
        return (
            <div>
                <div>
                    <Navbar>
                        <Navbar.Header>
                            <Navbar.Brand>
                                <a href="#home">mOOsic</a>
                            </Navbar.Brand>
                        </Navbar.Header>
                        <Nav pullRight>
                            <NavItem onClick={() => this.showRegistrationModal()}>
                                register
                            </NavItem>
                        </Nav>
                    </Navbar>
                </div>            
                
                <div className="Login">                  
                    <form onSubmit={(event) => this.handleSubmit(event)}>
                        <FormGroup controlId="username" bsSize="large">
                            <ControlLabel>username</ControlLabel>
                            <FormControl
                              autoFocus
                              type="username"
                              value={this.state.username}
                              onChange={(event) => this.handleChange(event)}
                            />
                        </FormGroup>
                        <FormGroup controlId="password" bsSize="large">
                            <ControlLabel>Password</ControlLabel>
                            <FormControl
                              value={this.state.password}
                              onChange={(event) => this.handleChange(event)}
                              type="password"
                            />
                            { (this.state.error != null) ? <HelpBlock>{this.state.error}</HelpBlock> : null }
                        </FormGroup>
                        
                        <Button
                            block
                            bsSize="large"
                            disabled={!this.validateForm()}
                            type="submit">
                            Login
                        </Button>
                    </form>
                </div>

                <RegistrationModal show={this.state.showModal} onHide={() => this.hideRegistrationModal()} handleRegistration={(user) => this.handleRegistration(user)}/>
            </div>
        );
    }
}
