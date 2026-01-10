import React from 'react';

/**
 * UserCard Component - Functional Component with Multiple Props
 * 
 * This component demonstrates:
 * - Destructuring props in function parameters
 * - Using multiple props
 * - Component styling with CSS classes
 */
function UserCard({ name, role, email }) {
  return (
    <div className="user-card">
      <h3>{name}</h3>
      <p><strong>Role:</strong> {role}</p>
      <p><strong>Email:</strong> {email}</p>
    </div>
  );
}

export default UserCard;
