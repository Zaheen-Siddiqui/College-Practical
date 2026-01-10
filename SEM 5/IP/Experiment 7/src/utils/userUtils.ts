// User class with TypeScript implementation
import { User as UserInterface, PasswordStrength } from '../types';

export class User implements UserInterface {
  username: string;
  email: string;
  age: number;
  gender: string;
  registrationDate: Date;
  id: number;
  hobbies: string[];
  technologies: string[];

  constructor(username: string, email: string, age: number, gender: string) {
    this.username = username;
    this.email = email;
    this.age = age;
    this.gender = gender;
    this.registrationDate = new Date();
    this.id = this.generateUserId();
    this.hobbies = [];
    this.technologies = [];
  }

  // Method to generate unique user ID using operators
  generateUserId(): number {
    return Math.floor(Math.random() * 10000) + Date.now();
  }

  // Method to add hobby
  addHobby(hobby: string): void {
    if (!this.hobbies.includes(hobby)) {
      this.hobbies.push(hobby);
    }
  }

  // Method to add technology
  addTechnology(tech: string): void {
    if (!this.technologies.includes(tech)) {
      this.technologies.push(tech);
    }
  }

  // Method to get user info
  getUserInfo(): string {
    return `User: ${this.username}, Email: ${this.email}, Age: ${this.age}`;
  }

  // Method to check if user is adult using conditional operator
  isAdult(): boolean {
    return this.age >= 18;
  }
}

// Validation utility functions
export const ValidationRules = {
  username: {
    minLength: 3,
    maxLength: 20,
    pattern: /^\w+$/,
    required: true
  },
  password: {
    minLength: 6,
    pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
    required: true
  },
  email: {
    pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    required: true
  },
  mobile: {
    pattern: /^\d{10}$/,
    required: true
  },
  age: {
    required: true
  }
};

// Constants
export const MIN_AGE = 13;
export const MAX_AGE = 100;
export const MIN_PASSWORD_LENGTH = 6;

// Password strength calculation function
export const calculatePasswordStrength = (password: string): PasswordStrength => {
  let score = 0;
  const checks = {
    length: password.length >= MIN_PASSWORD_LENGTH,
    lowercase: /[a-z]/.test(password),
    uppercase: /[A-Z]/.test(password),
    numbers: /\d/.test(password),
    special: /[!@#$%^&*()_+\-=[\]{};':"\\|,.<>?]/.test(password)
  };
  
  // Use for...in loop to count score
  for (const check in checks) {
    if (checks[check as keyof typeof checks]) {
      score++; // Increment operator
    }
  }
  
  let strength: 'Weak' | 'Medium' | 'Strong';
  if (score < 2) {
    strength = 'Weak';
  } else if (score < 4) {
    strength = 'Medium';
  } else {
    strength = 'Strong';
  }
  
  return {
    score: score,
    checks: checks,
    strength: strength
  };
};

// Field validation function
export const validateField = (fieldId: string, value: string): boolean => {
  const trimmedValue = value.trim();
  
  switch(fieldId) {
    case 'username': {
      return trimmedValue.length >= ValidationRules.username.minLength! && 
             trimmedValue.length <= ValidationRules.username.maxLength! &&
             ValidationRules.username.pattern!.test(trimmedValue);
    }
    case 'password': {
      return trimmedValue.length >= ValidationRules.password.minLength! &&
             ValidationRules.password.pattern!.test(trimmedValue);
    }
    case 'email': {
      return ValidationRules.email.pattern!.test(trimmedValue);
    }
    case 'mobile': {
      return ValidationRules.mobile.pattern!.test(trimmedValue);
    }
    case 'age': {
      const ageNum = parseInt(trimmedValue);
      return ageNum >= MIN_AGE && ageNum <= MAX_AGE;
    }
    default:
      return true;
  }
};
