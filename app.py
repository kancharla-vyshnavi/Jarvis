from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "Jarvis API is live"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })