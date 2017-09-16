import astropy.io.fits as fits
import numpy as np


def bias(bias_tables):
    bias_images = bias_tables

    # Opening data for each BIAS image:

    images = []
    for value in bias_images:
        image, header = fits.getdata(value, header=True)
        image = np.array(image, dtype=np.float)
        images.append(image)

    # Combination of BIAS images:

    bias_correction = np.median(images, axis=0)

    # Freeing system memory:

    del bias_images
    del images

    return bias_correction
