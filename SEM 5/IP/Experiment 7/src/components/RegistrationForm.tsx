import React, { useState, useEffect } from 'react';
import { UserFormData, FormErrors, FormStats, SubmissionInfo } from '../types';
import { User, ValidationRules, MIN_AGE, MAX_AGE, calculatePasswordStrength, validateField } from '../utils/userUtils';

interface RegistrationFormProps {
  onSubmit: (data: SubmissionInfo) => void;
  onStatsUpdate: (stats: FormStats[]) => void;
}

const RegistrationForm: React.FC<RegistrationFormProps> = ({ onSubmit, onStatsUpdate }) => {
  // State variables - demonstrating different types
  const [formData, setFormData] = useState<UserFormData>({
    username: '',
    password: '',
    email: '',
    mobile: '',
    age: '',
    gender: '',
    hobbies: [],
    technologies: [],
    personalInfo: ''
  });

  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [submissionCount, setSubmissionCount] = useState<number>(0);
  const [validationCounter, setValidationCounter] = useState<number>(0); // Track validation calls
  const [formStats, setFormStats] = useState<FormStats[]>([
    { field: 'username', errors: 0, validations: 0 },
    { field: 'password', errors: 0, validations: 0 },
    { field: 'email', errors: 0, validations: 0 },
    { field: 'mobile', errors: 0, validations: 0 },
    { field: 'age', errors: 0, validations: 0 }
  ]);

  // useEffect hook for component lifecycle
  useEffect(() => {
    console.log('Form initialized at:', new Date().toLocaleString());
    
    // Initialize stats using for...of loop - but only increment by 1 instead of for each field
    const updatedStats = [...formStats];
    let hasIncremented = false;
    for (const stat of updatedStats) {
      if (!hasIncremented) {
        stat.validations++;
        hasIncremented = true; // Only increment once instead of for each field
      }
    }
    setFormStats(updatedStats);
    onStatsUpdate(updatedStats);
  }, [formStats, onStatsUpdate]); // Include dependencies

  // Event handler for input changes
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value, type } = e.target;
    
    // Switch statement for different input types
    switch (type) {
      case 'checkbox': {
        const checkbox = e.target as HTMLInputElement;
        const isChecked = checkbox.checked;
        
        setFormData(prev => ({
          ...prev,
          [name]: isChecked 
            ? [...(prev[name as keyof typeof prev] as string[]), value]
            : (prev[name as keyof typeof prev] as string[]).filter(item => item !== value)
        }));
        break;
      }
      case 'radio': {
        setFormData(prev => ({ ...prev, [name]: value }));
        break;
      }
      default: {
        setFormData(prev => ({ ...prev, [name]: value }));
        
        // Real-time validation using conditions
        if (value.trim() && validateField(name, value)) {
          setErrors(prev => ({ ...prev, [name]: '' }));
        }
        break;
      }
    }
  };

  // Field validation function using various operators
  const validateFormField = (fieldId: string, value: string): string => {
    const trimmedValue = value.trim();
    
    // Using logical operators and conditions
    if (!trimmedValue && ValidationRules[fieldId as keyof typeof ValidationRules]?.required) {
      return `${fieldId.charAt(0).toUpperCase() + fieldId.slice(1)} is required`;
    }
    
    switch (fieldId) {
      case 'username':
        if (trimmedValue.length < ValidationRules.username.minLength!) {
          return `Username must be at least ${ValidationRules.username.minLength} characters`;
        }
        if (trimmedValue.length > ValidationRules.username.maxLength!) {
          return `Username must be less than ${ValidationRules.username.maxLength} characters`;
        }
        if (!ValidationRules.username.pattern!.test(trimmedValue)) {
          return 'Username can only contain letters, numbers, and underscores';
        }
        break;
        
      case 'password':
        const strength = calculatePasswordStrength(trimmedValue);
        if (strength.score < 3) {
          return 'Password must contain uppercase, lowercase, and number';
        }
        break;
        
      case 'email':
        if (!ValidationRules.email.pattern!.test(trimmedValue)) {
          return 'Please enter a valid email address';
        }
        break;
        
      case 'mobile':
        if (!ValidationRules.mobile.pattern!.test(trimmedValue)) {
          return 'Please enter a valid 10-digit mobile number';
        }
        break;
        
      case 'age':
        const ageNum = parseInt(trimmedValue);
        if (ageNum < MIN_AGE || ageNum > MAX_AGE) {
          return `Age must be between ${MIN_AGE} and ${MAX_AGE}`;
        }
        break;
    }
    
    return '';
  };

  // Form validation function with comprehensive error checking
  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};
    let errorCount = 0;
    
    // Required fields validation using loops
    const requiredFields = ['username', 'password', 'email', 'mobile', 'age', 'gender'];
    
    for (const field of requiredFields) {
      if (field === 'gender') {
        if (!formData.gender) {
          newErrors.gender = 'Please select a gender';
          errorCount++;
        }
      } else {
        const value = formData[field as keyof UserFormData] as string;
        const error = validateFormField(field, value);
        if (error) {
          newErrors[field] = error;
          errorCount++;
        }
      }
    }
    
    // Update statistics using while loop - but only every 3rd validation call
    setValidationCounter(prev => prev + 1);
    const shouldIncrementValidations = validationCounter % 3 === 0; // Only increment every 3rd call
    
    let i = 0;
    while (i < formStats.length) {
      if (shouldIncrementValidations) {
        formStats[i].validations++;
      }
      if (errorCount > 0) {
        formStats[i].errors++;
      }
      i++; // Increment operator
    }
    
    setErrors(newErrors);
    setFormStats([...formStats]);
    onStatsUpdate([...formStats]);
    
    // Return validation result using comparison operator
    return errorCount === 0;
  };

  // Form submission handler using class instantiation
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      alert(`Form validation failed. Please correct the errors.`);
      return;
    }
    
    setIsSubmitting(true);
    
    try {
      // Simulate API call delay
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Create User instance using class
      const user = new User(
        formData.username,
        formData.email,
        parseInt(formData.age as string),
        formData.gender
      );
      
      // Add hobbies and technologies using loops
      formData.hobbies.forEach(hobby => user.addHobby(hobby));
      formData.technologies.forEach(tech => user.addTechnology(tech));
      
      // Calculate user info using operators and conditions
      const userType = user.isAdult() ? 'Adult' : 'Minor';
      let experienceLevel: 'Beginner' | 'Intermediate' | 'Advanced';
      
      if (user.technologies.length > 3) {
        experienceLevel = 'Advanced';
      } else if (user.technologies.length > 1) {
        experienceLevel = 'Intermediate';
      } else {
        experienceLevel = 'Beginner';
      }
      
      const newSubmissionCount = submissionCount + 1;
      setSubmissionCount(newSubmissionCount);
      
      // Calculate success rate
      const totalValidations = formStats.reduce((sum, stat) => sum + stat.validations, 0);
      const totalErrors = formStats.reduce((sum, stat) => sum + stat.errors, 0);
      const successRate = totalValidations > 0 
        ? ((totalValidations - totalErrors) / totalValidations * 100).toFixed(1) 
        : '100';
      
      // Create submission info object
      const submissionInfo: SubmissionInfo = {
        ...user,
        userType,
        experienceLevel,
        hobbyCount: user.hobbies.length,
        techCount: user.technologies.length,
        submissionNumber: newSubmissionCount,
        mobile: formData.mobile,
        personalInfo: formData.personalInfo,
        successRate: `${successRate}%`,
        getUserInfo: () => {
          return `User: ${user.username} (ID: ${user.id}) - ${user.email}`;
        },
        isAdult: () => {
          return user.age >= 18;
        }
      };
      
      onSubmit(submissionInfo);
      
      // Reset form after successful submission
      setFormData({
        username: '',
        password: '',
        email: '',
        mobile: '',
        age: '',
        gender: '',
        hobbies: [],
        technologies: [],
        personalInfo: ''
      });
      setErrors({});
      
    } catch (error) {
      console.error('Submission error:', error);
      alert('Submission failed. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Cancel form function with confirmation
  const handleCancel = () => {
    // Check if form has data using object values
    const hasData = Object.values(formData).some(value => 
      Array.isArray(value) ? value.length > 0 : value.toString().trim() !== ''
    );
    
    let confirmMessage = 'Are you sure you want to cancel?';
    if (hasData) {
      confirmMessage += ' All entered data will be lost.';
    }
    
    if (window.confirm(confirmMessage)) {
      setFormData({
        username: '',
        password: '',
        email: '',
        mobile: '',
        age: '',
        gender: '',
        hobbies: [],
        technologies: [],
        personalInfo: ''
      });
      setErrors({});
      alert('Form has been reset successfully!');
    }
  };

  // Password strength indicator component
  const PasswordStrengthIndicator = ({ password }: { password: string }) => {
    if (!password) return null;
    
    const strength = calculatePasswordStrength(password);
    const className = `password-strength ${strength.strength.toLowerCase()}`;
    
    return (
      <div className={className}>
        Password strength: {strength.strength} ({strength.score}/5)
      </div>
    );
  };

  return (
    <div className="container form-section">
      <form onSubmit={handleSubmit}>
        {/* Basic Information Section */}
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="username">Username *</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              className={errors.username ? 'error' : formData.username && !errors.username ? 'success' : ''}
              required
            />
            <div className="error-message">{errors.username}</div>
          </div>
          
          <div className="form-group">
            <label htmlFor="password">Password *</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              className={errors.password ? 'error' : formData.password && !errors.password ? 'success' : ''}
              required
            />
            <PasswordStrengthIndicator password={formData.password} />
            <div className="error-message">{errors.password}</div>
          </div>
        </div>

        {/* Contact Information Section */}
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="email">Email Address *</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              className={errors.email ? 'error' : formData.email && !errors.email ? 'success' : ''}
              required
            />
            <div className="error-message">{errors.email}</div>
          </div>
          
          <div className="form-group">
            <label htmlFor="mobile">Mobile Number *</label>
            <input
              type="tel"
              id="mobile"
              name="mobile"
              value={formData.mobile}
              onChange={handleInputChange}
              className={errors.mobile ? 'error' : formData.mobile && !errors.mobile ? 'success' : ''}
              required
            />
            <div className="error-message">{errors.mobile}</div>
          </div>
        </div>

        {/* Personal Information Section */}
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="age">Age *</label>
            <input
              type="number"
              id="age"
              name="age"
              min={MIN_AGE}
              max={MAX_AGE}
              value={formData.age}
              onChange={handleInputChange}
              className={errors.age ? 'error' : formData.age && !errors.age ? 'success' : ''}
              required
            />
            <div className="error-message">{errors.age}</div>
          </div>
          
          <div className="form-group">
            <label>Gender *</label>
            <div className="radio-group">
              {['male', 'female', 'other'].map(gender => (
                <div key={gender} className="radio-item">
                  <input
                    type="radio"
                    id={gender}
                    name="gender"
                    value={gender}
                    checked={formData.gender === gender}
                    onChange={handleInputChange}
                    required
                  />
                  <label htmlFor={gender}>{gender.charAt(0).toUpperCase() + gender.slice(1)}</label>
                </div>
              ))}
            </div>
            <div className="error-message">{errors.gender}</div>
          </div>
        </div>

        {/* Hobbies Section */}
        <div className="form-group full-width">
          <label>Hobbies</label>
          <div className="checkbox-group">
            {['reading', 'traveling', 'sports', 'music', 'gaming'].map(hobby => (
              <div key={hobby} className="checkbox-item">
                <input
                  type="checkbox"
                  id={hobby}
                  name="hobbies"
                  value={hobby}
                  checked={formData.hobbies.includes(hobby)}
                  onChange={handleInputChange}
                />
                <label htmlFor={hobby}>{hobby.charAt(0).toUpperCase() + hobby.slice(1)}</label>
              </div>
            ))}
          </div>
        </div>

        {/* Technologies Section */}
        <div className="form-group full-width">
          <label>Technology Used</label>
          <div className="checkbox-group">
            {['html', 'css', 'javascript', 'python', 'java', 'react', 'typescript'].map(tech => (
              <div key={tech} className="checkbox-item">
                <input
                  type="checkbox"
                  id={tech}
                  name="technologies"
                  value={tech}
                  checked={formData.technologies.includes(tech)}
                  onChange={handleInputChange}
                />
                <label htmlFor={tech}>{tech.toUpperCase()}</label>
              </div>
            ))}
          </div>
        </div>

        {/* Personal Information Textarea */}
        <div className="form-group full-width">
          <label htmlFor="personalInfo">Personal Information</label>
          <textarea
            id="personalInfo"
            name="personalInfo"
            rows={4}
            placeholder="Tell us about yourself..."
            value={formData.personalInfo}
            onChange={handleInputChange}
          />
        </div>

        {/* Submit Buttons */}
        <div className="button-group">
          <button 
            type="submit" 
            className="submit-btn"
            disabled={isSubmitting}
          >
            {isSubmitting ? (
              <>
                <span className="loading-spinner"></span>
                Submitting...
              </>
            ) : (
              'Submit'
            )}
          </button>
          
          <button 
            type="button" 
            className="cancel-btn" 
            onClick={handleCancel}
            disabled={isSubmitting}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default RegistrationForm;
