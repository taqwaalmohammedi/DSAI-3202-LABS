import concurrent.futures
import time
import numpy as np
from skimage.feature import graycomatrix, graycoprops

def compute_glcm_features(image, filter_name):
    """
    Computes GLCM (Gray Level Co-occurrence Matrix) features for an image.
    """
    image = (image * 255).astype(np.uint8)
    graycom = graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    features = {}
    for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']:
        values = graycoprops(graycom, prop).flatten()
        for i, value in enumerate(values):
            features[f'{filter_name}_{prop}_{i+1}'] = value
    return features

def extract_features(image_dict):
    """
    Extracts GLCM features for a single image dictionary.
    """
    feature_set = {}
    for key, img in image_dict.items():
        feature_set.update(compute_glcm_features(img, key))
    return feature_set

def extract_features_parallel(images_list, tumor_presence):
    """
    Extracts GLCM features for all images in parallel.
    """
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        feature_dicts = list(executor.map(extract_features, images_list))

    glcm_features_list = []
    for feature_dict in feature_dicts:
        feature_dict['Tumor'] = tumor_presence
        glcm_features_list.append(feature_dict)

    end_time = time.time()
    print(f"Parallel Feature Extraction Time: {end_time - start_time:.2f} seconds")
    return glcm_features_list
