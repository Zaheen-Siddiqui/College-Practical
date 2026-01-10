// JavaScript Variables - Different types of variables
let formSubmissionCount = 0; // Number variable
const MIN_PASSWORD_LENGTH = 6; // Constant variable
const MAX_AGE = 100; // Constant variable
const MIN_AGE = 13; // Constant variable
let validationRules = {}; // Object variable
let userPreferences = []; // Array variable
let isFormValid = false; // Boolean variable
let currentUser = null; // Null variable

// JavaScript Class - User class with constructor and methods
class User {
    constructor(username, email, age, gender) {
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
    generateUserId() {
        return Math.floor(Math.random() * 10000) + Date.now();
    }

    // Method to add hobby
    addHobby(hobby) {
        if (!this.hobbies.includes(hobby)) {
            this.hobbies.push(hobby);
        }
    }

    // Method to add technology
    addTechnology(tech) {
        if (!this.technologies.includes(tech)) {
            this.technologies.push(tech);
        }
    }

    // Method to get user info
    getUserInfo() {
        return `User: ${this.username}, Email: ${this.email}, Age: ${this.age}`;
    }

    // Method to check if user is adult using conditional operator
    isAdult() {
        return this.age >= 18;
    }
}

// JavaScript Object - Validation rules object
validationRules = {
    username: {
        minLength: 3,
        maxLength: 20,
        pattern: /^\w+$/
    },
    password: {
        minLength: MIN_PASSWORD_LENGTH,
        pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/
    },
    email: {
        pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    },
    mobile: {
        pattern: /^\d{10}$/
    }
};

// JavaScript Array of objects for form statistics
let formStats = [
    { field: 'username', errors: 0, validations: 0 },
    { field: 'password', errors: 0, validations: 0 },
    { field: 'email', errors: 0, validations: 0 },
    { field: 'mobile', errors: 0, validations: 0 },
    { field: 'age', errors: 0, validations: 0 }
];

// JavaScript Event Listeners - Multiple event types
document.addEventListener('DOMContentLoaded', function() {
    initializeForm();
    setupEventListeners();
    setupRealTimeValidation();
});

// JavaScript Function - Initialize form with default values
function initializeForm() {
    console.log('Form initialized at:', new Date().toLocaleString());
    
    // Using loops to set up form elements
    const requiredFields = ['username', 'password', 'email', 'mobile', 'age'];
    
    // For...of loop to add event listeners
    for (const fieldId of requiredFields) {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener('blur', function() {
                validateField(this.id);
            });
        }
    }

    // For...of loop to initialize stats
    for (const stat of formStats) {
        stat.validations++;
    }
}

// JavaScript Function - Setup various event listeners
function setupEventListeners() {
    // Form submission event
    document.getElementById('registrationForm').addEventListener('submit', function(e) {
        e.preventDefault();
        formSubmissionCount++; // Increment operator
        
        if (validateForm()) {
            showConfirmBox();
        } else {
            alert(`Form submission failed. Attempt #${formSubmissionCount}`);
        }
    });

    // Mouse events
    document.getElementById('registrationForm').addEventListener('mouseover', function() {
        console.log('Mouse over form');
    });

    // Keyboard events
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            document.getElementById('registrationForm').dispatchEvent(new Event('submit'));
        }
        if (e.ctrlKey && e.key === 'r') {
            e.preventDefault();
            generateFormReport();
        }
    });

    // Focus events
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.boxShadow = '0 0 10px rgba(102, 126, 234, 0.5)';
        });
        
        input.addEventListener('blur', function() {
            this.style.boxShadow = '';
        });
    });
}

