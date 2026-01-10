import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';

/**
 * User Profile Page
 * Demonstrates dynamic routing with useParams hook
 * This page shows how to access route parameters
 */
function UserProfile() {
  // useParams hook to access route parameters
  const { userId } = useParams();
  
  // useNavigate hook for programmatic navigation
  const navigate = useNavigate();

  // Simulate user data based on ID
  const users = {
    '123': { name: 'Alice Johnson', role: 'Frontend Developer', email: 'alice@example.com' },
    '456': { name: 'Bob Smith', role: 'Backend Developer', email: 'bob@example.com' },
    '789': { name: 'Carol Williams', role: 'Full Stack Developer', email: 'carol@example.com' }
  };

  const user = users[userId] || { name: 'Unknown User', role: 'N/A', email: 'N/A' };

  const handleGoBack = () => {
    navigate('/');
  };

  const handleRandomUser = () => {
    const randomId = Math.floor(Math.random() * 1000);
    navigate(`/user/${randomId}`);
  };

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>👤 User Profile</h1>
        <p>Dynamic Route with useParams Hook</p>
      </div>

      <div className="content-section">
        <div className="profile-card">
          <div className="profile-avatar">
            {user.name.charAt(0)}
          </div>
          <h2>{user.name}</h2>
          <p className="user-id">User ID: {userId}</p>
          
          <div className="profile-info">
            <p><strong>Role:</strong> {user.role}</p>
            <p><strong>Email:</strong> {user.email}</p>
          </div>
        </div>

        <div style={{ textAlign: 'center', marginTop: '2rem' }}>
          <button 
            onClick={handleGoBack} 
            className="btn btn-primary"
            style={{ marginRight: '1rem' }}
          >
            ← Back to Home
          </button>
          <button 
            onClick={handleRandomUser} 
            className="btn btn-secondary"
          >
            Random User 🎲
          </button>
        </div>

        <div style={{ background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px', marginTop: '2rem' }}>
          <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>Router Hooks Demonstrated:</h3>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li><strong>useParams():</strong> Extracts route parameters (userId: {userId})</li>
            <li><strong>useNavigate():</strong> Programmatic navigation between routes</li>
            <li><strong>Dynamic Routes:</strong> URL pattern: /user/:userId</li>
          </ul>
          
          <h3 style={{ color: '#667eea', marginTop: '1.5rem', marginBottom: '0.5rem' }}>Try These:</h3>
          <ul style={{ lineHeight: '1.8', color: '#555' }}>
            <li>Visit <a href="/user/123" style={{ color: '#667eea', fontWeight: 'bold' }}>/user/123</a></li>
            <li>Visit <a href="/user/456" style={{ color: '#667eea', fontWeight: 'bold' }}>/user/456</a></li>
            <li>Visit <a href="/user/789" style={{ color: '#667eea', fontWeight: 'bold' }}>/user/789</a></li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
