import joblib

# Load trained model
model = joblib.load("models/pacemaker_ids_model.pkl")

# Define feature names
feature_names = ["PacketSize", "Frequency", "AnomalyScore", "PacketDelay", "ProtocolType"]

# Get feature importances
importances = model.feature_importances_

# Sort features by importance
sorted_features = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)

# Print feature importance ranking
print("📊 Feature Importance Ranking:")
for rank, (feature, importance) in enumerate(sorted_features, 1):
    print(f"{rank}. {feature}: {importance:.4f}")
 
