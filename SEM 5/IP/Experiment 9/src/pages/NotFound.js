import React from 'react';
import { useNavigate } from 'react-router-dom';

/**
 * 404 Not Found Page
 * Catch-all route for invalid URLs
 */
function NotFound() {
  const navigate = useNavigate();

  return (
    <div className="page-container">
      <div className="content-section not-found">
        <h1>404</h1>
        <h2>Page Not Found</h2>
        <p>Oops! The page you're looking for doesn't exist.</p>
        <button 
          onClick={() => navigate('/')} 
          className="btn btn-primary"
        >
          Go Home
        </button>
        
        <div style={{ marginTop: '3rem', textAlign: 'left', background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px' }}>
          <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>This demonstrates:</h3>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li>✅ Catch-all route using <code>path="*"</code></li>
            <li>✅ Handling invalid URLs gracefully</li>
            <li>✅ Using useNavigate for programmatic navigation</li>
            <li>✅ Better user experience with helpful error pages</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default NotFound;
