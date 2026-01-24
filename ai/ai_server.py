from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import json

from ir_generator import build_ir_prompt
from prompt_engine import (
    build_convert_prompt,
    build_explain_prompt
)
from gemini_client import init_gemini, convert_code

load_dotenv()
init_gemini()

app = Flask(__name__)
CORS(app)


@app.route("/convert", methods=["POST"])
def convert():
    data = request.json

    source = data.get("source")
    target = data.get("target")
    code = data.get("code")
    mode = data.get("mode", "convert")

    if not source or not code:
        return jsonify({"result": "Missing source or code"}), 200

    try:
        # ---------- IR MODE ----------
        if mode == "ir":
          
          ir_prompt = build_ir_prompt(source, code)
          mermaid_code = convert_code(ir_prompt)

          return jsonify({
              
              "result": mermaid_code
        })


        # ------- EXPLAIN MODE --------
        if mode == "explain":
            explain_prompt = build_explain_prompt(source, code)
            explanation = convert_code(explain_prompt)
            return jsonify({"result": explanation})

        # ------- CONVERT MODE --------
        if not target:
            return jsonify({"result": "Target language required"}), 200

        convert_prompt = build_convert_prompt(source, target, code)
        converted_code = convert_code(convert_prompt)

        return jsonify({"result": converted_code})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 200


if __name__ == "__main__":
    app.run(port=8000)
