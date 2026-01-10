import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './App.css';

// This is the entry point of our React application
// It renders the App component into the DOM element with id 'root'
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
