import React, { Component } from "react";

import Login from "./Login.js";
import User from "./User.js";


export default class App extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            user: null
        };
    }
    
    onLogIn(user){
        this.setState({user: user})
    }
    
    onLogout(){
        this.setState({user: null})
    }
    
    render() {
        if (this.state.user == null) {
            return <Login onLoggedIn={(user) => this.onLogIn(user)}/>;
        } else {
            return <User user={this.state.user} onLoggedOut={()=> this.onLogout()}/>;
        }
    }
}
