from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Use env variable if available, else fallback to localhost
AI_BASE = os.getenv("AI_BASE_URL", "http://localhost:8000")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/flowchart")
def flowchart():
    return render_template("flowchart.html")


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json

    try:
        ai_response = requests.post(
            f"{AI_BASE}/convert",
            json=data,
            timeout=60
        )

        return jsonify(ai_response.json())

    except Exception as e:
        print("FRONTEND → AI ERROR:", e)
        return jsonify({
            "result": "Cannot connect to AI backend. Is ai_server running?"
        }), 200


if __name__ == "__main__":
    app.run(port=5000)
