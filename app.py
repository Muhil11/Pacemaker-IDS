from flask import Flask, request, jsonify
from src.detect_intrusions import detect_attack
from src.send_alert import send_alert

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    features = data['features']

    is_attack = detect_attack(features)

    if is_attack:
        send_alert()
        return jsonify({"attack_detected": True, "message": "⚠️ Intrusion detected! Alert sent."})

    return jsonify({"attack_detected": False, "message": "✅ No intrusion detected."})

if __name__ == '__main__':
    app.run(debug=True)
 
