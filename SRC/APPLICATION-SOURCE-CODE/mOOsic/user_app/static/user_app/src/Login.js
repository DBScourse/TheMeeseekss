import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel, Nav, Navbar, NavItem, Modal } from "react-bootstrap";
import RegistrationModal from "./RegistrationModal"
import "./Login.css";

export default class Login extends Component {
   constructor(props) {
    super(props);

    this.state = {
        username: "",
        password: "",
        showModal: false
    };
  }

  validateForm() {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = event => {
    event.preventDefault();
  }
  
  handleShow() {
    this.setState({
        showModal: !this.state.showModal
    })
  }
  
  handleClose() {
		this.setState({ showModal: false });
	}

  render() {
    console.log(this.state);
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
                        <NavItem onClick={() => this.handleShow()}>
                            register
                        </NavItem>
                    </Nav>
                </Navbar>
            </div>            
            
            <div className="Login">
                
                <form onSubmit={this.handleSubmit}>
                  <FormGroup controlId="username" bsSize="large">
                    <ControlLabel>username</ControlLabel>
                    <FormControl
                      autoFocus
                      type="username"
                      value={this.state.username}
                      onChange={this.handleChange}
                    />
                  </FormGroup>
                  <FormGroup controlId="password" bsSize="large">
                    <ControlLabel>Password</ControlLabel>
                    <FormControl
                      value={this.state.password}
                      onChange={this.handleChange}
                      type="password"
                    />
                  </FormGroup>
                  <Button
                    block
                    bsSize="large"
                    disabled={!this.validateForm()}
                    type="submit"
                  >
                    Login
                  </Button>
                </form>
            </div>
            <div>
                <RegistrationModal show={this.state.showModal} onHide={this.handleClose}/>
            </div>
        </div>
    );
  }
}
