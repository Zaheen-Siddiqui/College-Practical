// TypeScript Interfaces and Types for the registration form

export interface User {
  username: string;
  email: string;
  age: number;
  gender: string;
  registrationDate: Date;
  id: number;
  hobbies: string[];
  technologies: string[];
}

export interface UserFormData {
  username: string;
  password: string;
  email: string;
  mobile: string;
  age: number | string;
  gender: string;
  hobbies: string[];
  technologies: string[];
  personalInfo: string;
}

export interface ValidationRule {
  minLength?: number;
  maxLength?: number;
  pattern?: RegExp;
  required?: boolean;
}

export interface ValidationRules {
  username: ValidationRule;
  password: ValidationRule;
  email: ValidationRule;
  mobile: ValidationRule;
  age: ValidationRule;
}

export interface FormStats {
  field: string;
  errors: number;
  validations: number;
}

export interface PasswordStrength {
  score: number;
  checks: {
    length: boolean;
    lowercase: boolean;
    uppercase: boolean;
    numbers: boolean;
    special: boolean;
  };
  strength: 'Weak' | 'Medium' | 'Strong';
}

export interface FormErrors {
  [key: string]: string;
}

export interface SubmissionInfo extends User {
  userType: 'Adult' | 'Minor';
  experienceLevel: 'Beginner' | 'Intermediate' | 'Advanced';
  hobbyCount: number;
  techCount: number;
  submissionNumber: number;
  mobile: string;
  personalInfo: string;
  successRate: string;
  getUserInfo: () => string;
  isAdult: () => boolean;
}
