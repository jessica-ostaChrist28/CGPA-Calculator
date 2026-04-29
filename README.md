# CGPA Calculator (Full Stack Project)

## Project Overview

This project is a full-stack CGPA Calculator application that allows users to sign up, log in, and calculate their CGPA based on subjects, credits, and grades. The system integrates a frontend user interface with a backend API and uses file-based storage for user authentication.

## Features
* User Signup and Login system
* File-based storage for user credentials
* CGPA calculation based on grades and credits
* Frontend and backend integration using REST APIs
* Basic UI navigation (Home, Login, Signup, Calculator)
  
## Tech Stack
**Frontend**
* HTML
* CSS
* JavaScript
  
**Backend**
* Python (Flask)
* Flask-CORS

**Storage**
* Text file (`users.txt`)

**Logic**
* CGPA calculation logic implemented in Python (inspired from C++ version)

## Project Structure
CGPA-Calculator/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/
│   ├── app.py
│   ├── data/
│   │   └── users.txt
│   ├── requirements.txt

## How to Run the Project Locally

### Step 1: Clone the Repository
```
git clone <your-repo-link>
cd CGPA-Calculator
```
### Step 2: Setup Backend
Navigate to backend folder:

```
cd backend
```
Install dependencies:
```
pip install flask flask-cors

```
Run the Flask server:
```
python app.py
```

The backend will run on:
```
http://127.0.0.1:5000
```
---

### Step 3: Run Frontend
Open the `frontend` folder and run `index.html` using Live Server or any browser.
---

## API Endpoints

### 1. Signup

```
POST /signup
```
Request Body:
```
{
  "username": "user",
  "password": "pass"
}
```
---
### 2. Login

```
POST /login
```

Request Body:
```
{
  "username": "user",
  "password": "pass"
}
```
---
### 3. CGPA Calculation
```
POST /cgpa
```
Request Body:

```
{
  "subjects": [
    { "credit": 3, "grade": "A" },
    { "credit": 4, "grade": "B+" }
    ]
}
```
Response:
```
{
  "cgpa": 8.5
}
```
---
## Known Limitations

* User data is stored in a text file, which is not secure or scalable
* No session management (user is not persistently logged in)
* CGPA is not stored per user
* UI uses prompt-based input for subjects (not user-friendly)
* File storage may reset when deployed on some platforms

---
## Future Improvements

* Replace text file storage with SQLite database
* Implement user session management
* Store CGPA history for each user
* Improve UI with dynamic form inputs
* Add input validation on backend
* Deploy using cloud platforms (Render, Netlify)
* Enhance security (password hashing)

---
## Learning Outcomes

This project helped in understanding:

* Full-stack application development
* Frontend and backend integration
* REST API design using Flask
* File handling and data parsing in Python
* Debugging real-world issues like CORS and server errors

---
## Conclusion

This project serves as a foundational full-stack application demonstrating authentication, API communication, and data processing. It can be further extended into a production-level system with database integration and improved user experience.
---

