# Pacemaker Intrusion Detection System (IDS)

## 📌 Overview
This project is a **Pacemaker Intrusion Detection System (IDS)** that monitors network traffic and detects potential cyberattacks on pacemakers. It uses **machine learning** to classify network traffic as either **normal** or **malicious** and sends an **alert** when an intrusion is detected.

## 🚀 Features
- **Machine Learning-based Detection**: Uses a trained model to classify traffic.
- **Flask API**: Provides a REST API for real-time intrusion detection.
- **Email Alerts**: Sends alerts when a possible attack is detected.
- **Feature Importance Analysis**: Identifies the most important network traffic features.

## 📂 Project Structure
```
📁 Pacemaker-IDS
│── data_preprocessing.py      # Prepares and normalizes network traffic data
│── train_model.py             # Trains a machine learning model
│── detect_intrusions.py       # Detects potential attacks
│── feature_importance.py      # Analyzes feature importance
│── send_alert.py              # Sends an alert via email
│── app.py                     # Flask API for real-time intrusion detection
│── models/                    # Stores trained models and scalers
│── data/network_traffic.csv    # Dataset for training and testing
│── README.md                  # Project documentation
```

## 📦 Requirements
### 1️⃣ **Programming Language & Frameworks**
- Python 3.x
- Flask (for the API)

### 2️⃣ **Python Libraries**
Install dependencies using:
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install pandas scikit-learn joblib flask smtplib numpy
```

### 3️⃣ **Files & Models**
- **`network_traffic.csv`** – Network traffic dataset
- **`pacemaker_ids_model.pkl`** – Trained Machine Learning model
- **`scaler.pkl`** – Scaler for normalizing input data

### 4️⃣ **SMTP Email Setup (For Alerts)**
To enable email alerts, configure `send_alert.py` with:
- **SMTP server details**
- **Sender email & password** *(Use environment variables for security!)*

## 🔥 How to Run
### 1️⃣ **Preprocess Data**
```bash
python data_preprocessing.py
```

### 2️⃣ **Train the Model**
```bash
python train_model.py
```

### 3️⃣ **Run the API**
```bash
python app.py
```
The API will be available at: `http://127.0.0.1:5000/detect`

### 4️⃣ **Send a Detection Request**
Use **Postman** or `curl` to send a request:
```bash
curl -X POST "http://127.0.0.1:5000/detect" -H "Content-Type: application/json" -d '{"features": [1000, 2, 0.8, 30, 1]}'
```

## ⚠️ Security Notes
- **Never hardcode passwords in `send_alert.py`**.
- **Use environment variables or secret management tools**.

## 🎯 Future Improvements
- Deploy on **Docker/Kubernetes**.
- Enhance **anomaly detection** with Deep Learning.
- Improve **email alert security** with OAuth.

## 📜 License
This project is open-source and available under the **MIT License**.

---
👨‍💻 Developed for **Pacemaker Intrusion Detection** 🚀

