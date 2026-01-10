import React, { useState } from 'react';

/**
 * Controlled Form Component
 * Demonstrates controlled components where React state manages form data
 */
function ControlledForm() {
  // State for form fields
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    password: '',
    confirmPassword: '',
    gender: '',
    country: '',
    interests: [],
    subscribe: false
  });

  // State for form errors
  const [errors, setErrors] = useState({});
  
  // State for submission status
  const [submitted, setSubmitted] = useState(false);

  // Handle input changes (onChange event)
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    
    if (type === 'checkbox' && name === 'interests') {
      // Handle checkbox array
      const updatedInterests = checked
        ? [...formData.interests, value]
        : formData.interests.filter(item => item !== value);
      
      setFormData({
        ...formData,
        interests: updatedInterests
      });
    } else if (type === 'checkbox') {
      // Handle single checkbox
      setFormData({
        ...formData,
        [name]: checked
      });
    } else {
      // Handle other inputs
      setFormData({
        ...formData,
        [name]: value
      });
    }

    // Clear error for this field when user types
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  // Validate form
  const validateForm = () => {
    const newErrors = {};

    if (!formData.fullName.trim()) {
      newErrors.fullName = 'Full name is required';
    } else if (formData.fullName.length < 3) {
      newErrors.fullName = 'Name must be at least 3 characters';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    if (!formData.gender) {
      newErrors.gender = 'Please select a gender';
    }

    if (!formData.country) {
      newErrors.country = 'Please select a country';
    }

    return newErrors;
  };

  // Handle form submission (onSubmit event)
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent default form submission
    
    const newErrors = validateForm();
    
    if (Object.keys(newErrors).length === 0) {
      // Form is valid
      setSubmitted(true);
      console.log('Form submitted:', formData);
      
      // Reset form after 3 seconds
      setTimeout(() => {
        setFormData({
          fullName: '',
          email: '',
          password: '',
          confirmPassword: '',
          gender: '',
          country: '',
          interests: [],
          subscribe: false
        });
        setSubmitted(false);
      }, 3000);
    } else {
      // Form has errors
      setErrors(newErrors);
      setSubmitted(false);
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        {/* Text Input */}
        <div className={`form-group ${errors.fullName ? 'error' : ''}`}>
          <label htmlFor="fullName">Full Name *</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
            placeholder="Enter your full name"
          />
          {errors.fullName && <div className="error-message">{errors.fullName}</div>}
        </div>

        {/* Email Input */}
        <div className={`form-group ${errors.email ? 'error' : ''}`}>
          <label htmlFor="email">Email *</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="your.email@example.com"
          />
          {errors.email && <div className="error-message">{errors.email}</div>}
        </div>

        {/* Password Inputs */}
        <div className="form-row">
          <div className={`form-group ${errors.password ? 'error' : ''}`}>
            <label htmlFor="password">Password *</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Min 6 characters"
            />
            {errors.password && <div className="error-message">{errors.password}</div>}
          </div>

          <div className={`form-group ${errors.confirmPassword ? 'error' : ''}`}>
            <label htmlFor="confirmPassword">Confirm Password *</label>
            <input
              type="password"
              id="confirmPassword"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              placeholder="Confirm password"
            />
            {errors.confirmPassword && <div className="error-message">{errors.confirmPassword}</div>}
          </div>
        </div>

        {/* Radio Buttons */}
        <div className={`form-group ${errors.gender ? 'error' : ''}`}>
          <label>Gender *</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="gender"
                value="male"
                checked={formData.gender === 'male'}
                onChange={handleChange}
              />
              Male
            </label>
            <label>
              <input
                type="radio"
                name="gender"
                value="female"
                checked={formData.gender === 'female'}
                onChange={handleChange}
              />
              Female
            </label>
            <label>
              <input
                type="radio"
                name="gender"
                value="other"
                checked={formData.gender === 'other'}
                onChange={handleChange}
              />
              Other
            </label>
          </div>
          {errors.gender && <div className="error-message">{errors.gender}</div>}
        </div>

        {/* Select Dropdown */}
        <div className={`form-group ${errors.country ? 'error' : ''}`}>
          <label htmlFor="country">Country *</label>
          <select
            id="country"
            name="country"
            value={formData.country}
            onChange={handleChange}
          >
            <option value="">Select a country</option>
            <option value="usa">United States</option>
            <option value="uk">United Kingdom</option>
            <option value="india">India</option>
            <option value="canada">Canada</option>
            <option value="australia">Australia</option>
          </select>
          {errors.country && <div className="error-message">{errors.country}</div>}
        </div>

        {/* Checkboxes (Multiple) */}
        <div className="form-group">
          <label>Interests</label>
          <div className="checkbox-group">
            <label>
              <input
                type="checkbox"
                name="interests"
                value="coding"
                checked={formData.interests.includes('coding')}
                onChange={handleChange}
              />
              Coding
            </label>
            <label>
              <input
                type="checkbox"
                name="interests"
                value="design"
                checked={formData.interests.includes('design')}
                onChange={handleChange}
              />
              Design
            </label>
            <label>
              <input
                type="checkbox"
                name="interests"
                value="music"
                checked={formData.interests.includes('music')}
                onChange={handleChange}
              />
              Music
            </label>
          </div>
        </div>

        {/* Single Checkbox */}
        <div className="form-group">
          <label className="checkbox-group">
            <input
              type="checkbox"
              name="subscribe"
              checked={formData.subscribe}
              onChange={handleChange}
            />
            Subscribe to newsletter
          </label>
        </div>

        {/* Submit Button */}
        <button type="submit" className="btn btn-primary">
          Submit Form
        </button>

        {/* Success Message */}
        {submitted && (
          <div className="success-message">
            ✅ Form submitted successfully! Check console for data.
          </div>
        )}
      </form>
    </div>
  );
}

export default ControlledForm;
