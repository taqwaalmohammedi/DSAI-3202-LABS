from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt
import concurrent.futures
import time

# Function to apply filters to a single image
def apply_filters(image):
    return {
        'Original': image,
        'Entropy': entropy(image, disk(2)),
        'Gaussian': nd.gaussian_filter(image, sigma=1),
        'Sobel': sobel(image),
        'Gabor': gabor(image, frequency=0.9)[1],
        'Hessian': hessian(image, sigmas=range(1, 100, 1)),
        'Prewitt': prewitt(image)
    }

# Sequential Processing
def process_images_sequential(images):
    start_time = time.time()
    processed_images = [apply_filters(image) for image in images[:5]]
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time:.2f} seconds")
    return processed_images

# Parallel Processing
def process_images_parallel(images):
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        processed_images = list(executor.map(apply_filters, images[:5]))
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time:.2f} seconds")
    return processed_images
