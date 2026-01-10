import React from 'react';
import RefsExample from '../components/RefsExample';

/**
 * Refs Demo Page
 * Demonstrates useRef hook for DOM manipulation
 */
function RefsDemo() {
  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🎯 Refs in React</h1>
        <p>DOM Access and Manipulation with useRef</p>
      </div>

      <div className="content-section">
        <h2>Understanding Refs</h2>
        <p style={{ marginBottom: '1rem', fontSize: '1.1rem', color: '#555' }}>
          Refs provide a way to access DOM nodes or React elements created in the render method.
          They are useful when you need to:
        </p>
        <div style={{ background: '#f8f9fa', padding: '1rem', borderRadius: '6px', marginBottom: '1.5rem' }}>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li>✅ Focus on an input field</li>
            <li>✅ Measure DOM element dimensions</li>
            <li>✅ Trigger animations</li>
            <li>✅ Integrate with third-party DOM libraries</li>
            <li>✅ Store mutable values that don't trigger re-renders</li>
            <li>✅ Access uncontrolled component values</li>
          </ul>
        </div>
        <RefsExample />
      </div>
    </div>
  );
}

export default RefsDemo;
