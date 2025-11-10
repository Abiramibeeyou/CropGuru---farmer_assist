import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import LabelEncoder
import os

class CropAlternatives:
    def __init__(self, preprocessed_csv_path=None):
        # Default path: data/crop_data_preprocessed.csv
        if preprocessed_csv_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            preprocessed_csv_path = os.path.join(base_dir, '../data/crop_data_preprocessed.csv')
            preprocessed_csv_path = os.path.normpath(preprocessed_csv_path)

        if not os.path.exists(preprocessed_csv_path):
            raise FileNotFoundError(f"Dataset not found at {preprocessed_csv_path}")

        self.df = pd.read_csv(preprocessed_csv_path)
        self.feature_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        self.X = self.df[self.feature_cols].values
        self.le = LabelEncoder()
        self.labels_enc = self.le.fit_transform(self.df['label'])
        self.labels = self.df['label'].values

    def get_alternative_crops(self, crop_name, top_n=3):
        if crop_name not in self.labels:
            return f"Crop '{crop_name}' not found in dataset."

        # Find all rows for the given crop
        crop_indices = np.where(self.labels == crop_name)[0]
        crop_vector = self.X[crop_indices].mean(axis=0).reshape(1, -1)

        # Compute distances
        dists = pairwise_distances(crop_vector, self.X, metric='euclidean').flatten()
        dist_df = pd.DataFrame({'crop': self.labels, 'distance': dists})
        dist_df = dist_df[dist_df['crop'] != crop_name]
        dist_df_grouped = dist_df.groupby('crop').min().reset_index()
        top_alternatives = dist_df_grouped.sort_values('distance').head(top_n)['crop'].tolist()

        return top_alternatives


# Example usage (optional for manual test)
if __name__ == "__main__":
    ca = CropAlternatives()  # By default, looks for data/crop_data_preprocessed.csv
    crop_input = 'maize'
    alternatives = ca.get_alternative_crops(crop_input)
    print(f"Top 3 Alternatives to {crop_input.capitalize()}:")
    for alt in alternatives:
        print("-", alt.capitalize())
