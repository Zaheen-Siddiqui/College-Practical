import React, { useState, useCallback } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import RegistrationForm from './components/RegistrationForm';
import Statistics from './components/Statistics';
import { FormStats, SubmissionInfo } from './types';
import { useDarkMode } from './hooks/useDarkMode';
import './styles/App.css';

const App: React.FC = () => {
  // Dark mode hook
  const { isDarkMode, toggleTheme } = useDarkMode();
  
  // State management using React hooks
  const [submissionCount, setSubmissionCount] = useState<number>(0);
  const [currentUser, setCurrentUser] = useState<string>('');
  const [formStats, setFormStats] = useState<FormStats[]>([
    { field: 'username', errors: 0, validations: 0 },
    { field: 'password', errors: 0, validations: 0 },
    { field: 'email', errors: 0, validations: 0 },
    { field: 'mobile', errors: 0, validations: 0 },
    { field: 'age', errors: 0, validations: 0 }
  ]);

  // Event handler for form submission
  const handleFormSubmit = (submissionInfo: SubmissionInfo) => {
    // Update submission count using increment operator
    setSubmissionCount(prev => prev + 1);
    setCurrentUser(submissionInfo.username);
    
    // Create comprehensive success message using template literals
    const message = `
Form submitted successfully! (Submission #${submissionInfo.submissionNumber})

=== USER INFORMATION ===
• Username: ${submissionInfo.username}
• Email: ${submissionInfo.email}
• Mobile: ${submissionInfo.mobile}
• Age: ${submissionInfo.age} (${submissionInfo.userType})
• Gender: ${submissionInfo.gender}
• User ID: ${submissionInfo.id}
• Registration Date: ${submissionInfo.registrationDate.toLocaleDateString()}

=== PREFERENCES ===
• Hobbies (${submissionInfo.hobbyCount}): ${submissionInfo.hobbies.length > 0 ? submissionInfo.hobbies.join(', ') : 'None selected'}
• Technologies (${submissionInfo.techCount}): ${submissionInfo.technologies.length > 0 ? submissionInfo.technologies.join(', ') : 'None selected'}
• Experience Level: ${submissionInfo.experienceLevel}

=== PERSONAL INFORMATION ===
${submissionInfo.personalInfo || 'No personal information provided'}

=== ADDITIONAL DETAILS ===
${submissionInfo.getUserInfo()}
Adult Status: ${submissionInfo.isAdult() ? 'Yes' : 'No'}
Form Validation Success Rate: ${submissionInfo.successRate}
    `;
    
    alert(message);
  };

  // Event handler for statistics updates
  const handleStatsUpdate = useCallback((updatedStats: FormStats[]) => {
    setFormStats(updatedStats);
  }, []);

  // Function to generate form report using various JavaScript concepts
  const generateFormReport = useCallback(() => {
    if (!currentUser) {
      alert('No user data available. Please submit the form first.');
      return;
    }
    
    // Calculate statistics using array methods and operators
    const totalValidations = formStats.reduce((sum, stat) => sum + stat.validations, 0);
    const totalErrors = formStats.reduce((sum, stat) => sum + stat.errors, 0);
    const successRate = totalValidations > 0 
      ? ((totalValidations - totalErrors) / totalValidations * 100).toFixed(2) 
      : '100';
    
    // Create comprehensive report object
    const report = {
      currentUser,
      statistics: {
        totalValidations,
        totalErrors,
        successRate: `${successRate}%`,
        submissionAttempts: submissionCount
      },
      timestamp: new Date().toISOString(),
      formStats
    };
    
    console.log('Form Report:', report);
    alert(`Form Report generated! Check console for details.\n\nCurrent User: ${currentUser}\nSuccess Rate: ${successRate}%`);
    return report;
  }, [currentUser, formStats, submissionCount]);

  // Key event handler for shortcuts
  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    // Ctrl+R for generating report
    if (e.ctrlKey && e.key === 'r') {
      e.preventDefault();
      generateFormReport();
    }
    // Ctrl+D for toggling dark mode
    if (e.ctrlKey && e.key === 'd') {
      e.preventDefault();
      toggleTheme();
    }
  }, [toggleTheme, generateFormReport]);

  // Add global keyboard listener
  React.useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleKeyDown]);

  return (
    <div className="app">
      {/* Dark Mode Toggle */}
      <button 
        className="dark-mode-toggle"
        onClick={toggleTheme}
        aria-label={`Switch to ${isDarkMode ? 'light' : 'dark'} mode`}
      >
        {isDarkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
      
      {/* Header Component */}
      <Header 
        title="User Registration Form" 
        subtitle="JavaScript Variables, Operators, Conditions, Loops, Functions, Events, Classes and Objects Demo"
      />
      
      {/* Statistics Component */}
      <Statistics 
        formStats={formStats}
        submissionCount={submissionCount}
        currentUser={currentUser}
      />
      
      {/* Main Registration Form Component */}
      <RegistrationForm 
        onSubmit={handleFormSubmit}
        onStatsUpdate={handleStatsUpdate}
      />
      
      {/* Footer Component */}
      <Footer 
        submissionCount={submissionCount}
        currentUser={currentUser}
      />
    </div>
  );
};

export default App;
