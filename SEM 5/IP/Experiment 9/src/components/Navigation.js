import React from 'react';
import { Link, NavLink } from 'react-router-dom';

/**
 * Navigation Component
 * Demonstrates React Router Link and NavLink components
 * NavLink allows us to style active links
 */
function Navigation() {
  return (
    <nav className="navigation">
      <div className="nav-container">
        <Link to="/" className="nav-brand">
          React Advanced 🚀
        </Link>
        
        <ul className="nav-links">
          <li>
            <NavLink 
              to="/" 
              className={({ isActive }) => isActive ? 'active' : ''}
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink 
              to="/forms" 
              className={({ isActive }) => isActive ? 'active' : ''}
            >
              Forms
            </NavLink>
          </li>
          <li>
            <NavLink 
              to="/events" 
              className={({ isActive }) => isActive ? 'active' : ''}
            >
              Events
            </NavLink>
          </li>
          <li>
            <NavLink 
              to="/refs" 
              className={({ isActive }) => isActive ? 'active' : ''}
            >
              Refs
            </NavLink>
          </li>
          <li>
            <NavLink 
              to="/keys" 
              className={({ isActive }) => isActive ? 'active' : ''}
            >
              Keys
            </NavLink>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
