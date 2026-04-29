from flask import Flask, request, jsonify
from flask_cors import CORS

# Step 1: Create app FIRST
app = Flask(__name__)
CORS(app)

# Step 2: Define routes AFTER app is created
@app.route('/')
def home():
    return "Backend running!"

@app.route('/cgpa', methods=['POST'])
def calculate_cgpa():
    data = request.json

    subjects = data['subjects']

    total_credits = 0
    total_points = 0

    grade_map = {
        "O": 10, "A+": 9, "A": 8,
        "B+": 7, "B": 6, "C": 5
    }

    for sub in subjects:
        credit = sub['credit']
        grade = sub['grade']

        total_credits += credit
        total_points += credit * grade_map.get(grade, 0)

    cgpa = total_points / total_credits

    return jsonify({"cgpa": cgpa})
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']

    # Check if user already exists
    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                u, p = line.strip().split()
                if u == username:
                    return {"status": "exists"}
    except:
        pass

    # Save new user
    with open("data/users.txt", "a") as file:
        file.write(username + " " + password + "\n")

    return {"status": "created"}


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    with open("data/users.txt", "r") as file:
        for line in file:
            u, p = line.strip().split()
            if u == username and p == password:
                return {"status": "success"}

    return {"status": "fail"}

# Step 3: Run app
if __name__ == '__main__':
    app.run(debug=True)