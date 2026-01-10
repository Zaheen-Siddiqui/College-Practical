# Experiment 8 - React Basics

## Objective
To enable students to set up React JS and build simple applications using JSX, components, props, and state.

## Features Demonstrated

### 1. JSX (JavaScript XML)
- HTML-like syntax in JavaScript
- Embedding expressions in JSX
- JSX attributes and styling

### 2. Components
- **Functional Components**: Modern React components using functions
- **Class Components**: Traditional React components using ES6 classes
- Component composition and reusability

### 3. Props
- Passing data from parent to child components
- PropTypes for type checking
- Default props

### 4. State Management
- **useState Hook**: State management in functional components
- **Class State**: State management in class components
- Updating state and re-rendering

## Project Structure

```
Experiment 8/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── index.js
│   ├── App.css
│   ├── components/
│   │   ├── FunctionalCounter.js
│   │   ├── ClassCounter.js
│   │   ├── Greeting.js
│   │   ├── UserCard.js
│   │   └── TodoList.js
│   └── styles/
│       └── components.css
├── package.json
└── README.md
```

## Installation

1. Open terminal in the Experiment 8 folder
2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

```bash
npm start
```

The application will open in your browser at `http://localhost:3000`

## Components Overview

### Greeting Component (Functional with Props)
Demonstrates basic props usage in a functional component.

### UserCard Component (Functional with Props)
Shows how to pass multiple props and display user information.

### FunctionalCounter (useState Hook)
Demonstrates state management using React Hooks (useState).

### ClassCounter (Class Component)
Demonstrates traditional state management using class components.

### TodoList Component
A practical example combining JSX, components, props, and state to create a simple todo list.

## Learning Outcomes

After completing this experiment, students will understand:
- How to set up a React project
- JSX syntax and how it differs from HTML
- Creating functional and class components
- Passing and using props
- Managing component state
- Handling events in React
