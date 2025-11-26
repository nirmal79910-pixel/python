# Portfolio Tools - Flask Web Application

## Overview
A modern, multi-page Flask web application featuring three useful tools. Built as a portfolio piece with a stunning dark mode design, responsive layout, and smooth interactions.

## Project Structure
```
├── main.py                 # Flask application with all routes
├── templates/
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Landing page
│   ├── bmi.html           # BMI Calculator page
│   ├── life_weeks.html    # Life in Weeks page
│   └── password.html      # Password Generator page
├── static/
│   ├── css/
│   │   └── style.css      # All custom styles (dark mode theme)
│   └── js/
│       └── script.js      # JavaScript for interactivity
└── attached_assets/       # User-provided assets
```

## Features

### 1. BMI Calculator (`/bmi`)
- Input weight (kg) and height (cm or m)
- Calculates BMI using standard formula
- Color-coded results: Green (Normal), Yellow (Underweight), Orange (Overweight), Red (Obese)
- Visual scale showing where the user falls

### 2. Life in Weeks (`/life-weeks`)
- Input current age or date of birth
- Based on 90-year lifespan
- Shows weeks lived vs weeks remaining
- Progress bar visualization
- Grid visualization showing all weeks
- Motivational quote and message

### 3. Password Generator (`/password`)
- Adjustable length (8-32 characters)
- Toggle options: Uppercase, Numbers, Symbols
- Password strength indicator
- Copy to clipboard functionality
- Security tips included

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with dark mode theme
- **Fonts**: Inter (Google Fonts)

## Running the Application
The application runs on `0.0.0.0:5000` with debug mode enabled for development.

## API Endpoints
- `GET /` - Landing page
- `GET/POST /bmi` - BMI Calculator
- `GET/POST /life-weeks` - Life in Weeks visualizer
- `GET /password` - Password Generator page
- `POST /api/generate-password` - API for password generation

## Recent Changes
- **2024**: Initial build with all three tools
- Modern dark mode design implemented
- Mobile-responsive layout
- Interactive JavaScript features

## User Preferences
- Dark mode aesthetic
- Modern, clean design
- Mobile-responsive layout
- Portfolio-quality UI/UX
