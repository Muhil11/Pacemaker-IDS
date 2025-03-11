import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load preprocessed data
df = pd.read_csv("data/network_traffic.csv")

# ✅ 1️⃣ Data Augmentation (Adding More Data - Synthetic)
synthetic_data = pd.DataFrame([
    [550, 3, 0.25, 22, 1, 0],   # Normal
    [900, 2, 0.6, 40, 0, 1],    # Attack
    [750, 4, 0.7, 30, 1, 1],    # Attack
    [600, 3, 0.3, 25, 0, 0],    # Normal
    [1200, 5, 0.9, 50, 1, 1],   # Attack
    [800, 2, 0.35, 27, 1, 0],   # Normal
], columns=["PacketSize", "Frequency", "AnomalyScore", "PacketDelay", "ProtocolType", "Label"])

df = pd.concat([df, synthetic_data], ignore_index=True)

# Show class distribution
print("Class distribution:\n", df["Label"].value_counts())

# ✅ 2️⃣ Feature Selection
X = df[['ProtocolType', 'PacketDelay', 'AnomalyScore']]  # Removed PacketSize & Frequency

# Target variable
y = df["Label"]  # 0 = Normal, 1 = Attack

# ✅ 3️⃣ Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ 4️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# ✅ 5️⃣ Train Random Forest Model with Hyperparameter Tuning & Cross-Validation
model = RandomForestClassifier(
    n_estimators=200,  
    max_depth=10,      
    min_samples_split=5,  
    min_samples_leaf=2,   
    random_state=42
)

# Cross-Validation (5-Fold)
cv_scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"🚀 Cross-Validation Accuracy: {np.mean(cv_scores) * 100:.2f}%")

# Train on full training set
model.fit(X_train, y_train)

# Evaluate Model on Test Set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Test Accuracy: {accuracy * 100:.2f}%")

# ✅ 6️⃣ Save Trained Model
joblib.dump(model, "models/pacemaker_ids_model.pkl")

# ✅ 7️⃣ Save Scaler
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Optimized Model and Scaler Saved Successfully!")
