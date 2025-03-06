import cv2

def load_images(image_paths):
    """
    Loads grayscale images from a list of paths.
    """
    images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_paths]
    return [img for img in images if img is not None]  # Remove None values
