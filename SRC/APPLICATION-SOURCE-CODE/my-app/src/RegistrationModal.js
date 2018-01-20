import React, { Component } from "react";
import {Modal, Button, FormGroup,  FormControl, ControlLabel} from "react-bootstrap";

import "./RegistrationModal.css";

export default class RegistrationModal extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: "",
            password: ""
        };
    }
    
    validateForm() {
        return this.state.username.length > 0 && this.state.password.length > 0;
    }

    handleChange = event => {
        this.setState({[event.target.id]: event.target.value});
    }

    handleSubmit(event) {
        console.log(this.state);
        event.preventDefault()
        this.props.handleRegistration({username: this.state.username, password: this.state.password});
    }
    
    render() {
        return (
            <div>  
                <Modal show={this.props.show} hide={this.props.onHide}>
                    <button type="button" className="close" onClick={this.props.onHide}>
                        <span>&times;</span>
                    </button>
                
                    
                    <h4 class="modal-title">please enter username and password</h4>
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
                        </FormGroup>
                        <Button
                            block
                            bsSize="large"
                            disabled={!this.validateForm()}
                            onClick={this.props.onHide}
                            type="submit">
                            register
                        </Button>
                    </form>
                </Modal>
            </div>
        );
    }    
}
