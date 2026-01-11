from flask import Flask, request, jsonify
from sentra_engine import run_sentra
from flask_cors import CORS
import json
from engine.auto_fixer import auto_fix_design
from engine.dashboard_metrics import get_metrics


app = Flask(__name__)
CORS(app)


HOST_IP = "192.168.1.2"   # ya "0.0.0.0" ya apna LAN IP
PORT = 5000

@app.route("/")
def home():
    return "SENTRA API is running"

@app.route("/check", methods=["POST"])
def check_design():
    data = request.json

    with open("input_designs/temp_design.json", "w") as f:
        json.dump(data, f)

    result = run_sentra(
        design_data=data,
        brand_rules_path="brand_kit/brand_rules.json"
    )


    return jsonify(result)

@app.route("/fix", methods=["POST"])
def fix_design():
    data = request.json

    if data is None:
        return jsonify({"error": "No JSON received"}), 400

    with open("brand_kit/brand_rules.json") as f:
        brand_rules = json.load(f)

    fixed_design, changes, fixed = auto_fix_design(data, brand_rules)

    return jsonify({
        "fixed": fixed,
        "changes": changes,
        "fixed_design": fixed_design
    })
@app.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify(get_metrics())



if __name__ == "__main__":
    app.run(host= '192.168.1.2', port=5000, debug=True)
