import { useState, useEffect } from 'react';

export const useDarkMode = () => {
  // Check for saved theme preference or default to 'light'
  const [theme, setTheme] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('theme') || 'light';
    }
    return 'light';
  });

  const [isDarkMode, setIsDarkMode] = useState(theme === 'dark');

  // Update body class and localStorage when theme changes
  useEffect(() => {
    if (typeof window !== 'undefined') {
      document.body.className = theme === 'dark' ? 'dark-mode' : '';
      localStorage.setItem('theme', theme);
      setIsDarkMode(theme === 'dark');
    }
  }, [theme]);

  // Toggle between light and dark themes
  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
  };

  return { isDarkMode, toggleTheme, theme };
};