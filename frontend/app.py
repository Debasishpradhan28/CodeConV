from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
