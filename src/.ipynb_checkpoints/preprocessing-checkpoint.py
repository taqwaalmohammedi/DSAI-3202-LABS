import cv2
import numpy as np
import glob

def load_images(dataset_path):
    """
    Loads images from the given dataset path.
    Returns a list of images.
    """
    image_paths = glob.glob(dataset_path + "/*.jpg")  # Change file extension if needed
    images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_paths]
    return images
