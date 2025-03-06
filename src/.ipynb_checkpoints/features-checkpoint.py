from skimage.feature import graycomatrix, graycoprops
import numpy as np

def extract_glcm_features(image):
    """
    Extracts GLCM texture features from an image.
    """
    graycom = graycomatrix(image, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
                           levels=256, symmetric=True, normed=True)

    features = {
        "contrast": graycoprops(graycom, 'contrast').mean(),
        "dissimilarity": graycoprops(graycom, 'dissimilarity').mean(),
        "homogeneity": graycoprops(graycom, 'homogeneity').mean(),
        "energy": graycoprops(graycom, 'energy').mean(),
        "correlation": graycoprops(graycom, 'correlation').mean(),
        "ASM": graycoprops(graycom, 'ASM').mean()
    }
    return features
