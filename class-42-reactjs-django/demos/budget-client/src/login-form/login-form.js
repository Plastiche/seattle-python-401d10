import React, { Component } from 'react';
import superagent from 'superagent';

class RegistrationForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
        this.onChangeUserName = this.onChangeUserName.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    
    onChangeUserName(event) {
        this.setState({
            username: event.target.value
        });
    }

    onChangePassword(event) {
        this.setState({
            password: event.target.value
        });
    }

    onSubmit(event) {
        event.preventDefault();
        
        const url = 'http://localhost:8000/api/v1/login'
        superagent
            .post(url)
            .send({
                username : this.state.username,
                password: this.state.password,
            }).then(response => {
                this.props.onLogin({token: response.body.token})
            }).then(token => {
                
            }).catch(error => {
                console.error(error)
                this.props.onLogin({error:error.toString()})
            });
    }


    render() {
        return (
        <form onSubmit={this.onSubmit}>
            <input name='username' placeholder='user name' value={this.state.username} onChange={this.onChangeUserName} />
            <input name='password' type='password' placeholder='password' value={this.state.password} onChange={this.onChangePassword} />
            <button type='submit'>register</button>
        </form>
        );
    }
}

export default RegistrationForm;