# app.py

from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    remarks = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character.")

    # Strength Result
    if score == 5:
        strength = "Very Strong"
        color = "green"
    elif score == 4:
        strength = "Strong"
        color = "limegreen"
    elif score == 3:
        strength = "Medium"
        color = "orange"
    elif score == 2:
        strength = "Weak"
        color = "orangered"
    else:
        strength = "Very Weak"
        color = "red"

    return strength, remarks, color


@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    remarks = []
    color = "black"

    if request.method == "POST":
        password = request.form["password"]
        strength, remarks, color = check_password_strength(password)

    return render_template(
        "index.html",
        strength=strength,
        remarks=remarks,
        color=color
    )


if __name__ == "__main__":
    app.run(debug=True)