import React from 'react';
import KeysList from '../components/KeysList';

/**
 * Keys Demo Page
 * Demonstrates the importance of keys in React lists
 */
function KeysDemo() {
  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🔑 Keys in React</h1>
        <p>Understanding the Importance of Keys in Lists</p>
      </div>

      <div className="content-section">
        <h2>Why Keys Matter</h2>
        <p style={{ marginBottom: '1rem', fontSize: '1.1rem', color: '#555' }}>
          Keys help React identify which items have changed, are added, or are removed.
          Keys should be given to elements inside an array to give them a stable identity.
        </p>
        <div style={{ background: '#f8f9fa', padding: '1rem', borderRadius: '6px', marginBottom: '1.5rem' }}>
          <h3 style={{ color: '#667eea', marginBottom: '0.5rem' }}>Key Best Practices:</h3>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li>✅ <strong>Use unique IDs</strong> from your data as keys</li>
            <li>✅ <strong>Stable:</strong> Keys should be stable across re-renders</li>
            <li>✅ <strong>Unique:</strong> Keys must be unique among siblings</li>
            <li>❌ <strong>Avoid array indexes</strong> as keys (causes issues when reordering)</li>
            <li>❌ <strong>Don't generate random keys</strong> (causes unnecessary re-renders)</li>
            <li>✅ <strong>Use consistent keys</strong> for the same items</li>
          </ul>
        </div>
        <KeysList />
      </div>
    </div>
  );
}

export default KeysDemo;