// Enhanced validation function with conditions and operators
function validateForm() {
    isFormValid = true;
    let errorCount = 0; // Variable to count errors
    
    // Clear previous errors
    clearErrors();
    
    // Username validation with multiple conditions
    const username = document.getElementById('username');
    const usernameValue = username.value.trim();
    
    // Using logical operators (&&, ||)
    if (usernameValue.length < validationRules.username.minLength || 
        usernameValue.length > validationRules.username.maxLength) {
        showError('username', `Username must be between ${validationRules.username.minLength} and ${validationRules.username.maxLength} characters`);
        errorCount++;
        isFormValid = false;
    } else if (!validationRules.username.pattern.test(usernameValue)) {
        showError('username', 'Username can only contain letters, numbers, and underscores');
        errorCount++;
        isFormValid = false;
    }
    
    // Password validation with complex conditions
    const password = document.getElementById('password');
    const passwordValue = password.value;
    
    if (passwordValue.length < validationRules.password.minLength) {
        showError('password', `Password must be at least ${validationRules.password.minLength} characters long`);
        errorCount++;
        isFormValid = false;
    } else if (!validationRules.password.pattern.test(passwordValue)) {
        showError('password', 'Password must contain uppercase, lowercase, and number');
        errorCount++;
        isFormValid = false;
    }
    
    // Email validation
    const email = document.getElementById('email');
    if (!validationRules.email.pattern.test(email.value)) {
        showError('email', 'Please enter a valid email address');
        errorCount++;
        isFormValid = false;
    }
    
    // Mobile validation
    const mobile = document.getElementById('mobile');
    if (!validationRules.mobile.pattern.test(mobile.value)) {
        showError('mobile', 'Please enter a valid 10-digit mobile number');
        errorCount++;
        isFormValid = false;
    }
    
    // Age validation with comparison operators
    const age = document.getElementById('age');
    const ageValue = parseInt(age.value);
    
    if (ageValue < MIN_AGE || ageValue > MAX_AGE) {
        showError('age', `Age must be between ${MIN_AGE} and ${MAX_AGE}`);
        errorCount++;
        isFormValid = false;
    }
    
    // Gender validation
    const gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        showError('gender', 'Please select a gender');
        errorCount++;
        isFormValid = false;
    }

    // Update statistics using loops
    updateFormStats(errorCount);
    
    // Return validation result using comparison operator
    return errorCount === 0;
}

// Function using loops to update form statistics
function updateFormStats(errorCount) {
    // While loop example
    let i = 0;
    while (i < formStats.length) {
        formStats[i].validations++;
        if (errorCount > 0) {
            formStats[i].errors++;
        }
        i++; // Increment operator
    }
}

// Function to validate individual field (called by events)
function validateField(fieldId) {
    const field = document.getElementById(fieldId);
    const value = field.value.trim();
    let isFieldValid = true;

    // Switch statement for different field types
    switch(fieldId) {
        case 'username': {
            if (value.length < validationRules.username.minLength || 
                !validationRules.username.pattern.test(value)) {
                isFieldValid = false;
            }
            break;
        }
        case 'password': {
            if (value.length < validationRules.password.minLength || 
                !validationRules.password.pattern.test(value)) {
                isFieldValid = false;
            }
            break;
        }
        case 'email': {
            if (!validationRules.email.pattern.test(value)) {
                isFieldValid = false;
            }
            break;
        }
        case 'mobile': {
            if (!validationRules.mobile.pattern.test(value)) {
                isFieldValid = false;
            }
            break;
        }
        case 'age': {
            const ageNum = parseInt(value);
            if (ageNum < MIN_AGE || ageNum > MAX_AGE) {
                isFieldValid = false;
            }
            break;
        }
        default:
            console.log('Unknown field:', fieldId);
    }

    // Update field appearance based on validation
    if (isFieldValid && value !== '') {
        field.classList.remove('error');
        field.classList.add('success');
    } else if (value !== '') {
        field.classList.add('error');
        field.classList.remove('success');
    }

    return isFieldValid;
}

function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const errorDiv = document.getElementById(fieldId + 'Error');
    
    field.classList.add('error');
    field.classList.remove('success');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function clearErrors() {
    const errorMessages = document.querySelectorAll('.error-message');
    const inputs = document.querySelectorAll('input');
    
    // For...of loop to clear errors
    for (const error of errorMessages) {
        error.style.display = 'none';
        error.textContent = '';
    }
    
    // forEach loop with arrow function
    inputs.forEach(input => {
        input.classList.remove('error', 'success');
    });
}

