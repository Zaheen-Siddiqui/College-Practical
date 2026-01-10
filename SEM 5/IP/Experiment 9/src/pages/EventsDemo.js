import React from 'react';
import EventsShowcase from '../components/EventsShowcase';

/**
 * Events Demo Page
 * Demonstrates various React event handlers
 */
function EventsDemo() {
  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🎯 Events in React</h1>
        <p>Interactive Event Handling Demonstration</p>
      </div>

      <div className="content-section">
        <h2>Event Handlers Overview</h2>
        <p style={{ marginBottom: '1rem', fontSize: '1.1rem', color: '#555' }}>
          React events are named using camelCase and you pass a function as the event handler.
          Events in React are synthetic events - cross-browser wrappers around native events.
        </p>
        <div style={{ background: '#f8f9fa', padding: '1rem', borderRadius: '6px', marginBottom: '1.5rem' }}>
          <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>Common Event Types:</h3>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li><strong>onClick</strong> - Triggered when element is clicked</li>
            <li><strong>onChange</strong> - Triggered when input value changes</li>
            <li><strong>onSubmit</strong> - Triggered when form is submitted</li>
            <li><strong>onMouseEnter/onMouseLeave</strong> - Triggered on mouse hover</li>
            <li><strong>onFocus/onBlur</strong> - Triggered when element gains/loses focus</li>
            <li><strong>onKeyDown/onKeyPress</strong> - Triggered on keyboard input</li>
          </ul>
        </div>
        <EventsShowcase />
      </div>
    </div>
  );
}

export default EventsDemo;
