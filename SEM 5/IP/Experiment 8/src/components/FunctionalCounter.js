import React, { useState } from 'react';

/**
 * FunctionalCounter Component - State Management with Hooks
 * 
 * This component demonstrates:
 * - useState Hook for state management
 * - Event handling in functional components
 * - State updates and re-rendering
 * - Multiple state variables
 */
function FunctionalCounter() {
  // useState Hook - Returns [stateValue, setStateFunction]
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);

  // Event handlers
  const increment = () => {
    setCount(count + step);
  };

  const decrement = () => {
    setCount(count - step);
  };

  const reset = () => {
    setCount(0);
  };

  const changeStep = () => {
    const newStep = prompt('Enter step value:', step);
    if (newStep && !isNaN(newStep)) {
      setStep(parseInt(newStep));
    }
  };

  return (
    <div className="counter">
      <h3>Functional Counter (useState Hook)</h3>
      <div className="counter-display">
        <div className="counter-value">{count}</div>
        <p>Step: {step}</p>
      </div>
      <div className="counter-buttons">
        <button onClick={decrement}>- Decrement</button>
        <button onClick={reset}>Reset</button>
        <button onClick={increment}>+ Increment</button>
        <button onClick={changeStep}>Change Step</button>
      </div>
    </div>
  );
}

export default FunctionalCounter;
