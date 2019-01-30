import React, { Component } from 'react';
import './App.css';
import Landing from './landing/landing'
import Main from './main/main'


class App extends Component {
  render() {
    return (
      <div className="App">
        <Landing />
        <Main />
      </div>
    );
  }
}

export default App;
