import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import joblib  # for saving scalers

def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def prepare_data_for_lstm(df, sequence_length=2):
    prices = df['avg_modal_price'].values.reshape(-1,1)
    scaler = MinMaxScaler()
    scaled_prices = scaler.fit_transform(prices)
    
    X, y = [], []
    for i in range(sequence_length, len(scaled_prices)):
        X.append(scaled_prices[i-sequence_length:i])
        y.append(scaled_prices[i])
    X, y = np.array(X), np.array(y)
    return X, y, scaler

def train_and_save_models(data: pd.DataFrame, save_dir="models", sequence_length=2):
    os.makedirs(save_dir, exist_ok=True)
    crops = data['commodity_name'].unique()
    models_info = {}

    for crop in crops:
        crop_df = data[data['commodity_name'] == crop].sort_values('month')
        if len(crop_df) <= sequence_length:
            print(f"Insufficient data for crop {crop} to train.")
            continue
        
        X, y, scaler = prepare_data_for_lstm(crop_df, sequence_length)
        model = create_lstm_model((sequence_length, 1))
        early_stop = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
        model.fit(X, y, epochs=100, batch_size=16, verbose=0, callbacks=[early_stop])
        
        # Save model & scaler
        model.save(os.path.join(save_dir, f"{crop}_lstm.h5"))
        joblib.dump(scaler, os.path.join(save_dir, f"{crop}_scaler.save"))
        print(f"Saved model and scaler for {crop}")
        
        models_info[crop] = {'model_path': f"{save_dir}/{crop}_lstm.h5",
                             'scaler_path': f"{save_dir}/{crop}_scaler.save"}

    return models_info

if __name__ == "__main__":
    import pandas as pd

    # Load your dataset here
    data = pd.read_csv("data/crop_price_dataset.csv", parse_dates=['month'])

    # Call the training function
    train_and_save_models(data, save_dir="models", sequence_length=2)
