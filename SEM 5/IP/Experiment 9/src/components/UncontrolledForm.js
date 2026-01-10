import React, { useRef, useState } from 'react';

/**
 * Uncontrolled Form Component
 * Demonstrates uncontrolled components using refs to access form values
 */
function UncontrolledForm() {
  // Create refs for form inputs
  const nameRef = useRef(null);
  const emailRef = useRef(null);
  const messageRef = useRef(null);
  const categoryRef = useRef(null);
  
  const [submitted, setSubmitted] = useState(false);
  const [formValues, setFormValues] = useState(null);

  // Handle form submission (onSubmit event)
  const handleSubmit = (e) => {
    e.preventDefault();

    // Access values using refs
    const formData = {
      name: nameRef.current.value,
      email: emailRef.current.value,
      message: messageRef.current.value,
      category: categoryRef.current.value
    };

    console.log('Uncontrolled Form Data:', formData);
    setFormValues(formData);
    setSubmitted(true);

    // Reset form
    setTimeout(() => {
      e.target.reset();
      setSubmitted(false);
      setFormValues(null);
    }, 3000);
  };

  // Handle focus on name input (demonstrates ref usage for DOM manipulation)
  const focusNameInput = () => {
    nameRef.current.focus();
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        {/* Text Input with Ref */}
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            ref={nameRef}
            defaultValue=""
            placeholder="Enter your name"
            required
          />
        </div>

        {/* Email Input with Ref */}
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            ref={emailRef}
            defaultValue=""
            placeholder="your.email@example.com"
            required
          />
        </div>

        {/* Select with Ref */}
        <div className="form-group">
          <label htmlFor="category">Category</label>
          <select id="category" ref={categoryRef} defaultValue="">
            <option value="">Select a category</option>
            <option value="general">General Inquiry</option>
            <option value="support">Technical Support</option>
            <option value="feedback">Feedback</option>
            <option value="other">Other</option>
          </select>
        </div>

        {/* Textarea with Ref */}
        <div className="form-group">
          <label htmlFor="message">Message</label>
          <textarea
            id="message"
            ref={messageRef}
            rows="4"
            defaultValue=""
            placeholder="Enter your message..."
            required
          />
        </div>

        {/* Buttons */}
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
          <button 
            type="button" 
            onClick={focusNameInput}
            className="btn btn-secondary"
          >
            Focus Name Input
          </button>
        </div>

        {/* Display submitted values */}
        {submitted && formValues && (
          <div className="success-message">
            <strong>✅ Form Submitted!</strong>
            <div style={{ marginTop: '0.5rem', textAlign: 'left' }}>
              <p><strong>Name:</strong> {formValues.name}</p>
              <p><strong>Email:</strong> {formValues.email}</p>
              <p><strong>Category:</strong> {formValues.category}</p>
              <p><strong>Message:</strong> {formValues.message}</p>
            </div>
          </div>
        )}
      </form>

      <div style={{ marginTop: '1.5rem', background: '#e7f3ff', padding: '1rem', borderRadius: '6px' }}>
        <h4 style={{ color: '#667eea', marginBottom: '0.5rem' }}>Refs Usage:</h4>
        <ul style={{ lineHeight: '1.6', color: '#555' }}>
          <li>✅ Access form values directly from DOM</li>
          <li>✅ No state updates on every keystroke</li>
          <li>✅ Useful for simple forms or integrating with non-React code</li>
          <li>✅ "Focus Name Input" button demonstrates DOM manipulation with refs</li>
        </ul>
      </div>
    </div>
  );
}

export default UncontrolledForm;
