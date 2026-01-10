import React from 'react';

interface FooterProps {
  submissionCount: number;
  currentUser?: string;
}

const Footer: React.FC<FooterProps> = ({ submissionCount, currentUser }) => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <p>&copy; {currentYear} User Registration System. All rights reserved.</p>
      <p>
        Forms submitted today: <strong>{submissionCount}</strong>
        {currentUser && ` | Current user: ${currentUser}`}
      </p>
      <div className="footer-links">
        <a href="#privacy">Privacy Policy</a>
        <a href="#terms">Terms of Service</a>
        <a href="#contact">Contact Us</a>
        <a href="#help">Help</a>
      </div>
    </footer>
  );
};

export default Footer;
