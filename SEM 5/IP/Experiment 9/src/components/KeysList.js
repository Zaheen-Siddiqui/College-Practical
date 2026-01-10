import React, { useState } from 'react';

/**
 * Keys List Component
 * Demonstrates proper usage of keys in React lists
 */
function KeysList() {
  // Initial items with unique IDs
  const [items, setItems] = useState([
    { id: 1, name: 'Learn React', priority: 'High', completed: false },
    { id: 2, name: 'Build a project', priority: 'Medium', completed: false },
    { id: 3, name: 'Deploy to production', priority: 'High', completed: false }
  ]);

  const [nextId, setNextId] = useState(4);
  const [newItemName, setNewItemName] = useState('');
  const [newItemPriority, setNewItemPriority] = useState('Medium');

  // Add new item with unique ID
  const addItem = () => {
    if (newItemName.trim()) {
      const newItem = {
        id: nextId,
        name: newItemName,
        priority: newItemPriority,
        completed: false
      };
      setItems([...items, newItem]);
      setNextId(nextId + 1);
      setNewItemName('');
    }
  };

  // Delete item by ID
  const deleteItem = (id) => {
    setItems(items.filter(item => item.id !== id));
  };

  // Toggle completion
  const toggleComplete = (id) => {
    setItems(items.map(item =>
      item.id === id ? { ...item, completed: !item.completed } : item
    ));
  };

  // Move item up
  const moveUp = (index) => {
    if (index > 0) {
      const newItems = [...items];
      [newItems[index - 1], newItems[index]] = [newItems[index], newItems[index - 1]];
      setItems(newItems);
    }
  };

  // Move item down
  const moveDown = (index) => {
    if (index < items.length - 1) {
      const newItems = [...items];
      [newItems[index], newItems[index + 1]] = [newItems[index + 1], newItems[index]];
      setItems(newItems);
    }
  };

  // Handle Enter key
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addItem();
    }
  };

  return (
    <div className="keys-demo">
      {/* Add Item Form */}
      <div className="form-container">
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>Add New Item</h3>
        <div className="add-item-form">
          <input
            type="text"
            value={newItemName}
            onChange={(e) => setNewItemName(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Enter item name..."
          />
          <select
            value={newItemPriority}
            onChange={(e) => setNewItemPriority(e.target.value)}
            style={{ padding: '0.8rem', border: '2px solid #ddd', borderRadius: '6px' }}
          >
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
          <button onClick={addItem} className="btn btn-primary">
            Add Item
          </button>
        </div>
      </div>

      {/* Items List with Keys */}
      <div style={{ background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px' }}>
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>
          Task List (Each item has a unique key)
        </h3>
        
        {items.length > 0 ? (
          <ul className="items-list">
            {/* 
              IMPORTANT: Using unique 'id' as key (CORRECT)
              Keys help React identify which items have changed, added, or removed
            */}
            {items.map((item, index) => (
              <li
                key={item.id}  // ✅ Using unique ID as key
                className="list-item"
                style={{
                  opacity: item.completed ? 0.6 : 1,
                  textDecoration: item.completed ? 'line-through' : 'none'
                }}
              >
                <div className="list-item-content">
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <input
                      type="checkbox"
                      checked={item.completed}
                      onChange={() => toggleComplete(item.id)}
                    />
                    <strong>{item.name}</strong>
                  </div>
                  <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.3rem' }}>
                    Priority: <span style={{
                      background: item.priority === 'High' ? '#f5576c' : item.priority === 'Medium' ? '#ffc107' : '#4CAF50',
                      color: 'white',
                      padding: '0.2rem 0.5rem',
                      borderRadius: '4px',
                      fontSize: '0.8rem'
                    }}>
                      {item.priority}
                    </span>
                    {' | '}ID: {item.id}
                  </div>
                </div>
                
                <div className="list-item-actions">
                  <button
                    onClick={() => moveUp(index)}
                    disabled={index === 0}
                    style={{
                      background: '#667eea',
                      color: 'white',
                      opacity: index === 0 ? 0.5 : 1,
                      cursor: index === 0 ? 'not-allowed' : 'pointer'
                    }}
                  >
                    ↑
                  </button>
                  <button
                    onClick={() => moveDown(index)}
                    disabled={index === items.length - 1}
                    style={{
                      background: '#667eea',
                      color: 'white',
                      opacity: index === items.length - 1 ? 0.5 : 1,
                      cursor: index === items.length - 1 ? 'not-allowed' : 'pointer'
                    }}
                  >
                    ↓
                  </button>
                  <button
                    onClick={() => deleteItem(item.id)}
                    style={{ background: '#f5576c', color: 'white' }}
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p style={{ textAlign: 'center', color: '#999', padding: '2rem' }}>
            No items yet. Add one above! 📝
          </p>
        )}

        {items.length > 0 && (
          <div className="stats-bar">
            Total: {items.length} | Completed: {items.filter(i => i.completed).length} | 
            Pending: {items.filter(i => !i.completed).length}
          </div>
        )}
      </div>

      {/* Keys Explanation */}
      <div style={{ background: '#fff3cd', padding: '1.5rem', borderRadius: '8px', marginTop: '2rem' }}>
        <h3 style={{ color: '#856404', marginBottom: '1rem' }}>⚠️ Why Keys Are Important</h3>
        <ul style={{ lineHeight: '1.8', color: '#856404' }}>
          <li>
            <strong>Efficient Updates:</strong> Keys help React identify which items changed, 
            avoiding unnecessary re-renders
          </li>
          <li>
            <strong>Preserve State:</strong> When items are reordered, keys ensure component 
            state is preserved correctly
          </li>
          <li>
            <strong>Correct Behavior:</strong> Without proper keys, React may update the wrong 
            elements when the list changes
          </li>
          <li>
            <strong>Performance:</strong> Using unique, stable keys improves rendering performance 
            for large lists
          </li>
        </ul>
      </div>

      {/* Bad vs Good Keys */}
      <div style={{ background: '#f8f9fa', padding: '1.5rem', borderRadius: '8px', marginTop: '2rem' }}>
        <h3 style={{ color: '#667eea', marginBottom: '1rem' }}>Key Usage Examples</h3>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
          <div style={{ background: '#ffebee', padding: '1rem', borderRadius: '6px' }}>
            <h4 style={{ color: '#c62828', marginBottom: '0.5rem' }}>❌ Bad Practice</h4>
            <pre style={{ background: 'white', padding: '0.5rem', borderRadius: '4px', fontSize: '0.85rem' }}>
{`items.map((item, index) => (
  <li key={index}>
    {item.name}
  </li>
))`}
            </pre>
            <p style={{ fontSize: '0.9rem', color: '#c62828', marginTop: '0.5rem' }}>
              Using array index causes issues when reordering
            </p>
          </div>
          
          <div style={{ background: '#e8f5e9', padding: '1rem', borderRadius: '6px' }}>
            <h4 style={{ color: '#2e7d32', marginBottom: '0.5rem' }}>✅ Good Practice</h4>
            <pre style={{ background: 'white', padding: '0.5rem', borderRadius: '4px', fontSize: '0.85rem' }}>
{`items.map(item => (
  <li key={item.id}>
    {item.name}
  </li>
))`}
            </pre>
            <p style={{ fontSize: '0.9rem', color: '#2e7d32', marginTop: '0.5rem' }}>
              Using unique ID ensures stability
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default KeysList;
