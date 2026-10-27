
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ML DevOps Lab</h1>
    <p>Flask application is running successfully!</p>
    <p>ISE-2: CI/CD Pipeline and Monitoring Tools</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



