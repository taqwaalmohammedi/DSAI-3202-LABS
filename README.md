# lab 4 part 2
# Brain Tumor Detection Using Parallel Processing

## Overview
This project detects **brain tumors from MRI images** using **machine learning and parallel processing**. The main tasks include:
- Loading and processing MRI images
- Applying multiple image filters
- Extracting texture features (GLCM)
- Training machine learning models for classification
- Evaluating model performance using accuracy, precision, recall, and F1-score

Parallel processing is used to speed up computations.


# How to Run the Project
python main.py 

# Install Required Libraries
```bash
pip install -r requirements.txt

data/
│── yes/   # Images with brain tumors
│── no/    # Images without brain tumors

#Parallel Processing Used
Image Filtering – Using ProcessPoolExecutor
Feature Extraction – Extracting GLCM features using multiprocessing
Model Training – Training multiple machine learning models in parallel
Machine Learning Models
Random Forest Classifier
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Best hyperparameters are selected using GridSearchCV.

Model Evaluation
Each model is evaluated based on:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