function showConfirmBox() {
    const result = confirm('Are you sure you want to submit the form?');
    if (result) {
        submitForm();
    }
}

// Enhanced submit function using class and objects
function submitForm() {
    // Create new User object using class
    const formData = new FormData(document.getElementById('registrationForm'));
    
    // Extract basic user data
    const username = formData.get('username');
    const email = formData.get('email');
    const age = parseInt(formData.get('age'));
    const gender = formData.get('gender');
    
    // Create user instance
    currentUser = new User(username, email, age, gender);
    
    // Add hobbies using loops
    const hobbies = formData.getAll('hobbies');
    for (const hobby of hobbies) {
        currentUser.addHobby(hobby);
    }
    
    // Add technologies using different loop
    const technologies = formData.getAll('technology');
    technologies.forEach(tech => currentUser.addTechnology(tech));
    
    // Calculate additional user info using operators
    const userType = currentUser.isAdult() ? 'Adult' : 'Minor';
    let experienceLevel;
    if (currentUser.technologies.length > 3) {
        experienceLevel = 'Advanced';
    } else if (currentUser.technologies.length > 1) {
        experienceLevel = 'Intermediate';
    } else {
        experienceLevel = 'Beginner';
    }
    
    // Create detailed user information object
    const userInfo = {
        ...currentUser,
        userType: userType,
        experienceLevel: experienceLevel,
        hobbyCount: currentUser.hobbies.length,
        techCount: currentUser.technologies.length,
        submissionNumber: formSubmissionCount
    };
    
    // Display success message with object properties
    displaySuccessMessage(userInfo);
    
    // Mark fields as success using conditional statements
    markFieldsAsSuccess();
    
    // Log statistics
    console.log('Form Statistics:', formStats);
}

// Function to display success message using template literals
function displaySuccessMessage(userInfo) {
    // Get additional form data
    const personalInfo = document.getElementById('personalInfo').value.trim();
    
    // Create comprehensive submitted information
    const message = `
Form submitted successfully! (Submission #${userInfo.submissionNumber})

=== USER INFORMATION ===
• Username: ${userInfo.username}
• Email: ${userInfo.email}
• Mobile: ${document.getElementById('mobile').value}
• Age: ${userInfo.age} (${userInfo.userType})
• Gender: ${userInfo.gender}
• User ID: ${userInfo.id}
• Registration Date: ${userInfo.registrationDate.toLocaleDateString()}

=== PREFERENCES ===
• Hobbies (${userInfo.hobbyCount}): ${userInfo.hobbies.length > 0 ? userInfo.hobbies.join(', ') : 'None selected'}
• Technologies (${userInfo.techCount}): ${userInfo.technologies.length > 0 ? userInfo.technologies.join(', ') : 'None selected'}
• Experience Level: ${userInfo.experienceLevel}

=== PERSONAL INFORMATION ===
${personalInfo || 'No personal information provided'}

=== ADDITIONAL DETAILS ===
${userInfo.getUserInfo()}
Adult Status: ${userInfo.isAdult() ? 'Yes' : 'No'}
Form Validation Success Rate: ${calculateSuccessRate()}%
    `;
    
    alert(message);
}

// Function to calculate form success rate
function calculateSuccessRate() {
    const totalValidations = formStats.reduce((sum, stat) => sum + stat.validations, 0);
    const totalErrors = formStats.reduce((sum, stat) => sum + stat.errors, 0);
    return totalValidations > 0 ? ((totalValidations - totalErrors) / totalValidations * 100).toFixed(1) : 100;
}

// Function using conditions to mark successful fields
function markFieldsAsSuccess() {
    const requiredInputs = document.querySelectorAll('input[required]');
    
    // Use for...of loop with conditions
    for (const input of requiredInputs) {
        if (input.value.trim() && !input.classList.contains('error')) {
            input.classList.add('success');
        }
    }
}

