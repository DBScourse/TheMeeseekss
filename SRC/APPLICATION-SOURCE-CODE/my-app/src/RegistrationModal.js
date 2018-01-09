import React, { Component } from "react";
import {Modal } from "react-bootstrap";

import "./RegistrationModal.css";

export default class RegistrationModal extends Component {
  

  render() {
    return (
        <div>
            <Modal show={this.props.show} hide={this.props.onHide}>"gili"</Modal>
        </div>
    );
  }    
}
