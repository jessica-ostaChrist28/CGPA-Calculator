from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Step 1: Create app FIRST
app = Flask(__name__)
CORS(app)

# Ensure data directory and file exist
def ensure_users_file():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/users.txt"):
        open("data/users.txt", "w").close()

ensure_users_file()

# Step 2: Define routes AFTER app is created
@app.route('/')
def home():
    return "Backend running!"

@app.route('/cgpa', methods=['POST'])
def calculate_cgpa():
    try:
        data = request.json
        
        if not data or 'subjects' not in data:
            return jsonify({"error": "Invalid request"}), 400

        subjects = data['subjects']
        
        if not subjects or len(subjects) == 0:
            return jsonify({"error": "No subjects provided"}), 400

        total_credits = 0
        total_points = 0

        grade_map = {
            "O": 10, "A+": 9, "A": 8,
            "B+": 7, "B": 6, "C": 5
        }

        for sub in subjects:
            try:
                credit = float(sub['credit'])
                grade = sub['grade']
                
                if credit <= 0:
                    return jsonify({"error": "Credits must be positive"}), 400
                if grade not in grade_map:
                    return jsonify({"error": f"Invalid grade: {grade}"}), 400
                    
                total_credits += credit
                total_points += credit * grade_map[grade]
            except (ValueError, KeyError):
                return jsonify({"error": "Invalid subject data"}), 400

        if total_credits == 0:
            return jsonify({"error": "Total credits cannot be zero"}), 400

        cgpa = round(total_points / total_credits, 2)

        return jsonify({"cgpa": cgpa})
    except Exception as e:
        return jsonify({"error": "Server error"}), 500
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"status": "error", "message": "Missing username or password"}), 400
        
        username = str(data['username']).strip()
        password = str(data['password']).strip()
        
        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password cannot be empty"}), 400
        
        if len(username) < 3 or len(password) < 3:
            return jsonify({"status": "error", "message": "Username and password must be at least 3 characters"}), 400

        # Check if user already exists
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        u, p = line.split(" ", 1)
                        if u == username:
                            return jsonify({"status": "exists"}), 200
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass

        # Save new user
        with open("data/users.txt", "a") as file:
            file.write(username + " " + password + "\n")

        return jsonify({"status": "created"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": "Server error"}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"status": "error", "message": "Missing username or password"}), 400
        
        username = str(data['username']).strip()
        password = str(data['password']).strip()
        
        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password cannot be empty"}), 400

        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        u, p = line.split(" ", 1)
                        if u == username and p == password:
                            return jsonify({"status": "success"}), 200
                    except ValueError:
                        continue
        except FileNotFoundError:
            return jsonify({"status": "fail"}), 401

        return jsonify({"status": "fail"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": "Server error"}), 500

# Step 3: Run app
if __name__ == '__main__':
    app.run(debug=True)