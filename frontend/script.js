function signup() {
    let username = document.getElementById("signupUsername").value;
    let password = document.getElementById("signupPassword").value;

    fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "created") {
            alert("Account created! Now login.");

            // Auto-fill login fields
            document.getElementById("loginUsername").value = username;
            document.getElementById("loginPassword").value = password;

            showLogin();
        } else {
            alert("User already exists!");
        }
    });
}

    function login() {
    console.log("Login button clicked"); // 👈 add this

    let username = document.getElementById("loginUsername").value;
    let password = document.getElementById("loginPassword").value;

    console.log(username, password); // 👈 check values

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data); // 👈 VERY IMPORTANT

        if (data.status === "success") {
            alert("Login successful!");

            document.getElementById("loginForm").style.display = "none";
            document.getElementById("signupForm").style.display = "none";
            document.getElementById("cgpaSection").style.display = "block";

        } else {
            alert("Invalid credentials!");
        }
    })
    .catch(err => {
        console.log("Error:", err);
    });
}
}
function showSignup() {
    document.getElementById("signupForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
}

function showLogin() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}

function calculate() {
    let n = document.getElementById("subjects").value;

    let subjects = [];

    for (let i = 0; i < n; i++) {
        let credit = parseFloat(prompt("Enter credit for subject " + (i+1)));
        let grade = prompt("Enter grade (O, A+, A, B+, B, C)");

        subjects.push({ credit: credit, grade: grade });
    }

    fetch("http://127.0.0.1:5000/cgpa", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ subjects: subjects })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "CGPA: " + data.cgpa;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}