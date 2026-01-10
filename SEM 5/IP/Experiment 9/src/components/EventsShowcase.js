import React, { useState } from 'react';

/**
 * Events Showcase Component
 * Demonstrates various React event handlers
 */
function EventsShowcase() {
  const [clickCount, setClickCount] = useState(0);
  const [inputValue, setInputValue] = useState('');
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [keyPressed, setKeyPressed] = useState('');
  const [isFocused, setIsFocused] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [eventLog, setEventLog] = useState([]);

  // Add event to log
  const logEvent = (message) => {
    const timestamp = new Date().toLocaleTimeString();
    setEventLog(prev => [`[${timestamp}] ${message}`, ...prev.slice(0, 9)]);
  };

  // onClick Event
  const handleClick = () => {
    setClickCount(prev => prev + 1);
    logEvent(`Button clicked! Count: ${clickCount + 1}`);
  };

  // onChange Event
  const handleChange = (e) => {
    setInputValue(e.target.value);
    logEvent(`Input changed: "${e.target.value}"`);
  };

  // onMouseMove Event
  const handleMouseMove = (e) => {
    setMousePosition({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY });
  };

  // onKeyDown Event
  const handleKeyDown = (e) => {
    setKeyPressed(e.key);
    logEvent(`Key pressed: "${e.key}"`);
  };

  // onFocus Event
  const handleFocus = () => {
    setIsFocused(true);
    logEvent('Input focused');
  };

  // onBlur Event
  const handleBlur = () => {
    setIsFocused(false);
    logEvent('Input blurred');
  };

  // onMouseEnter Event
  const handleMouseEnter = () => {
    setIsHovered(true);
    logEvent('Mouse entered interactive box');
  };

  // onMouseLeave Event
  const handleMouseLeave = () => {
    setIsHovered(false);
    logEvent('Mouse left interactive box');
  };

  // onDoubleClick Event
  const handleDoubleClick = () => {
    logEvent('Box double-clicked!');
    alert('You double-clicked the box!');
  };

  // Clear event log
  const clearLog = () => {
    setEventLog([]);
  };

  return (
    <div>
      <div className="events-grid">
        {/* Click Event */}
        <div className="event-card">
          <h3>onClick Event</h3>
          <button onClick={handleClick} className="btn btn-primary">
            Click Me!
          </button>
          <p style={{ marginTop: '1rem', fontSize: '1.2rem' }}>
            Clicks: <strong>{clickCount}</strong>
          </p>
        </div>

        {/* Change Event */}
        <div className="event-card">
          <h3>onChange Event</h3>
          <input
            type="text"
            value={inputValue}
            onChange={handleChange}
            placeholder="Type something..."
            style={{ width: '100%', padding: '0.5rem', marginBottom: '0.5rem' }}
          />
          <p>Value: <strong>{inputValue || '(empty)'}</strong></p>
        </div>

        {/* Focus/Blur Events */}
        <div className={`event-card ${isFocused ? 'active' : ''}`}>
          <h3>onFocus / onBlur Events</h3>
          <input
            type="text"
            onFocus={handleFocus}
            onBlur={handleBlur}
            placeholder="Click to focus"
            style={{ width: '100%', padding: '0.5rem', marginBottom: '0.5rem' }}
          />
          <p>Status: <strong>{isFocused ? '🟢 Focused' : '🔴 Not Focused'}</strong></p>
        </div>

        {/* KeyDown Event */}
        <div className="event-card">
          <h3>onKeyDown Event</h3>
          <input
            type="text"
            onKeyDown={handleKeyDown}
            placeholder="Press any key..."
            style={{ width: '100%', padding: '0.5rem', marginBottom: '0.5rem' }}
          />
          <p>Last Key: <strong>{keyPressed || '(none)'}</strong></p>
        </div>
      </div>

      {/* Mouse Events */}
      <div style={{ marginTop: '2rem' }}>
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>Mouse Events</h3>
        <div className="events-grid">
          <div className="event-card">
            <h3>onMouseMove Event</h3>
            <div
              onMouseMove={handleMouseMove}
              style={{
                background: '#f0f0f0',
                height: '150px',
                borderRadius: '6px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'crosshair'
              }}
            >
              Move mouse here
            </div>
            <p style={{ marginTop: '0.5rem' }}>
              Position: X: <strong>{mousePosition.x}</strong>, Y: <strong>{mousePosition.y}</strong>
            </p>
          </div>

          <div className="event-card">
            <h3>onMouseEnter / onMouseLeave</h3>
            <div
              className="interactive-box"
              onMouseEnter={handleMouseEnter}
              onMouseLeave={handleMouseLeave}
              onDoubleClick={handleDoubleClick}
              style={{
                background: isHovered 
                  ? 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
                  : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                padding: '2rem',
                height: '150px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
            >
              {isHovered ? '🎉 Hovering!' : 'Hover over me'}
              <div style={{ fontSize: '0.9rem', marginTop: '0.5rem' }}>
                (Try double-clicking too!)
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Event Log */}
      <div style={{ marginTop: '2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
          <h3 style={{ color: '#667eea' }}>Event Log (Last 10 Events)</h3>
          <button onClick={clearLog} className="btn btn-danger">
            Clear Log
          </button>
        </div>
        <div className="event-log">
          {eventLog.length > 0 ? (
            eventLog.map((log, index) => (
              <p key={index}>{log}</p>
            ))
          ) : (
            <p style={{ color: '#888' }}>No events yet. Interact with the components above!</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default EventsShowcase;
