def extract_zip(zip_path, extract_to):
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def load_dataset(csv_path):
    import pandas as pd
    return pd.read_csv(csv_path)

def preprocess_data(df):
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    from scipy import stats

    cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    df.drop_duplicates(inplace=True)
    for col in cols:
        if col in df.columns:
            df[col].fillna(df[col].mean(), inplace=True)
    df = df[(np.abs(stats.zscore(df[cols])) < 3).all(axis=1)]
    scaler = MinMaxScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df

def save_preprocessed_data(df, path):
    df.to_csv(path, index=False)
