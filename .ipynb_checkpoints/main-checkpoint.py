import glob
from src.data_loader import load_images
from src.filters import process_images_parallel
from src.features import extract_features_parallel
from src.model_training import train_and_evaluate_models
import pandas as pd

# Correct dataset path
dataset_path = "data/"  # Ensure this is the correct path

# Retrieve all image file paths
yes_image_paths = glob.glob(dataset_path + "yes/*.*")  # Load all files in 'yes'
no_image_paths = glob.glob(dataset_path + "no/*.*")    # Load all files in 'no'

# Load images
yes_images = load_images(yes_image_paths)
no_images = load_images(no_image_paths)

# Debugging: Check if images are loaded correctly
print(f"Number of Yes Images: {len(yes_images)}")
print(f"Number of No Images: {len(no_images)}")

if len(yes_images) == 0 or len(no_images) == 0:
    print("Error: No images were loaded. Check that the 'data/yes' and 'data/no' folders exist and contain images.")
else:
    # Apply filters (Parallel Processing)
    yes_inputs = process_images_parallel(yes_images)
    no_inputs = process_images_parallel(no_images)

    # Extract GLCM Features (Parallel Processing)
    yes_glcm_features = extract_features_parallel(yes_inputs, 1)
    no_glcm_features = extract_features_parallel(no_inputs, 0)

    # Convert to DataFrame and Save
    df = pd.DataFrame(yes_glcm_features + no_glcm_features)
    df.to_csv("brain_tumor_features_parallel.csv", index=False)
    print("Feature extraction completed and saved.")

    # Train & Evaluate ML Models
    train_and_evaluate_models("brain_tumor_features_parallel.csv")
