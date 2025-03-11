import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load trained model & scaler
model = joblib.load("models/pacemaker_ids_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Function to detect intrusion
def detect_intrusion(packet_size, frequency, anomaly_score, packet_delay, protocol_type):
    # Preprocess input
    input_data = pd.DataFrame([[packet_size, frequency, anomaly_score, packet_delay, protocol_type]], 
                              columns=["PacketSize", "Frequency", "AnomalyScore", "PacketDelay", "ProtocolType"])
    
    # Scale input
    input_data = scaler.transform(input_data)

    # Predict probability
    probability = model.predict_proba(input_data)[0][1]  # Get attack probability
    print(f"🔍 Attack Probability: {probability:.2f}")

    return "Attack Detected!" if probability > 0.5 else "Normal Traffic"

# Example test (Now includes all 5 features!)
print(detect_intrusion(1000, 2, 0.8, 30, 1))  # Expected: "Attack Detected!" or "Normal Traffic"
print(detect_intrusion(500, 3, 0.2, 20, 1))  # Expected: Normal Traffic
print(detect_intrusion(700, 1, 0.5, 35, 0))  # Expected: Attack Detected!
print(detect_intrusion(1200, 5, 0.9, 50, 1))  # Expected: Attack Detected!
print(detect_intrusion(800, 2, 0.3, 25, 1))  # Expected: Normal Traffic
print(detect_intrusion(600, 2, 0.4, 28, 0))  # Expected: Normal Traffic or Attack?
print(detect_intrusion(900, 4, 0.7, 45, 1))  # Expected: Attack Detected?
print(detect_intrusion(750, 1, 0.6, 38, 0))  # Expected: Attack Detected?