// Enhanced cancel function with loops and conditions
function cancelForm() {
    let confirmMessage = 'Are you sure you want to cancel?';
    
    // Check if any field has data using loops
    const inputs = document.querySelectorAll('input, textarea');
    let hasData = false;
    
    // Use for...of loop to check for data
    for (const input of inputs) {
        if (input.value.trim() !== '') {
            hasData = true;
            break; // Exit loop early when data found
        }
    }
    
    // Modify message based on condition
    if (hasData) {
        confirmMessage += ' All entered data will be lost.';
    }
    
    const result = confirm(confirmMessage);
    if (result) {
        // Reset form and clear all data
        document.getElementById('registrationForm').reset();
        clearErrors();
        
        // Reset counters using assignment operators
        formSubmissionCount = 0;
        currentUser = null;
        
        // Reset statistics using loop
        formStats.forEach(stat => {
            stat.errors = 0;
            stat.validations = 0;
        });
        
        alert('Form has been reset successfully!');
    }
}

// Setup real-time validation
function setupRealTimeValidation() {
    // Advanced real-time validation using multiple JavaScript concepts
    document.getElementById('username').addEventListener('input', function() {
        const value = this.value.trim();
        const minLength = validationRules.username.minLength;
        
        // Complex condition using logical operators
        if (value.length >= minLength && validationRules.username.pattern.test(value)) {
            this.classList.remove('error');
            this.classList.add('success');
            document.getElementById('usernameError').style.display = 'none';
        } else {
            this.classList.remove('success');
            if (value.length > 0) {
                this.classList.add('error');
            }
        }
    });

    document.getElementById('password').addEventListener('input', function() {
        const value = this.value;
        const strength = calculatePasswordStrength(value);
        
        // Update validation based on strength
        if (strength.score >= 3) {
            this.classList.remove('error');
            this.classList.add('success');
            document.getElementById('passwordError').style.display = 'none';
        }
    });

    document.getElementById('email').addEventListener('input', function() {
        const emailRegex = validationRules.email.pattern;
        if (emailRegex.test(this.value)) {
            this.classList.remove('error');
            this.classList.add('success');
            document.getElementById('emailError').style.display = 'none';
        }
    });

    document.getElementById('mobile').addEventListener('input', function() {
        const mobileRegex = validationRules.mobile.pattern;
        if (mobileRegex.test(this.value)) {
            this.classList.remove('error');
            this.classList.add('success');
            document.getElementById('mobileError').style.display = 'none';
        }
    });

    document.getElementById('age').addEventListener('input', function() {
        const age = parseInt(this.value);
        // Compound condition using comparison operators
        if (age >= MIN_AGE && age <= MAX_AGE) {
            this.classList.remove('error');
            this.classList.add('success');
            document.getElementById('ageError').style.display = 'none';
        }
    });
}

// Function to calculate password strength using various operators
function calculatePasswordStrength(password) {
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
        if (checks[check]) {
            score++; // Increment operator
        }
    }
    
    let strength;
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
}

// Additional function to demonstrate more JavaScript concepts
function generateFormReport() {
    if (!currentUser) {
        alert('No user data available. Please submit the form first.');
        return;
    }
    
    // Calculate statistics using various operators
    const totalValidations = formStats.reduce((sum, stat) => sum + stat.validations, 0);
    const totalErrors = formStats.reduce((sum, stat) => sum + stat.errors, 0);
    const successRate = totalValidations > 0 ? ((totalValidations - totalErrors) / totalValidations * 100).toFixed(2) : 0;
    
    // Create comprehensive report object
    const report = {
        user: currentUser,
        statistics: {
            totalValidations,
            totalErrors,
            successRate: `${successRate}%`,
            submissionAttempts: formSubmissionCount
        },
        timestamp: new Date().toISOString()
    };
    
    console.log('Form Report:', report);
    return report;
}
