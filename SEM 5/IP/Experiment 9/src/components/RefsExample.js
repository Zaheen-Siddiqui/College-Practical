import React, { useRef, useState } from 'react';

/**
 * Refs Example Component
 * Demonstrates various uses of useRef hook
 */
function RefsExample() {
  // Refs for different demonstrations
  const inputRef = useRef(null);
  const divRef = useRef(null);
  const counterRef = useRef(0);
  const scrollRef = useRef(null);
  
  const [renderCount, setRenderCount] = useState(0);
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

  // Focus input using ref
  const focusInput = () => {
    inputRef.current.focus();
    inputRef.current.style.background = '#fff3cd';
    setTimeout(() => {
      inputRef.current.style.background = 'white';
    }, 1000);
  };

  // Clear input using ref
  const clearInput = () => {
    inputRef.current.value = '';
    inputRef.current.focus();
  };

  // Measure element dimensions
  const measureElement = () => {
    if (divRef.current) {
      const { width, height } = divRef.current.getBoundingClientRect();
      setDimensions({ width: Math.round(width), height: Math.round(height) });
    }
  };

  // Increment counter without re-render
  const incrementWithoutRerender = () => {
    counterRef.current += 1;
    alert(`Counter value: ${counterRef.current}\nComponent did NOT re-render!`);
  };

  // Force re-render to show the difference
  const forceRerender = () => {
    setRenderCount(prev => prev + 1);
  };

  // Scroll to specific section
  const scrollToSection = () => {
    scrollRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };

  return (
    <div className="refs-demo">
      {/* Input Focus Demo */}
      <div className="input-ref-demo">
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>1. Focus Management</h3>
        <input
          ref={inputRef}
          type="text"
          placeholder="This input can be focused programmatically"
        />
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button onClick={focusInput} className="btn btn-primary">
            Focus Input
          </button>
          <button onClick={clearInput} className="btn btn-secondary">
            Clear Input
          </button>
        </div>
        <p style={{ marginTop: '0.5rem', color: '#666', fontSize: '0.9rem' }}>
          Using ref to directly access and manipulate DOM element
        </p>
      </div>

      {/* Measure Element Demo */}
      <div className="input-ref-demo">
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>2. Measuring Elements</h3>
        <div
          ref={divRef}
          style={{
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            padding: '2rem',
            borderRadius: '8px',
            marginBottom: '1rem',
            textAlign: 'center'
          }}
        >
          Resize your browser window and measure me!
        </div>
        <button onClick={measureElement} className="btn btn-primary">
          Measure Dimensions
        </button>
        {dimensions.width > 0 && (
          <p style={{ marginTop: '0.5rem' }}>
            Width: <strong>{dimensions.width}px</strong>, Height: <strong>{dimensions.height}px</strong>
          </p>
        )}
      </div>

      {/* Persistent Value Demo */}
      <div className="input-ref-demo">
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>3. Storing Mutable Values</h3>
        <p style={{ marginBottom: '1rem', color: '#666' }}>
          Refs can store values that persist across re-renders without causing re-renders.
        </p>
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
          <button onClick={incrementWithoutRerender} className="btn btn-primary">
            Increment (No Re-render)
          </button>
          <button onClick={forceRerender} className="btn btn-secondary">
            Force Re-render
          </button>
        </div>
        <div style={{ background: '#e7f3ff', padding: '1rem', borderRadius: '6px' }}>
          <p><strong>Counter Ref Value:</strong> {counterRef.current}</p>
          <p><strong>Render Count:</strong> {renderCount}</p>
          <p style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.5rem' }}>
            Click "Increment" to change ref value without re-rendering. 
            Then click "Force Re-render" to see the updated value.
          </p>
        </div>
      </div>

      {/* Scroll Demo */}
      <div className="scroll-demo">
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>4. Scrolling to Elements</h3>
        <button onClick={scrollToSection} className="btn btn-primary">
          Scroll to Target
        </button>
        
        <div className="scrollable-content">
          <p>Scroll down to see the target section...</p>
          <div style={{ height: '100px' }}></div>
          <p>Keep scrolling...</p>
          <div style={{ height: '100px' }}></div>
          
          <div ref={scrollRef} className="scroll-target">
            🎯 <strong>Target Section!</strong> You scrolled here using refs!
          </div>
          
          <div style={{ height: '100px' }}></div>
          <p>More content below...</p>
        </div>
      </div>

      {/* Refs Info */}
      <div style={{ background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px', marginTop: '2rem' }}>
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>useRef Hook Summary</h3>
        <ul style={{ lineHeight: '1.8', color: '#555' }}>
          <li>✅ <strong>Access DOM elements:</strong> Get direct reference to elements</li>
          <li>✅ <strong>Persist values:</strong> Store values that persist across re-renders</li>
          <li>✅ <strong>No re-renders:</strong> Changing ref values doesn't trigger re-renders</li>
          <li>✅ <strong>Focus management:</strong> Programmatically focus inputs</li>
          <li>✅ <strong>Measure elements:</strong> Get element dimensions and positions</li>
          <li>✅ <strong>Store previous values:</strong> Keep track of previous state or props</li>
          <li>✅ <strong>Integration:</strong> Work with third-party libraries that need DOM access</li>
        </ul>
      </div>
    </div>
  );
}

export default RefsExample;
