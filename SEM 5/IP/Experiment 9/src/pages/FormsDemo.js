import React from 'react';
import ControlledForm from '../components/ControlledForm';
import UncontrolledForm from '../components/UncontrolledForm';

/**
 * Forms Demo Page
 * Demonstrates both controlled and uncontrolled forms
 */
function FormsDemo() {
  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📝 Forms in React</h1>
        <p>Controlled vs Uncontrolled Forms with Validation</p>
      </div>

      <div className="content-section">
        <h2>Controlled Form</h2>
        <p style={{ marginBottom: '1.5rem', fontSize: '1.1rem', color: '#555' }}>
          In controlled forms, React state controls the form data. Every input change updates the state,
          giving you full control over the form values.
        </p>
        <ControlledForm />
      </div>

      <div className="content-section">
        <h2>Uncontrolled Form (with Refs)</h2>
        <p style={{ marginBottom: '1.5rem', fontSize: '1.1rem', color: '#555' }}>
          Uncontrolled forms use refs to access form values directly from the DOM, similar to traditional HTML forms.
        </p>
        <UncontrolledForm />
      </div>
    </div>
  );
}

export default FormsDemo;
