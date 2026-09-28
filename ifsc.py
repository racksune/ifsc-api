from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "success": True,
        "message": "IFSC API Online",
        "usage": "/ifsc?code=SBIN0001234"
    })

@app.route('/ifsc', methods=['GET'])
def ifsc_info():
    code = request.args.get('code', '').upper().strip()

    if not code:
        return jsonify({"error": "IFSC code do — ?code=SBIN0001234"}), 400

    try:
        res = requests.get(f"https://ifsc.razorpay.com/{code}", timeout=10)
        if res.status_code == 200:
            return jsonify({"success": True, "data": res.json()})
        return jsonify({"error": "Invalid IFSC code"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app = app