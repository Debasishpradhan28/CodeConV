from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

AI_CONTAINER_URL = "http://localhost:8000/convert"

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
            "http://localhost:8000/convert",
            json=data,
            timeout=60
        )
        return jsonify(ai_response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(port=5000)
