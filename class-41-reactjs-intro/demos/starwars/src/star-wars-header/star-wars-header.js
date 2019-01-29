import React, { Component } from 'react';

class StarWarsHeader extends Component {
    render() {
        return (
            <header>
                <h1>Star Wars Stuff</h1>
                <h2>{this.props.subTitle}</h2>
            </header>
        );
    }
}

export default StarWarsHeader;