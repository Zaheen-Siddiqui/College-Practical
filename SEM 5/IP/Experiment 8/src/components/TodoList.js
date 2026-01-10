import React, { useState } from 'react';

/**
 * TodoList Component - Practical Example
 * 
 * This component demonstrates:
 * - Complex state management (array of objects)
 * - Form handling
 * - Conditional rendering
 * - List rendering with map()
 * - Key prop for list items
 * - Event handling
 * - State updates with arrays
 */
function TodoList() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  // Add new todo
  const addTodo = () => {
    if (inputValue.trim() !== '') {
      const newTodo = {
        id: Date.now(),
        text: inputValue,
        completed: false
      };
      setTodos([...todos, newTodo]);
      setInputValue('');
    }
  };

  // Delete todo
  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  // Toggle todo completion
  const toggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id 
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };

  // Handle Enter key press
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addTodo();
    }
  };

  // Calculate statistics
  const totalTodos = todos.length;
  const completedTodos = todos.filter(todo => todo.completed).length;
  const pendingTodos = totalTodos - completedTodos;

  return (
    <div className="todo-list">
      {/* Input Section */}
      <div className="todo-input-container">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Enter a new todo..."
        />
        <button onClick={addTodo}>Add Todo</button>
      </div>

      {/* Todo List */}
      {todos.length > 0 ? (
        <ul className="todo-items">
          {todos.map(todo => (
            <li 
              key={todo.id} 
              className={`todo-item ${todo.completed ? 'completed' : ''}`}
            >
              <span 
                className="todo-text"
                onClick={() => toggleTodo(todo.id)}
              >
                {todo.completed ? '✅' : '⭐'} {todo.text}
              </span>
              <button 
                className="todo-delete"
                onClick={() => deleteTodo(todo.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <div className="empty-message">
          No todos yet. Add one above! 📝
        </div>
      )}

      {/* Statistics */}
      {todos.length > 0 && (
        <div className="todo-stats">
          <strong>Statistics:</strong> Total: {totalTodos} | 
          Completed: {completedTodos} | 
          Pending: {pendingTodos}
        </div>
      )}
    </div>
  );
}

export default TodoList;
