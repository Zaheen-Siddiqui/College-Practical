import React, { Component } from 'react';

/**
 * ClassCounter Component - Class Component with State
 * 
 * This component demonstrates:
 * - Class component syntax
 * - State management in class components
 * - this.state and this.setState()
 * - Event handling in class components
 * - Component lifecycle (constructor)
 */
class ClassCounter extends Component {
  // Constructor - initialize state
  constructor(props) {
    super(props);
    
    // State initialization in class components
    this.state = {
      count: 0,
      clicks: 0
    };

    // Bind event handlers (alternative to arrow functions)
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
  }

  // Event handler methods
  increment() {
    // setState() updates state and triggers re-render
    this.setState({
      count: this.state.count + 1,
      clicks: this.state.clicks + 1
    });
  }

  decrement() {
    this.setState({
      count: this.state.count - 1,
      clicks: this.state.clicks + 1
    });
  }

  // Arrow function - automatically binds 'this'
  reset = () => {
    this.setState({
      count: 0
      // Notice: clicks is not reset to demonstrate partial state updates
    });
  }

  // render() method - required in class components
  render() {
    return (
      <div className="counter">
        <h3>Class Counter (this.state & this.setState)</h3>
        <div className="counter-display">
          <div className="counter-value">{this.state.count}</div>
          <p>Total Clicks: {this.state.clicks}</p>
        </div>
        <div className="counter-buttons">
          <button onClick={this.decrement}>- Decrement</button>
          <button onClick={this.reset}>Reset Count</button>
          <button onClick={this.increment}>+ Increment</button>
        </div>
      </div>
    );
  }
}

export default ClassCounter;
