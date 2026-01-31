from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import time
import hashlib
import json
import os

from ir_generator import build_ir_prompt
from prompt_engine import (
    build_convert_prompt,
    build_explain_prompt,
    build_complexity_prompt,
    build_debug_prompt,
    build_interview_prompt
)
from gemini_client import init_gemini, convert_code

load_dotenv()
init_gemini()

app = Flask(__name__)
CORS(app)


CACHE = {}
LAST_REQUEST_TIME = 0
COOLDOWN_SECONDS = 40


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json or {}

    source = data.get("source")
    target = data.get("target")
    code = data.get("code")
    mode = data.get("mode", "convert")

    if not code:
        return jsonify({"result": "No code Provided"}), 200

    try:
        if mode == "ir":
            prompt = build_ir_prompt(source, code)

        elif mode == "explain":
            prompt = build_explain_prompt(source, code)

        elif mode == "complexity":
            prompt = build_complexity_prompt(code)    

        elif mode == "debug":
            prompt = build_debug_prompt(code)    

        elif mode == "interview":
            prompt = build_interview_prompt(code)    

        else:
            if not target:
                return jsonify({"result": "Target language required"}), 200
            prompt = build_convert_prompt(source, target, code)

        result = convert_code(prompt)
        return jsonify({"result": result}), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"result": "Server error"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
