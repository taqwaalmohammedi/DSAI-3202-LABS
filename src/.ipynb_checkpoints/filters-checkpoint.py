import concurrent.futures
import time
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt

def apply_filters(image):
    """
    Applies multiple filters to an image.
    """
    return {
        'Original': image,
        'Entropy': entropy(image, disk(2)),
        'Gaussian': nd.gaussian_filter(image, sigma=1),
        'Sobel': sobel(image),
        'Gabor': gabor(image, frequency=0.9)[1],
        'Hessian': hessian(image, sigmas=range(1, 100, 1)),
        'Prewitt': prewitt(image)
    }

def process_images_parallel(images):
    """
    Applies filters in parallel using multiprocessing.
    """
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        processed_images = list(executor.map(apply_filters, images[:5]))  # Process first 5 images for testing
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time:.2f} seconds")
    return processed_images
