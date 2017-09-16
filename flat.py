import astropy.io.fits as fits
import numpy as np


def flat(flat_tables, bias_correction):
    flat_images = flat_tables

    # Opening data for each FLAT image:

    bias_flat_images = []
    for value in flat_images:
        image, header = fits.getdata(value, header=True)
        image = np.array(image, dtype=np.float)

        # BIAS correction applied to FLAT images:

        bias_flat_images.append(image - bias_correction)

    # Normalization of BIAS corrected FLAT images:

    bias_flat_images = bias_flat_images/np.mean(bias_flat_images, axis=0)

    # Combination of BIAS corrected and normalized FLAT images:

    bias_flat_correction = np.median(bias_flat_images, axis=0)

    # Freeing system memory:

    del flat_images
    del bias_flat_images

    return bias_flat_correction
