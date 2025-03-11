import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Extract important features
    df = df[['PacketSize', 'Frequency', 'AnomalyScore', 'Label']]

    # Normalize numeric columns
    scaler = StandardScaler()
    df[['PacketSize', 'Frequency', 'AnomalyScore']] = scaler.fit_transform(df[['PacketSize', 'Frequency', 'AnomalyScore']])

    return df
