import React from 'react';
import './App.css';
import './styles/components.css';

// Import all components
import Greeting from './components/Greeting';
import UserCard from './components/UserCard';
import FunctionalCounter from './components/FunctionalCounter';
import ClassCounter from './components/ClassCounter';
import TodoList from './components/TodoList';

/**
 * Main App Component
 * Demonstrates JSX, component composition, and passing props
 */
function App() {
  // Sample user data to demonstrate props
  const users = [
    { id: 1, name: 'Alice Johnson', role: 'Developer', email: 'alice@example.com' },
    { id: 2, name: 'Bob Smith', role: 'Designer', email: 'bob@example.com' },
    { id: 3, name: 'Carol Williams', role: 'Manager', email: 'carol@example.com' }
  ];

  return (
    <div className="App">
      {/* JSX allows us to write HTML-like syntax in JavaScript */}
      <header className="App-header">
        <h1>Experiment 8: React Basics</h1>
        <p>Demonstrating JSX, Components, Props, and State</p>
      </header>

      <main className="App-main">
        {/* Section 1: JSX Demonstration */}
        <section className="demo-section">
          <h2>1. JSX (JavaScript XML)</h2>
          <div className="jsx-demo">
            <p>This is JSX - HTML-like syntax in JavaScript!</p>
            <p>Current Time: {new Date().toLocaleTimeString()}</p>
            <p>Math Expression: 2 + 2 = {2 + 2}</p>
            {/* JSX supports conditional rendering */}
            {true && <p>✅ This message is conditionally rendered</p>}
          </div>
        </section>

        {/* Section 2: Functional Components with Props */}
        <section className="demo-section">
          <h2>2. Functional Components with Props</h2>
          <Greeting name="Student" />
          <Greeting name="Teacher" message="Welcome to React!" />
          
          <div className="user-cards">
            {users.map(user => (
              <UserCard 
                key={user.id}
                name={user.name}
                role={user.role}
                email={user.email}
              />
            ))}
          </div>
        </section>

        {/* Section 3: State Management with Hooks */}
        <section className="demo-section">
          <h2>3. State Management (useState Hook)</h2>
          <FunctionalCounter />
        </section>

        {/* Section 4: Class Components with State */}
        <section className="demo-section">
          <h2>4. Class Component with State</h2>
          <ClassCounter />
        </section>

        {/* Section 5: Practical Example - Todo List */}
        <section className="demo-section">
          <h2>5. Practical Example: Todo List</h2>
          <TodoList />
        </section>
      </main>

      <footer className="App-footer">
        <p>Experiment 8 - React Basics Demo © 2025</p>
      </footer>
    </div>
  );
}

export default App;
