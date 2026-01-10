import React from 'react';

/**
 * Greeting Component - Functional Component with Props
 * 
 * This component demonstrates:
 * - Functional component syntax
 * - Props usage
 * - Default props
 * - JSX rendering
 */
function Greeting(props) {
  return (
    <div className="greeting">
      <h3>Hello, {props.name}! 👋</h3>
      <p>{props.message}</p>
    </div>
  );
}

// Default props - used when props are not provided
Greeting.defaultProps = {
  name: 'Guest',
  message: 'Welcome to React JS!'
};

export default Greeting;
