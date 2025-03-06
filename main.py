from preprocessing import load_images
from feature_extraction import extract_glcm_features
from parallel_processing import process_images_parallel
from model_training import train_all_models
import pandas as pd

# Load dataset
dataset_path = "dataset_path_here"
images = load_images(dataset_path)

# Process images in parallel
processed_images = process_images_parallel(images)

# Extract features
features = [extract_glcm_features(img['Original']) for img in processed_images]
df = pd.DataFrame(features)
df['Tumor'] = [1] * len(features)  # Update with actual labels

# Train models
trained_models, X_test, y_test = train_all_models(df.drop(columns=['Tumor']), df['Tumor'])

print("Pipeline Completed Successfully!")
