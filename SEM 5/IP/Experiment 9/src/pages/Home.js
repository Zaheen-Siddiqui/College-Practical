import React from 'react';
import { Link } from 'react-router-dom';

/**
 * Home Page Component
 * Landing page with links to all demonstrations
 */
function Home() {
  const features = [
    {
      icon: '📝',
      title: 'Forms',
      description: 'Learn about controlled and uncontrolled forms, validation, and handling multiple input types.',
      link: '/forms'
    },
    {
      icon: '🎯',
      title: 'Events',
      description: 'Explore various event handlers including mouse, keyboard, and focus events.',
      link: '/events'
    },
    {
      icon: '🎯',
      title: 'Refs',
      description: 'Understand refs for DOM manipulation, focus management, and accessing elements.',
      link: '/refs'
    },
    {
      icon: '🔑',
      title: 'Keys',
      description: 'Learn the importance of keys in lists and proper key usage patterns.',
      link: '/keys'
    }
  ];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🚀 React Advanced Concepts</h1>
        <p>Experiment 9: Forms, Events, Routers, Refs, and Keys</p>
      </div>

      <div className="content-section">
        <h2>Welcome to React Advanced Concepts!</h2>
        <p style={{ fontSize: '1.1rem', lineHeight: '1.8', color: '#555' }}>
          This interactive application demonstrates essential React concepts including form handling,
          event management, routing between pages, DOM manipulation with refs, and proper list key usage.
          Click on any card below to explore each concept in detail.
        </p>

        <div className="home-grid">
          {features.map((feature, index) => (
            <Link 
              to={feature.link} 
              key={index}
              className="feature-card"
            >
              <div className="icon">{feature.icon}</div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </Link>
          ))}
        </div>
      </div>

      <div className="content-section">
        <h2>🧭 Router Demonstration</h2>
        <p style={{ marginBottom: '1rem', fontSize: '1.1rem' }}>
          This application uses <strong>React Router</strong> for navigation. Try these features:
        </p>
        <ul style={{ lineHeight: '2', fontSize: '1.1rem', color: '#555' }}>
          <li>✅ Navigate between pages using the navigation bar</li>
          <li>✅ Click on cards to navigate to different sections</li>
          <li>✅ Use browser back/forward buttons (history works!)</li>
          <li>✅ Try dynamic routes: <Link to="/user/123" style={{ color: '#667eea', fontWeight: 'bold' }}>/user/123</Link></li>
          <li>✅ Test 404 page: <Link to="/invalid-page" style={{ color: '#667eea', fontWeight: 'bold' }}>/invalid-page</Link></li>
        </ul>
      </div>
    </div>
  );
}

export default Home;
