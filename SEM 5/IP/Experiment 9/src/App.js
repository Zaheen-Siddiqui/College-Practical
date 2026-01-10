import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import './styles/pages.css';
import './styles/components.css';

// Import components
import Navigation from './components/Navigation';

// Import pages
import Home from './pages/Home';
import FormsDemo from './pages/FormsDemo';
import EventsDemo from './pages/EventsDemo';
import RefsDemo from './pages/RefsDemo';
import KeysDemo from './pages/KeysDemo';
import UserProfile from './pages/UserProfile';
import NotFound from './pages/NotFound';

/**
 * Main App Component with React Router
 * Demonstrates routing between different pages
 */
function App() {
  return (
    <div className="App">
      {/* Navigation component appears on all pages */}
      <Navigation />

      {/* Routes configuration - different components for different paths */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/forms" element={<FormsDemo />} />
        <Route path="/events" element={<EventsDemo />} />
        <Route path="/refs" element={<RefsDemo />} />
        <Route path="/keys" element={<KeysDemo />} />
        
        {/* Dynamic route with parameter */}
        <Route path="/user/:userId" element={<UserProfile />} />
        
        {/* 404 Not Found - catch all route */}
        <Route path="*" element={<NotFound />} />
      </Routes>

      <footer className="app-footer">
        <p>Experiment 9 - React Advanced Concepts © 2025</p>
      </footer>
    </div>
  );
}

export default App;
