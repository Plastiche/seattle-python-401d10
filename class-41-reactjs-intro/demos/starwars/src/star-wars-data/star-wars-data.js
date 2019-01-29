import React, { Component } from 'react'

export default class StarWarsData extends Component {

    render() {
        return (
            <div className="results">

                Length: {this.props.items.length}

                <ul>
                {this.props.items.map(item => <li key={item.name}>{item.name}</li>)}
                </ul>
                

            </div>
        )
    }
}
