import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib
import os

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    return X, y_encoded, le

def scale_features(X_train, X_test):
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def get_models():
    return {
        'Logistic Regression': LogisticRegression(max_iter=300),
        'Support Vector Machine': SVC(kernel='rbf', gamma='scale'),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=7),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=300, random_state=42)
    }

def train_and_evaluate(models, X_train, y_train, X_test, y_test, label_encoder):
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = acc
        print(f"{name} Accuracy: {acc:.4f}")
        print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
        print("-" * 60)
    return results

def save_best_model_and_preprocessor(models, results, label_encoder, scaler):
    os.makedirs('utils', exist_ok=True)
    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]

    joblib.dump(best_model, 'utils/best_crop_model.pkl')
    joblib.dump(label_encoder, 'utils/label_encoder.pkl')
    joblib.dump(scaler, 'utils/scaler.pkl')

    print(f"Best Model: {best_model_name}")
    print("Model, LabelEncoder, and Scaler saved inside 'utils/' folder.")

def main():
    df = load_data('data/crop_recommendation.csv')
    X, y, label_encoder = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    models = get_models()
    results = train_and_evaluate(models, X_train_scaled, y_train, X_test_scaled, y_test, label_encoder)
    save_best_model_and_preprocessor(models, results, label_encoder, scaler)

if __name__ == '__main__':
    main()
