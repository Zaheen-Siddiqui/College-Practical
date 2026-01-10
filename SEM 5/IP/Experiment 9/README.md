# Experiment 9 - React Advanced Concepts

## Objective
To create web pages using ReactJS Forms, Events, Routers, Refs, and Keys.

## Features Demonstrated

### 1. **Forms** 📝
- Controlled components
- Uncontrolled components with refs
- Form validation
- Multiple input types (text, email, password, select, radio, checkbox)
- Form submission handling
- Real-time form validation

### 2. **Events** 🎯
- onClick events
- onChange events
- onSubmit events
- onFocus and onBlur events
- onMouseEnter and onMouseLeave events
- onKeyPress and onKeyDown events
- Event object handling
- Preventing default behavior

### 3. **Routers** 🧭
- React Router DOM setup
- Navigation between pages
- Route parameters (dynamic routes)
- Nested routes
- Link and NavLink components
- useNavigate hook
- useParams hook
- 404 Not Found page

### 4. **Refs** 🎯
- useRef hook
- Accessing DOM elements
- Focusing inputs
- Measuring elements
- Uncontrolled form inputs
- Managing focus
- Storing mutable values

### 5. **Keys** 🔑
- Unique keys for list items
- Why keys are important
- Key prop in dynamic lists
- Proper key usage patterns

## Project Structure

```
Experiment 9/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── index.js
│   ├── App.css
│   ├── pages/
│   │   ├── Home.js
│   │   ├── FormsDemo.js
│   │   ├── EventsDemo.js
│   │   ├── RefsDemo.js
│   │   ├── KeysDemo.js
│   │   ├── UserProfile.js
│   │   └── NotFound.js
│   ├── components/
│   │   ├── Navigation.js
│   │   ├── ControlledForm.js
│   │   ├── UncontrolledForm.js
│   │   ├── EventsShowcase.js
│   │   ├── RefsExample.js
│   │   └── KeysList.js
│   └── styles/
│       ├── pages.css
│       └── components.css
├── package.json
└── README.md
```

## Installation

1. Open terminal in the Experiment 9 folder
2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

```bash
npm start
```

The application will open in your browser at `http://localhost:3000`

## Pages Overview

### Home Page
Landing page with navigation to all demos.

### Forms Demo
- Controlled form with validation
- Uncontrolled form using refs
- Multiple input types demonstration

### Events Demo
- Interactive event handlers showcase
- Mouse events
- Keyboard events
- Focus events

### Refs Demo
- DOM manipulation with refs
- Focus management
- Element measurements
- Video player control

### Keys Demo
- Dynamic list rendering
- Proper key usage
- CRUD operations on lists

### User Profile (Dynamic Route)
Demonstrates route parameters with useParams hook.

## Learning Outcomes

After completing this experiment, students will understand:
- How to create and handle forms in React
- Different types of event handling
- Setting up React Router for navigation
- Using refs for DOM access and manipulation
- Importance and proper usage of keys in lists
- Controlled vs Uncontrolled components
- Route parameters and navigation
