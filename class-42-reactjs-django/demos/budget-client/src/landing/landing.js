import React, { Component } from 'react';
import LoginForm from '../login-form/login-form';


class Landing extends Component {

    constructor(props) {
        super(props)
        this.state = {
            token : 'pending'
        }
        this.handleLogin = this.handleLogin.bind(this)
    }

    handleLogin(response) {

        // LAB TASK: make the login reponse display on screen
        console.log(response)
    }

    render() {
        return (
            <div>
                <h1>Landing</h1>
                <LoginForm onLogin={this.handleLogin}/>
                <div>
                {/* LAB TASK: make the login reponse display on screen */}
                </div>
            </div>
        );
    }
}

export default Landing;
