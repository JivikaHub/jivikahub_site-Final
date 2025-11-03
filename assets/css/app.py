# app.py  -- simple Flask example to receive a contact form
from flask import Flask, request, render_template_string, redirect, url_for
import csv, os

app = Flask(__name__)
DATA_FILE = "submissions.csv"

@app.route("/", methods=["GET"])
def index():
    return "Flask is running. Use /contact to POST data."

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # save to CSV
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, message])
    return "Thanks — submission received."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
